from pyclbr import Class

import ply.lex as lex

class Lexer:

    tokens = (
        'LAMBDA',
        'INITIALIZE',
        'LISTEN',
        'RECEIVE',
        'SEND',
        'CONNECT',
        'DISCONNECT',
        'IP',
        'PORT',
        'DATA',
    )

    # Regular expression rules for simple tokens
    t_LAMBDA = r'.\\'
    t_INITIALIZE = 'Init'
    t_LISTEN = 'Listen'
    t_RECEIVE = 'Receive'
    t_SEND = 'Send'
    t_CONNECT = 'Connect'
    t_DISCONNECT = 'Disconnect'



    # A regular expression rule with some action code
    def t_IP(t):
        r'(?:[0-9]{1,3}\.){3}[0-9]{1,3}'
        t.value = (t.value)
        return t

# A regular expression rule with some action code
    def t_PORT(t):
        r'([012345]?[0-9]?[0-9]?[0-9]?[0-9]|6[0-4][0-9][0-9][0-9]|65[0-5][0-3][0-5])'
        t.value = int(t.value)
        return t

    # A regular expression rule with some action code
    def t_DATA(t):
        r'".*"'
        t.value = (t.value)
        return t

    # Define a rule so we can track line numbers
    def t_newline(t):
        r'\n+'
        t.lexer.lineno += len(t.value)


    # A string containing ignored characters (spaces and tabs)
    t_ignore = ' \t'


    # Error handling rule
    def t_error(t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)


    # Build the lexer
    lexer = lex.lex()

    def __init__(self, data):
        self.data = data

    def tokenize(self):     #Returns a space delimited string of tokens
        output = ""
        self.lexer.input(self.data)
        while True:
            tok = self.lexer.token()
            if not tok:
                break  # No more input
            output = output + str(tok.value) +" "
        return output
         #print(tok.value) #--Used to test



#Test the Class
test = Lexer(data = '''
        .\ Connect 127.0.0.1 2468
        .\ Send "Hola, Wenas"
        .\ Receive
        .\ Disconnect
        ''')

print(test.tokenize())