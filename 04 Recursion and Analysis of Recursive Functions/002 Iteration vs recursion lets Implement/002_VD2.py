# ham de qui xet dieu kien va goi lai ham de xu li
def deQui (n):
    if (n > 0): # if Nếu điều kiện này đúng (nghĩa là n còn lớn hơn 0)
        k = n ** 2
        print(k)
        deQui(n - 1) # vi while chi xet dieu kien dau ma de qui goi di goi lai ne gia tri n ko doi va dan den vong lap vo han
deQui(4)
# vi sao khong dung while thay cho if nhu VD1?