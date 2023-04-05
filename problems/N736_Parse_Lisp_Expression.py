class Solution:
    def evaluate(self, expression: str) -> int:
        def get_val(s: str) -> str:
            return memo.get(s, s)

        def parse():
            if tokens[0] == LET:  # Case let.
                for i in range(1, len(tokens) - 1, 2):
                    # tokens[i + 1] could be empty if a new left parentheses
                    # is found.
                    memo[tokens[i]] = get_val(tokens[i + 1] or tokens[i])

                return get_val(tokens[-1])
            else:
                x, y = map(int, map(get_val, tokens[1:]))
                if tokens[0] == ADD: 
                    return str(x + y)
                else:
                    return str(x * y)

        stack, memo, tokens = [], {}, ['']
        ADD, LET = 'add', 'let'
        for c in expression:
            if c == '(':
                if tokens[0] == LET:
                    parse()

                stack.append((tokens, dict(memo)))
                tokens = ['']
            elif c == ' ':
                tokens.append('')  # Add a new token.
            elif c == ')':
                val = parse()
                tokens, memo = stack.pop()
                tokens[-1] += val
            else:
                tokens[-1] += c

        return int(tokens[0])
