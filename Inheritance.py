class BaseClass:
    def base_class_method():
        print("This is method in the base class")


class FirstLevel(BaseClass):
    def first_level_class_method():
        print("This is method in the first inherited class")


class SecondLevel(FirstLevel):
    def second_level_class_method():
        print("This is method in the second inherited class")


class ThirdLevel(SecondLevel):
    def third_level_class_method():
        print("This is method in the third inherited class")


ThirdLevel.base_class_method()  #Third level class can access methods in base class
ThirdLevel.first_level_class_method()   #Third level class can access methods in first inherited class
ThirdLevel.second_level_class_method()  #Third level class can access methods in second inherited class
ThirdLevel.third_level_class_method()   #Third level class can access its own methods

