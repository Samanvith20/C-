def factioral(n):
    if n == 0:
        return 1
    else:
        return n * factioral(n-1)
    
print(factioral(5)) 