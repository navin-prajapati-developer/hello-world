# Lists in Python
fruits = ["apple", "banana", "mango", "orange"]

print("All fruits: ")
for fruit in fruits:
    print(fruit)

print("First fruit: " + fruits[0])
print("Last fruit: " + fruits[-1])
print("Total fruits: " + str(len(fruits)))

fruits.append("grapes")
print("After adding grapes: ")
print(fruits)
