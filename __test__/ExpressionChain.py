import pytest
from sys import path as sys_path
from ..utils import Path

main_path = str(Path().script_dir())
#main_path = main_path.join('..')
sys_path.append(main_path)

from SemanthicAnalyzer.states import ExpresionChain
from main import main

tokens, symbol_table = main(file_path='expression.pas', output=False)

def expression():
    exp_chain = ExpresionChain(symbol_table)
    index = 0
    while True:
        value = exp_chain.exec(tokens[index])
        if exp_chain.has_done(): break
        index += 1