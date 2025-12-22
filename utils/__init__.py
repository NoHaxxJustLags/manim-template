from manim import *


def create_title(text: str, **kwargs) -> Text:
    return Text(text, font_size=48, **kwargs).to_edge(UP)


def fade_in_sequence(scene: Scene, *mobjects, lag_ratio: float = 0.2):
    scene.play(AnimationGroup(*[FadeIn(m) for m in mobjects], lag_ratio=lag_ratio))


def fade_out_all(scene: Scene):
    scene.play(*[FadeOut(m) for m in scene.mobjects])
