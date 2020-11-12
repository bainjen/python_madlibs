numbers = [3, 5, 3, 6, 5]

total = 0

for num in numbers:
  total = total + num
  print(num)
  print(total)
  
mean = total / len(numbers)
print(mean)

directions = ['turn left',
              'go straight for 2 blocks',
              'turn right',
              'keep going until you see the dog statue',
              'turn right',
              'turn right again',
              'park right on the sidewalk']

directions_but_screemed = []
for next_step in directions:
  upper_case_step = next_step.upper()
  directions_but_screemed.append(upper_case_step)

# Question: what do you think would happen if you declared 
# `directions_but_screemed = []` inside the loop instead of before?

# Iterating over a range (i.e. doing something a certain number of times)
number_of_bacteria = 1    # Let's make it double each time for 10 generations
for generation in range(0, 10):
  number_of_bacteria = number_of_bacteria * 2
  print('After generation ' + str(generation) + ': ' + str(number_of_bacteria))