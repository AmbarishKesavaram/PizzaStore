from DeluxePizza import DeluxePizza

#---------------------------------

#---------------------------------

# This program gives user choice to select and sell pizza in Papa johns pizzeria
# This is a driver class.
# Modified within the program, shows 3 attempts for password entry. If invalid password entered, displays remaining attempts.


def orderPizza():
    while True:
        size = input("Size of Pizza: (Enter small/medium/large):")
        if size in ["small","medium","large"]:
            break
        else:
            print("Please enter valid input")

    cheese = int(input("Please enter no. of cheese toppings:"))
    pepperoni = int(input("Please enter no. of pepperoni toppings:"))
    mushroom = int(input("Please enter no. of mushroom toppings:"))
    veggie = int(input("Please enter no. of veggie toppings:"))
    while True:
        stuffedCheese = input("Should pizza base be stuffed with cheese? True/False :")
        if stuffedCheese in ["true","True","TRUE"]:
            stuffedCheese = bool(True)
            break
        elif stuffedCheese in ["false","False","FALSE"]:
            stuffedCheese = bool(False)
            break
        else:
            print("Please enter True/False!!")

    return DeluxePizza(size,cheese,pepperoni,mushroom,stuffedCheese,veggie)

def pizzasOfSizes(size):
    print("List of size pizzas sold today:")
    for i in range(len(todaysPizzas)):
        if todaysPizzas[i-1] != None :
            if todaysPizzas[i-1].get_size() == size:
                print(todaysPizzas[i - 1].__str__())
                print("\tPrice: $" + str(todaysPizzas[i - 1].calCost()) + "\n\n")

def cheaperThan(highest):
    dicts = {}
    for i in range(len(todaysPizzas)):
        if todaysPizzas[i-1] != None:
            if highest >= todaysPizzas[i-1].calCost():
                dicts[i] = todaysPizzas[i-1].calCost()
    return dicts

def lowestPrice():
    cost = []
    for i in range(len(todaysPizzas)):
        if todaysPizzas[i - 1] != None:
            cost.append(todaysPizzas[i - 1].calCost())
    return cost.index(min(cost))

def highestPrice():
    cost = []
    for i in range(len(todaysPizzas)):
        if todaysPizzas[i - 1] != None:
            cost.append(todaysPizzas[i - 1].calCost())
    return cost.index(max(cost))

def numberOPizzasOfSize(size):
    count = 0
    for i in range(len(todaysPizzas)):
        if todaysPizzas[i - 1] != None:
            if size == todaysPizzas[i - 1].get_size():
                count +=1
    return count

print("Welcome to Papa Johns!!")
totalPizzas = int(input("Maximum Number of Pizzes to prepare today:"))
todaysPizzas = [None]*totalPizzas
pizzasOrdered = 0
prompt = True

