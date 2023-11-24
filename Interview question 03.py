def reverse_integer(n):
  reversed = 0 
  
  while n > 0:
    remainder = n % 10
    reversed = reversed * 10 + remainder
    n = n // 10

  return reversed


number = 105887853

reversed_number = reverse_integer(number)

print("Số ban đầu là:", number)
print("Số sau khi đảo ngược là:", reversed_number)