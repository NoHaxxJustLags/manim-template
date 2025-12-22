from manim import *


class Example(Scene):
    def construct(self):
        circle = Circle(color=BLUE, fill_opacity=0.5)
        square = Square(color=RED, fill_opacity=0.5)
        
        self.play(Create(circle))
        self.play(Transform(circle, square))
        self.play(FadeOut(circle))
