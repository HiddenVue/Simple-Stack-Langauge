class Token():
    def __init__(self, Type, Value):
        self.type = Type
        self.value = Value

Tokens = {
    "TT_INT": Token("TT_INT", None),
    "TT_STRING": Token("TT_STRING", None),
    "TT_CHAR": Token("TT_CHAR", None),
    "TT_BOOL": Token("TT_BOOL", None),

    "TT_IDENTIFIER": Token("TT_IDENTIFIER", None),
}