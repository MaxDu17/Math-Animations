from manimlib.imports import *
class AddingText(Scene):
    def construct(self):
        my_first_text=TextMobject("Writing with manim is fun")
        second_line=TextMobject("and easy to do!")
        second_line.next_to(my_first_text,DOWN)
        third_line=TextMobject("for me and you!")
        third_line.next_to(my_first_text,DOWN)

        self.add(my_first_text, second_line)
        self.wait(2)
        self.play(Transform(second_line,third_line))
        self.wait(2)
        self.play(ApplyMethod(second_line.shift, 3*DOWN))
        self.play(ApplyMethod(my_first_text.shift,3*UP))
        self.wait(2)


class Coordinates(ThreeDScene):
    def func(self, x):
        return x**2 + 1

    def construct(self):
        func = lambda p: np.array([
            p[1]/2,  # x
            -p[0]/2,  # y
            0        # z
        ])
        # Normalized
        vector_field_norm = VectorField(func)
        # Not normalized
        vector_field_not_norm = VectorField(func, length_func=linear)
        self.play(*[GrowArrow(vec) for vec in vector_field_norm])
        self.wait(2)
        self.play(ReplacementTransform(vector_field_norm,vector_field_not_norm))
        self.wait(2)
    