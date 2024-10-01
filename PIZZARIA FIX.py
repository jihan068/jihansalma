# SAVING MENU USER OPTION
user_option = ""
# SAVING CRUST USER OPTION
user_crust = ""
# SAVING SIZE USER OPTION
user_size = ""
# SAVING EXTRA CHEESE USER OPTION
user_cheese = ""
# PRICE
price = 0
# ALL VARIANT PRICE Rp.50.000
# DISPLAY AND ASK MENU
print ("============= WELCOME TO PIZZARIA FASTBEAR =============")
print ("CHOOSE YOUR FAVORITE PIZZA")
print ("MENU\t\t\t| PRICE")
print (f"1. Frankfurter BBQ \t| Rp. 50.000")
print (f"2. Monsta Meat\t\t| Rp. 50.000")
print (f"3. Super Supreme \t| Rp. 50.000")
print (f"4. Chicken Lovers \t| Rp. 50.000")
print (f"5. Cheese Lovers \t| Rp. 50.000")
print (f"6. Sausage Cheese \t| Rp. 50.000")
menu_choice = input("Select your Pizza: ")
# MENU LOGICAL
if menu_choice == "1":
    price += 50000
    user_option = "Frankfurter BBQ"
elif menu_choice == "2":
    price += 50000
    user_option = "Monsta Meat"
elif menu_choice == "3":
    price += 50000
    user_option = "Super Supreme"
elif menu_choice == "4":
    price += 50000
    user_option = "Chicken Lovers"
elif menu_choice == "5":
    price += 50000
    user_option = "Cheese Lovers"
elif menu_choice == "6":
    price += 50000
    user_option = "Sausage Cheese"
else:
    print ("input the correct value!!")
# DISPLAY AND ASK CRUST
print (f"\nChoose your Crust Choice")
print ("CRUST\t\t| PRICE")
print (f"1. Pan Crust\t| FREE")
print (f"2. Sausage Crust| Rp. 7.000")
print (f"3. Cheesy Crust\t| Rp. 7.000")
crust_choice = input(f"Crust for your pizza: ")
# CRUST LOGICAL
if crust_choice == "1":
    price += 0
    user_crust = "Pan Crust"
elif crust_choice == "2":
    price += 7000
    user_crust = "Sausage Crust"
elif crust_choice == "3":
    price += 7000
    user_crust = "Cheesy Crust"
else:
    print ("Value didn't exist, we set to default")
    crust_choice == "1"
    user_crust = "Pan Crust"
    price += 0

# DISPLAY AND ASK SIZE
print (f"\nChoose your Pizza Size")
print ("SIZE\t\t| PRICE")
print (f"1. Personal\t| FREE")
print (f"2. Medium\t| Rp. 10.000")
print (f"3. Large\t| Rp. 15.000")
size_choice = input("Size Pizza: ")
# SIZE LOGICAL
if size_choice == "1":
    price += 0
    user_size = "Personal"
elif size_choice == "2":
    price += 10000
    user_size = "Medium"
elif size_choice == "3":
    price += 15000
    user_size = "Large"
else:
    print ("Value didn't exist, we set to default")
    size_choice == "1"
    user_size = "Personal"
    price += 0

# ASK FOR EXTRA CHEESE
extra_cheese = input("\nDo you want to add Extra Cheese for Rp.13.000? (yes/no): ")
# EXTRA CHEESE LOGICAL
if extra_cheese == "yes":
    price += 13000
    user_cheese = "With Extra Cheese"
elif extra_cheese == "no":
    price += 0
    user_cheese = "No Extra Cheese"
else :
    print ("Value didn't exist, we set to default")
    extra_cheese == "no"
    price += 0

print (F" ============= SUMMARY ORDER =============")
print (f"PIZZA\t\t: {user_option}\nCRUST\t\t: {user_crust}\nSIZE\t\t: {user_size}\nEXTRA CHEESE\t: {user_cheese}")
print (F" ============= TOTAL BILL =============")
print (f"THANKYOU FOR ORDERING IN PIZZARIA FASTBEAR")
print (f"Your Total bill is: Rp.{price:3,.0f}")
print (F" ============= END OF RECEIPT =============")

