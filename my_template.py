template_str ="my first_name is {} and my last_name is {}. my message is {}"
first_name = input("what is your first_name:")
last_name = input("what is your last_name:")
message = input("what is your message:")
print (template_str.format(first_name,last_name,message))