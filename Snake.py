import turtle
import random
import time

delay = 0.1
sc = 0
hs = 0
bodies = []


s = turtle.Screen()
s.title("Snake Game")
s.bgcolor("yellow")
s.setup(width=600, height=600)


head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("black")
head.fillcolor("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"


food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red") 
food.fillcolor("black")
food.penup()
food.goto(150, 250)


sb = turtle.Turtle()
sb.ht()
sb.penup()
sb.goto(-250, 250)
sb.write("Score: 0 | Highest Score: 0", font=("Arial", 14, "bold"))


def moveup():
    if head.direction != "down":
        head.direction = "up"

def movedown():
    if head.direction != "up":
        head.direction = "down"

def moveleft():
    if head.direction != "right":
        head.direction = "left"

def moveright():
    if head.direction != "left":
        head.direction = "right"

def movestop():
    head.direction = "stop"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


s.listen()
s.onkey(moveup,"Up")
s.onkey(movedown,"Down")
s.onkey(moveleft,"Left")
s.onkey(moveright,"Right")
s.onkey(movestop,"space")

# Main game loop
while True:
    s.update()

    
    if head.xcor() > 290:
        head.setx(-290)

    if head.xcor() < -290:
        head.setx(290)

    if head.ycor() > 290:
        head.sety(-290)
        
    if head.ycor() < -290:
        head.sety(290)

    # Collision with food
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        
        body = turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("square")
        body.color("green")
        bodies.append(body)

        # Score update
        sc += 10
        if sc > hs:
            hs = sc
        sb.clear()
        sb.write(f"Score: {sc} | Highest Score: {hs}", font=("Arial", 14, "bold"))
        delay -= 0.001

    
    for index in range(len(bodies) - 1, 0, -1):
        x = bodies[index - 1].xcor()
        y = bodies[index - 1].ycor()
        bodies[index].goto(x, y)

    if len(bodies)>0:
        x = head.xcor()
        y = head.ycor()
        bodies[0].goto(x, y)
    
    move()

    # Collision with body
    for body in bodies:
        if body.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for body in bodies:
                body.ht()
            bodies.clear()
            sc = 0
            delay = 0.1
            sb.clear()
            sb.write(f"Score: {sc} | Highest Score: {hs}", font=("Arial", 14, "bold"))

    time.sleep(delay)
s.mainloop()