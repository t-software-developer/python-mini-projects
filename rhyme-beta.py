import pronouncing

def rhyme(string):
    return pronouncing.rhymes(string)
  
word = input('Type a word: ')

# Get the list of rhymes
rhymes_list = rhyme(word)

# Iterate through the rhymes list and print each one line by line
for r in rhymes_list:
    print(r)
