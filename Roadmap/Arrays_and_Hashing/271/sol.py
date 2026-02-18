class Solution:

  def encode(self, strs):
    """ Encodes a list of strings and returns an encoded string.
    """
    res = ""
    for s in strs:
      # Encode with the length of the string followed by another delimiter.
      res += str(len(s)) + "#" + s
    return res
  
  def decode(self, s):
    """ Decodes a single string to a list of strings.
    """
    lst = []
    i = 0

    while i < len(s):
      # We want to find the delimiter.
      j = i
      while s[j] != "#":
        j+=1
      
      # Extract the string length at the start of each string.
      stringLength = int(s[i:j])
      # Extract entire string and append it.
      lst.append(s[j+1: j+1+stringLength])

      # Update i
      i = j+1+stringLength
    return lst
  