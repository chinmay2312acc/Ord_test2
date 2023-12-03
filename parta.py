print("Welcome to the new online ordering system.\n")
total_cost = 0
current_balance = int(input("enter the customers balance right now : "))
#items_count = 1
user_name = input("Please enter your username : ")
quantity = int(input("how many items you wanna enter :"))
if quantity>0 :
    for i in range(quantity) :
        price_of_item = float(input("Enter the price of item {}".format(quantity)+  ":£"))
        total_cost+=price_of_item
    if current_balance>total_cost :
        print("your remaining balance : ",(current_balance-total_cost))
    
    else :
        print("you dont have enough balance , you owe : ",total_cost-current_balance)
        print("You entered",quantity,"items and the total is €",total_cost)
        print("the member of staff who processed your order was : ",user_name)
else :
    print("invalid option ")