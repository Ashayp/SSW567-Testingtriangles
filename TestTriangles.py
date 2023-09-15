import unittest
from classifyTriangle import classify_triangle

class TestTriangles(unittest.TestCase):    
    def testSet1(self):
        self.assertEqual(classify_triangle(3,4,5),'Right','3,4,5 is a Right triangle')
        
    def testSet2(self):
        self.assertEqual(classify_triangle(4,3,5),'Right','4,3,5 is a Right triangle')

    def testSet3(self):
        self.assertEqual(classify_triangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testSet4(self):
        self.assertNotEqual(classify_triangle(10,10,10),'Isoceles','Should be Equilateral')

    def testSet5(self):
        self.assertEqual(classify_triangle(10,15,30),'Not a triangle','Should not be a triangle')

    def testSet6(self):
        self.assertEqual(classify_triangle(-10,15,30),'Scalene','Different numbers')    #buggy test

    def testSet7(self):
        self.assertNotEqual(classify_triangle(-10,15,30),'Scalene','Input Cannot be negative')

    def testSet8(self):         
        self.assertNotEqual(classify_triangle(-10,-10,-10),'Equilateral','Input Cannot be negative')                

    def testSet9(self):
        self.assertEqual(classify_triangle(0,1,1),'Not a triangle','Side is zero')


if __name__ == '__main__':    
    print('Running unit tests')
    unittest.main()