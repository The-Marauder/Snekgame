import turtle 
import random
import time
x = 0
score = 0
delay = 0.25
count = 0
boostcount = 0
OC = True
oldfruits = []
backdrop = turtle.Screen()
backdrop.title('Snake game')
backdrop.setup(1920,1080,0,0)
backdrop.tracer(0)
turtle.bgcolor("red")
turtle.speed(25)
turtle.pensize(4)
turtle.penup()
turtle.goto(-500,450)
turtle.pendown()
turtle.color('black')
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

fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape('circle')
fruit.color('black')
fruit.penup()
fruit.goto(200,200)
maxscore = 0
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.color("black")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(-20,475)
scoreboard.write("Score = 0" , align="center" ,font=("Sans",24,"bold"))
highscore = turtle.Turtle()
highscore.speed(0)
highscore.color("black")
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
specialfruit.goto(random.randint(-400,400),random.randint(-400,400))
def restart() :
    retry = True
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
        snake.sety(y+20)
    elif snake.direction == "down" :
        y = snake.ycor()
        snake.sety(y-20) 
    elif snake.direction == "left" :
        x = snake.xcor()
        snake.setx(x-20)
    elif snake.direction == "right" :
        x = snake.xcor()
        snake.setx(x+20)
retry = True
backdrop.listen()
backdrop.onkeypress(up,"Up")
backdrop.onkeypress(down,"Down")
backdrop.onkeypress(left,"Left")
backdrop.onkeypress(right,"Right")
backdrop.onkeypress(restart,"space      ")

while  retry == True:
    backdrop.update()
    if(score > maxscore ) :
        maxscore = score
    if(snake.distance(fruit)<20) :
        if(boosteractive == False) :
            x = random.randint(-400,400)
            y = random.randint(-400,400)
            fruit.goto(x,y)
            scoreboard.clear()
            score+=1
            scoreboard.write(f'Score : {score}',align="center" ,font=("Sans",24,"bold"))
            delay-= 0.01
            OC=True
            newfruit = turtle.Turtle()
            newfruit.speed(0)
            newfruit.shape('square')
            newfruit.color('violet')
            newfruit.penup()
            oldfruits.append(newfruit)
        elif(boosteractive ==  True) :
            x = random.randint(-400,400)
            y = random.randint(-400,400)
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

        oldfruits[0].goto(a,b)
    
    move()

    if snake.ycor() > 400 or snake.xcor() > 480 or snake.xcor() < -480 or snake.ycor() < -380:
        time.sleep(1)
        backdrop.clear()
        backdrop.bgcolor('red')
        scoreboard.goto(0,0)
        scoreboard.write("Game over! \n Your score was : {}".format(score),align='center',font=("Sans",30,"bold"))
        retry = False
        

    for food in oldfruits :
        if(snake.distance(food)<20) :
            time.sleep(1)
            backdrop.clear()
            backdrop.bgcolor('red')
            scoreboard.goto(0,0)
            scoreboard.write("Game over! \n Your score was : {}. Press space to retry".format(score),align='center',font=("Sans",30,"bold"))
            retry = False
            
    
    if(count<25 and score != 0 and OC == True and score%5 == 0) :   
        specialfruit.showturtle()
        count += 1
        print(count)
        
    elif(count>=25 and score%5!=0 and score != 0) :
        count = 0
        specialfruit.hideturtle()
        specialfruit.goto(random.randint(-400,400),random.randint(-400,400))
        OC = False
    
    if(snake.distance(specialfruit)<20) :
        specialfruit.hideturtle()
        specialfruit.goto(random.randint(-400,400),random.randint(-400,400))
        scoreboard.clear()
        scoreboard.write(f'Score : {score}',align="center" ,font=("Sans",24,"bold"))
        count = 0
        while(count < 30) :
            count+=1
            boosteractive = True

        

    time.sleep(delay) 

if(retry == False) :
    highscore.write(f'High score = {maxscore}',align="center" ,font=("Sans",24,"bold"))
   
  
    
