# -*- coding: utf-8 -*-

from unittest import TestCase
from pynes.composer import pynes_compiler, Cartridge

class WhatElse():

    def __init__(self, testcase):
        self.testcase = testcase
        self.start = 0
        self.last = None

    def has(self, text):
        index = self.testcase.asm.find(text)
        if index:
            self.start = index + len(text)
            self.last = text
        else:
            raise(AssertionError('"%s" was not found in code' % text))
        return self

    def and_then(self, text):
        index = self.testcase.asm[self.start:].find(text)
        if index:
            self.start += index
            self.last = text
        else:
            raise(AssertionError('"%s" was not found after "%s" in code' % (text, self.last)))
        return self


class ComposerTestCase(TestCase):

    def __init__(self, testname):
        TestCase.__init__(self, testname)

    def setUp(self):
        self.code = None

    def assert_asm_from(self, code):
        self.code = code
        self.cart = pynes_compiler(code)
        self.asm = self.cart.to_asm()
        return WhatElse(self)