#!/usr/bin/env Python
#思路： rank(mean(X-Y,5) / std(X-Y,5))
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
        self.neutral = True
        self.factorName = __name__.split('.')[-1]
        self.needFields = [t.PS, t.PE]  # 设置需要的字段

    def factor_definition(self):
        """
        收集派发指标
        :return:
        """
        s = time.time()
        needData = self.needData                                # 计算所需数据
        
        adjX = needData[t.PS]
        adjY = needData[t.PE]
        tmp1 = self.calculator.Mean(adjX-adjY,5)
        tmp2 = self.calculator.Std(adjX-adjY,5)

        factor = self.calculator.Wma(self.calculator.Rank(tmp1/tmp2),5)
        
        print('factor {0} done with {1} seconds'.format(self.factorName, time.time() - s))
        return factor

    def run_factor(self):
        self.run()



fct = Factor()
fct.run_factor()