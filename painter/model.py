# TODO: Add code here
import matplotlib.pyplot as plt
import pickle

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

class Circle:
    def __init__(self, center: Point, radius: float):
        self.center = center
        self.radius = radius

    def area(self)-> float:
        return 3.1416 * (self.radius * 2)



class Triangle:
    def __init__(self, point_1: Point, point_2: Point, point_3: Point):
        self.point_1 = point_1
        self.point_2 = point_2
        self.point_3 = point_3


class Rectangle:
    def __init__(self, point_1: Point, point_2: Point):
        self.point_1 = point_1
        self.point_2 = point_2


class Painter:
    FILE = ".painter"

    def __init__(self) -> None:
        self.shapes: list = []
        self._load()

    def _load(self) -> None:
        try:
            with open(Painter.FILE, "rb") as f:
                self.shapes = pickle.load(f)
        except (EOFError, FileNotFoundError):
            self.shapes = []

    def _save(self) -> None:
        with open(Painter.FILE, "wb") as f:
            pickle.dump(self.shapes, f)

    def add_shape(self, shape) -> None:
        self.shapes.append(shape)
        self._save()

    def total_area(self) -> float:
        return sum(shape.area() for shape in self.shapes)

    def clear(self) -> None:
        self.shapes = []
        self._save()
