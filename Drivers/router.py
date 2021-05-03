from sys import platform
import os


def get_path():

    if platform == "linux" or platform == "linux2":
        return r".\Drivers\chromedriver"
    elif platform == "win32":
        return '.\Drivers\chromedriver.exe'


if __name__ == "__main__":
    get_path()