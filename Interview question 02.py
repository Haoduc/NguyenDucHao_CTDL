def is_palindrome(arr):
  left = 0
  right = len(arr) - 1
  
  while left < right:
    if arr[left] != arr[right]:
      return False
    
    left += 1
    right -= 1

  return True

arr = [0, 6, 3, 4, 5]

if is_palindrome(arr):
  print("Mảng là palindrome")
else:
  print("Mảng không phải palindrome")