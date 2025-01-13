from manim import *

class TreeRight(VGroup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)            
        # Create the root node
        root = Circle(radius=0.2, color=WHITE).set_fill(WHITE, opacity=0.5)

            
        node_left = Circle(radius=0.15, color=BLUE).set_fill(BLUE, opacity=0.5)
        node_right = Circle(radius=0.15, color=BLUE).set_fill(BLUE, opacity=0.5)
        node_left.next_to(root, DOWN + LEFT * 2.5)
        node_right.next_to(root, DOWN + RIGHT * 2.5)

        line_left = Line(root.get_bottom(), node_left.get_top(), color=WHITE)
        line_right = Line(root.get_bottom(), node_right.get_top(), color=WHITE)

        leaf_yes_left = Circle(radius=0.1, color=GREEN).set_fill(GREEN, opacity=0.5)
        leaf_no_left = Circle(radius=0.1, color=RED).set_fill(RED, opacity=0.5)
        leaf_yes_left.next_to(node_left, DOWN + LEFT * 0.5)
        leaf_no_left.next_to(node_left, DOWN + RIGHT * 0.5)
        line_yes_left = Line(node_left.get_bottom(), leaf_yes_left.get_top(), color=WHITE)
        line_no_left = Line(node_left.get_bottom(), leaf_no_left.get_top(), color=WHITE)

        node_right_1 = Circle(radius=0.12, color=BLUE_A).set_fill(BLUE_A, opacity=0.5)
        node_right_1.next_to(node_right, DOWN + RIGHT * 0.5)
        line_right_1 = Line(node_right.get_bottom(), node_right_1.get_top(), color=WHITE)
        leaf_left_1 = Circle(radius = 0.1, color=RED).set_fill(color=RED, opacity=0.5)
        leaf_left_1.next_to(node_right, DOWN + LEFT * 0.5)
        line_left_1 = Line(node_right.get_bottom(), leaf_left_1.get_top(), color=WHITE)
        
        node_right_2 = Circle(radius=0.12, color=BLUE_B).set_fill(BLUE_B, opacity=0.5)
        node_right_2.next_to(node_right_1, DOWN + RIGHT * 0.5)
        line_right_2 = Line(node_right_1.get_bottom(), node_right_2.get_top(), color=WHITE)
        leaf_left_2 = Circle(radius = 0.1, color=RED).set_fill(color=RED, opacity=0.5)
        leaf_left_2.next_to(node_right_1, DOWN + LEFT * 0.5)
        line_left_2 = Line(node_right_1.get_bottom(), leaf_left_2.get_top(), color=WHITE)

        leaf_yes_last = Circle(radius=0.1, color=GREEN).set_fill(color=GREEN, opacity=0.5)
        leaf_yes_last.next_to(node_right_2, DOWN + LEFT *0.5)
        line_yes_last = Line(node_right_2.get_bottom(), leaf_yes_last.get_top(), color=WHITE)
        leaf_no_last = Circle(radius=0.1, color=RED).set_fill(color=RED, opacity=0.5)
        leaf_no_last.next_to(node_right_2, DOWN + RIGHT *0.5)
        line_no_last = Line(node_right_2.get_bottom(), leaf_no_last.get_top(), color=WHITE)


        self.add(
        root,                           #0
        node_left,                      #1
        node_right,                     #2
        line_left,                      #3
        line_right,                     #4
        leaf_yes_left,                  #5
        leaf_no_left,                   #6
        line_yes_left,                  #7
        line_no_left,                   #8
        node_right_1,                   #9
        line_right_1,                   #10
        leaf_left_1,                    #11
        line_left_1,                    #12
        node_right_2,                   #13
        line_right_2,                   #14
        leaf_left_2,                    #15
        line_left_2,                    #16
        leaf_yes_last,                  #17
        line_yes_last,                  #18
        leaf_no_last,                   #19
        line_no_last                    #20
        )
        self.scale(0.6)