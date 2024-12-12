
cities=[]
while(True):
    city=input("Give the name a city")
    if (city != "stop"):
        
        population=len(city)*1000000
        
        print(city)
        print(population)
        
        cities.append({"city":city,"population":population})
        
        
        
    else:
        break
cities.sort(key=lambda x:x["population"])
cities.reverse()    
print(cities)    
    

    

    