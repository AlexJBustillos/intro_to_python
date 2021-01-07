# comment

"""Welcome to Python"""

""" Data Types """

name = 'Alex'
age = 5
is_old = False
sei_1019 = True

print(name)

name = 'Lev'

print(name)

""" Methods for a string """
sentence = 'Today is Nicole birthday'

nicole_birthday = sentence.split(' ')
print(nicole_birthday)

new_sentence = " ".join(nicole_birthday)
# find index
print(new_sentence.index('N'))

# Upper and lower case
name.upper()
name.lower()

# replace
day_sentence = sentence.replace('birthday', 'Day')
print(day_sentence)

# in keyword
is_day = 'Day' in day_sentence
print(is_day)

# ranges
last_letter = day_sentence[-1]
nicole_range = day_sentence[9:15]
print(nicole_range)

# length
print(len(nicole_range))

equal_to = 5 == 5
not_equal = 5 != 5

not True
not False

true_story = 5 <= 5
this_should_be_true = 6 >= 5

print(5 < 4 or 6 > 30)
print('Alex' == 'alex' or 'Pete' == 'Pete')
print('Alex' == 'alex' and 'Pete' == 'pete')

print('' or 'Alex')

# list (array)
numbers = [3,4,5,6]
print(len(numbers))

numbers[1]
print(numbers[-1])
print(numbers[len(numbers) - 1])

five_alex = ['Alex'] * 5
print(five_alex)

one_through_five = list(range(5))
print(one_through_five)

for i in range(len(one_through_five)):
    num = one_through_five[i]
    print(num)

# create a list and iterate through the list and print value

chairs = [1,'alex',True,False,6]
for i in range(len(chairs)):
    say = chairs[i]
    print(say)

random_numbers = [45, 88, 4, 17]
random_numbers.sort()
print(random_numbers)
random_numbers.append(33)
print(random_numbers)

reverse_random_numbers = random_numbers[::-1]
print(reverse_random_numbers)

thirty_three = random_numbers.pop()
print(thirty_three)

random_numbers.insert(0, 99)
print(random_numbers)

random_numbers.insert(1, 5)
print(random_numbers)

# help
# print(help(random_numbers))
print(random_numbers.count(5))

# dictionaries (objects)

car = {
    "color": 'Blue',
    "make": 'Tesla',
    "model": 'S',
    "all_colors": ['Red', 'White', 'Black'],
    "cool_car": True,
    "other_tesla_products": {
        "product": "Model 3",
        "product2": "Model X",
        "product3": "CyberTruck",
    }
}
# print(help(car))



print(car["make"])
car["speed"] = 200
print(car)

print(car.get("color"))
# print(car.items())
print(car.keys())

# type conversion
int('33')
str(33)
float(33)
bool(0)
bool(3)

# string interpolation
# print('Hello my name is ' + name)
print(f"Hello my name is {name}")
phrase = 'This {} is a phrase {}'
print(phrase.format('sentence', name))
print(phrase)

#functions

def print_name(someone):
    return someone

print(print_name('Will'))

def old_enough(age):
    if age < 21:
        return 'Not old enough'
    elif age == 21:
        return 'You made it to adulthood'
    else:
        return 'You old'

print(old_enough(30))

def add(num1, num2):
    return num1 + num2

print(add(3, 5))

def subtract(one, two):
    return one - two

print(subtract(100, 45))

def random_function(num1, num2, num3):
    return num1 - num2 * num3

print(random_function(34, 20, 5))

