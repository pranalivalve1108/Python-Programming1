#Creating a Dictionary
student = {
    "name": "swara",
    "age": 21,
    "course": "python"
}
print(student)

#Accessing values
print(student["name"])
print(student.get("age"))

#Modifying a Dictionary
student["age"] = 23
student["city"] = "pune"
print(student)

#Removing items
print(student.pop("course"))

del student["city"]
print(student)

#Clear dictionary
dict = {
    1: "one",
    2: "two",
    3: "three"
}
print(dict)
print(dict.clear())

#Dictionary methods
print(student.keys())
print(student.values())
print(student.items())
student.update({"name": "Pranali"})
print(student)

#Looping through a Dictionary
for key, value in student.items():
    print(key, ":",value)