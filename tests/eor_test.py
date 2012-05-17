# -*- coding: utf-8 -*-

import unittest

from pynes.compiler import lexical, syntax, semantic
class EorTest(unittest.TestCase):

    '''Test logical EOR operation between $10 (Decimal 16) and the
    content of the Accumulator'''
    def test_eor_imm(self):
        tokens = lexical('EOR #10')
        self.assertEquals(2 , len(tokens))
        self.assertEquals('T_INSTRUCTION', tokens[0]['type'])
        self.assertEquals('T_NUMBER', tokens[1]['type'])
        ast = syntax(tokens)
        self.assertEquals(1 , len(ast))
        self.assertEquals('S_IMMEDIATE', ast[0]['type'])
        code = semantic(ast)
        self.assertEquals(code, [0x49, 0x10])

    '''Test logical EOR operation between the content of the
    Accumulator and the content of zero page $00'''
    def test_eor_zp(self):
        tokens = lexical('EOR $00')
        self.assertEquals(2 , len(tokens))
        self.assertEquals('T_INSTRUCTION', tokens[0]['type'])
        self.assertEquals('T_ADDRESS', tokens[1]['type'])
        ast = syntax(tokens)
        self.assertEquals(1 , len(ast))
        self.assertEquals('S_ZEROPAGE', ast[0]['type'])
        code = semantic(ast)
        self.assertEquals(code, [0x45, 0x00])

    def test_eor_zpx(self):
        tokens = lexical('EOR $10,X')
        self.assertEquals(4 , len(tokens))
        token = tokens[0]
        self.assertEquals('T_INSTRUCTION', tokens[0]['type'])
        self.assertEquals('T_ADDRESS', tokens[1]['type'])
        self.assertEquals('T_SEPARATOR', tokens[2]['type'])
        self.assertEquals('T_REGISTER', tokens[3]['type'])
        ast = syntax(tokens)
        self.assertEquals(1 , len(ast))
        self.assertEquals('S_ZEROPAGE_X', ast[0]['type'])
        code = semantic(ast)
        self.assertEquals(code, [0x55, 0x10])

    def test_sta_abs(self):
        tokens = lexical('EOR $1234')
        self.assertEquals(2 , len(tokens))
        self.assertEquals('T_INSTRUCTION', tokens[0]['type'])
        self.assertEquals('T_ADDRESS', tokens[1]['type'])
        self.assertEquals('$1234', tokens[1]['value'])
        ast = syntax(tokens)
        self.assertEquals(1 , len(ast))
        self.assertEquals('S_ABSOLUTE', ast[0]['type'])
        code = semantic(ast)
        self.assertEquals(code, [0x4D, 0x34, 0x12])


    def test_sta_absx(self):
        tokens = lexical('EOR $1234,X')
        self.assertEquals(4 , len(tokens))
        token = tokens[0]
        self.assertEquals('T_INSTRUCTION', tokens[0]['type'])
        self.assertEquals('T_ADDRESS', tokens[1]['type'])
        self.assertEquals('$1234', tokens[1]['value'])
        self.assertEquals('T_SEPARATOR', tokens[2]['type'])
        self.assertEquals('T_REGISTER', tokens[3]['type'])
        ast = syntax(tokens)
        self.assertEquals(1 , len(ast))
        self.assertEquals('S_ABSOLUTE_X', ast[0]['type'])
        code = semantic(ast)
        self.assertEquals(code, [0x5D, 0x34, 0x12])

    def test_sta_absy(self):
        tokens = lexical('EOR $1234,Y')
        self.assertEquals(4 , len(tokens))
        self.assertEquals('T_INSTRUCTION', tokens[0]['type'])
        self.assertEquals('T_ADDRESS', tokens[1]['type'])
        self.assertEquals('T_SEPARATOR', tokens[2]['type'])
        self.assertEquals('T_REGISTER', tokens[3]['type'])
        ast = syntax(tokens)
        self.assertEquals(1 , len(ast))
        self.assertEquals('S_ABSOLUTE_Y', ast[0]['type'])
        code = semantic(ast)
        self.assertEquals(code, [0x59, 0x34, 0x12])

    def test_sta_indx(self):
        tokens = lexical('EOR ($20,X)')
        self.assertEquals(6 , len(tokens))
        self.assertEquals('T_INSTRUCTION', tokens[0]['type'])
        self.assertEquals('T_OPEN', tokens[1]['type'])
        self.assertEquals('T_ADDRESS', tokens[2]['type'])
        self.assertEquals('$20', tokens[2]['value'])
        self.assertEquals('T_SEPARATOR', tokens[3]['type'])
        self.assertEquals('T_REGISTER', tokens[4]['type'])
        self.assertEquals('T_CLOSE', tokens[5]['type'])
        ast = syntax(tokens)
        self.assertEquals(1 , len(ast))
        self.assertEquals('S_INDIRECT_X', ast[0]['type'])
        code = semantic(ast)
        self.assertEquals(code, [0x41, 0x20])

    def test_sta_indy(self):
        tokens = lexical('EOR ($20),Y')
        self.assertEquals(6 , len(tokens))
        self.assertEquals('T_INSTRUCTION', tokens[0]['type'])
        self.assertEquals('T_OPEN', tokens[1]['type'])
        self.assertEquals('T_ADDRESS', tokens[2]['type'])
        self.assertEquals('T_CLOSE', tokens[3]['type'])
        self.assertEquals('T_SEPARATOR', tokens[4]['type'])
        self.assertEquals('T_REGISTER', tokens[5]['type'])
        ast = syntax(tokens)
        self.assertEquals(1 , len(ast))
        self.assertEquals('S_INDIRECT_Y', ast[0]['type'])
        code = semantic(ast)
        self.assertEquals(code, [0x51, 0x20])