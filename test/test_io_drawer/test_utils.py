import os
import unittest

from io_drawer.utils import (format_timestamp, get_header_file_path,
                             get_trace_string_file_path)


class TestUtils(unittest.TestCase):

    def test_format_timestamp(self):
        # Test with valid timestamps
        self.assertEqual(format_timestamp(0x0000), ' 0:00:00')
        self.assertEqual(format_timestamp(0x0005), ' 0:00:05')
        self.assertEqual(format_timestamp(0x003C), ' 0:01:00')
        self.assertEqual(format_timestamp(0x005B), ' 0:01:31')
        self.assertEqual(format_timestamp(0x0313), ' 0:13:07')
        self.assertEqual(format_timestamp(0x1960), ' 1:48:16')
        self.assertEqual(format_timestamp(0x473E), ' 5:03:58')
        self.assertEqual(format_timestamp(0xFFFE), '18:12:14')

        # Test with invalid timestamps
        self.assertEqual(format_timestamp(-1), '--------')
        self.assertEqual(format_timestamp(0xFFFF), '--------')
        self.assertEqual(format_timestamp(0x10000), '--------')

    def test_get_header_file_path(self):
        path = get_header_file_path()
        self.assertTrue(os.path.exists(path))
        self.assertEqual(os.path.basename(path), 'mex_pte.h')

    def test_get_trace_string_file_path(self):
        path = get_trace_string_file_path()
        self.assertTrue(os.path.exists(path))
        self.assertEqual(os.path.basename(path), 'mexStringFile')
