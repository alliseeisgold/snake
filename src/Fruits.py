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


class Fruit(ABC):
    """
        Abstract class for fruits
    """

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_radius(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    """
        Returns coordinates of the fruit. 
    """

    @abstractmethod
    def get_coords(self):
        pass

    """
        Returns color of the fruit.
    """

    @abstractmethod
    def get_color(self):
        pass


class Apple(Fruit):
    """
        Class for Apples.
        If Snake eats Apple, your score will increase to 5.
    """

    def __str__(self):
        return 'Apple'

    def __init__(self, coordinates):
        self.radius = 7
        self.color = "red"
        self.coordinates = coordinates

    def get_color(self):
        return self.color

    def get_coords(self):
        return self.coordinates

    def get_radius(self):
        return self.radius


class Pineapple(Fruit):
    """
        Class for Pineapples.
        If Snake eats Pineapple, your score will increase to 10.
    """

    def __str__(self):
        return 'Pineapple'

    def __init__(self, coordinates):
        self.radius = 10
        self.color = "yellow"
        self.coordinates = coordinates

    def get_color(self):
        return self.color

    def get_coords(self):
        return self.coordinates

    def get_radius(self):
        return self.radius


def generate_fruit(fruit):
    """
        Factory method to generate new fruit on random point in the field.
    """
    field = Field()
    coordinates = [randint(50, field.get_length() - 60),
                   randint(50, field.get_height() - 60)]
    if fruit == "Apple":
        return AppleCreator().create(coordinates)
    elif fruit == "Pineapple":
        return PineappleCreator().create(coordinates)
