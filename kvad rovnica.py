import math

a=int(input("Zadaj hodnotu a: "))
b=int(input("Zadaj hodnotu b: ") or "0")
c=int(input("Zadaj hodnotu c: ") or "0")


d=(b*b)-(4*a*c)

if d>0 :
    d=math.sqrt(d)

    x1=(-b+d)/(2*a)
    x2=(-b-d)/(2*a)

    print("Rovnica má korene "x1,"a",x2)

elif d==0:
    x1=(-b)/(2*a)

    print("Rovnica má koreň ",x1)

elif d<0 :
    print("kvadratická rovnica nemá koreň v reálnych číslach")

