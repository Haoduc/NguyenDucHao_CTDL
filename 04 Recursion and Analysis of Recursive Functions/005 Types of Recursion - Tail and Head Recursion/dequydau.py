def calculate(n):
    if n > 0:
        calculate(n -1)
        k = n ** 2
        print(k)
        
    #if
calculate(4)
#def
# gọi de quy lap di lap lai roi minh tinh toan gia tri nguoc lại
#in ra la luot 1 4 9 16 
