# Day-9

we can update strings or switching addresses but cannot modify as they are immutable.
```
python
name="divi"
name[0]="D"
#we cannot modify error
name="Divi"
#name gets modified
```

```
python
#Task1
# After the 🔑
message = "    🚨🔍📱🔑secret_code✌️"
code = "SECRET_CODE✌️"
index=message.find('🔑')
output=message[index+1:].upper()
if(output==code):
  print("you are the hacker ")
else:
  print("try again")
```
```
python
#Task2
#Remove junk[*,(] to find the secret
# message = "    🚨🔍📱🔑****secret_code✌️((("
message = "    🚨🔍📱🔑secret_code✌️"
code = "SECRET_CODE✌️"
index=message.find('🔑')
output=message[index+1:].upper().strip('*').strip('(')

if(output==code):
  print("you are the hacker ")
else:
  print("try again")
```

## copy by value
```
python
p1=[10,2,3]
p2=p1.copy()
p3=p1[:]
print(id(p1),id(p2),id(p3))
p1.pop(1)
p1.remove(3)
```

## copy by reference
```
python
a=[1,2,3]
a_copy=a
a1=[1,2,3]
a_copy.append(4)
a.append(5)
a1.append(6)

price_list = [1000, 1500, 400]
price_list_copy = price_list ## Copy by reference
price_list1 = [1000, 1500, 400]
 
price_list_copy.append(600)
price_list.append(700)
price_list1.append(800)
 #copy by reference
print(price_list, price_list_copy, price_list1)
print(a,a_copy,a1)
marks=[40,30,27,68,90,57]
marks.append(87)
print(marks)
print(marks[::-1])
```

```
python
quote = "Dream is something"
# print(quote[<start>: <end>: <skip>])
print(quote[1:3])  # re
print(quote[-1])  # m
```
```
pop takes index and remove takes values
 
print(quote[-4:-1])  # rea
 
 
print(quote[1:10:2])  # ra ss
print(quote[::-1])  # gnihtemos si maerD
print(quote[-1:-4:-1]) # gni
 ```
```
python
m=['Akki']*3
print(m)
#output ['Akki','Akki','Akki']
```

 
 ```
python
# Remove -> .pop(), .remove()
# Add -> .append() , .insert()
# Copy -> : (slice), copy
 
h1 = [198, 175, 140, 1777]
# h1.pop(1)
h1.remove(1777)  # pop - index | remove - value
print(h1)
 
# Repetition
cloned_treasures = ["Gold Coin"] * 3
print(cloned_treasures)
 
 
# split (str -> list) vs join (list -> str)
shop_stock = "vanilla,lime,chocolate"
shop_stock_list = shop_stock.split(",")
 
print(shop_stock_list, shop_stock_list[2])
 
avatar = ["Fire", "Water", "Earth", "Air"]
 
print(",".join(avatar))
print("|".join(avatar))
```

```
python
#reverse sentence
message="world the save to time no is there"
o=message.split()[::-1]
print(" ".join(o))
#o/p: there is no time to save the world
```

```
python
a=[1,2,3,4]
#the insertion position is mentioned in  the below statement
a[1:3]=[7,8,0,4,5]
print(a)
#o/p :[ 1, 7, 8, 0, 4, 5, 4]
```


```
python
c=1
n=int(input())
while(c<n):
    print('✨'*c)
    c=c+1
#output
5
✨
✨✨
✨✨✨
✨✨✨✨

#for loop
c=1
n=int(input())
for c in range(1,n):
    print('✨'*c)
    
```

```
python
p=[10,20,30]
for i in range(0,len(p)):
    p[i]=p[i]*2
print(p)
#output:[20, 40, 60]

#using while

c=0
while c <len(p):
  p[i]=p[i]*2
  i=i+1

#by creating a new list

p=[10,20,30]
v=[]
for i in range(len(p)):
    v.append(2*p[i])
print(v)

#list comprehension-> copy of the result
p1=[i*2 for i in p]


```python

avengers = [
    "Hulk",
    "Iron man",
    "Black widow",
    "Captain america",
    "Spider man",
    "Thor",
]
 
 
# Output
# [4, 8, 11, 15, 10, 4]
 
 
# Task 4.1 - for loop

lengths = []

for name in avengers:

    lengths.append(len(name))

print(lengths)
 heart 1
 
# Task 4.2 - List comprehension

lengths=[len(name) for name in avengers]
length of avenger in each avenger in list

#Task 5.1 - lengths greater than 10
lengths = []

for i in avengers:
      if len(i)>10:
        lengths.append(i)
print(lengths)

#Task 5.2 -list comprehension

#output
#[11,15]
output=[ len(name) for name in avengers if len(name)>10]

# Output
# [
#     "Black widow",
#     "Captain america",
# ]
output=[ name  for name in avengers if len(name)>10]
print(output)
```
# Dictionaries->Hash maps -> key:value pairs
keys should be unique doesnt allow duplicates
```
person={
        "name":"kumari",
        "age":21,
        "gender":"female"
}
#type
print(type(person))

#accessing
print(person["name"])

#modifying
person["age"]=person["age"]+1
or
person["age"]+=1

#methods
print(person.keys())
print(person.values())
```

```
python
#Task6
books = [
    {   "title": "Infinite Jest",
        "rating": 4.5,
        "genre": "Fiction"
    },
    {   "title": "The Catcher in the Rye",
        "rating": 3.9,
        "genre": "Fiction"
    },
    {  "title": "Sapiens",
        "rating": 4.9,
        "genre": "History"
    },
    {  "title": "A Brief History of Time",
        "rating": 4.8,
        "genre": "Science"
    },
    {   "title": "Clean Code",
        "rating": 4.7,
        "genre": "Technology"
    },
]
#Task- 6.1 using for loop high rated books->=4.7

high_rated=[]
for book in books:
    if(book['rating']>=4.7):
        high_rated.append(book["title"])
print(high_rated)
     
#Task 6.2 list comprehension
high_rated=[book["title"] for book in books if book[rating]>=4.7]
print(high_rated)
```
