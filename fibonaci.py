def fibonaci(n: int) -> int:
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return(fibonaci(n-1) + fibonaci(n-2))

print(fibonaci(20))

