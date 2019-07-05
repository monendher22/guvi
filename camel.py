def snake_to_camel(word):
  import re
  return ' '.join(x.capitalize() or ' ' for x in word.split(' '))
print(snake_to_camel(input()))
