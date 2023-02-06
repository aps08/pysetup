import os
import sys
import unittest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

# above code so that you can import any thing from the src directory

# Test file names should be like *_test.py
# Test function name should start with test. Example:
# def test_main():
#   code here
# your test cases goes here
