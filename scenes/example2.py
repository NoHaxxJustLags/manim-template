from manim import *


class Example3D(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        sphere = Sphere(radius=1, color=BLUE, fill_opacity=0.7)

        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.play(Create(axes), Create(sphere))
        self.begin_ambient_camera_rotation(rate=0.3)
        self.wait(3)
        self.stop_ambient_camera_rotation()
        self.play(FadeOut(axes), FadeOut(sphere))
