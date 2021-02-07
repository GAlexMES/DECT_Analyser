from helper import switchDependingCharacter, toBinary


def bearerHandler(type):
    def bearerRequestHandler(message):
        print(type)
        print("FMID: %s" % message[2:5])
        print("PMID: %s" % message[5:10])
        print("ECN: %s" % message[10])
        print("LBN: %s" % message[11])
        octett12 = toBinary(message[12])
        octett13 = toBinary(message[13])
        print("ser type: %s%s" % (octett12[2::], octett13[0]))
        print("ser type/max life/aux: %s" % octett13[1:4])
        print("slot type: %s" % message[14])
        mcsIndex = octett12[0:2] + toBinary(message[15])
        if mcsIndex == "111111":
            print("2-level modulation (all fields), no coding")
        else:
            print("MCS index: %d" % int(mcsIndex, 2))

    return bearerRequestHandler

def wait(message):
    print("Wait")
    print("FMID: %s" % message[2:5])
    print("PMID: %s " % message[5:10])
    print("PMID can be spare 11110000111100001111")
    print("Spare 00001111 . . . . 00001111 is %s" % message[10:16])


def attributeB(type):
    def attributeBHandler(message):
        print(type)
        print("FMID: %s" % message[2:5])
        octett5 = toBinary(message[5])
        messageType = octett5[0:2]
        if messageType == "00":
            print("Message type: This message impacts only the bearer whose ECN and LBN values are given in the message ")
        if messageType == "01":
            print("Message type: This message impacts all bearers of the connection given by the ECN value ")
        if messageType == "10":
            print("Message type: reserved")
        if messageType == "11":
            print("Message type: ECN/LBN assignation message: this message impacts only the bearer where the message is sent and the given ECN and LBN values are allocated to such bearer ")

        octett6 = toBinary(message[6])
        print("ECN: %s%s" % (octett5[2:4], octett6[0:2]))
        octett7 = toBinary(message[7])
        print("LBN %s%s" % ( octett6[2:4], octett7[0:2]))
        print("CF: %s" % octett7[2])
        print("spare: %s" % octett7[3])
        print("PMID: %s" % message[10])

        octett12 =  toBinary(message[12])
        print("up/down/sm/ss: %s" % octett12[0:2])
        octett13 = toBinary(message[13])
        print("SER type: %s%s " % (octett12[2:4], octett13[0]))
        print("ser type/max life/aux %s" % octett13[1::])
        print("Slot type: %s" % message[14])
        octett15 = toBinary(message[15])
        aFieldModulationType = octett15[0:2]
        if aFieldModulationType == "00":
            print("A field modulation type: 2-level modulation")
        if aFieldModulationType == "01":
            print("A field modulation type: 4-level modulation")
        if aFieldModulationType == "10":
            print("A field modulation type: 8-level modulation")
        if aFieldModulationType == "11":
            print("A field modulation type: MCS based configuration")

        bzFieldModulationType = octett15[0:2]
        if bzFieldModulationType == "00":
            print("B+Z field modulation type: 2-level modulation")
        if bzFieldModulationType == "01":
            print("B+Z field modulation type: 4-level modulation")
        if bzFieldModulationType == "10":
            print("B+Z field modulation type: 8-level modulation")

        if bzFieldModulationType == "11":
            print("B+Z field modulation type:")
            if message[10] == "1":
                print("B+Z field modulation type: 16-level modulation")
            elif message[10] == "5":
                print("B+Z field modulation type: 64-level modulation")
            else:
                print("B+Z field modulation type: reserved")

            if message[11] == "0":
                print("Adaptive code rates for extended modulation: 1,0 (no coding)")
            elif message[11] == "2":
                print("Adaptive code rates for extended modulation: 1/3")
            elif message[11] == "4":
                print("Adaptive code rates for extended modulation: 0,4")
            elif message[11] == "6":
                print("Adaptive code rates for extended modulation: 0,5")
            elif message[11] == "8":
                print("Adaptive code rates for extended modulation: 0,6")
            elif message[11] == "B":
                print("Adaptive code rates for extended modulation: 0,75")
            elif message[11] == "C":
                print("Adaptive code rates for extended modulation: 0,8")
            else:
                print("Adaptive code rates for extended modulation: reserved")
        else:
            print("MCS index: %s%s" % (message[10],message[11]))
    return attributeBHandler
cases = {
    "0": bearerHandler("ACCESS_REQUEST"),
    "1": bearerHandler("bearer_handover_request"),
    "2": bearerHandler("connection_handover_request"),
    "3": bearerHandler("unconfirmed_access_request"),
    "4": bearerHandler("bearer_confirm"),
    "5": wait,
    "6": attributeB("attributes_B_request"),
    "7":  attributeB("attributes_B_confirm"),
    "8": lambda a: print("bandwidth_B_request, not implemented yet"),
    "9": lambda a: print("bandwidth_B_confirm, not implemented yet"),
    "A": lambda a: print("channel_list, not implemented yet"),
    "B": lambda a: print("unconfirmed_dummy, not implemented yet"),
    "C": lambda a: print("unconfirmed_handover, not implemented yet"),
    "D": lambda a: print("reserved"),
    "E": lambda a: print("reserved"),
    "F": lambda a: print("release, not implemented yet"),
}


def advancedConnectionControl(message):
    print("Message Type: Advanced Connection Control")
    switchDependingCharacter(cases, message, 1)
