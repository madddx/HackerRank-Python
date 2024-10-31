a = input()
b = input().split()
print(any(i[::-1] == i for i in b) and all(int(i)>=0 for i in b))
