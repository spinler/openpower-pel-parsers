import json
from collections import OrderedDict
from pel.hwdiags.parserdata import ParserData


def parseSRCToJson(refcode: str,
                   word2: str, word3: str, word4: str, word5: str,
                   word6: str, word7: str, word8: str, word9: str) -> str:
    """
    SRC Parser for openpower-hw-diags analyzer component.
    """

    out = OrderedDict()

    parser = ParserData()

    # The last byte of the refcode indicates the reason for this PEL. A value of
    # '10' indicates a system checkstop attention. Any other values is secondary
    # analysis, whether it is for a TI or manually called on the command line.
    if '10' == refcode[6:8]:
        out["Primary Attention"] = "system checkstop"
    else:
        out["Primary Attention"] = "secondary analysis"

    # Parse the signature.
    out["Signature Description"] = parser.get_signature(word6, word7, word8)

    return json.dumps(out)