while prompt:
        print("Papa John, what do you want to do?")
        print("1.   Enter a new pizza order (password required)")
        print("2.   Change information of a specific order (password required)")
        print("3.   Display details for all pizzas of a specific size (s/m/l)")
        print("4.   Statistics on today’s pizzas")
        print("5.   Quit")
        options = 1
        try:
           choice =  int(input("Please enter your choice >"))
           if choice == 1:
               while options <= 3:
                   password = input("Please enter password:")
                   if password == "deluxepizza":
                       while True:
                           pizzas = int(input("Number of pizzas to enter?"))
                           if pizzas <= (totalPizzas - pizzasOrdered):
                               for pizza in range(pizzas):
                                   todaysPizzas[pizza] = orderPizza()
                                   pizzasOrdered +=1
                               break
                           else:
                               print("Pizza limit exceded!! Please give smaller number")

                       prompt = True

                       break
                   else:
                       options += 1
                       if options == 4:
                           print("You are out off options!!")
                           prompt = True
                       else:
                           print("Wrong Password.. You have "+ str(4 - options)+" more time to enter right password!!")
                           prompt = False

           elif choice == 2:
               while options <= 3:
                   password = input("Please enter password:")
                   if password == "deluxepizza":
                       while True:
                           updatePizza = int(input("Enter pizza number you wish to update:"))
                           if updatePizza <= len(todaysPizzas) and todaysPizzas[updatePizza-1] != None:
                               print( todaysPizzas[updatePizza-1].__str__())
                               print("\tPrice: $"+str(todaysPizzas[updatePizza-1].calCost())+"\n\n")

                               while True:
                                   print("Papa Johns,  what would you like to change?")
                                   print("\t1 - Size")
                                   print("\t2 - Cheese filled or not")
                                   print("\t3 - Number of cheese toppings")
                                   print("\t4 - Number of pepperoni toppings")
                                   print("\t5 -	Number of mushroom toppings")
                                   print("\t6 -	Number of vegetable toppings")
                                   print("\t7 - Quit")
                                   updateOption = int(input("Enter choice >"))

                                   if updateOption == 1:
                                       while True:
                                           size = input("Enter new size: small/medium/large")
                                           if size in ["small","medium","large"]:
                                                todaysPizzas[updatePizza-1].set_size(size)
                                                break
                                           else:
                                               print("Enter correct size!!")

                                   elif updateOption == 2:
                                       while True:
                                           stuffedCheese = input("Change pizza base.. stuff with cheese? True/False :")
                                           if stuffedCheese in ["true", "True", "TRUE"]:
                                               stuffedCheese = bool(True)
                                               todaysPizzas[updatePizza-1].set_stuffedWithCheese(stuffedCheese)
                                               break
                                           elif stuffedCheese in ["false", "False", "FALSE"]:
                                               stuffedCheese = bool(False)
                                               todaysPizzas[updatePizza - 1].set_stuffedWithCheese(stuffedCheese)
                                               break
                                           else:
                                               print("Please enter True/False!!")

                                   elif updateOption == 3:
                                       cheese = int(input("Change no. of cheese toppings:"))
                                       todaysPizzas[updatePizza - 1].set_no_of_cheese_toppings(cheese)


                                   elif updateOption == 4:
                                       pepperoni = int(input("Change no. of pepperoni toppings:"))
                                       todaysPizzas[updatePizza - 1].set_no_of_pepperoni_toppings(pepperoni)

                                   elif updateOption == 5:
                                       mushroom = int(input("Change no. of mushroom toppings:"))
                                       todaysPizzas[updatePizza - 1].set_no_of_mushroom_toppings(mushroom)

                                   elif updateOption == 6:
                                       vegetable = int(input("Change no. of vegetable toppings:"))
                                       todaysPizzas[updatePizza - 1].set_veggieToppings(vegetable)
                                   elif updateOption == 7:
                                       print(todaysPizzas[updatePizza - 1].__str__())
                                       print("\tPrice: $" + str(todaysPizzas[updatePizza - 1].calCost()) + "\n\n")
                                       break
                                   else:
                                       print("Please enter numbers between 1 and 7")
                               break

                           else:
                               print("Invalid pizza number..")
                               pizzaUpdatePrompt = input("Do you want to re-enter the pizza number to update? Yes/No")
                               if(pizzaUpdatePrompt in ["yes","Yes","YES"]):
                                   continue
                               elif(pizzaUpdatePrompt in ["no","No","NO"]):
                                   break
                               else:
                                   break


                       prompt = True
                       break


                   else:
                       options += 1
                       if options == 4:
                           print("You are out off options!!")
                           prompt = True
                       else:
                           print("Wrong Password.. You have " + str(4 - options) + " more time to enter right password!!")
                           prompt = False

           elif choice == 3:
               while True:
                   pizzaSize = input("Please enter the size of pizza you want to know details about.. (small/medium/large)")
                   if pizzaSize in ["small","medium","large"]:
                       pizzasOfSizes(pizzaSize)
                       count = 0
                       for i in range(len(todaysPizzas)):
                           if todaysPizzas[i-1] != None :
                                if pizzaSize == todaysPizzas[i-1].get_size() :
                                    count +=1

                       print("Our Chef, made "+ str(count) +" "+ pizzaSize +" size pizza today ")
                       break
                   else:
                       print("Please enter valid size")

               prompt = True

           elif choice == 4:
               while True:
                   print("Papa John, what information would you like?")
                   print("\t1.	Cost and details of cheapest pizza")
                   print("\t2.	Cost and details of most costly pizza")
                   print("\t3.	Number of pizzas sold today")
                   print("\t4.	Number of pizzas of a specific size")
                   print("\t5.	Average cost of pizzas")
                   print("\t6.	Quit")

                   info = int(input("Enter your choice >"))

                   if info == 1:
                       index = lowestPrice()
                       print(todaysPizzas[index].__str__())
                       print("\tPrice: $" + str(todaysPizzas[index].calCost()) + "\n\n")
                   elif info == 2:
                       index = highestPrice()
                       print(todaysPizzas[index].__str__())
                       print("\tPrice: $" + str(todaysPizzas[index].calCost()) + "\n\n")
                   elif info == 3:
                       count = 0
                       for i in range(len(todaysPizzas)):
                           if todaysPizzas[i-1] != None:
                               count += 1
                       print("Number of pizzas sold today: "+str(count))

                   elif info == 4:
                       size = input("Size of pizza: (small/medium/large) ")
                       print("Number of pizzas of "+size+" size: "+ str( numberOPizzasOfSize(size)))
                   elif info == 5:
                       costliest = todaysPizzas[highestPrice()].calCost()
                       costs = list(cheaperThan(costliest).values())
                       avg = sum(costs)/len(costs)

                       print("Average cost of pizzas is:"+str(avg))
                   elif info == 6:
                       break
                   else:
                       print("Please enter numbers between 1 and 6")


               prompt = True

           elif choice == 5:
               print("Thank you for choosing Papa Johns Pizzeria!! See you next time")

               prompt = False
           else:
               print("Please choose between 1 and 5")
               prompt = True
        except ValueError:
            print("Please input a number")
            prompt = True




