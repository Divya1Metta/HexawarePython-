
# Day10
## unpacking operator 
```
python
#Strings,touples are immutable
#len() can be used on-->string,list,tuple
#merging lists
t1=[80,90]
t2=[50,60]
t3=[*t1,*t2]
print(t3)
print(t1+t2)

#unpacking ->**dict
movie={
    'name':'Khaidi',
    'year':2020
}
#copy
mv1={**movie,"actor":"Karthi"}
print(mv1)
#overrides what ever is in given last
mv2={**movie,"actor":"Karthi",'year':2021}
mv3={"actor":"Karthi",'year':2021,**movie}
print(mv2,mv3)






coordinates=[(5,4),(1,1),(6,10),(9,10)]
distance=[]

#task 1.1 ->for loop  root x**2+y**2
for cord in coordinates :
    x=cord[0]
    y=cord[1]
    d=(((x**2)+(y**2))**0.5)
    distance.append(d)
print(distance)
#task 1.2 ->for loop+unpacking
distance=[]
for cord in coordinates :
    x,y=cord
    distance.append(((x**2)+(y**2))**0.5)
print(distance)
#task 1.3  ->unpacking+list comprehension
distance=[round(((x**2)+(y**2))**0.5,2) for x,y in coordinates]
print(distance)

person = {
    "name": "Lionel Messi",
    "age": 36,
    "address": {
        "city": "rosario",
        "country": "Argentina",
    },
    # "stats": {"goals": 300, "assists": 500},
    "sport": "football",
    # "height": 168,
}
 
# print(person["stats"]["goals"]) # KeyError: 'stats'
# print(person.get("stats").get("goals")) # 'NoneType' object has no attribute 'get'
 
# Default value - person.get(key, default value)
print(person.get("height", 174))
 
print(person.get("stats",{}).get("goals"))
      

person = {
    "name": "Lionel Messi",
    "age": 36,
    "address": {
        "city": "rosario",
        "country": "Argentina",
    },
    # "stats": {"goals": 300, "assists": 500},
    "sport": "football",
    # "height": 168,
}
 
# print(person["stats"]["goals"]) # KeyError: 'stats'
# print(person.get("stats").get("goals")) # 'NoneType' object has no attribute 'get'
 
# Default value - person.get(key, default value)
print(person.get("height", 174))
print(person.get("stats", {}).get("goals"))  # None
print(person.get("stats", {"goals": 0}).get("goals"))  # None


employees = [
    {"name": "A", "experience":1},
    {"name":"B"},
    {"name":"C","experience":5},
]
#updation of experience by 1 for everyone
for employee in employees:
    employee["experience"]=employee.get("experience",0) + 1
print(employees)

#status to be added senior 5 or more,mid 3-5,jnr<3

for employee in employees:
    experience = employee.get("experience")
    if experience < 3:
        employee["status"] = "Junior"
    elif experience < 5:
        employee["status"] = "Mid-Level"
    else:
        employee["status"] = "Senior"


# a = 10
# b = 10
# c = 10
 
 
# Multiple variable assignment
a = b = c = 10
print(a, b, c)
 
 
# Unpacking / Destructuring
# poojitha, shivam, samar = ("Black current", "Choco chip", "Butterscotch") # Tuple
poojitha, shivam, samar = "Black current", "Choco chip", "Butterscotch"  # Tuple
 
print(poojitha)
print(shivam)
print(samar)
 
movies = ["Mission Impossible", "JJK", "Avengers Infinity War"]
# mathesh = movies[0]
# nandhini = movies[1]
# devesh  = movies[2]
 
mathesh, nandhini, devesh = movies
print(mathesh, nandhini, devesh)
 
 
# t1, t2, t3 = [100, 200, 300, 400]
# print(t1, t2, t3)  # ❌
 
 
# t1, t2, t3, _ = [100, 200, 300, 400]
# print(t1, t2, t3)  # _ -> skip
 
 
# t1, _ , t2, t3, = [100, 200, 300, 400]
# print(t1, t2, t3)  # 100 300 400
 
# * -> Unpacking operator
# t1, t2, *t3 = [100, 200, 300, 400, 60, 40, 30]
# print(t1, t2, t3)  # 100 200 [300, 400, 60, 40, 30]
 
 
# * -> Unpacking operator
t1, t2, *t3 = (100, 200, 300, 400, 60, 40, 30)
print(t1, t2, t3)  # 100 200 [300, 400, 60, 40, 30]
 
 
# Task 1
coordinates = [(5, 4), (1, 1), (6, 10), (9, 10)]
 
# For each point find the distance from origin
 
# Task 1.1 - for loop
 
# distances = []
# for cord in coordinates:
#     x = cord[0]
#     y = cord[1]
#     d = (x**2 + y**2) ** 0.5
#     distances.append(d)
 
# print(distances)
 
# Task 1.2 - for loop + unpacking
 
# distances = []
# for cord in coordinates:
#     x, y = cord
#     d = (x**2 + y**2) ** 0.5
#     distances.append(d)
 
# print(distances)
 
coordinates = [(5, 4), (1, 1), (6, 10), (9, 10)]
distances = []
for x, y in coordinates:
    d = (x**2 + y**2) ** 0.5
    distances.append(round(d, 2))
 
print(distances)
 
 
# Task 1.3 - unpacking + list comprehension
 
 
distances = [round((x**2 + y**2) ** 0.5, 2) for x, y in coordinates]
print(distances)
# Output
# [6.4, 1.414, 11.66, 13.45]
 
 
# t1, t2, *z1, t3 = (100, 200, 300, 400, 60, 40, 30)
t1, t2, *_, t3 = (100, 200, 300, 400, 60, 40, 30)
print(t1, t2, t3)
 
# Copy
marks1 = [70, 80, 60]
# marks2 = [*marks1] # copy - 1. slice    2. .copy()
marks2 = [*marks1, 75, 68]
marks3 = [100, 60, *marks1, 75, 68]
print(marks2)
print(marks3)
 
# Merging multiple lists
t1 = [80, 90]
t2 = [50, 60]
t3 = [*t1, *t2]  # t1 + t2
 
print(t3)
 
# t3 = [80, 90, 50, 60]
 
# Unpacking -> ** Dict
movie = {"name": "John wick", "year": 2014}
 
# Copy
mv1 = {**movie, "actor": "Keanu Reeves"}
mv2 = {**movie, "actor": "Keanu Reeves", "year": 2015}
mv3 = {"actor": "Keanu Reeves", "year": 2015, **movie}
print(mv1)
print(mv2)
print(mv3)
print(movie)
 
# Dict - No duplicate keys
 

# Why?: Motivation of function
 
 
a = 8
b = 10
 
print("The sum is: ", a + b)
 
 
a1 = 60
b1 = 70
 
print("The sum is: ", a1 + b1)
 
a2 = 600
b2 = 70
 
print("The sum is: ", a2 + b2)
 
 
# Function
# 1. Declaration / Definition
# 2. Function name
# 3. Parameters - 2
# 4. Function body
def add(a, b):
    return round(a + b, 2)
 
 
# Function call
print("The sum is: ", add(8, 10))
print("The sum is: ", add(60, 70))
print("The sum is: ", add(600, 70))  # arguments
print("The sum is: ", add(60.748494, 70.89898))
print("The sum is: ", add(160.748494, 170.89898))
 
 
# Default values
def driving_test(name, age, car="Dezire"):
    if age >= 18:
        return f"{name} eligible for driving. You will be tested in {car}"
    else:
        return "Try again after few years 👶🍼"
 
 
print(driving_test("Sai Subash", 20, "Creata"))
print(driving_test("Sai Ganesh", 20))
 
 
# Types of argument
# 1. Position argument
# 2. Keyword argument
 
# Position argument
# print(driving_test(20, "Poojitha"))
 
# Keyword argument
print(driving_test(age=20, name="Poojitha"))
print(driving_test("Abishek", car="Honda city", age=20))
 

library_list = [

    {

        "title": "Python Programming",

        "author": "Eric Matthes",

        "year": 2019,

        "available": True

    },

    {

        "title": "Automate the Boring Stuff with Python",

        "author": "Al Sweigart",

        "year": 2020,

        "available": True

    },

    {

        "title": "Learning Python I",

        "author": "Mark Lutz",

        "year": 2013,

        "available": False

    },

    {

        "title": "Fluent Python",

        "author": "Luciano Ramalho",

        "year": 2015,

        "available": True

    },

    {

        "title": "Adavance Python",

        "author": "Mark Lutz",

        "year": 2015,

        "available": False

    },

]

#Task 1 write a funtion add_book(library,book)
def add_book(library_list,new_book):
    library_list.append(new_book)
add_book(library_list,{

        "title": "java",

        "author": "ABC",

        "year": 2022,

        "available": True

    },
)
print(library_list)
# Task 2
# Search books by author
# Write a function serach_by_author(library, author_name)
def find_book(library_list,author_name):
    for book in library_list:
        if book["author"]=="author_name":
            print(book)
print(find_book(library_list,"Luciano Ramalho"))       

#alternative
def find_book(library_list,author_name):
    return [book for book in library if book["author"]=="author_name" ]
# Task 3
# Check Out Book Function: Write a function check_out_book(library, title) 
# that marks a book as not available if it exists and is available in the library.

def check_out_book(library,title):
    for book in library:
        if (book["title"] == title and book["available"]==True):
            book["available"]=False
            return f"{title} is available for check out"
        elif (book["title"] == title and book["available"]==False):
            return f" {title} is unavailable for check out"
    return f"{title}  not found"
print(check_out_book(library_list,'Adavance Python'))




movies = [
    {
        "title": "Inception",
        "ratings": [5, 4, 5, 4, 5]
    },
    {
        "title": "Interstellar",
        "ratings": [5, 5, 4, 5, 4]
    },
    {
        "title": "Dunkirk",
        "ratings": [4, 4, 4, 3, 4]
    },
    {
        "title": "The Dark Knight",
        "ratings": [5, 5, 5, 5, 5]
    },
    {
        "title": "Memento",
        "ratings": [4, 5, 4, 5, 4]
    },
]
# Function
# Task 1
# get_movies_avg_rating
from pprint import pprint
def movie_avg_rating(movies):
    for movie in movies:
        movie["average_rating"]=sum(movie["ratings"])/len(movie["ratings"])
    return movies
pprint(["average_rating"])   
 
# Task 2 - break it into 2 functions
 
 
# Expected Output
# output = [
#     {"title": "Inception", "ratings": [5, 4, 5, 4, 5], "average_rating": 4.6},
#     {"title": "Interstellar", "ratings": [5, 5, 4, 5, 4], "average_rating": 4.2},
#     {"title": "Dunkirk", "ratings": [4, 4, 4, 3, 4], "average_rating": 4.1},
#     {"title": "The Dark Knight", "ratings": [5, 5, 5, 5, 5], "average_rating": 5},
#     {"title": "Memento", "ratings": [4, 5, 4, 5, 4], "average_rating": 4.2},
# ]
 

#Idea
# Object Oriented Programming
# Modeling our problem as real-world objects
 
# Car
# What makes a car?
# 1. engine
# 2. wheels
# 3. name
# 4. doors
 
 
#  Car
# 1. engine - v8
# 2. wheels - 4
# 3. name - Ferrari
# 4. doors - 2
 
 
# 1. engine - v4
# 2. wheels - 4
# 3. name - Alto
# 4. doors - 4
 
 
#  Car -> blueprint | Class blueprint object
 
 
class Car:
    def __init__(
        self, name, engine, wheels, doors
    ):  # creating object calls init (constructor)
        self.name = name
        self.engine = engine
        self.wheels = wheels
        self.doors = doors
 
 
ferrari = Car("Ferrari", "v8", 4, 2)  # object
alto = Car("Alto", "v4", 4, 4)  # object
 
print(ferrari.name, ferrari.wheels)
 
```
