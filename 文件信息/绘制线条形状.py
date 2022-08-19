import turtle as turtle

# turtle.goto(150,-180)
turtle.hideturtle()  # 隐藏画笔
turtle.pencolor('black')
turtle.pensize(1)  # 设置画笔的宽度
turtle.speed(10)  # 画笔速度
for i in range(120):
    turtle.left(120)  # 160
    turtle.fd(100)
    turtle.left(50)
    turtle.fd(200)

# turtle.color("red", "yellow")   #画笔红色，填充黄色
# turtle.begin_fill()
# for i in range(50):
#     turtle.forward(200)
#     turtle.left(170)


# turtle.circle(100)  #画圆

# turtle.fillcolor('blue')
# turtle.end_fill()
turtle.mainloop()
