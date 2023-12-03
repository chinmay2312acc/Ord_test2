# Question 16(b)# Student name:
Standard_Postal_List = ["Netherlands","Denmark","Poland","Portugal","Finland","Romania","France","Germany","Greece","Spain","Hungary","Sweden","Ireland"]

user_country = input("enter your home coutntry")
if Standard_Postal_List.count(user_country) == 1 :
    print("This country uses standard postage and packaging cost ")
else :
    print("this country is not on the approved list")
    user_choice = input("Would you like to add this country to the approved Postal List for future deliveries, y/n: ")
    if user_choice == "y" :
        print(user_country,"has been added to the Standard Postal List")
        Standard_Postal_List.append(user_country)
        Standard_Postal_List.sort()
        print(Standard_Postal_List)
        
    else :
        print("this coutnry wont be added to the list ")