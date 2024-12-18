import Tokens

def Tokenize(Data):
    TokenizedData = []

    SpiltData = Data.split("\n") 

    for LineIndex,Line in enumerate(SpiltData):
        if LineIndex == 0:
            TokenizedData.append(Tokens.Token("TT_IDENTIFIER", Line))
            continue

        if Line == "" or Line == " " or Line == "\t" or Line == "\n":
            continue

        if Line[0] == ":":
            continue

        for WordIndex,Word in enumerate(Line.split(" ")):
            if Word == "" or Word == " " or Word == "\t" or Word == "\n":
                continue
    
            if Word == "FALSE" or Word == "TRUE":
                TokenizedData.append(Tokens.Token("TT_BOOL", Word))
                continue

            if Word.isnumeric():
                TokenizedData.append(Tokens.Token("TT_INT", Word))
                continue

            if Word[0] == "\"" and Word[-1] == "\"":
                TokenizedData.append(Tokens.Token("TT_STRING", Word[1:-1]))
                continue

            if Word[0] == "'" and Word[-1] == "'":
                TokenizedData.append(Tokens.Token("TT_CHAR", Word[1:-1]))
                continue

            if Word[0].isalpha():
                TokenizedData.append(Tokens.Token("TT_IDENTIFIER", Word))
                continue
            if Word[0] == "&":
                TokenizedData.append(Tokens.Token("TT_VARIABLE", Word))
                continue
            
            print(f"[!] Unknown token [LINE: {LineIndex+1}, WORD: {WordIndex+1}]: " + Word)
            exit()
            
    return TokenizedData

