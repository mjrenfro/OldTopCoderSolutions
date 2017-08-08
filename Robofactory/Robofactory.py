import sys
import unittest

'''
Constraints
-	n will be between 1 and 50, inclusive.
-	query and answer will contain exactly n elements.
-	Each element in query will be between 1 and 1000, inclusive.
-	Each element in answer will be either "Odd" or "Even".
-	It is guaranteed that there will be at least one possible number of the corrupted robot.
'''

class Robofactory:

    def IsCorrect(self, query,answer):
        return (answer is "Odd" and query%2 is 1) or (answer is "Even" and query%2 is 0)

    def reveal(self,queries, answers):
        #iterate through both at the same time
        for i,(query,answer) in enumerate(zip(queries, answers)):

            #check to see if answer is not accurate
            if not self.IsCorrect(query, answer):
                #corrupted only if the previous entry was odd
                if queries[i-1]%2==1:
                    return i

        #all correct and first element is odd
        if answers[0] is "Odd":
            return 0

        #corrupted element cannot be determined
        return -1

class Test(unittest.TestCase):
    roboFactory =Robofactory()
    def test_reveal1(self):
        self.assertEqual(self.roboFactory.reveal([3,2,2], ["Odd","Odd","Even"]),1)
    def test_reveal2(self):
        self.assertEqual(self.roboFactory.reveal([1,3,5,10], ["Odd","Odd", "Odd", "Even"]),0)
    def test_reveal3(self):
        self.assertEqual(self.roboFactory.reveal([2,3,5,10],["Even", "Odd", "Odd", "Even"]),-1)
    def test_reveal4(self):
        self.assertEqual(self.roboFactory.reveal([2,4,6,10], ["Even","Even", "Even", "Even"]),-1)
    def test_reveal5(self):
        self.assertEqual(self.roboFactory.reveal([107],["Odd"]),0)
    def test_reveal6(self):
        self.assertEqual(self.roboFactory.reveal([1,1,1],["Odd","Odd", "Even"]),2)

if __name__ == '__main__':
    unittest.main()
