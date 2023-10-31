import requests
import sqlite3
import threading

__all__ = ['updata_sqlite_data']


def __download_web_data() -> dict:
    '''
    下載aqx_p_02細懸浮微粒資料（PM2.5） 1個小時更新一次
     '''
    aqsp02_url="https://data.moenv.gov.tw/api/v2/aqx_p_02?api_key=2c345b7a-6a24-4fd2-8e56-6e3ad28d56e4"

    response = requests.get(aqsp02_url)
    response.raise_for_status()
    print("下載成功 OK")
    #print(response.json())
    return response.json()


# res = __download_web_data()   #single python testing command


def __create_table(conn: sqlite3.Connection):
    cursor = conn.cursor()
    cursor.execute(
        '''
        CREATE TABLE  IF NOT EXISTS 全國PM_25(
            "id"	INTEGER ,
            "測站名稱"	TEXT NOT NULL,
            "城市名稱"	TEXT NOT NULL,
            "懸浮微粒濃度"	INTEGER,
            "更新時間"	TEXT ,
            "測試單位"	TEXT,
            PRIMARY KEY("id" AUTOINCREMENT),
            UNIQUE(測站名稱,更新時間) ON CONFLICT REPLACE 
        );
        '''
    )
    
    conn.commit()


def __insert_data(conn: sqlite3.Connection, values: list | tuple) -> None:
    '''
    新增資料
    '''
    cursor = conn.cursor()
    sql = '''
    REPLACE INTO 全國PM_25(
        測站名稱,
        城市名稱,
        懸浮微粒濃度,
        更新時間,
        測試單位
        )
        VALUES(?,?,?,?,?)
    '''
    cursor.execute(sql, values)
    conn.commit()


def updata_sqlite_data() -> None:
    '''
    下載,並更新資料庫
    '''
    data = __download_web_data()
    conn = sqlite3.connect("PM_25.db")
   
    __create_table(conn)
    for item in data['records']:
        __insert_data(conn, [item['site'], item['county'], item['pm25'],item['datacreationdate'], item['itemunit']])
    

    print("資料定期更新OK")
    conn.close()
