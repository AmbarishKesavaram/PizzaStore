class Pizza:
    def __init__(self,size,no_of_cheese_toppings,no_of_pepperoni_toppings,no_of_mushroom_toppings):
        self.size = size;
        self.no_of_cheese_toppings= no_of_cheese_toppings
        self.no_of_pepperoni_toppings = no_of_cheese_toppings
        self.no_of_mushroom_toppings = no_of_cheese_toppings

    def get_size(self):
        return self.size
    def set_size(self,size):
        self.size = size

    def get_no_of_cheese_toppings(self):
        return self.no_of_cheese_toppings
    def set_no_of_cheese_toppings(self, no_of_cheese_toppings):
        self.no_of_cheese_toppings = no_of_cheese_toppings

    def get_no_of_pepperoni_toppings(self):
        return self.no_of_pepperoni_toppings
    def set_no_of_pepperoni_toppings(self,no_of_pepperoni_toppings):
        self.no_of_pepperoni_toppings = no_of_pepperoni_toppings

    def get_no_of_mushroom_toppings(self):
        return self.no_of_mushroom_toppings
    def set_no_of_mushroom_toppings(self,no_of_mushroom_toppings):
        self.no_of_mushroom_toppings = no_of_mushroom_toppings


    def calCost(self):
        if self.get_size() == "small":
            return (10+ 2* (self.get_no_of_cheese_toppings()+self.get_no_of_mushroom_toppings()+self.get_no_of_pepperoni_toppings()))
        elif self.get_size() == "medium":
            return (12+ 2* (self.get_no_of_cheese_toppings()+self.get_no_of_mushroom_toppings()+self.get_no_of_pepperoni_toppings()))
        elif self.get_size() == "large":
            return (14+ 2* (self.get_no_of_cheese_toppings()+self.get_no_of_mushroom_toppings()+self.get_no_of_pepperoni_toppings()))

    def __str__(self):
        return "A "+self.get_size()+" pizza size with "+ str(self.get_no_of_cheese_toppings())+" cheese, "+str(self.get_no_of_pepperoni_toppings())+" pepperoni, "+str(self.get_no_of_mushroom_toppings())+" mushroom toppings should cost $"+str(self.calCost())
