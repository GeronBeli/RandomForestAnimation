from manim import *

class TreeLeft(VGroup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)            
        # Create the root node
        root = Circle(radius=0.2, color=WHITE).set_fill(WHITE, opacity=0.5)

        # Level 1 - Left and Right decision nodes
        left_leaf = Circle(radius=0.15, color=RED).set_fill(RED, opacity=0.5)
        right_node = Circle(radius=0.15, color=BLUE).set_fill(BLUE, opacity=0.5)
        left_leaf.next_to(root, DOWN + LEFT * 2)
        right_node.next_to(root, DOWN + RIGHT * 2)

        # Lines to Level 1
        line_left = Line(root.get_bottom(), left_leaf.get_top(), color=WHITE)
        line_right = Line(root.get_bottom(), right_node.get_top(), color=WHITE)



        # Level 2 - Right subtree
        right_left_node = Circle(radius=0.12, color=BLUE_A).set_fill(BLUE_A, opacity=0.5)
        right_right_node = Circle(radius=0.12, color=BLUE_A).set_fill(BLUE_A, opacity=0.5)
        right_left_node.next_to(right_node, DOWN + LEFT * 1.5)
        right_right_node.next_to(right_node, DOWN + RIGHT * 1.5)

        # Lines to Level 2
        line_right_left = Line(right_node.get_bottom(), right_left_node.get_top(), color=WHITE)
        line_right_right = Line(right_node.get_bottom(), right_right_node.get_top(), color=WHITE)

        # Level 2 Leaves
        yes_leaf_1 = Circle(radius=0.1, color=GREEN).set_fill(GREEN, opacity=0.5)
        no_leaf_1 = Circle(radius=0.1, color=RED).set_fill(RED, opacity=0.5)
        yes_leaf_2 = Circle(radius=0.1, color=GREEN).set_fill(GREEN, opacity=0.5)
        no_leaf_2 = Circle(radius=0.1, color=RED).set_fill(RED, opacity=0.5)

        yes_leaf_1.next_to(right_left_node, DOWN + LEFT * 0.5)
        no_leaf_1.next_to(right_left_node, DOWN + RIGHT * 0.5)
        yes_leaf_2.next_to(right_right_node, DOWN + LEFT * 0.5)
        no_leaf_2.next_to(right_right_node, DOWN + RIGHT * 0.5)

        # Lines to leaves
        line_yes_1 = Line(right_left_node.get_bottom(), yes_leaf_1.get_top(), color=WHITE)
        line_no_1 = Line(right_left_node.get_bottom(), no_leaf_1.get_top(), color=WHITE)
        line_yes_2 = Line(right_right_node.get_bottom(), yes_leaf_2.get_top(), color=WHITE)
        line_no_2 = Line(right_right_node.get_bottom(), no_leaf_2.get_top(), color=WHITE)

        

        self.add(
            root,                           #0    
            right_node,                     #1
            line_left,                      #2
            line_right,                     #3
            left_leaf,                      #4
            right_left_node,                #5
            right_right_node,               #6
            line_right_left,                #7
            line_right_right,               #8
            yes_leaf_1,                     #9
            no_leaf_1,                      #10
            yes_leaf_2,                     #11
            no_leaf_2,                      #12
            line_yes_1,                     #13
            line_no_1,                      #14
            line_yes_2,                     #15
            line_no_2,                      #16
        )
        self.scale(0.6)

