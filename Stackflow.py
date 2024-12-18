import os
import sys

import Lexer
import Tokens
import Parser
import Interpreter
import json

argv = sys.argv

if len(argv) != 2:
    print("[i] Usage: Stackflow <filepath>")
    sys.exit(1)
elif len(argv) == 2:
    FilePath = argv[1]

    if not os.path.exists(FilePath):
        print("[!] File does not exist")
        sys.exit(1)

    if not FilePath.endswith(".sf"):
        print("[!] File is not a Stackflow file")
        sys.exit(1)
    
    with open(FilePath, "r") as File:
        Data = File.read()
        
    TokenizedData = Lexer.Tokenize(Data)
    AST_TREE = Parser.Parse(TokenizedData)
    AST_TREE = Interpreter.Interpret(AST_TREE)
    
    print(AST_TREE)

