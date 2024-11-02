from shutil import copy
from os.path import abspath


def fc(file1, file2):
    copy(abspath(file1), abspath(file2))
