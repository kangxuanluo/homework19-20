homework19

x = int(input("x?"))
n = int(input("n?"))
r = x
t = "2"
for n in range(n-1):
    r *= x
    for X2 in "X2":
        t += X2
print(t,"=",r)

homework20
t=1
x=1/(t**2)
p=0

while x >0.001:
    print(p)
    x = 1 / (t ** 2)
    p  += x
    t+=1
quit()
