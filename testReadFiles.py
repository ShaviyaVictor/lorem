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

      self.assertEqual(data, readFiles.counter(count))



if __name__ == '__main__' :
  unittest.main()