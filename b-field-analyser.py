from helper import prepareBFields, getMessagesFromHexDump

# 80 Byte in hey
from messageTypes.messageTypeAnalyser import analyseMessageHeader

bFieldDatas = getMessagesFromHexDump('./ppMessages.dump')

message = 0

for bFieldData in bFieldDatas:
    print("# Message %d " % message)
    message = message +1
    print("Parsing Data into B-Fields:")
    bFields = prepareBFields(bFieldData)

    print("\nStarting analysis: \n")

    i = 0
    for bField in bFields:
        print("## Analyzing b%d: %s" % (i, bField))
        i = i+1
        analyseMessageHeader(bField)
        print("")