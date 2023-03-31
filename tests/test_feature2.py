from feature2 import Feature2
import pytest
import time

class Feature2Tests():

    def test_feature2method1():
        assert Feature2.feature2method1() == False

    def test_feature2method2():
        assert Feature2.feature2method2() == True

    def test_feature2method3():
        assert Feature2.feature2method3 == False