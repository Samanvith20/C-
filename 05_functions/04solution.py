
def radius(r):
    area=3.14*r*r
    circumference=2*3.14*r
    return area,circumference

area,circumference=radius(5)
# round function is used to round off the value to 2 decimal places
print(f"Area: {round(area,2)}\nCircumference: {round(circumference,2)}")