#!/usr/bin/env Python
#思路：-1 * sum(rank(correlation(rank(high), rank(volume), 3)), 3)
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
        self.needFields = [t.HIGH, t.ADJFCT, t.VOLUME]  # 设置需要的字段

    def factor_definition(self):
        """
        收集派发指标
        :return:
        """
        s = time.time()
        needData = self.needData  #计算所需数据

        adjHigh = needData[t.HIGH] * needData[t.ADJFCT]
        temp1 = self.calculator.Rank(adjHigh)
        Vol = self.calculator.Rank(needData[t.VOLUME])
        temp2 = self.calculator.Corr(temp1,Vol,3)
        temp2 = self.calculator.Rank(temp2)
        factor = - self.calculator.Sum(temp2,3)
        print('factor {0} done with {1} seconds'.format(self.factorName, time.time() - s))
        return factor

    def run_factor(self):
        self.run()



fct = Factor()
fct.run_factor()