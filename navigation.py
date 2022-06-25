import requests

import json

a=requests.get("https://api.merakilearn.org/courses")

get_url=a.json()

my_file=open("courses.json","w")
b=json.dump(get_url,my_file,indent=6)

serial_no=0
for i in range(0,len(get_url)):
    serial_no+=1
    for k,v in get_url[i].items():
        
        if k=="name":

            print(serial_no, v,'-',get_url[i]['id'])


choose=int(input("which course you want to learn please enter :-"))
idd=get_url[choose-1]['id']

url="https://api.merakilearn.org/courses/"+str(idd)+"/exercises"
get_data=requests.get(url)
data=get_data.json()
file=open("courses_excercies.json","w")
json.dump(data,file,indent=6)
print(get_url[choose-1]['name'],'-',get_url[choose-1]['id'])

serial=1
serial1=1
list1=[]
list2=[]
j=0
k=1
for i in data["course"]["exercises"]:  
    if i["parent_exercise_id"]==None:
        print(serial,i['name'])
        print(" ",serial1,i['slug'])
        serial+=1
        list1.append(i)
        list2.append(i)
    elif i["parent_exercise_id"]==i["id"]:

        print(serial,i["name"])
        serial+=1
        list1.append(i)
        new_no=1
    
    elif i["parent_exercise_id"]!=i["id"]:
        print(" ",new_no,i["name"])
        new_no=1
        list2.append(i)

file= open("list1.json","w")
json.dump(list1,file,indent=6)
file=open("list2.json","w")
json.dump(list2,file,indent=6)


navigation=str(input("enter if you want next..N  or for previous...P="))
if navigation=='N':
    parent_id=int(input("which parent id you want to enter please="))

    serial=1
    for i in list1:
        if i['parent_excercise_id']==i['id']:
            print(serial,list1[parent_id-1]['name'])
            serial+=1
            break
        else:
            if i['parent_excsercise_id']!=i['id']:
                print(serial,list1[parent_id-1]['name'])

                print(" ",list1[parent_id-1]['content'])
                serial+=1
                break
    l=[]
    l1=[]
    new_no=1
    idd=list1[parent_id-1]['id'] 

    for j in list2:
        if j['parent_exercise_id']==idd:
            print(" ",new_no,j['name']) 
            l.append(j['name'])  
            l1.append(j['content'])
            new_no+=1
    navigation=str(input("enter what you want next/N or previous/P="))
    if navigation=='N':
        child_id=int(input("which child id you want please enter="))

        # idd=l1[child_id-1]
        # for i in idd:
        #     print(i)

        for i in range(len(l)):
            if child_id-1==1:
                print(l[i])
                print(l1[i])
                break
        
        navigation=str(input("enter what you want next/N or previous/P="))
        if navigation=='N':

            for i in range(len(l)):
                if child_id-1==i:
                    print(l[i])
                    print(l1[i])

        elif navigation=='P':
            serial=1
            for i in list1:
                if i['parent_excrcise_id']==i['id']:
                    print(serial,list1[parent_id-1]['name'])
                    serial+=1
                    break
                else:
                    if i['parent_excsercise_id']!=i['id']:
                        print(serial,list1[parent_id-1]['name'])

                        print(" ",list1[parent_id-1]['content'])
                        serial+=1
                        break
            l=[]
            l1=[]
            new_no=1
            idd=list1[parent_id-1]['id'] 

            for j in list2:
                if j['parent_exercise_id']==idd:
                    print(" ",new_no,j['name']) 
                    l.append(j['name'])  
                    l1.append(j['content'])
                    new_no+=1
            navigation=str(input("enter what you want next/N or previous/P="))
            if navigation=='N':
                child_id=int(input("which child id you want please enter="))

                # idd=l1[child_id-1]
                # for i in idd:
                #     print(i)

                for i in range(len(l)):
                    if child_id-1==1:
                        print(l[i])
                        print(l1[i])
                        break
                
                navigation=str(input("enter what you want next/N or previous/P="))
                if navigation=='N':

                    for i in range(len(l)):
                        if child_id-1==i:
                            print(l[i])
                            print(l1[i])

                elif navigation=='P':
                    serial=1
                    for i in list1:
                        if i['parent_excrcise_id']==i['id']:
                            print(serial,list1[parent_id-1]['name'])
                            serial+=1
                            break
                        else:
                            if i['parent_excsercise_id']!=i['id']:
                                print(serial,list1[parent_id-1]['name'])

                                print(" ",list1[parent_id-1]['content'])
                                serial+=1
                                break
                    
                    






