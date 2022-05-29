# python function to calculate the sum of upper & lower letters in string.
def up_low(string):
  uppers = 0
  lowers = 0
  for char in string:
    if char.islower():
      lowers += 1
    elif char.isupper():
      uppers +=1
    else: 
      pass
  return(uppers, lowers)

print(up_low('The quick Brow Fox'))