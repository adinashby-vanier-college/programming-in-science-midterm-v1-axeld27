import math

# Q1: Calculate the area of a circle
def area_of_circle(radius):
    r = radius
    area = float((float(r ** 2) * math.pi)) 
    return round((area), 2)

# Q2: Hollow Right Triangle
def hollow_right_triangle(n):
    result = ""
    row = 1
    if n >= 4:
        for i in range(row):
            result += "*"
        result += "\n"
        

        for j in range(row, n):
            if j == n - 1 or j == n :
                result += "*"  
            else:
                result += " " 
        result += "\n"

        for i in range(n):
            result += "*"
        result += "\n"

        return result.strip()
    
    else: 
        return ("The triangle height should be at least 4.")


# Q3: Inverted Pyramid
def inverted_pyramid(n):
    result = ""
    if n >= 3:  
        for i in range(n + 1): 
            for j in range(i):
                result += " "
            for j in range(i, n):
                result += "*"
            for j in range(i, n- 1):
                result += "*"
            result += "\n"
        return result.strip() 
    
    else:
        return("The pyramid height should be at least 3.")




# ----------------------------------------------------------------
print(area_of_circle(10))
print()

print(hollow_right_triangle(3))
print()

print(hollow_right_triangle(4))
print()

print(hollow_right_triangle(5))
print()

print(inverted_pyramid(2)) 
print()

print(inverted_pyramid(4))
print()

print(inverted_pyramid(5))
print()