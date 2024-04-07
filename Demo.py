from manim import *

class Demo(Scene):
    def construct(self):

        title = Title(f"How to Find Rational Points of A Circle")
        page_number = MarkupText(
            "8"
        ).move_to([6.5,4,0])
        page_number.match_y(title)

        ax = Axes(
            x_range=[-2.4, 2.4, 1],
            y_range=[-1.2, 1.2, 1],
            tips=False,
            axis_config={"include_numbers": True}
        ).scale_to_fit_height(5)

        Circle1 = ax.plot(lambda x: (1 - x ** 2) ** (1/2), x_range=[-1, 1, 0.01])
        Circle2 = ax.plot(lambda x: (-1)*(1 - x ** 2) ** (1/2), x_range=[-1, 1, 0.01])

        a = ValueTracker(0.6)

        Point_P1 = ax.get_graph_label(
            graph=Circle1,
            label= Tex("P"),
            x_val=0.6,
            dot=True,
            direction=UR
        )

        Point_P1.add_updater(
            lambda mob: mob.become(ax.get_graph_label(
                graph=Circle1,
                label= Tex("P"),
                x_val= a.get_value(),
                dot=True,
                direction=UR
                )
            )
        )

        Point_P2 = ax.get_graph_label(
            graph=Circle1,
            label= Tex("P"),
            x_val=-1,
            dot=True,
            direction=UL
        )

        Eq_Name = Tex(
            "Equation C"
        ).next_to(ax, DOWN).scale(0.6)
            
        Eq_Name1 = MathTex(
            r"x^{2} + y^{2} = 1"
        )
        Eq_Name1.next_to(Eq_Name, DOWN)

        Line = ax.plot(lambda x: (0.5)*(x+1), x_range=[-1.5, 1], use_smoothing=False)

        Point_R = ax.get_graph_label(
            graph=Line,
            label= Tex("R"),
            x_val=0.6,
            dot=True,
            direction=UR
        )

        Point_Name1 = MathTex(
            r"P = \left( 0,-1 \right)"
        ).move_to([4,2,0])

        Point_Name2 = MathTex(
            r"R = \left( s,t \right)"
        ).next_to(Point_Name1, DOWN)

        Rational_m = Tex(
            "m is rational"
        ).next_to(Point_Name2, DOWN)

        Rational_b = Tex(
            "m and b are rational"
        ).next_to(Point_Name2, DOWN)

        Slope_Intercept1 = MathTex(
            r"y = mx + b"
        ).next_to(Rational_m, DOWN)

        rect= Rectangle(width=2.0, height=5.0, color=BLACK, fill_color=BLACK, fill_opacity=1).move_to([2,0,0])

        Slope_Intercept2 = MathTex(
            r"y = mx + m"
        ).next_to(Rational_m, DOWN)

        Points_Plug_In1 = MathTex(
            r"0 = m(-1) + b"
        ).next_to(Slope_Intercept1, DOWN)

        Points_Plug_In2 = MathTex(
            r"0 = -m + b"
        ).next_to(Slope_Intercept1, DOWN)

        Points_Plug_In3 = MathTex(
            r"m = b"
        ).next_to(Slope_Intercept1, DOWN)

        Quadratic_Equation1 = MathTex(
            r"x^{2} + y^{2} = 1"
        ).next_to(Slope_Intercept1, DOWN)

        Quadratic_Equation2 = MathTex(
            r"x^{2} + (mx + m)^{2} = 1"
        ).next_to(Slope_Intercept1, DOWN)

        Quadratic_Equation3 = MathTex(
            r"x^{2} + m^{2}x^{2} + 2mx + m^{2}= 1"
        ).next_to(Slope_Intercept1, DOWN)

        Quadratic_Equation4 = MathTex(
            r"(1 + m^{2})x^{2} + 2mx + m^{2} - 1 = 0"
        ).next_to(Slope_Intercept1, DOWN)
        Quadratic_Equation4.shift(LEFT*0.5)

        Factored_Equation = MathTex(
            r"(1 + m^{2})(x-\alpha)(x-\beta)=0"
        ).next_to(Quadratic_Equation4, DOWN)

        Quadratic_Formula1 = MathTex(
            r"x_{1,2} = \frac{-b \pm \sqrt{b^2-4ac}}{2a}"
        ).next_to(Factored_Equation, DOWN)

        Quadratic_Formula3 = MathTex(
            r"\alpha, \beta = \frac{-b \pm \sqrt{b^2-4ac}}{2a}"
        ).next_to(Factored_Equation, DOWN)

        Quadratic_Formula4 = MathTex(
            r"\alpha + \beta = \frac{-b + \sqrt{b^2-4c}}{2} + \frac{-b - \sqrt{b^2-4c}}{2}"
        ).next_to(Factored_Equation, DOWN)

        Quadratic_Formula5 = MathTex(
            r"\alpha + \beta = \frac{-b}{a}"
        ).next_to(Factored_Equation, DOWN)

        Quadratic_Formula6 = MathTex(
            r"\alpha + \beta = \frac{-2m^{2}}{1+m^{2}}"
        ).next_to(Factored_Equation, DOWN)

        Zeroes = MathTex(
            r"\alpha = -1, \beta = s"
        ).next_to(Quadratic_Equation1, DOWN)

        Beta1 = MathTex(
            r"\beta = \frac{-b}{a} + 1"
        ).next_to(Zeroes, DOWN)

        Beta2 = MathTex(
            r"\beta = \frac{1-m^{2}}{1+m^{2}}"
        ).next_to(Zeroes, DOWN)

        t1 = MathTex(
            r"y = mx + m"
        ).next_to(Beta1, DOWN)

        t2 = MathTex(
            r"t = m(\frac{1-m^{2}}{1+m^{2}}) + m"
        ).next_to(Beta1, DOWN)

        t3 = MathTex(
            r"y = \frac{2m}{1+m^{2}}"
        ).next_to(Beta1, DOWN)

        Rat_Param = MathTex(
            r"\left( \frac{1-m^{2}}{1+m^{2}},\frac{2m}{1+m^{2}} \right)"
        ).next_to(t3, DOWN)

        self.add(title, page_number)
        
        self.play(
            Create(Circle1),
            Create(Circle2),
            Create(Eq_Name),
            Create(Eq_Name1)
        )

        self.play(
            Create(ax)
        )

        self.wait(5)

        self.play(
            Create(Point_P1)
        )

        self.play(
            a.animate.set_value(-1),
            Transform(Point_P1, Point_P2)
        )

        self.remove(Point_P1)
        self.add(Point_P2)

        self.play(
            Create(Line),
            Create(Point_R)
        )

        self.wait(0.2)

        self.play(
            ax.animate.shift(LEFT * 2),
            Line.animate.shift(LEFT * 2),
            Circle1.animate.shift(LEFT * 2),
            Circle2.animate.shift(LEFT * 2),
            Point_P2.animate.shift(LEFT * 2),
            Point_R.animate.shift(LEFT * 2),
            Eq_Name.animate.shift(LEFT * 2),
            Eq_Name1.animate.shift(LEFT * 2),
            Create(rect)
        )

        self.wait(0.2)

        self.play(
            Create(Point_Name1),
            Create(Point_Name2)
        )

        self.play(
            Create(Rational_m),
        )

        self.play(
            Create(Slope_Intercept1),
        )

        self.play(
            Create(Points_Plug_In1),
        )

        self.play(
            Transform(Points_Plug_In1, Points_Plug_In2)
        )

        self.remove(Points_Plug_In1)
        self.add(Points_Plug_In2)

        self.play(
            Transform(Points_Plug_In2, Points_Plug_In3)
        )

        self.play(
            Transform(Slope_Intercept1, Slope_Intercept2),
        )

        self.play(
            Transform(Rational_m, Rational_b),
        )

        self.play(
            FadeOut(Points_Plug_In2)
        )

        self.play(
            Create(Quadratic_Equation1)
        )

        self.play(
            Transform(Quadratic_Equation1,Quadratic_Equation2)
        )

        self.play(
            Transform(Quadratic_Equation1, Quadratic_Equation3)
        )

        self.play(
            Transform(Quadratic_Equation1, Quadratic_Equation4)
        )

        self.play(
            Create(Factored_Equation)
        )

        self.play(
            Create(Quadratic_Formula1)
        )

        self.play(
            Transform(Quadratic_Formula1, Quadratic_Formula3)
        )

        self.play(
            Transform(Quadratic_Formula1, Quadratic_Formula5)
        )

        self.play(
            Transform(Quadratic_Formula1, Quadratic_Formula6)
        )

        self.play(
            FadeOut(Factored_Equation, Quadratic_Equation1)
        )

        self.play(
            Quadratic_Formula1.animate.next_to(Slope_Intercept2, DOWN)
        )

        Zeroes.next_to(Quadratic_Formula1, DOWN)

        self.play(
            Create(Zeroes)
        )

        Beta1.next_to(Slope_Intercept1, DOWN)
        Beta2.next_to(Slope_Intercept1, DOWN)

        self.play(
            Transform(Quadratic_Formula1, Beta1)
        )

        self.play(
            Transform(Quadratic_Formula1, Beta2)
        )

        self.play(
            FadeOut(Zeroes)
        )

        t1.next_to(Quadratic_Formula1, DOWN)
        t2.next_to(Quadratic_Formula1, DOWN)
        t3.next_to(Quadratic_Formula1, DOWN)

        self.play(
            Create(t1)
        )

        self.play(
            Transform(t1,t2)
        )

        self.play(
            Transform(t1,t3)
        )

        Rat_Param.next_to(Quadratic_Formula1, DOWN)

        self.play(
            Transform(t1, Rat_Param)
        )

        self.remove(t1)
        self.add(Rat_Param)

        self.play(
            FadeOut(Point_Name1, Point_Name2, Rational_m, Slope_Intercept1, Quadratic_Formula1),
            Rat_Param.animate.shift(UP * 4)
        )

        a = ValueTracker(0.5)

        m = ax.get_graph_label(
            graph=Circle1,
            label=Tex("R"),
            x_val= 0.5,
            dot=True,
            direction=UR,
        )

        m.add_updater(
            lambda mob: mob.become(ax.get_graph_label(
                graph=Circle1,
                label=Tex("R"),
                x_val= a.get_value(),
                dot=True,
                direction=RIGHT,
                )
            )
        )

        a_value = Tex(
            "s = "
        ).next_to(Rat_Param, DOWN)

        a_number = DecimalNumber(
            (1 - (a.get_value() ** 2))/(1 + (a.get_value() ** 2)),
            num_decimal_places=3
        )

        a_number.add_updater(
            lambda mob: mob.set_value((1 - (a.get_value() ** 2))/(1 + (a.get_value() ** 2))).next_to(a_value, RIGHT)
        )

        t_value = Tex(
            "t = "
        ).next_to(a_value, DOWN)

        m_number = DecimalNumber(
            (2 * a.get_value())/(1 + (a.get_value() ** 2)),
            num_decimal_places=3
        )

        m_number.add_updater(
            lambda mob: mob.set_value((2 * a.get_value())/(1 + (a.get_value() ** 2))).next_to(t_value, RIGHT)
        )

        self.add(m)
        self.remove(Point_R)

        self.play(
            Create(a_value),
            Create(a_number),
            Create(t_value),
            Create(m_number),
            FadeOut(Line)
        )

        self.play(
             a.animate.set_value(-0.2)
        )

        self.play(
             a.animate.set_value(0.99)
        )

        self.play(
            a.animate.set_value(0.03)
        )