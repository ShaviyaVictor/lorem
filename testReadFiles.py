import unittest
import readFiles

class testTeadFiles(unittest.TestCase) :
  """
  Class to test the functions on the readfiles module
  
  Args:
    unittest.TestCase: Class from the unittest module to create unit tests
  """


  def testGetData(self) :
    """
    1st Test case to confirm that we are getting data from the file 
    """

    with open('test.txt', 'r') as handle :
      data = handle.read()

      self.assertEqual(data, readFiles.readFile('test.txt'))



  def testNonFile(self) :
    '''
    2nd TestCase to confirm that an exeption is raised when a wrong file is inputted

    And we therefore input a wrong file name at the assertEqual function expecting to get a None response
    '''

    self.assertEqual(None, readFiles.readFile('testing.txt'))




  def testCounter(self) :
    '''
    3rd TestCase to confrim that we can count how many times a single word is being used
    '''

    with open('test.txt', 'r') as handle :
      data = handle.read()

      count = 0

      for word in data.split() :
        if word == 'lorem' :
          count += 1

      self.assertEqual(count, readFiles.counter('test.txt'))



  def testLineCounter(self) :
    '''
    4th TestCase to confirm that whether we can see how many lines we have in our text file
    '''

    with open('test.txt', 'r') as handle :
      data = handle.readlines()

      self.assertEqual(data, readFiles.lineCounter('test.txt'))



  def testWordLength(self) :
    '''
    5th TestCase to confirm whether we can actually see the longest word in the text file
    '''






if __name__ == '__main__' :
  unittest.main()