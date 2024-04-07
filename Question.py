from manim import *

class Question(Scene):
    def construct(self):

        title = Title(f"Question of Interest")
        page_number = MarkupText(
            "7"
        ).move_to([6.5,4,0])
        page_number.match_y(title)

        Quest= Tex(
            "What are the rational points of an equation?"
        )

        Rat1= Tex(
            "Rational points are of the form "
        )

        Frac1 = Tex(
            "(Fraction, Fraction)"
        )

        RatFrac1 = VGroup(Rat1, Frac1).arrange(RIGHT)

        Rat2= Tex(
            "Rational points are of the form "
        )

        Frac2 = MathTex(
            r"\left( \frac{a}{b}, \frac{c}{d} \right)"
        )

        RatFrac2 = VGroup(Rat2, Frac2).arrange(RIGHT)

        Rat3= Tex(
            "Rational Points:"
        )

        Frac3 = MathTex(
            r"\left( m, q \right)"
        )

        mq = Tex(
            ", where m and q are rational"
        )

        RatFrac3 = VGroup(Rat3, Frac3, mq).arrange(RIGHT)

        ax = Axes(
            x_range=[-2.5, 2.5, 0.5],
            y_range=[0, 6.25, 1],
            tips=False,
            axis_config={"include_numbers": True}
        )
        ax.scale_to_fit_height(3.5)
        ax.move_to([-3,-1,0])

        parabola = ax.plot(lambda x: x ** 2, x_range=[-2.5, 2.5], use_smoothing=False)

        label1 = ax.get_graph_label(
            graph=parabola,
            label= MathTex(r"\left( 2, 4 \right)"),
            x_val=2,
            dot=True,
            direction=UL,
        )

        label2 = ax.get_graph_label(
            graph=parabola,
            label= MathTex(r"\left( 1.5, 2.25 \right)"),
            x_val=3/2,
            dot=True,
            direction=DR,
        )

        Rat_Points1 = MathTex(
            r"y = x^{2}"
        )

        Rat_Points2 = MathTex(
            r"\left( 2, 4 \right)"
        )

        Rat_Points3 = MathTex(
            r"\left( \frac{3}{2}, \frac{9}{4} \right)"
        )

        Rat_Points = VGroup(Rat_Points1, Rat_Points2, Rat_Points3).arrange(DOWN)
        Rat_Points.move_to([3.5,0,0])

        Rat_Param1 = MathTex(
            r"y = x^{2}"
        )

        Rat_Param2 = MathTex(
            r"\left( m, m^{2} \right)"
        )

        Rat_Param = VGroup(Rat_Param1, Rat_Param2).arrange(DOWN)
        Rat_Param.move_to([3.5,0,0])

        m_value = MathTex(
            r"m = "
        ).next_to(Rat_Param, DOWN)

        m_valuesq = MathTex(
            r"m^{2} = "
        ).next_to(m_value, DOWN)

        a = ValueTracker(1.00)

        m = ax.get_graph_label(
            graph=parabola,
            label=MathTex(r"\left( m, m^{2} \right)"),
            x_val= 1,
            dot=True,
            direction=RIGHT,
        )

        m.add_updater(
            lambda mob: mob.become(ax.get_graph_label(
                graph=parabola,
                label=MathTex(r"\left( m, m^{2} \right)"),
                x_val= a.get_value(),
                dot=True,
                direction=RIGHT,
                )
            )
        )

        a_number = DecimalNumber(
            a.get_value(),
            num_decimal_places=3
        )

        a_number.add_updater(
            lambda mob: mob.set_value(a.get_value()).next_to(m_value, RIGHT)
        )

        a_numbersq = DecimalNumber(
            a.get_value() ** 2,
            num_decimal_places=3
        )

        a_numbersq.add_updater(
            lambda mob: mob.set_value(a.get_value() ** 2).next_to(m_valuesq, RIGHT)
        )

        self.add(
            Quest, title, page_number
        )

        self.play(
            Quest.animate.shift(2 * UP)
        )

        self.play(
            Create(RatFrac1),
        )

        self.wait(2)

        self.play(
            Transform(RatFrac1, RatFrac2)
        )

        self.add(RatFrac2)
        self.remove(RatFrac1)
        self.wait(2)

        self.play(
            Transform(RatFrac2, RatFrac3)
        )

        self.add(RatFrac3)
        self.remove(RatFrac2)
        self.wait(2)

        self.play(
            FadeOut(Quest)
        )

        self.wait(0.5)

        self.play(
            RatFrac3.animate.shift(2*UP)
        )

        self.wait(2)

        self.play(
            Create(ax),
            Create(parabola),
        )

        self.wait(2)

        self.play(
            Create(label1),
            Create(label2),
            Create(Rat_Points)
        )

        self.wait(2)

        self.play(
            FadeOut(label1, label2)
        )

        self.wait(1)

        self.play(
            Transform(Rat_Points, Rat_Param)
        )

        self.play(
            Create(m),
            Create(a_number),
            Create(a_numbersq),
            Create(m_value),
            Create(m_valuesq)
        )

        self.play(
            a.animate.set_value(2.5)
        )

        self.play(
            a.animate.set_value(-2.5)
        )

        self.play(
            a.animate.set_value(2.5)
        )

        self.play(
            a.animate.set_value(-2.5)
        )