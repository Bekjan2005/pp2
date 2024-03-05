y1, m1, d1 = int(input()), int(input()), int(input()) 
y2, m2, d2 = int(input()), int(input()), int(input()) 
a = datetime(y1, m1, d1) 
b = datetime(y2, m2, d2) 
d = b - a 
print((b-a).total_seconds())