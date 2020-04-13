import turtle

bob = turtle.Turtle()
paper = turtle.Screen()

paper.title("A Hy-Camp Turtle")

paper.bgcolor("black") # make the paper black

bob.shape("turtle")

def draw_square(length):
    for x in range(4):
        bob.forward(length)
        bob.left(90)

bob.color("red")

for i in range(24):
    # change pen color depending if i is even or odd
    if i % 2 == 0:
        bob.color("red")   # even
    else:
        bob.color("orange")   #odd

    draw_square(225)

    # turn the turtle 15 degrees to start the square in a different direction
    bob.left(15)

bob.hideturtle()
paper.exitonclick()
paper.mainloop()

