# -*- encoding: utf-8 -*-
"""
    tests
    -----

    Entry-point of the testsuite.

    :copyright: (c) 2013 by Morgan Delahaye-Prat.
    :license: BSD, see LICENSE for more details.
"""






# testenv setup

import os
import sys
import unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))


# import all the tests here

from helpers import *
from schema import *
from widget import *
from modifiers import *
from form import *


if __name__ == '__main__':

    unittest.main()
