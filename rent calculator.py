#rent calculator in python
#we need to take operators/ input from the user
  #total rent 
  #total food/groceries oredered
  #electricity units speed
  #charge per unit 
  #persons living in room/flat 

 #then use operator (+, //) hence output will occur

rent =int(input("Enter your hostel/flat rent = "))
food =int(input("Enter the total amount of food/groceries ordered ="))
electricity_used =int(input("Enter the total of electricity used in units ="))
charge_per_unit =float(input("Enter the charge per unit ="))

persons =int(input("Enter the number of persons living in room/flat ="))

total_electricity_bill = electricity_used * charge_per_unit
print("\nTotal bill of Electricity: ",total_electricity_bill)

output= (food+ rent+ total_electricity_bill)//persons
print("\nEach person will pay= ₹", output)