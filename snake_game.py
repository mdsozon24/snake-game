import turtle
import time
import random


delay = 0.1
score = 0
high_score = 0
#windows part
#windows part

window = turtle.Screen()
window.title('Make by @Sozon')
window.bgcolor('black')
window.setup(width=800,height=700)
window.tracer(0)


#snake body part

snake = turtle.Turtle()
snake.speed(0)
snake.goto(0,0)
snake.shape('circle')
snake.color('#F7F70C')
snake.penup()
snake.direction = 'stop'

#snake food

food = turtle.Turtle()
food.speed(0)
food.goto(0,100)
food.shape('circle')
food.color('red')
food.penup()

body = []

#Score bord

bord = turtle.Turtle()
bord.speed(0)
bord.goto(0,310)
bord.shape('circle')
bord.color('orange')
bord.penup()
bord.hideturtle()
bord.write("Score: 0  High Score: 0",align='center',font=("Courier",24,"normal"))

#Moving the snake

def up():
    if snake.direction!='down':
        snake.direction =  'up'
def down():
    if snake.direction!='up':
        snake.direction =  'down'
def left():
    if snake.direction!='right':
        snake.direction =  'left'
def right():
    if snake.direction!='left':
        snake.direction =  'right'

def move():
    if snake.direction == 'up':
        y=snake.ycor()
        snake.sety(y+20)

    if snake.direction == 'down':
        y=snake.ycor()
        snake.sety(y-20)

    if snake.direction == 'left':
        x=snake.xcor()
        snake.setx(x-20)

    if snake.direction == 'right':
        x=snake.xcor()
        snake.setx(x+20)

#Control snake
window.listen()
window.onkeypress(up , 'i')
window.onkeypress(down , 'j')
window.onkeypress(left , 'e')
window.onkeypress(right , 'f')

#main game loop

while True:
    window.update()
    move()

    #For game over

    if snake.xcor()>390 or snake.xcor()<-398 or snake.ycor()>300 or snake.ycor()<-330:
        time.sleep(1)
        snake.goto(0,0)
        snake.direction = 'stop'
        for b in body:
            b.goto(1000,1000)
        body.clear()

        score = 0
        bord.clear()
        bord.write("Score: {}  High Score: {}".format(score,high_score),align='center',font=("Courier",24,"normal"))


    #body overlap
        
    for c in body:
        if c.distance(snake)<20:
            time.sleep(1)
            snake.goto(0,0)
            snake.direction = 'stop'
            for b in body:
                b.goto(1000,1000)
            body.clear()

            
    #food location
        
    if snake.distance(food)<20:
        x = random.randint(-380,380)
        y = random.randint(-320,300)
        food.goto(x,y)

        #Add body part

        new_body = turtle.Turtle()
        new_body.speed(0)
        new_body.shape('circle')
        new_body.color('#53C09F')
        new_body.penup()
        body.append(new_body)

        score+=10
        if score>=high_score:
            high_score = score
        bord.clear()
        bord.write("Score: {}  High Score: {}".format(score,high_score),align='center',font=("Courier",24,"normal"))

    #move new body part

    for i in range(len(body)-1,0,-1):
        x = body[i-1].xcor()
        y = body[i-1].ycor()
        body[i].goto(x,y)
    if len(body) > 0:
        x = snake.xcor()
        y = snake.ycor()
        body[0].goto(x, y)
    time.sleep(delay)

window.mainloop()