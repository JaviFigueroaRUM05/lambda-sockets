import ply.yacc as yacc
from Lexer import Lexer



class Parser:

    #Parsing Rules
    tokens = Lexer.tokens
    newLine = r'\n+'
    ignore = ' \t'


    def p_start(p):
        '''start : client
        | server'''
    def p_client(p):
        '''client : connect expression disconnect'''
    def p_server(p):
        '''server : init listen expression'''
    def p_expression(p):
        '''expression : disconnect expression
        | connect expression
        | listen expression
        | init expression
        | send expression
        | receive expression
        | epsilon
        '''
    def p_connect(p):
        '''connect : LAMBDA CONNECT IP PORT'''
    def p_disconnect(p):
        '''disconnect : LAMBDA DISCONNECT'''
    def p_listen(p):
        '''listen : LAMBDA LISTEN'''
    def p_init(p):
        '''init : LAMBDA INITIALIZE'''
    def p_send(p):
        '''send : LAMBDA SEND DATA'''
    def p_receive(p):
        '''receive : LAMBDA RECEIVE'''
    def p_empty(p):
        ''' epsilon : '''

    def p_error(p):
        if not p:
            print("EOF, Parsed Successfully.")
            return
        print("Error encountered: " + p.__str__())

    parser = yacc.yacc()

    test = Lexer(data='''
            .\ Connect 127.0.0.1 2468
            .\ Send "Hola Wenas"
            .\ Receive
            .\ Disconnect
            ''')
    data = test.tokenize()
    print(data)
    parser.parse(data)




