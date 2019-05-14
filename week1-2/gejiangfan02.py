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
        self.needFields = [ t.CLOSE, t.ADJFCT, t.OPEN,t.HIGH,t.LOW, t.VOLUME]  # 设置需要的字段

    def factor_definition(self):
        """
        收集派发指标
        :return:
        """
        s = time.time()
        needData = self.needData                                # 计算所需数据

        adjClose = needData[t.CLOSE]
        adjOpen = needData[t.OPEN]
        adjLow = needData[t.LOW]
        adjHigh = needData[t.HIGH]
        ret1 = (adjHigh - adjLow) / adjLow
        ret2 = (adjClose - adjOpen) / adjOpen
        vol = (needData[t.VOLUME]) ** 0.5
        result1 = -(self.calculator.Corr(ret1,vol,num=5))
        result2 = -(self.calculator.Corr(ret2,vol,num=5))
        factor = -np.log(abs(result1 * result2))

        print('factor {0} done with {1} seconds'.format(self.factorName, time.time() - s))
        return factor

    def run_factor(self):
        self.run()



fct = Factor()
fct.run_factor()