print('Can you ride the rollercoaster?')
age = int(input('What is your age?: '))

if age > 18:
  print('Definitely!')
elif age > 12:
  height = int(input('What is your height in inches?: '))
  if height >= 48:
    print('Okay, you can ride it')
  else:
    print('Sorry kid, come back after you grow.')
else:
  print('Sorry, kid. Come back in a couple of years')

  # can nest conditionals