# Question 1

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Question 2

a = 15
b = 12

res = a + b
print(res)

# Question 3

num = float(input("Enter a number: "))
if num > 0: print("Positive")
elif num < 0: print("Negative")
else: print("Zero")

# Question 4

num = 10
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")

if (num % 2) == 0:
    print("{0} is Even".format(num))
else:
    print("{0} is Odd".format(num))

# Question 5

i = 1
n = 10

for num in range(i, n + 1):
    print(num)


# Question 8

correct_password = "python123"
password = ""
attempt_count = 0

while password != correct_password:
  password = input("Please enter your password: ")
  attempt_count += 1

print("Access granted. Number of incorrect attempts: ", attempt_count - 1)


# Question 9

a = [10, 20, 30, 40, 50]

sum1 = sum(a)
avg = sum1 / len(a) if a else 0  

print(sum1)
print(avg)


# Question 10

a = [1, 2, 3, 4, 5]

for x in a:
    print(x, end=' ')


# Question 11

a = [20, 30, 50]
res = sum(a)
print(res)


# Question 12

def fizzBuzz(n):
    res = []

    for i in range(1, n + 1):

        # Check if i is divisible by both 3 and 5
        if i % 3 == 0 and i % 5 == 0:

            # Add "FizzBuzz" to the result list
            res.append("FizzBuzz")

        # Check if i is divisible by 3
        elif i % 3 == 0:

            # Add "Fizz" to the result list
            res.append("Fizz")

        # Check if i is divisible by 5
        elif i % 5 == 0:

            # Add "Buzz" to the result list
            res.append("Buzz")
        else:

            # Add the current number as a string to the
            # result list
            res.append(str(i))

    return res


if __name__ == "__main__":
    n = 50
    res = fizzBuzz(n)
    print(' '.join(res))


# Question 13

string = "2026"

rev = ""
for y in string:
    rev = y + rev

print(rev)

# Question 14

marks = int(input("Enter marks: "))
if marks >= 80: print("A")
elif marks >= 70: print("B")
elif marks >= 60: print("C")
elif marks >= 50: print("D")
else: print("Fail")

# Question 33

nums = [1, 2, 3, 4, 5]
for n in nums:
    print(f"Number: {n}, Square: {n**2}")

# Question 34

original = [1, 2, 3, 4, 5, 6]
evens = [n for n in original if n % 2 == 0]
print(evens)

# Question 35

a = [1, 2, 3, 4, 5] 

total = 0

for num in a:
    total += num

print(total)


# Question 36

students = {}
num_students = int(input("Enter number of students: "))

for i in range(num_students):
    name = input(f"Enter name for student {i+1}: ")
    marks = []
    for subj in range(1, 6):
        mark = int(input(f"Enter mark for subject {subj}: "))
        marks.append(mark)
    students[name] = marks

print("Students and their marks:")
for name, marks in students.items():
    print(f"{name}: {marks}")


# Question 37

d = {'Car':100, 'Bike':1292, 'Boat': 2100}
mk = None # max_key
mv = float('-inf') # max_value

for k, v in d.items():
    if v > mv:
        mv = v
        mk = k

print(mk)

# Question 38

a = [1, 3, 2, 6, 3, 2, 8, 2, 9, 2, 7, 3]
count = 0
for val in a:
	if val == 3:
		count += 1
print(count)

# Question 39

a = [1, 2, 3, 1, 2, 4, 5, 6, 5]
s = set()
dup = []

for n in a:
    if n in s:
        dup.append(n)
    else:
        s.add(n)
print(dup)

# Question 41

square = lambda x: x ** 2

print(square(2))  
print(square(9)) 

# Question 45

list1 = [3, 6, 9]
list2 = [4, 1, 0]
added_lists = list(map(lambda x, y: x + y, list1, list2))
print(added_lists) 
