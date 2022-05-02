from __future__ import annotations
from abc import ABC, abstractmethod
from random import randint
from src.Field import Field


class FruitCreator(ABC):
    """
        Abstract factory for pattern
    """

    @abstractmethod
    def factory_method(self):
        pass

    def create(self, coordinates):
        """
            Creates fruit on coordinates
        """
        fruit = self.factory_method(coordinates)
        return fruit


class AppleCreator(FruitCreator):
    """
        Creator class for Apples
    """

    def factory_method(self, coordinates):
        return Apple(coordinates)


class PineappleCreator(FruitCreator):
    """
        Creator class for Pineapples
    """

    def factory_method(self, coordinates):
        return Pineapple(coordinates)


# class Fruit(ABC):
#     """
#         Abstract class for fruits
#     """
#
#     @abstractmethod
#     def __str__(self):
#         pass
#
#     @abstractmethod
#     def getCoord(self):
#         pass
#
#     @abstractmethod
#     def getColor(self):
#         pass


class Apple:
    """
        Class for Apples.
        Apple gives 10 points.
    """

    def __init__(self, coordinates):
        self.color = "red"
        self.coordinates = coordinates

    def getColor(self):
        return self.color

    def getCoords(self):
        return self.coordinates


class Pineapple:
    """
        Class for Pinepples.
        Pineapple clones a Snake. If Snake eats Pineapple, amount of Snakes will increase.
    """

    def __init__(self, coordinates):
        self.color = "yellow"
        self.coordinates = coordinates

    def getColor(self):
        return self.color

    def getCoords(self):
        return self.coordinates


def generate_fruit(fruit):
    """
        Factory method to generate new fruit on random Point
    """
    coordinates = [randint(0, Field.lengthX - 1),
                   randint(0, Field.heightY - 1)]
    if fruit == "Apple":
        return AppleCreator().create(coordinates)
    elif fruit == "Pineapple":
        return PineappleCreator().create(coordinates)
