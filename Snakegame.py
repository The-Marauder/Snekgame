import turtle 
import random
import time
x = 0
score = 0
delay = 0.01
count = 0
boostcount = 0
speed = 1.7
OC = True
oldfruits = []
backdrop = turtle.Screen()
backdrop.title('Snake game')
backdrop.setup(1920,1080,0,0)
backdrop.tracer(0)
turtle.bgcolor("black")
turtle.speed(25)
turtle.pensize(4)
turtle.penup()
turtle.goto(-500,450)
turtle.pendown()
turtle.color('white')
turtle.forward(1000)
turtle.right(90)
turtle.forward(850)
turtle.right(90)
turtle.forward(1000)
turtle.right(90)
turtle.forward(850)
turtle.penup()
turtle.hideturtle()


snake = turtle.Turtle()
snake.speed(0)
snake.shape('square')
snake.color('violet')
snake.penup()
snake.goto(0,0)
snake.direction = 'stop'   
boosteractive = False
boostercount = 0
fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape('circle')
fruit.color('red')
fruit.penup()
fruit.goto(200,200)
maxscore = 0
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(-20,475)
scoreboard.write("Score = 0" , align="center" ,font=("Sans",24,"bold"))
highscore = turtle.Turtle()
highscore.speed(0)
highscore.color("white")
highscore.penup()
highscore.hideturtle()
highscore.goto(0,-450)
highscore.write("High Score = 0" , align="center" ,font=("Sans",24,"bold"))


specialfruit = turtle.Turtle()
specialfruit.speed(0)
specialfruit.shape('circle')
specialfruit.color('green')
specialfruit.penup()
specialfruit.hideturtle()
specialfruit.goto(random.randint(-380,400),random.randint(-380,400))
def restart() :
    global retry,score
    if(retry == False) :
        
        retry = True
        snake.goto(0,0)
        move()
        scoreboard.clear()
        scoreboard.write("Score = 0" , align="center" ,font=("Sans",24,"bold"))
        score = 0
        newfruit.hideturtle()
        oldfruits.clear()
   
def up() :
    if  snake.direction != "down" :
        snake.direction = "up"
def down() :
     if  snake.direction != "up" :
        snake.direction = "down"
def right() :
    if  snake.direction != "left" :
        snake.direction = "right"
def left() :
    if  snake.direction != "right" :
        snake.direction = "left"
def move() :
    if snake.direction == "up" :
        y = snake.ycor()
        snake.sety(y+speed)
    elif snake.direction == "down" :
        y = snake.ycor()
        snake.sety(y-speed) 
    elif snake.direction == "left" :
        x = snake.xcor()
        snake.setx(x-speed)
    elif snake.direction == "right" :
        x = snake.xcor()
        snake.setx(x+speed)
retry = True
backdrop.listen()
backdrop.onkeypress(up,"Up")
backdrop.onkeypress(down,"Down")
backdrop.onkeypress(left,"Left")
backdrop.onkeypress(right,"Right")
backdrop.onkeypress(restart,"space")

while  True:
    if(retry == False) :
        highscore.clear()
        highscore.write(f'High score = {maxscore}',align="center" ,font=("Sans",24,"bold"))

    backdrop.update()
    if(score > maxscore ) :
        maxscore = score
    if(retry == True) :
        if(snake.distance(fruit)<20) :
            if(boosteractive == False) :
                x = random.randint(-380,400)
                y = random.randint(-380,400)
                fruit.goto(x,y)
                scoreboard.clear()
                score+=1
                scoreboard.write(f'Score : {score}',align="center" ,font=("Sans",24,"bold"))
                speed+=0.05
                OC=True
                boostercount = 0
                count = 0
                newfruit = turtle.Turtle()
                newfruit.speed(0)
                newfruit.shape('square')
                newfruit.color('violet')
                newfruit.penup()
                oldfruits.append(newfruit)
            elif(boosteractive ==  True) :
                x = random.randint(-380,400)
                y = random.randint(-380,400)
                fruit.goto(x,y)
                scoreboard.clear()
                score+=2
                scoreboard.write(f'Score : {score}',align="center" ,font=("Sans",24,"bold"))
                OC=True
                newfruit = turtle.Turtle()
                newfruit.speed(0)
                newfruit.shape('square')
                newfruit.color('violet')
                newfruit.penup()
                oldfruits.append(newfruit)
                newfruit.speed(0)
                newfruit.shape('square')
                newfruit.color('violet')
                newfruit.penup()
                oldfruits.append(newfruit)
        
        for index in range(len(oldfruits)-1,0,-1) :
            a = oldfruits[index-1].xcor()
            b = oldfruits[index-1].ycor()
            
            oldfruits[index].goto(a,b)
            

        if len(oldfruits)>0 :
            a = snake.xcor()
            b = snake.ycor()

            oldfruits[0].goto(a ,b)
        
        move()

        if snake.ycor() > 440 :
            snake.goto(snake.xcor(),-385) 
        if snake.ycor()<-385 :
            snake.goto(snake.xcor(),440)   
        if snake.xcor()<-490 :
            snake.goto(490,snake.ycor())
        if snake.xcor()>490  :
            snake.goto(-490,snake.ycor())     
        for food in oldfruits :
            if(snake.distance(food)<20) :
                time.sleep(1)
                backdrop.bgcolor('black')
                scoreboard.clear()
                scoreboard.write("Game over! \n Your score was : {}. Press space to retry".format(score),align='center',font=("Sans",30,"bold"))
                retry = False
                print("glitch")
                
                
        
        if(count<30 and score != 0 and OC == True and score%5 == 0) :   
            specialfruit.showturtle()
            count += 1
        elif(count>=30 and score%5 == 0) :
            count = 0
            specialfruit.hideturtle()
            specialfruit.goto(random.randint(-380,400),random.randint(-380,400))
            OC = False
        
        if(snake.distance(specialfruit)<20) :
            specialfruit.hideturtle()
            specialfruit.goto(random.randint(-380,400),random.randint(-380,400))
            scoreboard.clear()
            scoreboard.write(f'Score : {score}',align="center" ,font=("Sans",24,"bold"))
            OC = False
            boostercount = 0
            boosteractive = True
        if (boostercount < 50 or boosteractive == True and OC== False) :
            boostercount+=1  
        elif(boostercount >=50) :
            boosteractive = False 
            boostercount = 0    
        

        

    time.sleep(delay) 


   
  
    
