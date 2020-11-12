game_text = 'Just as I arrived at PLACE, I realized I had forgotten my OBJECT.'

# goal is to strip down to words only and split them into a list
stripped_text = game_text.replace('.', '')
stripped_text = stripped_text.replace(',', '')
words = stripped_text.split(' ')
print(words)

categories = []
for word in words:
  if word.isupper() and word != 'I' and word != 'A':
    categories.append(word)

picked_words = []
for category in categories:
  picked = input('Tell me a ' + category.lower() + ': ')
  picked_words.append(picked)

for i in range(len(categories)):
  category = categories[i]
  picked = picked_words[i]
  game_text = game_text.replace(category, picked)

print(game_text)

# user input has to be put into a string using quotes or there is an error: NameError name 'user input' is not defined
# problem when run in python 2