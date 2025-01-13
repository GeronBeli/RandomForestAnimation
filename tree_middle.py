from manim import *

class TreeMiddle(VGroup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)            
        # Create the root node
        root = Square(side_length=0.3, color=WHITE).set_fill(WHITE, opacity=0.5)

        # Level 1 - Left and Right decision nodes
        node_left = Square(side_length=0.2, color=BLUE).set_fill(BLUE, opacity=0.5)
        node_right = Square(side_length=0.2, color=BLUE).set_fill(BLUE, opacity=0.5)
        node_left.next_to(root, DOWN + LEFT * 2.5)
        node_right.next_to(root, DOWN + RIGHT * 2.5)

        # Lines to Level 1
        line_left = Line(root.get_bottom(), node_left.get_top(), color=WHITE)
        line_right = Line(root.get_bottom(), node_right.get_top(), color=WHITE)

        # Level 2 - Left subtree
        left_leaf = Square(side_length=0.15, color=RED).set_fill(RED, opacity=0.5)
        left_leaf.next_to(node_left, DOWN + LEFT * 0.5)
        line_left_leaf = Line(node_left.get_bottom(), left_leaf.get_top(), color=WHITE)

        left_right_node = Square(side_length=0.15, color=BLUE_A).set_fill(BLUE_A, opacity=0.5)
        left_right_node.next_to(node_left, DOWN + RIGHT * 0.5)
        left_right_line = Line(node_left.get_bottom(), left_right_node.get_top(), color=WHITE)

        leaf_yes_1 = Square(side_length=0.12, color= GREEN).set_fill(GREEN, opacity=0.5)
        leaf_no_1 = Square(side_length=0.12, color= RED).set_fill(RED, opacity=0.5)
        leaf_no_1.next_to(left_right_node, DOWN + RIGHT * 0.5)
        leaf_yes_1.next_to(left_right_node, DOWN + LEFT * 0.5)
        line_leaf_yes_1 = Line(left_right_node.get_bottom(), leaf_yes_1.get_top(), color=WHITE)
        line_leaf_no_1 = Line(left_right_node.get_bottom(), leaf_no_1.get_top(), color=WHITE)


        # Level 2 - Right subtree
        right_left_node = Square(side_length=0.15, color=BLUE_A).set_fill(BLUE_A, opacity=0.5)
        right_left_node.next_to(node_right, DOWN + LEFT * 0.5)
        right_right_leaf = Square(side_length=0.15, color=GREEN).set_fill(GREEN, opacity=0.5)
        right_right_leaf.next_to(node_right, DOWN + RIGHT * 0.5)

        line_right_left = Line(node_right.get_bottom(), right_left_node.get_top(), color=WHITE)
        line_right_right = Line(node_right.get_bottom(), right_right_leaf.get_top(), color=WHITE)

        # Leaves of the second level
        right_left_yes = Square(side_length=0.15, color=GREEN).set_fill(GREEN, opacity=0.5)
        right_left_no = Square(side_length=0.15, color=RED).set_fill(RED, opacity=0.5)
        right_left_yes.next_to(right_left_node, DOWN + LEFT * 0.5)
        right_left_no.next_to(right_left_node, DOWN + RIGHT * 0.5)

        line_yes = Line(right_left_node.get_bottom(), right_left_yes.get_top(), color=WHITE)
        line_no = Line(right_left_node.get_bottom(), right_left_no.get_top(), color=WHITE)


        self.add(
        root,                           #0
        node_left,                      #1
        node_right,                     #2
        line_left,                      #3
        line_right,                     #4
        left_right_node,                #5
        left_right_line,                #6
        left_leaf,                      #7
        leaf_yes_1,                     #8
        leaf_no_1,                      #9
        line_leaf_yes_1,                #10
        line_leaf_no_1,                 #11
        right_left_node,                #12
        right_right_leaf,               #13
        line_left_leaf,                 #14
        line_right_left,                #15
        line_right_right,               #16
        right_left_yes,                 #17
        right_left_no,                  #18
        line_yes,                       #19
        line_no                         #20
        )
        self.scale(0.6)
