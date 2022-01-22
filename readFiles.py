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



def counter(textFile) :
  '''
  Function that makes a count of how many times a single word has been used in our file
  '''

  with open(textFile, 'r') as handle :
    data = handle.read()

    count = 0

    for word in data.split() :
      if word == 'lorem' :
        count += 1

    return count



def lineCounter(textFile) :
  '''
  Function that will read the lines present in our text file
  '''

  with open(textFile, 'r') as handle :
    data = handle.readlines()

    return data






# def wordLength(textFile) :
#   '''
#   testing whether we can actually see the longest word with my function
#   '''

#   with open(textFile, 'r') as handle :
#     data = handle.read()

#     single = data.split()

#     length = len(single)

#     print(single, length)

# wordLength(textFile)




