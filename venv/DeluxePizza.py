from Pizza import Pizza
class DeluxePizza(Pizza):
    numberOfPizzas=0
    def __init__(self,size,no_of_cheese_toppings,no_of_pepperoni_toppings,no_of_mushroom_toppings, stuffedWithCheese, veggieToppings):
        super().__init__(size,no_of_cheese_toppings,no_of_pepperoni_toppings,no_of_mushroom_toppings)
        self.stuffedWithCheese = stuffedWithCheese
        self.veggieToppings = veggieToppings
        DeluxePizza.numberOfPizzas += 1

    def get_veggieToppings(self):
        return self.veggieToppings
    def set_veggieToppings(self, veggieToppings):
        self.veggieToppings = veggieToppings

    def get_stuffedWithCheese(self):
        return self.stuffedWithCheese
    def set_stuffedWithCheese(self, stuffedWithCheese):
        self.stuffedWithCheese = stuffedWithCheese

    def get_numberOfPizzas(self):
        return self.numberOfPizzas

    def calCost(self):
        if self.get_size() == "small":
            if self.get_stuffedWithCheese() == False :
                return (10+ 2* (self.get_no_of_cheese_toppings()+self.get_no_of_mushroom_toppings()+self.get_no_of_pepperoni_toppings())+ 3*self.get_veggieToppings())
            else:
                return (10 + 2 + 2 * (self.get_no_of_cheese_toppings() + self.get_no_of_mushroom_toppings() + self.get_no_of_pepperoni_toppings())+ 3*self.get_veggieToppings())
        elif self.get_size() == "medium":
            if self.get_stuffedWithCheese() == False:
                return (12 + 2 * (self.get_no_of_cheese_toppings() + self.get_no_of_mushroom_toppings() + self.get_no_of_pepperoni_toppings())+ 3*self.get_veggieToppings())
            else:
                return (12 + 4 + 2 * (self.get_no_of_cheese_toppings() + self.get_no_of_mushroom_toppings() + self.get_no_of_pepperoni_toppings())+ 3*self.get_veggieToppings())
        elif self.get_size() == "large":
            if self.get_stuffedWithCheese() == False:
                return (14+ 2 * (self.get_no_of_cheese_toppings() + self.get_no_of_mushroom_toppings() + self.get_no_of_pepperoni_toppings())+ 3*self.get_veggieToppings())
            else:
                return (14 + 6 + 2 * (self.get_no_of_cheese_toppings() + self.get_no_of_mushroom_toppings() + self.get_no_of_pepperoni_toppings())+ 3*self.get_veggieToppings())

    def __str__(self):
        order = "Pizza #"+str(DeluxePizza.numberOfPizzas)
        order += "\n\tPizza size: "+self.get_size()
        order += "\n\tCheese filled dough: "+str(self.get_stuffedWithCheese())
        order += "\n\tNumber of cheese toppings: "+str(self.get_no_of_cheese_toppings())
        order += "\n\tNumber of Pepperoni toppings: "+str(self.get_no_of_pepperoni_toppings())
        order += "\n\tNumber of Mushroom toppings: "+str(self.get_no_of_mushroom_toppings())
        order += "\n\tNumber of vegetable toppings: "+str(self.get_veggieToppings())
        return order
