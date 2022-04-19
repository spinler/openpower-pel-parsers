from pel.datastream import DataStream
from collections import OrderedDict
from pel.peltool.private_header import getTimestamp


class ExtendedUserHeader:
    """
    This represents the Extended User Header section in a PEL.  It is  a required
    section.  It contains code versions, an MTMS subsection, and a string called
    a symptom ID.

    The Section base class handles the section header structure that every
    PEL section has at offset zero.
    """

    def __init__(self, stream: DataStream, sectionID: int, sectionLen: int,
                 versionID: int, subType: int, componentID: int):
        self.stream = stream
        self.sectionID = sectionID
        self.sectionLen = sectionLen
        self.versionID = versionID
        self.subType = subType
        self.componentID = componentID
        self.machineType = ""
        self.serialNumber = ""
        self.serverFWVersion = ""
        self.subsystemFWVersion = ""
        self.reserved4B = 0
        self.refTime = ""
        self.reserved1B1 = 0
        self.reserved1B2 = 0
        self.reserved1B3 = 0
        self.symptomIDSize = ""
        self.symptomID = ""

    def toJSON(self) -> str:
        self.machineType = bytes.decode(self.stream.get_mem(8))
        self.serialNumber = bytes.decode(self.stream.get_mem(12))
        self.serverFWVersion = bytes.decode(self.stream.get_mem(16))
        self.subsystemFWVersion = bytes.decode(self.stream.get_mem(16))
        self.reserved4B = self.stream.get_int(4)
        self.refTime = getTimestamp(self.stream)
        self.reserved1B1 = self.stream.get_int(1)
        self.reserved1B2 = self.stream.get_int(1)
        self.reserved1B3 = self.stream.get_int(1)
        self.symptomIDSize = self.stream.get_int(1)
        self.symptomID = bytes.decode(self.stream.get_mem(self.symptomIDSize))

        out = OrderedDict()
        out["Section Version"] = self.versionID
        out["Sub-section type"] = self.subType
        out["Created by"] = "0x{:02X}".format(self.componentID)
        out["Reporting Machine Type"] = self.machineType
        out["Reporting Serial Number"] = self.serialNumber.strip("\u0000")
        out["FW Released Ver"] = self.serverFWVersion.strip("\u0000")
        out["FW SubSys Version"] = self.subsystemFWVersion.strip("\u0000")
        out["Common Ref Time"] = self.refTime
        out["Symptom Id Len"] = str(self.symptomIDSize)
        out["Symptom Id"] = self.symptomID.strip("\u0000")

        return out
