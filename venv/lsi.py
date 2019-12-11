#!/usr/bin/env python3

from Lexer import Lexer
from Parser import Parser
import sys

file_name = sys.argv[1]

with open(file_name, 'r') as source_file:
    data = source_file.read()
    
    lexer = Lexer(data)
    tokens = lexer.tokenize()

    parser = Parser()
    parser.run_parser(tokens)
