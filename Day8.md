# Day-8
Case Study Q/A
## Python

REPLIT----> Read,Evaluate,Print,Loop
## Task 1: convert temp in celsius

```python
n=float(input())
celsius = (n - 32) * 5 / 9
c=str(celsius)
print(f"The equivalent of {n}°F is {c}°C")
```

## Task 2: Find the age of the person given the birth year 2000

```python
age=int(input())
a=2024-age
print(f"your age is {a}")
```

## Task3 : Print area of circle

```python
radius= float(input())
area=3.14*radius*radius
print(f"area of circle is {area}")
```
{}--->Interpolation

## Task4 : Building __loader__
```python
n=int(input())
m=n//10
i=10-m
print('['+"="*m +' '*i+']'+ str(n) + "%")
# print(f"[{'=' * m} {' '* i}] {n}%")
#output
32
[===       ]32%

76
[=======   ]76%
```
## Task5 : comparisiom of outputs
```python
n1=input()
n2=input()
height1=int(input())
height2=int(input())
if height1>height2:
  print(f'{n1} taller than {n2}') 
else:
  print(f'{n2} taller than {n1}')
```

#Exercises


## Task1
```python
stock1= 'vanilla'
stock2= 'lime'
stock3= 'choclate'
#ask user their fav flavour
n=input('what is your fav flavour?')
#output
#case1:yes,we do have it
#case2:no,we ran ouyt of stock
if n==stock1 or n==stock2 or n==stock3:
  print('yes,we do have it')
else:
  print('no,we ran out of stock')
```


## Task2
```python
shop='vanilla,lime,choclate'
n=input('what is your fav flavour?')
if n in shop:
  print('yes,we do have it')
else:
  print('no,we ran out of stock')
#edge case for gives output also for substring
#using terenary operator-
#print("yes,we do have it" if (n in shop) else "no,we ran out of stock")
```

## Code Debt--->Tommorow i will make it better

## Five pillars of Code Quality

1. Readability consequence code debt-->75
2. Maintainabiility
3. Extensibility
4. Testability  #debugging
5. Performance

Terenary operator-->3 operands{true,false,condition}

Binary operators:=,-,/,and,or,<,>,==,<=,>=

unary:++,--,not
```python
n="--Divya--"
print(n.strip('-')) 
removes all --
print(n.lstrip('-'))
removes -- only on left
print(n.rstrip('-'))
removes -- only on right

print(n.find('Divya')) --->0 returns index position of first occurence
print(n.find('*')) --->-1

print(n.replace("D","I")--->Iivya is output
print(n)--->It doesnt change from input as strings are immutable

```
## : Slicing operator
```python
message = "    🚨🔍📱🔑secret_code✌️"
code = "SECRET_CODE✌️"
output= print(UPPR(message[8:]))
if(output==code):
  print("you are the hacker ")
else:
  print("try again")
```
