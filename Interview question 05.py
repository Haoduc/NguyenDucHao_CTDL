def find_duplicates(arr):
  flags = [False] * (max(arr) + 1)  # Tạo một danh sách kiểm tra với độ dài phù hợp
  result = []

  for x in arr:
    if flags[x]:
      result.append(x)
    else:
      flags[x] = True
  
  return result

arr = [0, 3, 6, 4, 1, 4, 0, 9, 5]

print(find_duplicates(arr))
