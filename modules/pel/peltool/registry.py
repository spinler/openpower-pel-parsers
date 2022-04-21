import json


class Registry:
    def __init__(self):

        try:
            # If module not installed, just don't print the
            # SRC details
            import pel_registry
            path = pel_registry.get_path()
            self.pels = self.loadJson(path)
        except ModuleNotFoundError:
            self.pels = []

    def loadJson(self, path: str):
        with open(path, "r") as f:
            load_dict = json.load(f)
            return load_dict["PELs"]

    def getErrorMessage(self, code: str, srcType: str) -> dict:
        output = {}

        for pel in self.pels:
            if "ReasonCode" not in pel["SRC"]:
                continue

            entryType = pel["SRC"].get("Type", "BD")
            if srcType != entryType:
                continue

            if code not in pel["SRC"]["ReasonCode"]:
                continue

            output['Message'] = pel['Documentation']['Message']

            if ('MessageArgSources' in pel['Documentation']):
                output['MessageArgSources'] = \
                    pel['Documentation']['MessageArgSources']

            if 'Words6To9' in pel['SRC'] and pel['SRC']['Words6To9']:
                output['Words6To9'] = pel['SRC']['Words6To9']

            return output

        return output
