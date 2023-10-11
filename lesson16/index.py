import datasource

def main():
    names=datasource.cityNames()
    city=datasource.cities_info("屏東縣新埤")
    print(city)
    

if __name__=="__main__":
    main()