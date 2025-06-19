menu = {
  "pizza": 90,
  "pasta": 80,
  "salad": 70,
  "soup": 60,
  "sandwich": 50,
}

order_total=0
number_of_items=0

print("Welcome to the restaurant!")

print("Here is our menu:")
for item, price in menu.items():
  print(f"{item}: ${price}")

item=input("What would you like to order? ")
number_of_items =int(input("How many would you like to order? "))

for item in menu :
  if item in menu:
    order_total += menu[item] * number_of_items
    print(f"Your order total is now: ${order_total}")
    another_item = input("Would you like to order anything else? (yes/no) ")
    if another_item == "no":
      print(f"Your final order total is: ${order_total}")
      break
    elif another_item == "yes":
      item = input("What would you like to order? ")
      continue
    elif another_item != "yes" and another_item != "no":
      print("we don't have that item in our menu")
      break

print("Thank you for your order!")
print("Your order will be ready soon!")
print("Have a nice day!")
      
      