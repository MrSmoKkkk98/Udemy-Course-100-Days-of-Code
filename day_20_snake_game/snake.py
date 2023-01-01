from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.all_segments = []
        self.create_snake()

    def create_snake(self):
        for i in STARTING_POSITIONS:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(i)
            self.all_segments.append(new_segment)
        
    def move(self):
        for seg_num in range(len(self.all_segments) - 1, 0, -1):
            new_x = self.all_segments[seg_num - 1].xcor()
            new_y = self.all_segments[seg_num - 1].ycor()
            self.all_segments[seg_num].goto(x=new_x, y=new_y)
        self.all_segments[0].forward(MOVE_DISTANCE)

    def up(self):
        self.screen.onkeyrelease(self.move(), "Up")
    
    def down(self):
        self.screen.onkeyrelease(self.move(), "Down")
    
    def left(self):
        self.screen.onkeyrelease(self.move(), "Left")
    
    def right(self):
        self.screen.onkeyrelease(self.move(), "Right")