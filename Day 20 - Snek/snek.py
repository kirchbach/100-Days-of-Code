from turtle import Turtle

SNEK_SEGMENT_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snek:
    def __init__(self):
        self.snek_segments = []
        self.build_snek()
        self.head = self.snek_segments[0]

    def build_snek(self):
        for position in SNEK_SEGMENT_POS:
            self.add_segment(position)


    def add_segment(self, position):
        snek_seg = Turtle("square")
        snek_seg.penup()
        snek_seg.color("white")
        snek_seg.goto(position)
        self.snek_segments.append(snek_seg)

    def extend(self):
        self.add_segment(self.snek_segments[-1].position())

    def reset(self):
        for seg in self.snek_segments:
            seg.goto(1000, 1000)
        self.snek_segments.clear()
        self.build_snek()
        self.head = self.snek_segments[0]

    def move(self, screen):
        screen.update()
        for seg in range(len(self.snek_segments) - 1, 0, -1):
            self.snek_segments[seg].goto(self.snek_segments[seg - 1].pos())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
