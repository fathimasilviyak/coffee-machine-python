# coffee-machine-python

### A virtual coffee machine using python that takes inputs from user to make the desired type of coffee
If the coffee machine is on, the user can choose the type of coffee he want. There are 3 types of coffee available

1. Espresso
2. Latte
3. Cappuccino

If the user's input is "off" then the coffee machine will be turn off.

Each type of the coffee requires different amount of ingrediences. Such as water, milk, and coffee powder. When the user want to get the report from the coffee machine, he can simply enter "report", and it will shows the available amount of ingredients, with their current profit.

Report, before the purchase:
* Water: 300ml
* Milk: 200ml
* Coffee: 100g
* Money: $0

When the user inputs the type of coffee he wants, the coffee machine will check the availability of the required amount of ingredients.

If any of the incredients are insufficient to make the coffee, then it will inform the user that the particular ingredient is not available, otherwise it will ask the user to insert the coins. 

The user can insert four kinds of coins:

* Quarters = $0.25
* Dimes = $0.10
* Nickles = $0.05
* Pennies = $0.01

The coffe machine will then process the coins to find the total paid amount in dollar.

Each type of the coffee has different cost. 

If the user inserted enough money to purchase the drink they selected, then the cost of the drink gets added to the machine as the profit, and the ingredients to make the drink will be deducted from the coffee machine resources, and these will be reflected the next time report is printed.

If the user doesnt provide enough money then he will get a message that says "Sorry that's not enough money, money refunded".
 
If he inserts more money, the machine will offer the coffe with the change. 


  
