import Lexer
import Parser
import math

def Interpret(AST_TREE):

    for Command in AST_TREE["body"]["commands"]: # May god have mercy on your soul when trying to find anything in this junk of a interpreter
        for i in Command["arguments"]:
            if i.type == "TT_VARIABLE":
                for j in AST_TREE["body"]["defined"]["Variables"]:
                    if j["name"] == i.value.strip("&"):
                        i.value = j["value"]
                        break

        if Command["type"] == "LOAD":
            if len(Command["arguments"]) == 0:
                print("[!] Not enough arguments for LOAD")
                exit()

            ModuleName = Command["arguments"][0].value 

            if not ModuleName.endswith(".sf"):
                print("[!] Module is not a Stackflow file")
                exit()

            try:
                with open(ModuleName, "r") as File:
                    Data = File.read()
            except:
                print("[!] Module does not exist")
                exit()

            TokenizedData = Lexer.Tokenize(Data)
            ModuleAST_TREE = Parser.Parse(TokenizedData)

            AST_TREE["modules"].append(ModuleAST_TREE)

            continue

        if Command["type"] == "CREATESTACK":
            AST_TREE["stacks"].append({"name": Command["arguments"][0].value, "values": []})   
            continue 

        if Command["type"] == "DELETESTACK":
            AST_TREE["stacks"].remove({"name": Command["arguments"][0].value, "values": []})
            continue

        if Command["type"] == "PUSHTOSTACK":
            if len(Command["arguments"]) <= 1:
                print("[!] Not enough arguments for PUSHTOSTACK")
                exit()

            for i in AST_TREE["stacks"]:
                if i["name"] == Command["arguments"][0].value:
                    i["values"].append(Command["arguments"][1].value)
                    break

            continue

        if Command["type"] == "POPFROMSTACK":
            for i in AST_TREE["stacks"]:
                if i["name"] == Command["arguments"][0].value:
                    if len(i["values"]) == 0:
                        print("[!] Stack is empty")
                        exit()
                    i["values"].pop()
                    break
            continue

        if Command["type"] == "CLEARSTACK":
            for i in AST_TREE["stacks"]:
                if i["name"] == Command["arguments"][0].value:
                    i["values"] = []
                    break

        if Command["type"] == "CREATEINT":
            if len(Command["arguments"]) <= 1:
                print("[!] Not enough arguments for CREATEINT")
                exit()

            AST_TREE["body"]["defined"]["Variables"].append({"name": Command["arguments"][0].value, "type": "INT", "value": Command["arguments"][1].value})
            continue

        if Command["type"] == "CREATESTRING":
            if len(Command["arguments"]) <= 1:
                print("[!] Not enough arguments for CREATESTRING")
                exit()

            AST_TREE["body"]["defined"]["Variables"].append({"name": Command["arguments"][0].value, "type": "STRING", "value": Command["arguments"][1].value})
            continue

        if Command["type"] == "CREATECHAR":
            if len(Command["arguments"]) <= 1:
                print("[!] Not enough arguments for CREATECHAR")
                exit()

            if len(Command["arguments"][1].value) > 3:
                print("[!] Char must be a single character")
                exit()

            AST_TREE["body"]["defined"]["Variables"].append({"name": Command["arguments"][0].value, "type": "CHAR", "value": Command["arguments"][1].value})
            continue

        if Command["type"] == "CREATEBOOL":
            if len(Command["arguments"]) <= 1:
                print("[!] Not enough arguments for CREATEBOOL")
                exit()

            AST_TREE["body"]["defined"]["Variables"].append({"name": Command["arguments"][0].value, "type": "BOOL", "value": Command["arguments"][1].value})    
            continue

        if Command["type"] == "DELETEINT":
            if len(Command["arguments"]) == 0:
                print("[!] Not enough arguments for DELETEINT")
                exit()

            for i in AST_TREE["body"]["defined"]["Variables"]:
                if i["name"] == Command["arguments"][0].value:
                    AST_TREE["body"]["defined"]["Variables"].remove(i)
                    break

        if Command["type"] == "DELETESTRING":
            if len(Command["arguments"]) == 0:
                print("[!] Not enough arguments for DELETESTRING")
                exit()

            for i in AST_TREE["body"]["defined"]["Variables"]:
                if i["name"] == Command["arguments"][0].value:
                    AST_TREE["body"]["defined"]["Variables"].remove(i)
                    break

        if Command["type"] == "DELETECHAR":
            if len(Command["arguments"]) == 0:
                print("[!] Not enough arguments for DELETECHAR")
                exit()

            for i in AST_TREE["body"]["defined"]["Variables"]:
                if i["name"] == Command["arguments"][0].value:
                    AST_TREE["body"]["defined"]["Variables"].remove(i)
                    break

        if Command["type"] == "DELETEBOOL":
            if len(Command["arguments"]) == 0:
                print("[!] Not enough arguments for DELETEBOOL")
                exit()

            for i in AST_TREE["body"]["defined"]["Variables"]:
                if i["name"] == Command["arguments"][0].value:
                    AST_TREE["body"]["defined"]["Variables"].remove(i)
                    break

        if Command["type"] == "SETINT":
            if len(Command["arguments"]) <= 1:
                print("[!] Not enough arguments for SETINT")
                exit()

            for i in AST_TREE["body"]["defined"]["Variables"]:
                if i["name"] == Command["arguments"][0].value:
                    i["value"] = Command["arguments"][1].value
                    break

        if Command["type"] == "SETSTRING":
            if len(Command["arguments"]) <= 1:
                print("[!] Not enough arguments for SETSTRING")
                exit()

            for i in AST_TREE["body"]["defined"]["Variables"]:
                if i["name"] == Command["arguments"][0].value:
                    i["value"] = Command["arguments"][1].value
                    break

        if Command["type"] == "SETCHAR":
            if len(Command["arguments"]) <= 1:
                print("[!] Not enough arguments for SETCHAR")
                exit()

        if Command["type"] == "SETBOOL":
            if len(Command["arguments"]) <= 1:
                print("[!] Not enough arguments for SETBOOL")
                exit()

            for i in AST_TREE["body"]["defined"]["Variables"]:
                if i["name"] == Command["arguments"][0].value:
                    i["value"] = Command["arguments"][1].value
        
        if Command["type"] == "OUTPUT":
            if len(Command["arguments"]) == 0:
                print("[!] Not enough arguments for OUTPUT")
                exit()

            
            print(Command["arguments"][0].value.replace("\\n", "\n").replace("\\s"," "), end="")
            break

        if Command["type"] == "ADDINT":
            if len(Command["arguments"]) <= 1:
                print("[!] Not enough arguments for ADDINT")
                exit()

            for i in AST_TREE["body"]["defined"]["Variables"]:
                if i["name"] == Command["arguments"][0].value:
                    i["value"] = int(i["value"]) + int(Command["arguments"][1].value)
                    break

        if Command["type"] == "MINUSINT":
            if len(Command["arguments"]) <= 1:
                print("[!] Not enough arguments for MINUSINT")
                exit()

            for i in AST_TREE["body"]["defined"]["Variables"]:
                if i["name"] == Command["arguments"][0].value:
                    i["value"] = int(i["value"]) - int(Command["arguments"][1].value)
                    break    

        if Command["type"] == "MUTIPLYINT":
            if len(Command["arguments"]) <= 1:
                print("[!] Not enough arguments for MUTIPLYINT")
                exit()

            for i in AST_TREE["body"]["defined"]["Variables"]:
                if i["name"] == Command["arguments"][0].value:
                    i["value"] = int(i["value"]) * int(Command["arguments"][1].value)
                    break

        if Command["type"] == "DIVIDEINT":
            if len(Command["arguments"]) <= 1:
                print("[!] Not enough arguments for DIVIDEINT")
                exit()

            for i in AST_TREE["body"]["defined"]["Variables"]:
                if i["name"] == Command["arguments"][0].value:
                    i["value"] = int(i["value"]) / int(Command["arguments"][1].value)
                    break    

        if Command["type"] == "FLOORINT":
            for i in AST_TREE["body"]["defined"]["Variables"]:
                if i["name"] == Command["arguments"][0].value:
                    i["value"] = math.floor(int(i["value"]))
                    break

    return AST_TREE 

