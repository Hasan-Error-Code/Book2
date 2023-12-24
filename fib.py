def find_fib(n):
    if n <= 2:
        return 1
    fib, fib_next, = 1, 1

    i = 3
    while i <= n:
        i += 1
        fib, fib_next = fib_next, fib
        
        return fib_next
    
for x in range(1, 11):
    print(find_fib(x))