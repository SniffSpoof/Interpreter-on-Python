import tokenizater
import AST


if __name__ == "__main__":
	text = '7 % 2'
	tokens = tokenizater.tokenize(text)
	ast = AST.parse(tokens)
	result = AST.evaluate(ast)
	print(result)
