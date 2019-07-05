def reverseWordSentence(Sentence):
  words = Sentence.split('')
  newwords = [word[::-1] for word in words]
  newSentence = ''.join(newwords)
  return newSentence
print(reverseWordSentence(input()))
