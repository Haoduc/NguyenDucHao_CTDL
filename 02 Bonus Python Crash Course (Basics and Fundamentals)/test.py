# Định nghĩa hàm radixsort nhận một mảng A là đối số đầu vào.
def radixsort(A):
    n = len(A)
    
    # Nếu mảng rỗng, không cần làm gì cả.
    if n == 0:
        return

    # Tìm giá trị lớn nhất trong mảng để xác định số lượng chữ số.
    maxelement = max(A)
    digits = len(str(maxelement))

    # Bắt đầu quá trình sắp xếp theo chữ số từ hàng đơn vị đến hàng tỷ (hoặc hàng chục nếu chữ số lớn nhất thấp hơn hàng chục).
    for i in range(digits):
        # Tạo 10 hộp (bins) cho mỗi chữ số từ 0 đến 9.
        bins = [[] for _ in range(10)]

        # Đặt từng phần tử của mảng vào hộp tương ứng dựa trên chữ số ở vị trí i.
        for j in range(n):
            e = int((A[j] / 10**i) % 10)  # Lấy chữ số thứ i của phần tử A[j].
            bins[e].append(A[j])

        # Gom lại các phần tử từ các hộp vào mảng A theo thứ tự, bắt đầu từ hộp 0 đến hộp 9.
        k = 0
        for x in range(10):
            if len(bins[x]) > 0:
                for y in range(len(bins[x])):
                    A[k] = bins[x][y]
                    k += 1

# Mảng đầu vào.
A = [63, 250, 835, 947, 651, 28]

# In ra màn hình mảng ban đầu.
print('Original Array:', A)

# Gọi hàm radixsort để sắp xếp mảng A.
radixsort(A)

# In ra màn hình mảng sau khi được sắp xếp.
print('Sorted Array:', A)
