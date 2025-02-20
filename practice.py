a = 'Janah'
print(a)
print(a[::-1])

print("4/2 is >> ", 4/2)


#functions 
def add_numbers(a, b):
    return a+b

result = add_numbers(5,5)
print(f"Sum: {result}")

def greet(name="Guest"):
    print(f"Hello, {name}")
    
greet("Janah")
greet()


#Classss
class Patient:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
        
    def display_info(self):
        print(f"Patient Name: {self.name}, Age: {self.age}")
        
#Creating object 
patient1 = Patient("Jane Doe", 30)
patient1.display_info()
        
# Class Inheritance 
class Employee: 
    def __init__(self, name, role):
        self.name = name
        self.role = role
        
    def work(self):
        print(f"{self.name} is working as {self.role}")
            
class Developer(Employee):
    def __init__(self, name, prog_language):
        super().__init__(name, "Developer")
        self.language = prog_language
        
    def code(self):
        print(f"{self.name} is coding in {self.language}")
      
dev = Developer("Janah", "Python")
dev.work()
dev.code()


fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)


for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")


# Create a list of squares
squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

# Filter even numbers
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)  # [0, 2, 4, 6, 8]

person = {"name": "Janah", "age": 28, "city": "Manila"}

# Loop through keys
for key in person:
    print(key)

# Loop through values
for value in person.values():
    print(value)

# Loop through key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")
