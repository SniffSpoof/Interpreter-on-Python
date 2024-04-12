class NumberNode:
    def __init__(self, value):
        self.value = value


class BinOpNode:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right


class VariableNode:
    def __init__(self, name):
        self.name = name


class AssignNode:
    def __init__(self, variable_name, value_node):
        self.variable_name = variable_name
        self.value_node = value_node


class Interpreter:
    def __init__(self):
        self.symbol_table = {}  # Initialize symbol table

    def assign_variable(self, name, value):
        self.symbol_table[name] = value  # Assign value to variable in symbol table

    def evaluate(self, node):
        # Evaluate the AST node
        if isinstance(node, NumberNode):
            return node.value
        elif isinstance(node, VariableNode):
            return self.symbol_table.get(node.name, 0)  # Get value from symbol table
        elif isinstance(node, BinOpNode):
            left = self.evaluate(node.left)
            right = self.evaluate(node.right)
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
        elif isinstance(node, AssignNode):  # Handle assignment node
            value = self.evaluate(node.value_node)  # Evaluate the expression
            self.assign_variable(node.variable_name, value)  # Assign value to variable


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
        elif token[1] == 'ID':  # Handle variable token
            pos += 1
            if pos < len(tokens) and tokens[pos][1] == 'ASSIGN':  # Check for assignment
                pos += 1  # Consume '=' token
                value_node = parse_expression()  # Parse the expression on the right side of '='
                return AssignNode(token[0], value_node)  # Create an AssignNode
            else:
                return VariableNode(token[0])
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

