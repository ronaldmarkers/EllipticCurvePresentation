from manim import *

class Group(Scene):
    def construct(self):

        title = Title(f"Definition of Group")
        page_number = MarkupText(
            "10"
        ).move_to([6.5,4,0])
        page_number.match_y(title)

        Definition = Tex(
            "A group is a set and an operation that follows the following constraints"
        ).move_to([0,2,0])

        Definition.scale_to_fit_width(12)

        Def1 = MarkupText(
            "1.) The operations is closed under the set. i.e. Answers are in the set"
        )

        Def2 = MarkupText(
            "2.) The set has an identity element. i.e. The element can't change other elements with the operation"
        )

        Def3 = MarkupText(
            "3.) The operations follows the associative property i.e. Order doesn't matter"
        )

        Def4 = MarkupText(
            "4.) There is an inverse element. i.e. The element will take you to the identity element"
        )

        Constraints = VGroup(Def1, Def2, Def3, Def4).arrange(DOWN, center=False, aligned_edge=LEFT)
        Constraints.move_to([-3,0,0])
        Constraints.scale_to_fit_width(12)

        Example1 = MarkupText(
            "Example: Addition under Integers is a group"
        )

        Example2 = MarkupText(
            "Integer + Integer = Integer, 0 is identity element, a + b = b + a, a + (-a) = 0"
        )

        Examples = VGroup(Example1, Example2).arrange(DOWN, center=False, aligned_edge=LEFT)
        Examples.move_to([-3,-2,0])
        Examples.scale_to_fit_width(12)

        NonExample1 = MarkupText(
            "Non-Example: Multiplication Under Integers isn't a group"
        )

        NonExample2 = MarkupText(
            "If the identity element of this set is 1, then if a*b = 1, then either a or b isn't an integer."
        )

        NonExamples = VGroup(NonExample1, NonExample2).arrange(DOWN, center=False, aligned_edge=LEFT)
        NonExamples.move_to([-3,-3,0])
        NonExamples.scale_to_fit_width(12)

        self.add(title, page_number)
        self.add(Definition, Constraints, Examples, NonExamples)