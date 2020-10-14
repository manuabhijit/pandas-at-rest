#!/usr/bin/env python3
from pandasExecutor.executor import PandaExecutor

"""
Module Docstring
"""

__author__ = "Your Abhijit"
__version__ = "0.1.1"
__license__ = "MIT"


def main():
    dataFilePath = 'localS3/location1/sample.csv'
    codeFilePath = 'localS3/location1/code.py'

    code = open(codeFilePath, "r").read()

    respDf = PandaExecutor().runCode(code, dataFilePath)
    print(respDf)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
