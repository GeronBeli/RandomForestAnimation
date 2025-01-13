from manim import *

from tree_left import TreeLeft
from tree_middle import TreeMiddle
from tree_right import TreeRight

FLAG = True

class RandomForest(Scene):
    def construct(self):
        title = Text("Random Forest Classifier", font_size=48).to_edge(UP)
        
        self.play(Write(title), run_time=2)
        self.wait()
        
        subsets = VGroup()
        for i in range(3):
            dots = VGroup(*[
                Dot(radius=0.05, color=random_bright_color())
                for _ in range(7)
            ])
            dots.arrange_in_grid(rows=1, buff=0.1).scale(0.8)
            dots.move_to(UP * 2 + RIGHT * (i - 1) * 5)
            subsets.add(dots)

        for dots in subsets:
            self.play(LaggedStartMap(FadeIn, dots, lag_ratio=0.2), run_time=1.5)
        self.wait()

        trees = VGroup()
        tree_classes = [TreeLeft, TreeMiddle, TreeRight] 

        for i, tree_class in enumerate(tree_classes):
            tree = tree_class()
            tree.next_to(subsets[i], DOWN, buff=0.2)  
            trees.add(tree)  


      
        for tree in trees:
            self.play(DrawBorderThenFill(tree), run_time=2)
            self.wait(0.5)

        paths = [
            [0, 2, 4],  
            [0, 4, 2, 15, 12, 19, 17],  
            [0, 4, 2, 10, 9, 14, 13, 20, 19]    
        ]

        if FLAG:
            paths[2] = [0, 3, 1, 7, 5]

        

        for i, tree in enumerate(trees):
            for step in paths[i]:
                self.play(tree[step].animate.set_color(YELLOW), run_time=0.5)
            self.wait()

        result_box = Rectangle(width=3, height=1.5, color=GREEN if FLAG else RED).move_to(DOWN * 3)
        result_text = Text(f"Result: {1 if FLAG else 0}", font_size=24).move_to(result_box.get_center())

        arrows = VGroup()
        for tree in trees:
            arrow = Arrow(
                start=tree.get_bottom(),
                end=result_box.get_top(),
                buff=0.2,
                color=YELLOW,
                stroke_width=3
            )
            arrows.add(arrow)

        self.play(LaggedStartMap(Create, arrows, lag_ratio=0.2), run_time=2)
        self.play(Create(result_box), FadeIn(result_text), run_time=2)
        self.wait()

        # Fade out everything
        self.play(FadeOut(subsets), FadeOut(trees),  FadeOut(arrows), FadeOut(result_box), FadeOut(result_text),
                  FadeOut(title))
        self.wait()
