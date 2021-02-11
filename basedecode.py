#!/usr/bin/env/python
# a simple tool created on python for decoding data in base64
# tool author: krishpranav
#github.com/krishpranav

#imports
import os, re, sys, time, platform, json, argparse
from colorama import init
from termcolor import colored


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

