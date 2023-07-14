import unittest
import json
import tempfile
import os
from pel.peltool.config import Config, fuzzyMatch

configData = {
    "no_plugins_unless":
    [
        {
            "refcode": "BD802004"
        },
        {
            "refcode": "BC30E510"
        },
        {
            "refcode": "BD**6513"
        },
        {
            "refcode": "B7*0F10*"
        }
    ]
}


class TestConfig(unittest.TestCase):

    def test_fuzzyMatch(self):
        self.assertTrue(fuzzyMatch("BD602004", "BD602004"))

        self.assertTrue(fuzzyMatch("bC60e510", "BC60E510"))

        self.assertFalse(fuzzyMatch("BD602004", "BD6020044"))

        self.assertTrue(fuzzyMatch("BD602004", "********"))

        self.assertTrue(fuzzyMatch("BD602004", "BD**2004"))

        self.assertTrue(fuzzyMatch("bd60dead", "BD**DEAD"))

        self.assertTrue(fuzzyMatch("BD853531", "BD*5*53*"))

    def test_pluginsAllowed(self):

        file = tempfile.NamedTemporaryFile(delete=False)
        file.write(bytes(json.dumps(configData), 'utf-8'))
        file.close()

        config = Config()
        config.setConfigFile(file.name)

        test_refcodes = [("BD802004", True),
                         ("BC30E510", True),
                         ("BD806513", True),
                         ("B700F105", True),
                         ("BDDDDEAD", False)]

        for refcode, allow in test_refcodes:
            config.setRefCode(refcode)

            self.assertEqual(allow, config.allow_plugins)

        # Do it again, this time turn off plugins always
        config.allow_plugins = False
        for refcode, _ in test_refcodes:
            config.setRefCode(refcode)

            self.assertFalse(config.allow_plugins)

        os.remove(file.name)
