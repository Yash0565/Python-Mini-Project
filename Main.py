import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel","yash","srivastava"]
a=random.randint(0,len(word_list)-1)
chosen_word=word_list[a]
lives=6
print(chosen_word)
display=[]
for j in range(0,len(chosen_word)):
  display.append("_")
#print(display)
end_of_game=False

while not end_of_game:
  guess=input("Guess a letter: ").lower()

  for j in range(0,len(chosen_word)):
    if(guess==chosen_word[j]):
      display[j]=chosen_word[j]
  print(display)
  for i in chosen_word.lower():
    if (guess.lower()==i):
      print("It's there")
      break
  if guess not in chosen_word:
      print("Its not there")
      lives-=1
      if lives == 0:
            end_of_game = True
            print("You lose.")


  if "_" not in display:
      end_of_game = True
      print("You win.")

  print(stages[lives])
