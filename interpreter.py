from AST import Interpreter
from AST import parse
import tokenizater


def run(code):
    tokens = tokenizater.tokenize(code)

    interpreter = Interpreter()
    node = parse(tokens)

    return interpreter.evaluate(node), interpreter.symbol_table
