# -*- coding: utf-8 -*-
# ↑ This is for recognising Japanese letters in .py file.
"""
Puzzle 20
id 365

a: "A", args: "B", "C" (2 arguments in args)
"""
import time

def func(a, *args):
    print(a) # "A". Executed only once
    for arg in args: # Loop 2 times
        print(arg) # 1st: "B", 2nd "C"

func("A", "B", "C")
time.sleep(3)
print("Me (*´∀`*)oo0(So if the order change, it will be more concretely understandable)")
time.sleep(3)
def func(a, *args):
    print("(*^o^)oo0( " + a + " )")
    for arg in args:
        print("(*^o^)oo0( " + arg + " )")

func("B", "C", "A")
