# Định nghĩa hàm selectionsort nhận một mảng A là đối số đầu vào.
def selectionsort(A):
    # Lấy độ dài của mảng A.
    n = len(A)
    
    # Duyệt qua tất cả các phần tử của mảng A trừ phần tử cuối cùng.
    for i in range(n-1):
        # Gán giá trị hiện tại của i cho biến position.
        position = i
        
        # Duyệt qua các phần tử còn lại của mảng, bắt đầu từ vị trí i+1.
        for j in range(i + 1, n):
            # Nếu phần tử tại vị trí j nhỏ hơn phần tử tại vị trí position,
            if A[j] < A[position]:
                # Cập nhật giá trị của position cho vị trí j.
                position = j
                
        # Hoán đổi giữa phần tử tại vị trí i và phần tử tại vị trí position.
        temp = A[i]
        A[i] = A[position]
        A[position] = temp

# Mảng đầu vào.
A = [3, 5, 8, 9, 6, 2]

# In ra màn hình mảng ban đầu.
print('Original Array: ', A)

# Gọi hàm selectionsort để sắp xếp mảng A.
selectionsort(A)

# In ra màn hình mảng sau khi được sắp xếp.
print('Sorted Array: ', A)
