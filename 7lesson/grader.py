'''
def grader(grade):
    grade = int(grade)
    if grade >= 90:
        return "A"
    elif grade >=70:
        return "B"
    elif grade >= 50:
        return "C"
    else:
        return "D"

user_input = input("What is the students marks?:")
computed_grade = grader(user_input)
print("The students grade is {}".format(computed_grade))
'''
def ager(age):
    age = int (age)
    if age <= 13:
        return "primary"
    elif age == 13:
        return "secondary"
    elif age == 18:
        return "secondary"
    else:
        return "tertiary"
        
user_input = input("what is the students age?:")
computed_age = ager(user_input)
print("the students age is {}".format(computed_age))


        
        
        