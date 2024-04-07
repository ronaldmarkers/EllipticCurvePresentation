from manim import *

class EC(Scene):
    def construct(self):

        title = Title(f"What Is An Elliptic Curve?")
        page_number = MarkupText(
            "9"
        ).move_to([6.5,4,0])
        page_number.match_y(title)

        Elliptic_Curve = MathTex(
            r"y^{2} = x^{3} + Ax + B"
        ).move_to([-4,1,0])

        Discriminant = MathTex(
            r"4A^{3} - 27B^{2} \neq 0"
        ).next_to(Elliptic_Curve, DOWN)

        NonSingular = Tex(
            "Non-Singular Polynomial"
        ).next_to(Discriminant, DOWN)

        ax = Axes(
            x_range=[-3, 3, 1],
            y_range=[-4, 4, 1],
            tips=False,
            axis_config={"include_numbers": True}
        ).scale_to_fit_height(4)
        ax.move_to([3,0,0])

        a = ValueTracker(-1)

        EC = ax.plot_implicit_curve(lambda x, y: x ** 3 - y ** 2 - x + 1)

        EC.add_updater(
            lambda mob: mob.become(ax.plot_implicit_curve(lambda x, y: x ** 3 - y ** 2 + (a.get_value() * x) + 1))
        )

        self.add(title, page_number, ax, Elliptic_Curve, Discriminant, NonSingular)

        self.play(
            Create(EC)
        )

        self.play(
            a.animate.set_value(-3.3)
        )

        self.play(
            a.animate.set_value(8.6)
        )