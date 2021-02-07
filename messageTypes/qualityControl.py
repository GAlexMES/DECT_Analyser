from helper import switchDependingCharacter


def bearerAndConnectionControl(printFn):
    def messageHandler(message):
        fmid = message[2:5]
        pmid = message[5:10]
        param1 = message[10:12]
        param2 = message[12:14]
        control = message[14:16]
        if not control == "0F":
            print("Expected 56-63 to be 00001111/0F but it was %s" % control)

        print("FMID: %s" % fmid)
        print("PMID: %s"% pmid)

        printFn(param1, param2)

    return messageHandler



def comand0000(param1, param2):
    print("Param_1: %s means LBN LBN" % param1)
    print("Param_2: %s means LBN LBN" % param2)
    print("Meaning: ")
    print("antenna switch for the bearer(s) identified by LBN")
    print("request: PT --> FT")
    print("reject: FT --> PT ")

def comand0001(param1, param2):
    print("Param_1: %s means RPN" % param1)
    print("Param_2: %s should be 0F" % param2)
    print("Meaning: ")
    print("antenna switch for all bearers of this connection to the RFP identified by its RPN")
    print("request: PT --> FT")
    print("reject: FT --> PT ")

def comand0010(param1, param2):
    if param1[0] == "0":
        print("Param_1: %s should be 0 LBN" % param1)
        print("Param_2: %s means LBN LBN" % param2)
        print("Meaning: ")
        print("bearer handover/bearer replacement of the bearer(s) identified by LBN")
        print("request: FT --> PT ")
        print("reject: PT --> FT ")
        return

    if param1[0] == "F":
        print("Param_1: %s should be F LBN" % param1)
        print("Param_2: %s means LBN LBN" % param2)
        print("Meaning: ")
        print("bearer handover/bearer replacement of the bearer(s) identified by LBN")
        print("request: PT --> FT")
        print("reject: FT --> PT ")
        return

    print("Expected first byte of Param_1 to be 0 or F but was %s. Param_2 was %s" % (param1, param2))


def comand0011(param1, param2):
    print("Param_1: %s should be 0F" % param1)
    print("Param_2: %s should be 0F" % param2)
    print("Meaning: ")
    print("connection handover")
    print("request: FT --> PT")
    print("reject: PT --> FT ")

def comand0100(param1, param2):
    print("Param_1: %s should be 0 LBN" % param1)
    print("Param_2: %s is the frequency error" % param2)
    print("Meaning: ")
    print("frequency control for the bearer identified by LBN")
    print("request: FT --> PT")
    print("reject: PT --> FT ")

def comand0101(param1, param2):
    print("Param_1: %s is the RPN" % param1)
    print("Param_2: %s is the frequency error" % param2)
    print("Meaning: ")
    print("frequency control for all bearers of this connection to the RFP identified by its RPN")
    print("request: FT --> PT")
    print("reject: PT --> FT ")

def comand0110(param1, param2):
    print("Param_1: %s is the RPN" % param1)
    print("Param_2: %s is the advance timing, increment decrement" % param2)
    print("Meaning: ")
    print("Advance timing for all the bearers of this connection to the RFP identified by its RPN ")
    print("request: FT --> PT")
    print("reject: PT --> FT ")

def comand0111(param1, param2):
    print("Param_1: %s is the RPN" % param1)
    print("Param_2: %s should be 0F" % param2)
    print("Meaning: ")
    print("PT --> FT: PT informs that it is transmitting prolonged preamble in all the frames ")


def comand1000(param1, param2):
    if param1[0] == "0":
        print("Param_1: %s should be 0 SN" % param1)
        print("Param_2: %s should be 0 CN" % param2)
        print("Meaning: ")
        print("frequency replacement to carrier CN (note 10) on slot pair SN ")
        print("request: PT --> FT")
        print("reject: FT --> PT ")
        return

    if param1[0] == "1":
        print("Param_1: %s should be 1 SN" % param1)
        print("Param_2: %s should be 0 CN" % param2)
        print("Meaning: ")
        print(" frequency replacement to carrier CN (note 10) on slot pair SN  ")
        print("grant: PT --> FT")
        return

    print("Expected Param_1 to be 0 or 1 but was %s. Param_2 was %s" % (param1, param2))

def comand1001(param1, param2):
    if param2[0] == "0":
        print("Param_1: %s means LBN SN" % param1)
        print("Param_2: %s should be 00 CN" % param2)
        print("Meaning: ")
        print("frequency replacement of the bearer identified by LBN (note 11) to carrier CN (note 10) on slot pair SN request (note 12) ")
        return
    if param2[0] == "1":
        print("Param_1: %s means LBN SN" % param1)
        print("Param_2: %s should be 01 CN" % param2)
        print("Meaning: ")
        print("frequency replacement of the bearer identified by LBN (note 11) to carrier CN (note 10) on slot pair SN request (note 12) ")
        return

    if param2[0] == "2":
        print("Param_1: %s means LBN SN" % param1)
        print("Param_2: %s should be 10 CN" % param2)
        print("Meaning: ")
        print("frequency replacement of the bearer identified by LBN (note 11) to carrier CN (note 10) on slot pair SN request (note 12) ")
        return

    print("Expected first byte of Param_2 to be 00, 10 or 01 but was %s. Param_1 was %s" % (param2, param1))


def reset(message):
    print("reset")
    print("FMID: %s" % message[2:5])
    print("PMID: %s" % message[5:10])
    ctrl = message[10]
    if ctrl == "1":
        print("Ctrl: request first TDMA half frame")
    elif ctrl == "2":
        print("Ctrl: request second TDMA half frame")
    elif ctrl == "3":
        print("Ctrl: request both TDMA half frame")
    elif ctrl == "5":
        print("Ctrl: confirm first TDMA half frame")
    elif ctrl == "6":
        print("Ctrl: confirm second TDMA half frame")
    elif ctrl == "7":
        print("Ctrl: confirm both TDMA half frame")
    else:
        print("Ctrl: reserved")

    print("LBN: %s" % message[11])
    print("spare 0F: %s" % message[12:14])
    print("spare 0F: %s" % message[14:16])

reserved = lambda a: print("reserved")

cases = {
    "0": bearerAndConnectionControl(comand0000),
    "1":  bearerAndConnectionControl(comand0001),
    "2":  bearerAndConnectionControl(comand0010),
    "3":  bearerAndConnectionControl(comand0011),
    "4":  bearerAndConnectionControl(comand0100),
    "5":  bearerAndConnectionControl(comand0101),
    "6":  bearerAndConnectionControl(comand0110),
    "7":  bearerAndConnectionControl(comand0111),
    "8":  bearerAndConnectionControl(comand1000),
    "9":  bearerAndConnectionControl(comand1001),
    "A": reserved,
    "B": reserved,
    "C": reserved,
    "D": reserved,
    "E": reset,
    "F": lambda a: print("Bearer quality in an asymmetric connection , not implemented yet"),
}


def qualityControl(message):
    print("Message Type: Quality Control")
    switchDependingCharacter(cases, message, 1)

