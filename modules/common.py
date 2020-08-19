import os
import sys


class Common():

    @classmethod
    def blockPrint(cls):
        sys.stdout = open(os.devnull, 'w')

    @classmethod
    def enablePrint(cls):
        sys.stdout = sys.__stdout__
