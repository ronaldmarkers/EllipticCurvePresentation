from manim import *

class Hook(Scene):
    def construct(self):

        title = Title(f"What Do All Of These Things Have In Common?")
        page_number = MarkupText(
            "2"
        ).move_to([6.5,4,0])
        page_number.match_y(title)

        bitcoin = ImageMobject("bitcoin.png").move_to([-4.25,0.25,0], [0,0,0])
        bitcoin.scale(0.5)
        subtitle_1 = MarkupText(
            'Encryption', font="Century Gothic"
        ).move_to([-5,-1.25,0], [0,0,0])
        subtitle_1.match_x(bitcoin)
        subtitle_1.scale(0.5)

        flt = ImageMobject("flt.png").move_to([0,0.25,0], [0,0,0])
        flt.scale(0.5)     
        subtitle_2a = MarkupText(
            'Fermat\'s', font="Century Gothic"
        )
        subtitle_2b = MarkupText(
            'Last Theorem', font="Century Gothic"
        )
        subtitle2 = VGroup(subtitle_2a, subtitle_2b).arrange(DOWN)
        subtitle2.scale(0.5)

        bsd = ImageMobject("bsd.jpg").move_to([4.25,0.25,0], [0,0,0])
        bsd.scale(0.5)
        subtitle_3a = MarkupText(
            'Birch Swinnerton', font="Century Gothic"
        ).move_to([4.25,-1.25,0], [0,0,0])
        subtitle_3b = MarkupText(
            'Dyer Conjecture', font="Century Gothic"
        ).move_to([4.25,-1.88,0], [0,0,0])
        subtitle3 = VGroup(subtitle_3a, subtitle_3b).arrange(DOWN, center=False, aligned_edge=LEFT)
        subtitle3.scale(0.5)

        ax = Axes().scale(0.75)

        graph = ImplicitFunction(
            lambda x, y: x ** 3 - y ** 2 - x,
            color=YELLOW
        ).scale(0.75)

        subtitle_1.match_y(subtitle3)
        subtitle2.match_y(subtitle_1)

        self.add(title, page_number)
        self.add(bitcoin)
        self.add(flt)
        self.add(bsd)

        self.play(
            Create(subtitle_1), Create(subtitle2), Create(subtitle3)
        )

        self.wait(8)

        self.play(
            FadeOut(bitcoin, flt, bsd, subtitle_1, subtitle2, subtitle3)
        )

        self.wait(0.5)

        self.play(
            Create(ax)
        )

        self.play(
            Create(graph)
        )