def circle(r):
    pi=3.1415
    return r*r*pi

def cylinder(r,h):
    return circle(r)*h

def user_input():
    r=int(input("Enter a radius:"))
    h=int(input("Enter a height:"))
    print(cylinder(r,h))
    
user_input()