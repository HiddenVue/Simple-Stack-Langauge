Keywords = { 
    "LOAD", # 
    "CREATESTACK", #
    "DELETESTACK", # 
    "PUSHTOSTACK", # 
    "PULLFROMSTACK", #
    "CREATEINT", #
    "CREATESTRING", #
    "CREATECHAR", #
    "CREATEBOOL", #
    "DELETEINT", #
    "DELETESTRING", #
    "DELETECHAR", #
    "DELETEBOOL", #
    "POPFROMSTACK", #
    "CLEARSTACK", #
    "SETINT", #
    "SETSTRING", #
    "SETCHAR", #
    "SETBOOL", #
    "ADDINT", #
    "MINUSINT", #
    "MUTIPLYINT", #
    "DIVIDEINT", #
    "FLOORINT", #
    "OUTPUT", #
}

def Parse(TokenizedData):
    AST_TREE = {
        "type": "NULL",
        "modules": [],
        "stacks": [],
        "body": {
            "defined": {
                "Variables": [],
                "Functions": []
            },
            "commands": []
        }
    }
    
    if len(TokenizedData) == 0:
        return AST_TREE
    
    Index = 1

    if TokenizedData[0].type == "TT_IDENTIFIER" and TokenizedData[0].value == "#PROGRAM":
        AST_TREE["type"] = "PROGRAM"
    elif TokenizedData[0].type == "TT_IDENTIFIER" and TokenizedData[0].value == "#MODULE":
        AST_TREE["type"] = "MODULE"
    else:
        print("[!] Program type not defined at line 1")        


    while Index < len(TokenizedData):
        if TokenizedData[Index].type == "TT_IDENTIFIER":
            Exists = False

            for i in Keywords:
                if TokenizedData[Index].value == i:
                    Exists = True
                    break

            for i in AST_TREE["body"]["defined"]:
                if TokenizedData[Index].value == i:
                    Exists = True
                    break

            if not Exists:
                print(f"[!] \"{TokenizedData[Index].value}\" is not defined")
                exit()
            else:
                try:
                    arguments = []

                    for i in range(Index + 1, len(TokenizedData)):
                        if TokenizedData[i].type == "TT_IDENTIFIER":
                            break
                        else:
                            arguments.append(TokenizedData[i])

                    AST_TREE["body"]["commands"].append({
                        "type": TokenizedData[Index].value,
                        "arguments": arguments
                    })
                except:
                    print(f"[!] No arguments given to command \"{TokenizedData[Index].value}\"")
                    exit()
                    pass
                
        Index += 1 

    return AST_TREE
