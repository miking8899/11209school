import requests
import csv
import io

__cities=[]

def download()->list[list]:
    url='https://data.moi.gov.tw/MoiOD/System/DownloadFile.aspx?DATA=CA18EE06-4A50-4861-9D97-7853353D7108'
    response=requests.request("GET",url)
   
    try:
        response.raise_for_status()
    except:
        print("連線ERROR")
        raise Exception("連線錯誤","網路中斷")
    else:
        if not response.ok:
            print("下載失敗")
        else:
            print("下載成功")
            file=io.StringIO(response.text)
            csv_reader=csv.reader(file)
            next(csv_reader)
            return list[csv_reader]
        
def cities_info()->list[list]:
    if len(cities)==0:
        try:
            data_list=__download()
        except Exception as e:
            print(f"錯誤:{e}")
        else:
            for row in data_list:
                if row[0]=="111":
                    __cities.append(row)
    return __cities

def cityNames()->list[str]:
    cities=cities_info()
    names=[]
    
    for row in cities:
        cityName=row[1]
        names.append(cityName)
    return names
              