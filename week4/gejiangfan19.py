# coding=utf8
__author__ = 'gejf'

import time

import numpy as np
import pandas as pd
from FactorModule.FactorBase import FactorBase
from DataReaderModule.Constants import ALIAS_FIELDS as t

class Factor(FactorBase):

    def __init__(self):
        super(Factor,self).__init__()
        self.neutral = False
        self.factorName = __name__.split('.')[-1]
        self.needFields = [t.LOW, t.CLOSE, t.OPEN, t.ADJFCT]  # 设置需要的字段

    def factor_definition(self):
        """
        收集派发指标
        :return:
        """
        s = time.time()
        needData = self.needData                                # 计算所需数据

        adjX = needData[t.CLOSE] * needData[t.ADJFCT]
        adjY = needData[t.LOW] * needData[t.ADJFCT]
        adjOpen = needData[t.OPEN] * needData[t.ADJFCT]
        ret1 = self.calculator.Sum(adjX - adjOpen,5)
        ret2 = self.calculator.Sum(adjY- adjOpen,5)
        factor = 100*ret1/ret2

        print('factor {0} done with {1} seconds'.format(self.factorName, time.time() - s))
        return factor

    def run_factor(self):
        self.run()



fct = Factor()
fct.run_factor()