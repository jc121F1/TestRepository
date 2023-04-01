import pytest
import time
from feature3 import Feature3

class Test_Feature3Tests():

    def test_feature3method1(self):
        assert Feature3.feature3method1() == True

    def test_feature3method2(self):
        assert Feature3.feature3method2() == True

    def test_feature3method3(self):
        assert Feature3.feature3method3() == True
