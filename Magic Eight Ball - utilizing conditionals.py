# Practicing Conditionals
# We will create a Magich 8-Ball program, that has 9 possible answer; We're going to put in practice what we've learned from control flow/conditionals

# I'd like to use the input() from the last lecture, but it seems this is not currently not supported by the terminal here; I'll change update this code in future.

# We're importing random that we will use in our conditional statement later.
import random

# Initializing name and question variable, these variables will be used in a print statement where we will print out the name of the user and user's question.

# Note: question variable must be a type of question that can be answered with either "yes" or "no".

name = 'Garry'
question = 'Is python for me?'

# Initializing answer variable that will contain magic 8-ball answer later, we will make it an empty string for now and will update it later using conditional statement.

answer = ''

# And now we will use the random module we've import, to generate random number, and this random number will help us to generate random answer.
random_number = random.randint(1, 9)

# We will craete an if statement that will handle scenario if user didn't input a name we will give it a default value.

# and if we're give a value that is not a string we will tell the user to input a string value 

if name == '' and question == '':
  if type(name) != str:
    print('Invalid input, please provide a string input')
  else:
    print('Name and Question cannot be empty')
else:
  if random_number == 1:
    answer = 'Yes - definitely.'
  elif random_number == 2:
    answer = 'It is decidedly so.'
  elif random_number == 3:
    answer = 'Without a doubt.'
  elif random_number == 4:
    answer = 'Reply hazy, try again.'
  elif random_number == 5:
    answer = 'Ask again later.'
  elif random_number == 6:
    answer = 'Better not tell you now.'
  elif random_number == 7:
    answer = 'My sources say no.'
  elif random_number == 8:
    answer = 'Outlook not so good.'
  elif random_number == 9:
    answer = 'Very doubtful'
  else:
    answer = 'Conditional Statement has an error!'

# This is a conditional that will handle the scenario where if question and name is empty the program will not proceed and print out the final result.
if answer:
  print(name + ' asks: ' + question)
  print('Magic 8-Ball says: ' + answer)