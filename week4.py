class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print("This is:", self.name, ", aged:", self.age, ", gender:", self.gender)

# Create an instance of the Person class
obj = Person("Kamau", 17, "male")

# Call the introduce method
obj.introduce()

