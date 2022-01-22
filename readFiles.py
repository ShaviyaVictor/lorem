# with open('test.txt', 'r') as handle:
#   data = handle.read()

#   print(data)


textFile = 'test.txt'

def readFile(textFile) :
  '''
  Function that reads a text file and returns the data from the text file
  '''

  with open(textFile, 'r') as handle :
    data = handle.read()

    return data