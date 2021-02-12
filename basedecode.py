#!/usr/bin/env/python
# a simple tool created on python for decoding data in base64
# tool author: krishpranav
#github.com/krishpranav

#imports
import os, re, sys, time, platform, json, argparse
from colorama import init
from termcolor import colored
import base64, base58, base62, base64, base91
sys.path.append(os.path.join(os.path.dirname(__file__), "lib"))
import base92

class BaseCrack:

    def __init__(self, output=None, magic_mode_call=False, quit_after_fail=True):
        self.output = output
        self.api_call = False
        self.magic_mode_call = magic_mode_call
        self.image_mode_call = False
        self.quit_after_fail = quit_after_fail
        self.b64_once = False
        self.b64_url = False
        self.current_iter_base = None

    #main function
    def decode_base(self, encoded_base):
        def contains_replacement_char(res):
            if u'\ufffd' in res: return True
            else:
                count = 0
                for char in res:
                    if ord(char) > 127: count += 1
                return True if count > 0 else False




