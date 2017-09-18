def area_rectangle(base,height):
    int_base = int(base)
    int_height = int(height)
    area = int_base * int_height
    return area
base = input("what is the base?:")
height = input("what is the height?:")
area = area_rectangle(base,height)
print(area)


    