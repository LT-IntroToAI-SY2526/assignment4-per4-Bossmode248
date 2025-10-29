# object oriented programming

# (define-struct dog [fur_color name age favorite_food])

class Dog: 
    """
    a simple dog class to learn OOP concepts. 


    Attributes:
        Breed- the breed of the dog
        fur_color: color of the dogs fir
        name: name of the dog
        age: age of the dog 
    """
    def __init__(self, breed = "lol", fur_color = "black", age = "1000", name = "Lebron James"):
        """initialize a new dog with breed, fur color, name, and age."""
        self.breed = breed 
        self.fur_color = fur_color
        self.age = age
        self.name = name
    def __str__(self):
        """String representation of a dog"""
        return f"{self.name} is a {self.age} year old {self.fur_color} {self.breed}"
    def bark(self):
        return f"{self.name} says wolf wolf"
    def birthday(self):
        self.age =+ 1
    def paintDog(self, new_color):
        self.fur_color = new_color
        

if __name__ == "__main__":
    berg_dog = Dog("labrador", "black", "Logan", 9)
    aidan_dog = Dog("lab pit", "grey", "cubby", 9)
    print(berg_dog)
    print(berg_dog.bark)