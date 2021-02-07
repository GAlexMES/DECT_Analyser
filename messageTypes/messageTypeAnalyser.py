from helper import switchDependingCharacter
from messageTypes.reserved import reserved
from messageTypes.advancedConnectionControl import advancedConnectionControl
from messageTypes.escape import escape
from messageTypes.extendedSystemInformation import extendedSystemInformation
from messageTypes.gfChannelDataPacket import gfChannelDataPacket
from messageTypes.nullOrSegmentationInformation import nullOrSegmentationInformation
from messageTypes.qualityControl import qualityControl

cases = {
    "0": reserved,
    "8": reserved,

    "1": advancedConnectionControl,
    "9": advancedConnectionControl,

    "2": nullOrSegmentationInformation,
    "A": nullOrSegmentationInformation,

    "3": qualityControl,
    "B": qualityControl,

    "4": extendedSystemInformation,
    "C": extendedSystemInformation,

    "5": gfChannelDataPacket,
    "D": gfChannelDataPacket,

    "6": reserved,
    "E": reserved,

    "7": escape,
    "F": escape,
}

def analyseMessageHeader(message):
    switchDependingCharacter(cases, message, 0)
