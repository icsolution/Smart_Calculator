class SmartCalculator:
    def __init__(self):
        self.variable = {}

    def solve(self, target) -> 'The program calculates the sum of numbers':
        try:
            if '=' not in target:
                for k, v in self.variable.items():
                    target = target.replace(k, str(v))
            result = eval(target)
            return result if result != int(result) else int(result)
        except (SyntaxError, NameError):
            if '(' in target or ')' in target or '***' in target:
                balanced = self.is_balanced(target)
                if not balanced or '***' in target:
                    return 'Invalid expression'
            if '=' in target and target.count('=') == 1:
                name, value = target.replace(' ', '').split('=', 1)
                if name.isalpha():
                    if value.isdigit():
                        self.variable[name] = value
                        return
                    elif value in self.variable:
                        self.variable[name] = self.variable[value]
                        return
                else:
                    return 'Invalid assignment'
            if target.strip().isalpha():
                return 'Unknown variable'
            return 'Invalid identifier'

    @staticmethod
    def is_balanced(target) -> 'Check if the parentheses are balanced':
        while '()' in target:
            target = target.replace('()', '')
        return not target


if __name__ == '__main__':
    calc = SmartCalculator()
    while True:
        expression = input()
        if expression.startswith('/'):
            if 'exit' in expression:
                print('Bye!')
                quit()
            elif 'help' in expression:
                print(calc.solve.__annotations__['return'])
            else:
                print('Unknown command')
        elif expression:
            if '//' in expression:
                expression = expression.replace('//', '***')
            result = calc.solve(expression)
            if result is not None:
                print(result)
