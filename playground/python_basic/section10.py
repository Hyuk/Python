name = ['Kim', 'Lee', 'Park']

try:
  z = 'Kim'
  x = name.index(z)
  print('{} Found it! in name index {}'.format(z, x+1))
except:
  print('Not found it! - Occurred!')
else:
  print('Ok! else!')