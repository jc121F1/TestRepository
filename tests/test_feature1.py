from feature1 import Feature1

class Test_Feature1Tests():
    
    def test_feature1method1(self):
        assert Feature1().feature1method1() == False

    def test_feature1method2(self):
        assert Feature1().feature1method2() == True