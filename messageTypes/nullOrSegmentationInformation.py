from helper import switchDependingCharacter, toBinary, toDecimal


def handlePDUInformation(number, firstOctett, secondOctettBinary, thirdOctett):
    print("Send sequence number of the %s PDU transported in this slot: %s" % (number, firstOctett))
    print("9th bit of the send sequence number: %s" % (number, secondOctettBinary[0]))
    if secondOctettBinary[1] == "1":
        print("bn25 == 1 => Indicates this is the last segment of the PDU ")

    if secondOctettBinary[2] == "1":
        print("bn26 == 1 => Indicates that the rest of the PDU shall be filling with padding")

    print("Sequence number of the %s PDU segment: %s" % (number, thirdOctett))

def handleEUSlot(message):
    print("This is an E+U slot, any other case")

    secondOctett = toBinary(message[6:8])
    handlePDUInformation("first", message[4:6], secondOctett, message[8:10])
    if secondOctett[3] == "1":
        print("bn27 == 1 => Indicates that there is a second PDU segment in this slot")
        secondOctett = toBinary(message[12:14])
        handlePDUInformation("second", message[10:12], secondOctett, message[14:16])

def eytendedNCF(message):
    print("Extended NCF format")
    extendedNCF = toDecimal(message[2:4])

    if extendedNCF >= 0 and extendedNCF <= 60:
        print("%d Cf or CLf data in the B-field" % extendedNCF)
    else:
        print("reserved")

cases = {
    "0": lambda a: print("no CF or CLF data in the B-field"),
    "1": lambda a: print("one B-subfield contains CF or CLF data"),
    "2": lambda a: print("two B-subfields contain CF or CLF data"),
    "3": lambda a: print("three B-subfields contain CF or CLF data"),
    "4": lambda a: print("four B-subfields contain CF or CLF data"),
    "5": lambda a: print("five B-subfields contain CF or CLF data"),
    "6": lambda a: print("six B-subfields contain CF or CLF data"),
    "7": lambda a: print("seven B-subfields contain CF or CLF data"),
    "8": lambda a: print("eight B-subfields contain CF or CLF data"),
    "9": lambda a: print("nine B-subfields contain CF or CLF data"),
    "A": lambda a: print("This is an E+U slot, and the U subfields contain the first part of a DLC PDU"),
    "B": lambda a: print("This is an E+U slot, and the U subfields contain the first part of a DLC PDU, and the rest of the PDU is empty"),
    "C": lambda a: handleEUSlot,
    "D": lambda a: print("reserved"),
    "E": lambda a: print("reserved"),
    "F": lambda a: print("the multiplex for 4-level, 8-level, 16-level and 64-level is indicated in bits bn8 to bn15"),
}

def nullOrSegmentationInformation(message):
    print("Message Type: Null or If Segmentation Information")
    switchDependingCharacter(cases, message, 1)
