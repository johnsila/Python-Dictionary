#dictionary is a collection which is unoedered,chsngsble and indexed.
students={
    "name":"john",
    "amno":"bit-01-0696/2019",
    "course":"bscit",
    "email":"jjohnsila@gmail.com"    
}
print(students)

#ACCESSING AN ITEM
x=students["name"]
print(x)

#ACCESING USING GET()
X=students.get("course")
print(X)

#CHANGE VALUES
#REFERING KEY NAME
students["name"]="ken"
print(students)

#LOOP THROUGH
#PRINT ALL KEY NAMES IN THE DICTIONARY
for a in students:
    print(a)

#PRINT ALL VALUES IN DICTIONARY
for b in students:
    print(students[b])

#FUNCTION TO RETURN VALUES OF DIC VALUES()
for x in students.values():
    print(x)

#loop using items()
for x,y in students.items():
    print(x,"/",y)

#check key existence
if "name" in students:
    print("key availabe")
else:
    print("key unavailable")

#dictionary length of items in dic
print(len(students))

#adding an item
students["age"]=27
print(students)

#removing an item in dictionary using pop()
students.pop("course")
print(students)

#remove last added item using popitem()
students.popitem()
print(students)


#copy a dictionary USING COPY()
STD=students.copy()
print(STD)

#COPY DIC USING DICT()
STDS= dict(students)
print(STDS)

#NESTED DICTIONARIES
family={
    "1stborn":{
        "name":"jr",
        "age":34
    },
    "2ndborn":{
        "name":"john",
        "age":27
    },
    "3rdborn":{
        "name":"faith",
        "age":14
    }
}
print(family)


#creating dictionary using dict()
car= dict( barnd="landrover",model="l4",year="2004")
print(car)

#update dictionary update()
car.update({"transmision":"manual"})
print(car)

#set default method
x=car.setdefault("madel","range")
print(x)