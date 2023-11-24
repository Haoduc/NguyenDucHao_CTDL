# Hàm linnearsearch thực hiện tìm kiếm tuyến tính trong một danh sách A để tìm kiếm phần tử key.
def linnearsearch(A, key):
    index = 0  # Khởi tạo biến index là 0
    while index < len(A):  # Lặp qua danh sách A cho đến khi index vượt quá độ dài của danh sách.
        if A[index] == key:  # Kiểm tra nếu phần tử tại vị trí index bằng với key.
            return index  
        index = index + 1  # Tăng giá trị của index lên 1 để kiểm tra phần tử tiếp theo trong danh sách.
    return -1  

A = [84, 21, 47, 96, 15]  
found = linnearsearch(A, 47)  
print("Kết quả: ", found)  
