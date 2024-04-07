from manim import *

class History(Scene):
    def construct(self):

        title = Title(f"Brief History Of Elliptic Curves")
        page_number = MarkupText(
            "6"
        ).move_to([6.5,4,0])
        page_number.match_y(title)
        
        Diophantus = ImageMobject("Diophantus.png").move_to([-4,0.25,0]).scale_to_fit_height(3)
        Dio_Name = MarkupText(
            "Diophantus", font="Century Gothic"
        ).move_to([-4,-2,0])
        Dio_Name.scale_to_fit_height(0.4)

        Newton = ImageMobject("Newton.jpg").move_to([0,0.25,0]).scale_to_fit_height(3)
        New_Name1 = MarkupText(
            "Sir Isaac", font="Century Gothic"
        )
        New_Name1.scale_to_fit_height(0.4)
        New_Name2 = MarkupText(
            "Newton", font="Century Gothic"
        )
        New_Name2.scale_to_fit_height(0.4)
        New_Name = VGroup(New_Name1, New_Name2).arrange(DOWN)
        New_Name.move_to([0,-2,0])

        Fermat = ImageMobject("Fermat.jpg").move_to([4,0.25,0]).scale_to_fit_height(3)
        Fer_Name1 = MarkupText(
            "Pierre De", font="Century Gothic"
        )
        Fer_Name1.scale_to_fit_height(0.4)
        Fer_Name2 = MarkupText(
            "Fermat", font="Century Gothic"
        )
        Fer_Name2.scale_to_fit_height(0.4)
        Fer_Name = VGroup(Fer_Name1, Fer_Name2).arrange(DOWN)
        Fer_Name.move_to([4,-2,0])

        Jacobi = ImageMobject("Jacobi.jpg").move_to([-3,0.25,0]).scale_to_fit_height(3)
        Jac_Name1 = MarkupText(
            "Carl Gustav", font="Century Gothic"
        )
        Jac_Name1.scale_to_fit_height(0.4)
        Jac_Name2 = MarkupText(
            "Jacob Jacobi", font="Century Gothic"
        )
        Jac_Name2.scale_to_fit_height(0.4)
        Jac_Name = VGroup(Jac_Name1, Jac_Name2).arrange(DOWN)
        Jac_Name.move_to([-3,-2,0])

        Weirstrass = ImageMobject("Weirstrass.jpg").move_to([3,0.25,0]).scale_to_fit_height(3)
        Weir_Name1 = MarkupText(
            "Karl", font="Century Gothic"
        )
        Weir_Name1.scale_to_fit_height(0.4)
        Weir_Name2 = MarkupText(
            "Weirstrass", font="Century Gothic"
        )
        Weir_Name2.scale_to_fit_height(0.4)
        Weir_Name = VGroup(Weir_Name1, Weir_Name2).arrange(DOWN)
        Weir_Name.move_to([3,-2,0])

        Mordell = ImageMobject("Mordell.jpeg").move_to([-4,0.25,0]).scale_to_fit_height(3)

        Mor_Name1 = MarkupText(
            "Louis J.", font="Century Gothic"
        )
        Mor_Name1.scale_to_fit_height(0.3)
        Mor_Name2 = MarkupText(
            "Mordell", font="Century Gothic"
        )
        Mor_Name2.scale_to_fit_height(0.3)
        Mor_Name = VGroup(Mor_Name1, Mor_Name2).arrange(DOWN)
        Mor_Name.move_to([-4,-2,0])

        MorWei_Name1 = MarkupText(
            "Mordell-Weil", font="Century Gothic", weight="BOLD"
        )
        MorWei_Name1.scale_to_fit_height(0.3)
        MorWei_Name2 = MarkupText(
            "Theorem", font="Century Gothic", weight="BOLD"
        )
        MorWei_Name2.scale_to_fit_height(0.3)
        MorWei_Name = VGroup(MorWei_Name1, MorWei_Name2).arrange(DOWN)
        MorWei_Name.move_to([-4,-2,0])

        Hasse = ImageMobject("hasse.jpg").move_to([0,0.25,0]).scale_to_fit_height(3)

        Has_Name1 = MarkupText(
            "Helmut", font="Century Gothic"
        )
        Has_Name1.scale_to_fit_height(0.3)
        Has_Name2 = MarkupText(
            "Hasse", font="Century Gothic"
        )
        Has_Name2.scale_to_fit_height(0.3)
        Has_Name = VGroup(Has_Name1, Has_Name2).arrange(DOWN)
        Has_Name.move_to([0,-2,0])

        HasWei_Name1 = MarkupText(
            "Hasse-Weil", font="Century Gothic", weight="BOLD"
        )
        HasWei_Name1.scale_to_fit_height(0.3)
        HasWei_Name2 = MarkupText(
            "L-Functions", font="Century Gothic", weight="BOLD"
        )
        HasWei_Name2.scale_to_fit_height(0.3)
        HasWei_Name = VGroup(HasWei_Name1, HasWei_Name2).arrange(DOWN)
        HasWei_Name.move_to([0,-2,0])

        Wiles = ImageMobject("Wiles.jpg").move_to([4,0.25,0]).scale_to_fit_height(3)

        Wil_Name1 = MarkupText(
            "Andrew", font="Century Gothic"
        )
        Wil_Name1.scale_to_fit_height(0.3)
        Wil_Name2 = MarkupText(
            "Wiles", font="Century Gothic"
        )
        Wil_Name2.scale_to_fit_height(0.3)
        Wil_Name = VGroup(Wil_Name1, Wil_Name2).arrange(DOWN)
        Wil_Name.move_to([4,-2,0])

        Mod_Name1 = MarkupText(
            "Modular Forms", font="Century Gothic", weight="BOLD"
        )
        Mod_Name1.scale_to_fit_height(0.3)
        Mod_Name2 = MarkupText(
            "Fermat's Last Theorem", font="Century Gothic", weight="BOLD"
        )
        Mod_Name2.scale_to_fit_height(0.3)
        Mod_Name = VGroup(Mod_Name1, Mod_Name2).arrange(DOWN)
        Mod_Name.move_to([4,-2,0])
        
        self.add(title, page_number)
        self.add(Mordell, Mor_Name, Hasse, Has_Name, Wiles, Wil_Name)

        self.play(
            FadeOut(Mor_Name, Has_Name, Wil_Name)
        )

        self.play(
            FadeIn(MorWei_Name, HasWei_Name, Mod_Name)
        )