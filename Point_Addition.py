from manim import *

class PA(Scene):
    def construct(self):

        title = Title(f"Elliptic Point Addition: ")
        title1 = MathTex(r"P \oplus P").move_to([3.5,3.25,0])
        page_number = MarkupText(
            "12"
        ).move_to([6.5,4,0])
        page_number.match_y(title)

        Elliptic_Curve = MathTex(
            r"y^{2} = x^{3} - 2x"
        ).move_to([-4,2,0])

        ax = Axes(
            x_range=[-3, 3, 1],
            y_range=[-4, 4, 1],
            tips=False,
            axis_config={"include_numbers": True}
        ).scale_to_fit_height(5)

        EC = ax.plot_implicit_curve(lambda x, y: x ** 3 - y ** 2 - 2*x)

        p = Dot(color=RED).move_to(ax.c2p(-1,np.sqrt((-1)**3-2*(-1))))

        labelp = Tex(r"P").next_to(p, UP)

        q = Dot(color=RED).move_to(ax.c2p(-1/169,np.sqrt((-1/169)**3-2*(-1/169))))

        labelq = Tex(r"Q").next_to(q, UR)

        r = Dot(color=RED).move_to(ax.c2p(9/4,np.sqrt((9/4)**3-2*(9/4))))

        labelr = Tex(r"R").next_to(r, UL)

        neg = Dot(color=RED).move_to(ax.c2p(9/4,(-1)*(np.sqrt((9/4)**3-2*(9/4)))))

        labelneg = Tex(r"-R").next_to(neg, UR)

        Line = ax.plot(lambda x: (1/2)*(x+1) + 1)

        Line2 = ax.plot_implicit_curve=(lambda x,y: x-(9/4)+(0.0000000000000000001)*y)

        self.add(title, title1, page_number, EC, p, r, neg, ax, Elliptic_Curve, Line, labelneg, labelp, labelr)

        