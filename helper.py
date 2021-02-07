def getMessagesFromHexDump(filename):
    bFieldData = []
    with open(filename) as fp:
        line = fp.readline()
        message = ""
        while line:
            line = line.replace("\n", "")
            if len(line.replace(" ", "")) == 0:
                bFieldData.append(message)
                message = ""
            else:
                message = message + line[4::]
            line = fp.readline()
    return bFieldData


def prepareBFields(bFieldData):
    bFieldDataCleaned =  bFieldData.replace(" ", "").upper()
    bFields = []
    while len(bFieldDataCleaned) >= 20:
        bFields.append(bFieldDataCleaned[0: 20])
        print("b%d: %s" % (len(bFields), bFields[len(bFields)-1]))
        bFieldDataCleaned = bFieldDataCleaned[ 20 :: ]

    if len(bFieldDataCleaned) > 0:
        print("Too many (or to less) bytes. Could not parse this last bytes: %s", bFieldDataCleaned)
    return bFields

def toBinary(hex):
    return bin(int(hex, 16))[2:].zfill(8)

def toDecimal(hex):
    return int(hex, 16)

def switchDependingCharacter(dictionary, message, start, length = 1):
    dictionary.get(message[start:start+length], lambda a: print("%s is not a hex character or there was no case defined" % a))(message)