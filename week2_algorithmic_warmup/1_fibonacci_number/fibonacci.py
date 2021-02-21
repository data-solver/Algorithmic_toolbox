# Uses python3
def calc_fib(n):
    f1 = 0
    f2 = 1
    if n == 0:
        return f1
    if n == 1:
        return f2
    i = 1
    fn = f1 + f2
    while i < n:
        fn = f1 + f2
        fn_old = fn
        print(f"f1 ={f1}\n f2={f2}\n fn={fn}")
        f2_old = f2
        f2 = fn_old
        f1 = f2_old
        i += 1
    return fn
        
        
    
n = int(input())
print(calc_fib(n))