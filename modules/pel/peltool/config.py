import os
import json


def fuzzyMatch(refcode: str, fuzzyRefcode: str) -> bool:
    """
    A case insensitive compare that also allows '*' for wildcards.
    """
    if len(refcode) != len(fuzzyRefcode):
        return False

    for i in range(len(fuzzyRefcode)):
        if refcode[i].upper() != fuzzyRefcode[i].upper() and fuzzyRefcode[i] != '*':
            return False

    return True


class Config:
    """
    Holds configuration options passed into it from a JSON config file.
    """

    def __init__(self) -> None:
        self.allow_plugins = True
        self.serviceable_only = False
        self.non_serviceable_only = False
        self.__no_plugins_unless__refcodes = []
        self.__refcode = ""

    def setConfigFile(self, file: str) -> None:
        if not os.path.exists(file):
            raise Exception(f"Invalid config file path {file}")

        self.__parseConfig(file)

    def setRefCode(self, refcode: str) -> None:
        self.__refcode = refcode

        if not self.allow_plugins:
            return

        # Check if the refcode is in the plugins allow list.
        if len(self.__no_plugins_unless__refcodes) == 0:
            self.allow_plugins = True
        else:
            self.allow_plugins = False
            for refcode in self.__no_plugins_unless__refcodes:
                if fuzzyMatch(self.__refcode, refcode):
                    self.allow_plugins = True
                    break

    def __parseConfig(self, file: str) -> None:

        with open(file, "r") as config_file:

            config_data = json.load(config_file)

            for entry in config_data.get("no_plugins_unless", {}):
                if "refcode" in entry:
                    self.__no_plugins_unless__refcodes.append(
                        entry["refcode"])
