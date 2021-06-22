# Add the modules directory to the path.
import os, sys
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'modules'))

import unittest

from collections import OrderedDict

from pel.hwdiags.parserdata import ParserData


class TestParserData(unittest.TestCase):

    def setUp(self):
        self._parser = ParserData()

        # The actual data files are built in another repository. So there is
        # only limited testing we can do. At least we can test paths for invalid
        # or unsupported model_ec.
        self._model_ec = '23ABcdEf'

    def test_params(self):
        # test not a hex string
        with self.assertRaises(AssertionError):
            self._parser.query_model_ec('some_string')

        # test hex string not 8 characters
        with self.assertRaises(AssertionError):
            self._parser.query_model_ec('0123ABcdEf')

        # test if data for model_ec exists
        self.assertFalse(self._parser.query_model_ec(self._model_ec))

    def test_attn_desc(self):
        attn_type = 0x44

        data = self._parser.get_attn_desc(self._model_ec, attn_type)

        exp_attn = str(attn_type)

        self.assertEqual(data, exp_attn)

    def test_chip_data(self):
        model_ec = self._model_ec
        node_pos = 0x33
        chip_pos = 0x2222

        data = self._parser.get_chip_desc(self._model_ec, node_pos, chip_pos)

        exp_chip = "node %d unknown %d (%s)" % (node_pos, chip_pos,
                                                model_ec.upper())

        self.assertEqual(data, exp_chip)

    def test_sig_data(self):
        sig_id   = '5555'
        sig_inst = 0x66
        sig_bit  = 0x77

        data = self._parser.get_sig_desc(self._model_ec, sig_id, sig_inst,
                                         sig_bit)

        exp_sig  = "id:%s(%d)[%s] " % (sig_id.upper(), sig_inst, sig_bit)

        self.assertEqual(data, exp_sig)

    def test_signature(self):
        word_a = '11111111'
        word_b = '22223344'
        word_c = '55556677'

        data = self._parser.get_signature(word_a, word_b, word_c)

        model_ec = word_a

        chip_pos  = int(word_b[0:4], base=16)
        node_pos  = int(word_b[4:6], base=16)
        attn_type = int(word_b[6:8], base=16)

        sig_id   =     word_c[0:4]
        sig_inst = int(word_c[4:6], base=16)
        sig_bit  = int(word_c[6:8], base=16)

        exp_chip = "node %d unknown %d (%s)" % (node_pos, chip_pos,
                                                model_ec.upper())

        exp_sig  = "id:%s(%d)[%s] " % (sig_id.upper(), sig_inst, sig_bit)

        exp_attn = str(attn_type)

        expected = OrderedDict()
        expected["Chip Desc"] = exp_chip
        expected["Signature"] = exp_sig
        expected["Attn Type"] = exp_attn

        self.assertEqual(data, expected)

