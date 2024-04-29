class Animal:
    animals_list = []

    def __init__(self, animal_type, legs):
        self.animal_type = animal_type
        self.legs = legs
        if self.animal_type not in self.animals_list:
            self.animals_list.append(self.animal_type)

    def display_lists(self):
        print(self.animals_list)

    def describe_animal(self):
        print(f"The {self.animal_type} has {self.legs} legs.")
    
    def sort_animals(self):
        self.animals_list.sort()
        print(self.animals_list)
    
    def compare_legs(self, other):
        if self.legs > other.legs:
            print(f"{self.animal_type} > {other.animal_type}.")
        elif self.legs < other.legs:
            print(f"{self.animal_type} < {other.animal_type}.")
        else:
            print(f"{self.animal_type} = {other.animal_type}.")
    

dog = Animal("Dog", 4)
spider = Animal("Spider", 8)
bird = Animal("Bird", 2)
crab = Animal("Crab", 6)

dog.describe_animal()
# dog.display_lists()

spider.describe_animal()
# spider.display_lists()

dog.compare_legs(spider)
bird.sort_animals()
class Animal:
    animals_list = []

    def __init__(self, animal_type, legs):
        self.animal_type = animal_type
        self.legs = legs
        if self.animal_type not in self.animals_list:
            self.animals_list.append(self.animal_type)

    def display_lists(self):
        print(self.animals_list)

    def describe_animal(self):
        print(f"The {self.animal_type} has {self.legs} legs.")
    
    def sort_animals(self):
        self.animals_list.sort()
        print(self.animals_list)
    
    def compare_legs(self, other):
        if self.legs > other.legs:
            print(f"{self.animal_type} > {other.animal_type}.")
        elif self.legs < other.legs:
            print(f"{self.animal_type} < {other.animal_type}.")
        else:
            print(f"{self.animal_type} = {other.animal_type}.")
    

dog = Animal("Dog", 4)
spider = Animal("Spider", 8)
bird = Animal("Bird", 2)
crab = Animal("Crab", 6)

dog.describe_animal()
# dog.display_lists()

spider.describe_animal()
# spider.display_lists()

dog.compare_legs(spider)
bird.sort_animals()