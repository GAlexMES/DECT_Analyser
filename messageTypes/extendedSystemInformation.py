from helper import switchDependingCharacter

reserved = lambda a: print("reserved")

cases = {
    "0": lambda a: print("TARI messages, not implemented yet"),
    "1": lambda a: print("no-emission mode sync information or ULE Dummy Bearer subfield 2 , not implemented yet"),
    "2": lambda a: print("ULE Dummy Bearer subfield 3, not implemented yet"),
    "3": reserved,
    "4": reserved,
    "5": reserved,
    "6": reserved,
    "7": reserved,
    "8": reserved,
    "9": reserved,
    "A": lambda a: print("ULE Dummy Bearer subfield 0, not implemented yet"),
    "B": lambda a: print("ULE Dummy Bearer subfield 1, not implemented yet"),
    "C": reserved,
    "D": reserved,
    "E": reserved,
    "F": reserved,
}

def extendedSystemInformation(message):
    print("Message Type: Quality Control")
    switchDependingCharacter(cases, message, 1)

