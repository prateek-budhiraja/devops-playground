import sys

def add(num1, num2):
    return num1+num2

num1 = 0
num2 = 0

print(sys.argv)
print(len(sys.argv))

if(len(sys.argv) > 1):
    num1 = int(sys.argv[1]);
    num2 = int(sys.argv[2]);

print(add(num1, num2))