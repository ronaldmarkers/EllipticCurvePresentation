from manim import *

class Title(Scene):
    def construct(self):


        text1 = MarkupText(
            'Elliptic Curves: ', font="Century Gothic"
        )
        text2 = MarkupText(
            'Understanding Their Significance', font="Century Gothic"
        )
        text3 = MarkupText(
            'and the Point Addition Operation', font="Century Gothic"
        )
        text4 = MarkupText(
            'Raul Marquez', font="Century Gothic"
        ).scale(0.75)

        Image = ImageMobject(
            "UTRGV.png"
        ).scale(0.25)

        group = VGroup(text1, text2, text3, text4).arrange(DOWN, center=False, aligned_edge=LEFT)
        group.move_to([-2.5,-1,0])  
        group.scale(0.5)

        Image.move_to([-3.75,-3,0])

        graph = ImplicitFunction(
            lambda x, y: x ** 3 - y ** 2 - x,
            color=YELLOW
        ).move_to([3,1,0])
        

        line = ImplicitFunction(
            lambda x, y: 0.2 * x + 4 - y
        ).move_to([3,1,0])

        self.add(
            group, Image
        )

        self.play(
            Create(graph)
        )

        self.play(
            Create(line)
        )


