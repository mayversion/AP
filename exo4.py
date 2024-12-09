first_age=int(input("Please type in the age of the first person:"))
second_age=int(input("Please type in the age of the second person:"))

if first_age > second_age:
    print(f"The older age is: {first_age}")
elif first_age < second_age:
    print(f"The older age is: {second_age}")
else:
    print("Both people have the same age !")