## python dictionaries 
student = {"name":"John","age":"45" , "courses":[
    "English","Math","Compsci"
]
,
"friend":{
 "name":"Mandla",
 "age":22
 }
}
my_friend = student.get("fr iend")
for key,value in student.items():
    if type(value == int):
        print(value , value)
    else:
        print(key,value)
   

with open("/Python/Carriculumn.txt") as file:
    print(file.readline())
    




