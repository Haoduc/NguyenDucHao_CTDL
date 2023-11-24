def is_anagram(s1, s2):
  s1 = s1.lower().replace(" ", "")
  s2 = s2.lower().replace(" ", "")

  if len(s1) != len(s2):
    return False

  s1 = sorted(s1)
  s2 = sorted(s2)

  if s1 == s2: 
      return True
  
  return False


ban1 = "restful"
ban2 = "fluster" 

if is_anagram(ban1, ban2):
  print(ban1, "và", ban2, "là anagram.")
else:
  print(ban1, "và", ban2, "không phải là anagram.")