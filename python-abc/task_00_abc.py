#!/usr/bin/env python3
"""class and subclasses
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """class animal
    """
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """method dog
    """
    def sound(self):
        """method sound

        Return: bark
        """
        return "Bark"


class Cat(Animal):
    """class cat
    """
    def sound(self):
        return "Meow"
