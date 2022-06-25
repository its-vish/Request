# import requests
# a=requests.get("https://api.merakilearn.org/courses")
# # print(help(a))
# print(a.headers)

# import requests 
# res=requests.get("https://api.merakilearn.org/courses")  
# p=res.json()
# print(p)
# print(type(p))


# # HOW TO PASS PARAMETERS IN YOUR URL

# import requests
# payload={'key1':'value1'}
# res=requests.get("https://api.merakilearn.org/courses",params=payload)
# # print(res.url)




# Cloud computing is the on-demand delivery of IT resources over the Internet with pay-as-you-go pricing. Instead of buying, owning, and maintaining physical data centers and servers, you can access technology services, such as computing power, storage, and databases, on an as-needed basis from a cloud provider like Amazon Web Services (AWS).



# l1=[[4,5,6],[5,6,8],[9,10,11]]
# sum=0
# i=0
# while i<len(l1):
#     if i==0:
#         for j in l1[i]:
#             sum+=j

#     elif i!=0:
#         s=len(l1[i])
#         sum+=(l1[i][s-1])
#     i=i+1
# print(sum)