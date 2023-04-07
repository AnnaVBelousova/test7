

a1 = int (input())
n = int (input())
d = int (input())



new_lst  = [a1 + (el-1) * d for el in range(a1, n+1)]

print(new_lst)