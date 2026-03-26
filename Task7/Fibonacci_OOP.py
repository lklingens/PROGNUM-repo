#!/usr/bin/env python
# coding: utf-8

# In[ ]:


N = int(input("Enter your number for N:"))
M = int(input("Enter your number for M:"))

class Fibonacci:
    """Class for calculating Fibonacci sequence."""
    previous = 0  # Starting number; previous term
    new = 1  # Second number; new term
    numbers = []  # List with numbers
    
    def __init__(self, N, M):
        self.N = N
        self.M = M
    def reset(self):
        """Function thay resent the class variables to their starting values."""
        self.previous = 0
        self.new = 1
        self.numbers = []
    def fibo_term(self):
        self.reset()  # To reset the function every time it is called.
        
        for k in range(self.N):
            following = self.previous + self.new 
            self.previous = self.new
            self.new = following
        return self.new
    def fibo_mod(self):
        self.reset()  # To reset the function every time it is called.
        
        for k in range(self.N):  # Ensures the code only runs until the Nth term.
            if self.previous % self.M == 0:
                self.numbers.append(self.previous)
            following = self.previous + self.new  # Calculates the next Fibonacci number
            self.previous = self.new
            self.new = following
        return self.numbers
    
trial = Fibonacci(N, M)
print(f"The {N}th Fibonacci term is: {trial.fibo_term()}")
print(f"The Fibonacci terms less than the {N}th term that can be divided by {M} are:\n{trial.fibo_mod()}")

