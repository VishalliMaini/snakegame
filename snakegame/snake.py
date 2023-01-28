from turtle import Turtle,Screen
STARTING_POS=[(0,0),(-20,0),(-40,0)]
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:
    def __init__(self):
        self.segments=[]
        self.createSnake()
        self.head=self.segments[0]


    def createSnake(self):
        for p in STARTING_POS:
            self.add_segment(p)
    def add_segment(self,position):
        new_seg = Turtle(shape="square")
        new_seg.penup()
        new_seg.color("white")
        new_seg.goto(position)
        self.segments.append(new_seg)

    def extend(self):
        self.add_segment(self.segments[-1].position())
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)

    def up(self):
        #rule of game if is gong up it is going down it is not allowed to move up it is  allowed only to move
        if(self.head.heading()!=DOWN):
            self.head.setheading(90)

    def down(self):
        if (self.head.heading() != UP):
            self.head.setheading(270)

    def left(self):
        if (self.head.heading() != RIGHT):
            self.head.setheading(180)

    def right(self):
        if (self.head.heading() != LEFT):
            self.head.setheading(0)
