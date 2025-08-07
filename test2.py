for n in [1, 3, 5, 6]:
    print(n)

for c in 'Un ds':
    print(c)

total = 0
for i in range(1,100*1):
    total += i
print(total)


# 원을 3개 그릴건데 for문으로 만들기

import turtle

for x, y, z in [(200,200,50), (-200,-200,30), (100,100,50)]:
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.circle(z)
    turtle.write(str((x,y)))
