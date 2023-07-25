#!/usr/bin/env python3

def print_fibonacci(length):
    
    fibonacci_seq = []
    if length > 0:
        
        fibonacci_seq = [0, 1]
    
        while len(fibonacci_seq) < length:
            next_term = fibonacci_seq[-1] + fibonacci_seq[-2]
            fibonacci_seq.append(next_term)
        
        return print(fibonacci_seq)
    else:
        return print(fibonacci_seq)
        
        

print_fibonacci(15)