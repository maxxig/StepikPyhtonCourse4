class Calculator:
    def __call__(self, a, b, operation):
        if isinstance(a, int|float) and isinstance(b, int|float):
            if operation == '+':
                return a + b
            elif operation == '-':
                return a - b
            elif operation == '*':
                return a * b
            elif operation == '/':
                if b == 0 :
                    raise ValueError('Деление на ноль невозможно')
                else:
                    return a / b
        else:
            pass


# TEST_4:
calculator = Calculator()

print(calculator(10, 0, '+'))
print(calculator(10, 0, '-'))
print(calculator(10, 0, '*'))