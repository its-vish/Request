import requests 
res=requests.get("https://api.merakilearn.org/courses")  
print(res.text) 
print(res.status_code)
print(res.ok)
print(res.cookies)
print(res.headers)


# https://campus.unipune.ac.in/CCEP/Log...
