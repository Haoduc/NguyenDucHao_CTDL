def dai_thua(n):
    if n == 0:
        return 1
    else:
        return n*dai_thua(n-1)

a=int(input("Nhập vào 1 số tự nhiên: "))
ket_qua=dai_thua(a)
print(f"Kết quả tính được là: {a}! = {ket_qua}")