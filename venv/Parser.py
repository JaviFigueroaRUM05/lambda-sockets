import ply.yacc as yacc
from Lexer import Lexer
from int_code import Lambda_Sockets

class Parser:

    def __init__(self):
        self.isClient = 0 
        self.ls = Lambda_Sockets()

    def run_parser(self, data):
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
            self.isClient = 1
            host = p[3]
            port = p[4]
            self.ls.connect(host, int(port))

        def p_disconnect(p):
            '''disconnect : LAMBDA DISCONNECT'''
            self.ls.disconnect()

        def p_listen(p):
            '''listen : LAMBDA LISTEN'''
            self.ls.listen()

        def p_init(p):
            '''init : LAMBDA INITIALIZE'''
            self.isClient = 0
            self.ls.init()

        def p_send(p):
            '''send : LAMBDA SEND DATA'''
            if self.isClient == 0:
                self.ls.server_send(p[3])
            else:
                self.ls.client_send(p[3])

        def p_receive(p):
            '''receive : LAMBDA RECEIVE'''
            if self.isClient == 0:
                self.ls.server_receive()
            else:
                self.ls.client_receive()

        def p_empty(p):
            ''' epsilon : '''

        def p_error(p):
            if p:
                print("Error encountered: " + p.__str__())

        tokens = Lexer.tokens
        parser = yacc.yacc()
        test = Lexer(data)
        data = test.tokenize()
        parser.parse(data)




