l,b,h=map(int,input("Enter the length, breadth and height of the cuboid: ").split() )
volume=l*b*h
print(f"The volume of the cuboid is: {volume}" )
print(f"LSA of the cuboid is: {2*(l*b + b*h + h*l)}" )