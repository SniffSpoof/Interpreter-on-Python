class NumberNode:
    def __init__(self, value):
        self.value = value

class BinOpNode:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

def parse(tokens):
    pos = 0

    def parse_expression():
        nonlocal pos
        node = parse_term()
        while pos < len(tokens) and tokens[pos][1] in ['PLUS', 'MINUS']:
            op = tokens[pos][1]
            pos += 1
            node = BinOpNode(node, op, parse_term())
        return node

    def parse_term():
        nonlocal pos
        node = parse_factor()
        while pos < len(tokens) and tokens[pos][1] in ['MULTIPLY', 'DIVIDE', 'REMAIN']:
            op = tokens[pos][1]
            pos += 1
            node = BinOpNode(node, op, parse_factor())
        return node

    def parse_factor():
        nonlocal pos
        token = tokens[pos]
        if token[1] == 'NUMBER':
            pos += 1
            return NumberNode(float(token[0]))
        elif token[1] == 'LPAREN':
            pos += 1
            node = parse_expression()
            if tokens[pos][1] != 'RPAREN':
                raise SyntaxError("Expected ')'")
            pos += 1
            return node
        else:
            raise SyntaxError("Invalid syntax")

    return parse_expression()


def evaluate(node):
    if isinstance(node, NumberNode):
        return node.value
    elif isinstance(node, BinOpNode):
        left = evaluate(node.left)
        right = evaluate(node.right)
        if node.op == 'PLUS':
            return left + right
        elif node.op == 'MINUS':
            return left - right
        elif node.op == 'MULTIPLY':
            return left * right
        elif node.op == 'DIVIDE':
            return left / right
        elif node.op == 'REMAIN':
            return left % right


