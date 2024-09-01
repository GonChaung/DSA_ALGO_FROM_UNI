# name - Thant Si Thu Naing
# section - 541
# id - 6611720

def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


Stack = []
postfix_expr = input().split()
for token in postfix_expr:
    if is_number(token):
        # Fill in code here for token being a number
        Stack.append(float(token))
    else:
        # Fill in code here for token not being a number
        if len(Stack) != 1:
            second = Stack.pop()
            first = Stack.pop()
            result = 0
            match token:
                case "+":
                    result = first + second
                case "*":
                    result = first * second
                case "/":
                    result = first / second
                case "-":
                    result = first - second
                case "%":
                    result = first % second
                case "^":
                    result = first ** second
            Stack.append(result)

print('%.1f' % Stack[0])


        
