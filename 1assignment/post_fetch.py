#import urllib.request
#import json
#import urllib.request
#= urllib.request.urlopen("https://jsonplaceholder.typicode.com/posts").read()
#print(blog_content)
#str_blog_content=blog_content.decode("utf-8")
#print(str_blog_content)


import urllib.request
import json
blog_content= urllib.request.urlopen("https://jsonplaceholder.typicode.com/posts").read()
print(blog_content)
str_blog_content=blog_content.decode("utf-8")
print(str_blog_content)
str_blog_content=json.loads(str_blog_content)
print(str_blog_content)
values = range(12)
for i in values:
    print(i)
n= ("what is the id")
def user_number(id):
    calculated_id = int(id)
    return user_number
user_number = input("what is the id?")
calculated_id = (user_number)
print("json.loads(str_blog_content)")