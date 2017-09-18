import urllib.request
blog_content = urllib.request.urlopen("https://jsonplaceholder.typicode.com/posts").read()
print(blog_content)


import urllib.request
blog_content = urllib.request.urlopen(" http://date.jsontest.com/").read()
print(blog_content)