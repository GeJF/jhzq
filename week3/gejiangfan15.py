#!/usr/bin/env Python
#思路： -1 * rank(cov(rank(X), rank(Y), 5))
# -*- coding:utf-8 -*-
# author: gejf
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
        self.needFields = [t.CLOSE, t.ADJFCT, t.VOLUME]  # 设置需要的字段

    def factor_definition(self):
        """
        收集派发指标
        :return:
        """
        s = time.time()
        needData = self.needData  #计算所需数据

        adjClose = self.calculator.Rank(needData[t.CLOSE] * needData[t.ADJFCT])
        Vol = self.calculator.Rank(needData[t.VOLUME])
        stdC = self.calculator.Std(adjClose,5)
        stdV = self.calculator.Std(Vol,5)
        temp = self.calculator.Corr(adjClose,Vol,5)
        factor = - self.calculator.Rank(temp * stdC * stdV)
        print('factor {0} done with {1} seconds'.format(self.factorName, time.time() - s))
        return factor

    def run_factor(self):
        self.run()



fct = Factor()
fct.run_factor()