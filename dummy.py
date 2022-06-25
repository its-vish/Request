

import requests
import json
URL=requests.get("https://api.merakilearn.org/courses")
# print(URL)
DATA=URL.json()
b=open("new.json","w")
c=json.dump(DATA,b,indent=4)
serial_no=0
for i in range(0,len(DATA)):
    print(serial_no+1,".",DATA[i]["name"],"ID:",DATA[i]["id"])
    serial_no+=1
print()
courses_name=int(input("enter your course number which you want to learn :-"))
print(DATA[courses_name-1]["name"])
print(courses_name)
URL2=requests.get('https://api.merakilearn.org/courses/'+str(DATA[courses_name-1]["id"])+'/exercises')
d=URL2.json()
e=open("p.json","w")
f=json.dump(d,e,indent=4)

# list2=[]
# j=0
# k=1
# for i in d["course"]["exercises"]:  
#     if i["parent_exercise_id"]==[]:
#         j=j+1
#         list2.append(i)
#     if i["parent_exercise_id"]==i["id"]:
#         print(j+1,".",i["name"])
#         list2.append(i)
#     j=j+1  
#     if i["parent_exercise_id"]!=i["id"]:
#         print(" ",k,".",i["name"])
#         list2.append(i)
#     k=k+1
# with open("q.json","w") as f:
#     json.dump(list2,f,indent=4)
# print()
# topic_no=int(input("choose topic number :-"))
# for l in range(0,len(list2)):
#     if topic_no==l+1:
#         print(topic_no,list2[l]["name"])
#         a=list2[l]["parent_exercise_id"]

# s=1
# w=[]
# g=[]
# for d in range(0,len(list2)):
#     if list2[d]["parent_exercise_id"]==a:
#         print(" ",s,list2[d]["name"])
#         w.append(list2[d]["name"])
#         g.append(list2[d]["content"])
#         s+=1
# child_number=int(input("which child you want to print :-"))
# print()
# print("Child data is",child_number)
# print()
# print(g[child_number-1])


	

	
