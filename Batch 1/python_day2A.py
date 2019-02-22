
worldmap = {"Mumbai":{"MS":"India"},"Pune":{"MS":"India"},"Kolhapur":{"MS":"India"},"Nagpur":{"MS":"India"},"Ankleshwar":{"GJ":"India"},"Baroda":{"GJ":"India"},"Surat":{"GJ":"India"},"Indore":{"MP":"India"}}

def updateDB():
    #worldmap = {"Mumbai":{"MS":"India"},"Pune":{"MS":"India"},"Kolhapur":{"MS":"India"},"Nagpur":{"MS":"India"},"Ankleshwar":{"GJ":"India"},"Baroda":{"GJ":"India"},"Surat":{"GJ":"India"},"Indore":{"MP":"India"}}
    city_input = input("\nPlease enter city name = ")
    state_input = input("\nPlease enter state name = ")
    country_input = input("\nPlease enter country name = ")

    worldmap[city_input] = {state_input:country_input}

    print("\n\nThank you for updation! Updated database:\n")
    for city,v in worldmap.items():
        for state,country in v.items():
            print(str(city)+"  "+str(state)+"  "+str(country))

def checkDB():
    chek1 = input("\nDo you want to check city details? =")
    if(chek1=="y"):
        check_city()
    else:
        check_cities()


def check_city():
    inpt2 = input("\nEnter city name = ")
    for city,v in worldmap.items():
        if(city==inpt2):
            for state,country in v.items():
                print(str(inpt2)+" is in "+str(state)+" state and in "+str(country))
                break
        else:
            continue


def check_cities():
    chek2 = input("\nDo you want to check state's city names? =")
    if(chek2=="y"):
        inpt3 = input("\nEnter state name = ")
        for city,v in worldmap.items():
            for state,country in v.items():
                if(state==inpt3):
                    print(str(city))
                    break
                else:
                    continue
    else:
        print("\nYou wasted your time!\n")

#----------------Main prgram--------------------------------
choice = input("\nDo you want to update database? (y/n) = ")

if(choice=="y"):
    updateDB()
else:
    choice2 = input("\nDo you want to check database? \(y/n\) = ")
    if(choice2=="y"):
        checkDB()
    else:
        print("\nYou wasted your time!\n")
