import re

token_patterns = [
    (r'[0-9]+(\.[0-9]+)?', 'NUMBER'),
    (r'[a-zA-Z_][a-zA-Z0-9_]*', 'ID'),
    (r'\+', 'PLUS'),
    (r'\-', 'MINUS'),
    (r'\*', 'MULTIPLY'),
    (r'/', 'DIVIDE'),  # Removed backslash to match '/'
    (r'\%', 'REMAIN'),
    (r'\(', 'LPAREN'),
    (r'\)', 'RPAREN'),
    (r'\=', 'ASSIGN'),  # Match '=' separately
    (r'\s+', 'WS')
]


def tokenize(text):
    tokens = []
    pos = 0

    while pos < len(text):
        match = None
        for pattern, token_type in token_patterns:
            regex = re.compile(pattern)
            match = regex.match(text, pos)
            if match:
                value = match.group(0)
                if token_type != 'WS':
                    tokens.append((value, token_type))
                break
        if not match:
            raise SyntaxError(f"Invalid token: {text[pos]}")
        else:
            pos = match.end()

    return tokens
