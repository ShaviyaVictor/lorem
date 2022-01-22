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



def readFile(textFile) :
  '''
  Function that reads the text file and returns the data from the text file
  
  Raises:
    FileNotFoundError: If it cannot find the file
  '''

  try :
    with open(textFile, 'r') as handle :
      data = handle.read()

      return data

  except FileNotFoundError :
    return None