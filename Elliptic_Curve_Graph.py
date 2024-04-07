from manim import *

class EllipticCurve(Scene):
    def construct(self):

        number_plane = NumberPlane(
            background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 4,
                "stroke_opacity": 0.6
            }
        )

        t = MathTex("y^{2} = x^{3} - x").move_to([0,3,0], [0,0,0])

        text_rect = Rectangle(width=4.0, height=1.0, color=WHITE, fill_color=BLACK, fill_opacity=1).move_to(t)

        graph = ImplicitFunction(
            lambda x, y: x ** 3 - y ** 2 - x,
            color=YELLOW
        )

        self.bring_to_back(number_plane)

        self.bring_to_front(text_rect)
	
        self.bring_to_front(t)

        self.play(
            graph.animate.generate_points()
        )

