from pel.datastream import DataStream
from collections import OrderedDict
from pel.peltool.pel_values import *
from enum import Enum, unique
import json
from


@unique
class UserDataFormat(Enum):
    json = 0x1
    cbor = 0x2
    text = 0x3
    custom = 0x4


def get_value(data: memoryview, start: int, end: int) -> int:
    return int.from_bytes(data[start: start + end], byteorder="big")


class UserData:
    """
    This represents the User Data section in a PEL.  It is free form data
    that the creator knows the contents of.  The component ID, version,
    and sub-type fields in the section header are used to identify the
    format.

    The Section base class handles the section header structure that every
    PEL section has at offset zero.
    """

    def __init__(self, stream: DataStream, sectionID: int, sectionLen: int,
                 versionID: int, subType: int, componentID: int, creatorID: str):
        self.stream = stream
        self.sectionID = sectionID
        self.sectionLen = sectionLen
        self.versionID = versionID
        self.subType = subType
        self.componentID = componentID
        self.creatorID = creatorID
        self.dataLength = sectionLen - 8
        self.data = self.stream.get_mem(self.dataLength)

    def parse(self, out: OrderedDict) -> str:
        import importlib
        name = (self.creatorID.lower() + "%04X" % self.componentID).lower()
        try:
            cls = importlib.import_module("udparsers." + name + "." + name)
            mv = memoryview(self.data)
            return cls.parseUDToJson(self.subType, self.versionID, mv)
        except:
            from udparsers.helpers.errludP_Helpers import hexDump
            out["Data"] = hexDump(self.data, 0, self.dataLength)

    def getBuiltinFormatJSON(self, out: OrderedDict):
        if self.subType == UserDataFormat.json.value:
            out.update(json.loads(bytes.decode(self.stream.data).strip()))
        elif self.subType == UserDataFormat.cbor.value:
            pad = get_value(self.stream.data, self.dataLength - 4, 4)
            if self.dataLength > pad + 4:
                self.dataLength = self.dataLength - pad - 4
            out.update(json.loads(bytes.decode(
                self.stream.get_mem(self.dataLength)).strip()))
        elif self.subType == UserDataFormat.text.value:
            pass

    def toJSON(self) -> str:

        out = OrderedDict()
        out["Section Version"] = self.versionID
        out["Sub-section type"] = self.subType
        out["Created by"] = "0x{:02X}".format(self.componentID)

        if creatorIDs[self.creatorID] == "BMC" and self.componentID == 0x2000:
            self.getBuiltinFormatJSON(out)
        else:
            value = self.parse()
            if value != "":
                out.update(json.loads(value))

        return out
