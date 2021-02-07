from helper import switchDependingCharacter

cases = {
    "0": lambda a: print("no CF data in the B-field"),
    "1": lambda a: print("one B-subfield contains CF data"),
    "2": lambda a: print("two B-subfields contain CF data"),
    "3": lambda a: print("three B-subfields contain CF data"),
    "4": lambda a: print("four B-subfields contain CF data"),
    "5": lambda a: print("five B-subfields contain CF data"),
    "6": lambda a: print("six B-subfields contain CF data "),
    "7": lambda a: print("seven B-subfields contain CF data"),
    "8": lambda a: print("eight B-subfields contain CF data"),
    "9": lambda a: print("nine B-subfields contain CF data"),
    "A": lambda a: print("This is an E+U slot, and the U part contains the first part of a DLC PDU"),
    "B": lambda a: print("This is an E+U slot, and the U part contains the first part of a DLC PDU, and the rest of the PDU is empty"),
    "C": lambda a: print("0 outstanding subfields"),
    "D": lambda a: print("1 outstanding subfield"),
    "E": lambda a: print("2 outstanding subfields"),
    "F": lambda a: print("> 2 outstanding subfields"),
}

def gfChannelDataPacket(message):
    print("Message Type: Gf Channel Data Packet")
    switchDependingCharacter(cases, message, 1)