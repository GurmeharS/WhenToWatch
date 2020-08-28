import os
import sys
from enum import Enum


class Common():

    @classmethod
    def blockPrint(cls):
        sys.stdout = open(os.devnull, 'w')

    @classmethod
    def enablePrint(cls):
        sys.stdout = sys.__stdout__


class GameStatus(Enum):
    ended = 1
    postponed = 2
    running = 3
    halftime = 4
    unknown = 5
