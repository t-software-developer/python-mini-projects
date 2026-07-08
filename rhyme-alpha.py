import pronouncing

def rhyme(string):
  return pronouncing.rhymes(string)
  
word = str(input('Type a word: '))
print(rhyme(word))
  