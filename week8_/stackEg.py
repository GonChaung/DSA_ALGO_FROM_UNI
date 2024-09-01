def isEmpty(s):
    return len(s) == 0

def stackPush(s,x):
    return s.append(x)

def stackPop(s):
    return s.pop()

def stackPeek(s):
    return s[len(s)-1]

myStack = []

print(myStack)

for i in range(3):
    print(myStack.pop())

while not(len(myStack) == 0):
    print(myStack.pop())
print(myStack)