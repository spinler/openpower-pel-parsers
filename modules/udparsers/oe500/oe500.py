import json
from collections import OrderedDict

from pel.hexdump import hexdump
from pel.datastream import DataStream
from pel.hwdiags.parserdata import ParserData


def _parse_signature_list(version: int, stream: DataStream) -> OrderedDict:
    """
    Parser for the signature list.
    """

    out = OrderedDict()

    parser = ParserData()

    # The first 4 bytes contains the number of signatures in this data.
    sig_count = stream.get_int(4)

    # Iterate each signature.
    out["Signature List"] = []
    for i in range(0, sig_count):
        # Extact the three words of the signature.
        a = stream.get_mem(4).hex()
        b = stream.get_mem(4).hex()
        c = stream.get_mem(4).hex()

        # Get the signature data.
        out["Signature List"].append(parser.get_signature(a, b, c))

    return out


def _parse_register_dump(version: int, stream: DataStream) -> OrderedDict:
    """
    Parser for the register dump.
    """

    out = OrderedDict()

    out["Warning"] = "User data parser TBD"

    return out


def _parse_guard_list(version: int, stream: DataStream) -> OrderedDict:
    """
    Parser for the guard list.
    """

    out = OrderedDict()

    out["Warning"] = "User data parser TBD"

    return out


def _parse_default(version: int, stream: DataStream) -> OrderedDict:
    """
    Default parser for user data sections that are not currently supported.
    """

    out = OrderedDict()

    out["Warning"] = "Unsupported user data type"

    return out


def parseUDToJson(subtype: int, version: int, data: memoryview) -> str:
    """
    Default function required by all component PEL user data parsers.
    """

    # Determine which parser to use.
    parsers = {
        1: _parse_signature_list,
        2: _parse_register_dump,
        3: _parse_guard_list,
    }
    subtype_func = parsers.get(subtype, _parse_default)

    # Get the parsed output of this data.
    stream = DataStream(data, byte_order='big', is_signed=False)
    out = subtype_func(version, stream)

    # If any warnings were added to the data, include the hex dump.
    if "Warning" in out:
        out["Hex Dump"] = hexdump(data)

    # Convert to JSON format and dump to a string.
    return json.dumps(out)

