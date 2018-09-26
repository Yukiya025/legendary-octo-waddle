# -*- coding: utf-8 -*-
# ↑ This is for recognising Japanese letters in .py file.
"""
Puzzle 21
id 76
"""
def ping(i):
    if i > 0:
        return pong(i - 1)
    return "0"

def pong(i):
    if i > 0:
        return ping(i - 1)
    return "1"

print(ping(29)) # 1
print(ping(10)) # 0
print(pong(29)) # 0
print(pong(10)) # 1
print("Me (*´∀`*)oo0(So the answer will be different by given numbers are odd or not and by which function is designated in print())")
