#!/usr/bin/env python3

import sys

print("Hello, World - from my_tool.py")

print("my_tool.py - " +__name__) # __main__

def sum(a, b):
    return a + b

def main():
    result = sum(int(sys.argv[1]), int(sys.argv[2]))
    print(result)

if __name__ == "__main__":
    main()