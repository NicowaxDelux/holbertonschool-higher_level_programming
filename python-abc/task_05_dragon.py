#!/usr/bin/env python3


class SwimMixin:
    """ class swinmixin
    """
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """ class flymixin
    """
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """class dragon
    """
    def roar(self):
        print("The dragon roars!")
