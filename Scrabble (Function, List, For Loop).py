# In this project, I will process some data from a group
# of friends playing scrabble. I will use dictionaries to organize players, words, and points.

# Putting into practice Function, List - List Comprehension, Dictionary and loop into practice

# I am currently lazy while doing this and will skip commenting, but in future when I am bored and have nothing to do I will put some comment here explaining the code.

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {key:value for key, value in zip(letters, points)}
letter_to_points[" "] = 0

def score_word(word):
  point_total = 0
  word = word.upper()

  for char in word:
    if char not in letter_to_points:
      continue
    point_total += letter_to_points[char]
  return point_total

brownie_points = score_word("BROWNIE")

player_to_words = {
  "player1": ['blue', 'tennies', 'exit'],
  "wordNerd": ['earth', 'eyes', 'machine'],
  "Lexi Con": ['eraser', 'belly', 'husky'],
  "Prof Reader": ['zap', 'coma', 'period']
  }

player_to_points = {}

for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = player_points

print(player_to_points)