
#worldmap ={country_1{states_1{cities_1,cities_2},states_2{cities_1,cities_2}},country_2{states_1,states_2},country_3{states_1,states_2}}

# print("----------------Testing---------------------")
# intt = range(5)
#
# for i in intt:
#     worldmap = {"key_"+str(i):"value"+str(i)}
#     print(worldmap)
#
# print("----------------Definition---------------------")
#
# countries = range(3)
# states = range(5)
# cities = range(10)
#
# for i in countries:
#     for j in states:
#         worldmap = {"Country_"+str(i+1):"States_"+str(j+1)}
#         for k,v in worldmap.items():
#             print(str(k) + "  " + str(v))
# print()
# print("----------------Access---------------------")


# countries = range(1)
# states = range(3)
# cities = [["A"],["B","C"],["D","E","F","G"]]
#
#
# for i in countries:
#     for j in states:
#         #worldmap = {"Country_"+str(i+1):"States_"+str(j+1)}
#         for k in cities[j]:
#             worldmap = {"Country_"+str(i):{"States_"+str(j):"Cities_"+str(k)}}
#             #print(worldmap)
#             for ke,va in worldmap.items():
#                 for va_ke,va_va in va.items():
#                     print(str(ke) + "  " + str(va_ke) + "  " + str(va_va))
#
# print(worldmap)
print("-------------------------Static Database---------------------")

#countries = range(1)
# states = ["MS","GJ","MP"]
# cities = ["Mumbai","Pune","Kolhapur","Nagpur","Ankleshwar","Baroda","Surat","Indore"]
#
samplewp = {"Mumbai":{"MS":"India"},"Pune":{"MS":"India"},"Kolhapur":{"MS":"India"},"Nagpur":{"MS":"India"},"Ankleshwar":{"GJ":"India"},"Baroda":{"GJ":"India"},"Surat":{"GJ":"India"},"Indore":{"MP":"India"}}
#print(str(samplewp))
for city,v in samplewp.items():
    for state,country in v.items():
        print(str(city)+"  "+str(state)+"  "+str(country))


#
#
#
# for i in cities:
#     for j in states:
#         worldmap[str(i)] = {"States_"+str(j):"India"}
#         for ke,va in worldmap.items():
#             for va_ke,va_va in va.items():
#                 print(str(ke) + "  " + str(va_ke) + "  " + str(va_va))
#
# #print(worldmap("F"))
#
print("\n----------------City input => country and state result---------------------")

#inpt ="Ankleshwar"
inpt = input("Enter city name = ")
for city,v in samplewp.items():
    if(city==inpt):
        for state,country in v.items():
            inpt2 = state
            print(str(inpt)+" is in "+str(state)+" state and in "+str(country))
            break
    else:
        continue
print("\n\n----------------State input => country and cities result---------------------")

#inpt2 ="GJ"
cities_print =[]

for city,v in samplewp.items():
    for state,country in v.items():
        if(state==inpt2):
            country_print = country
            cities_print.append(str(city))
            break
        else:
            continue
#print(str(cities_print))
strng =" "
for i in cities_print:
    strng = strng + str(i) + ", "
strng = strng[:-2]

strng[:-1]
print(str(inpt2)+" is in "+str(country_print)+" and cities within are "+strng)
