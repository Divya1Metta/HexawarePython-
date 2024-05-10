# break -> stop loop
# continue -> skip one iteration
# return -> exits out of function


def print_nums():
    for num in range(1, 10):
        if num == 6:
            break

        print(num)
    print("Execution continues 🎊")


def skip_even():
    for num in range(1, 10):
        if num % 2 == 0:
            continue
        print(num)
    print("Execution continues 🎊")


# Task 1: Find the first negative value | break or continue
def first_negative(numbers):
    # Your students will fill this in
    negative_num = None
    for num in numbers:
        if num < 0:
            negative_num = num
            break
    return negative_num


# Clue: membership operator (in)
def process_until_duplicate(fruits):
    fruit_set = set()
    for fruit in fruits:
        if fruit in fruit_set:
            print("Duplicate found, processing stopped.")
            break
        fruit_set.add(fruit)
        print(f"Processed {fruit}")
    print("Operation done ✅")


if __name__ == "__main__":
    # print_nums()
    # skip_even()
    # Test case
    # print(first_negative([3, 5, 7, -1, 9, -3]))  # -1
    process_until_duplicate(["apple", "banana", "carrot", "apple", "date", "banana"])


# Expected output
# Processed apple
# Processed banana
# Processed carrot
# Duplicate found, processing stopped.


# Task 3: Nested loops


def censorship_bot(messages, banned_words):
    pass


messages = [
    "Hello everyone!",
    "This is a bad word example!",
    "Let's keep our chat clean!",
    "Oops another bad content!",
    "Have a nice day!",
]

# Multiple banned words
banned_words = ["bad", "oops"]


# Expected output
# Approved message: Hello everyone!
# Approved message: Let's keep our chat clean!
# Approved message: Have a nice day!


# print("This is cool"
#       "We will dot it ⚡😊✌️"
#       "This is cool"
#       )

# Multi-line string

print("This is cool" "\nWe will dot it ⚡😊✌️" "\nThis is cool")

#  """ -> Multi line support
print(
    """
This is cool
We will dot it ⚡😊✌️
This is cool
"""
)

followers = 10_000
name = "Manju"
print(
    f"""
Hi, this is {name}.
I have {followers} followers
"""
)


# """ """ or ''' '''
# Documentation
def to_upper_case(text):
    """
    This helps in converting the text into uppercase
    """
    return text.upper() + " 🎊"


print(to_upper_case(name))
print(help(to_upper_case))
