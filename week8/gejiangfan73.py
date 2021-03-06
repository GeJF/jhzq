#!/usr/bin/env Python
#思路： ((X-min(X,3))+(X-min(X,6))+(X-min(X,12))+(X-min(X,24)))/4*(max(X,24)-min(X,24))
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
        self.needFields = [t.PB]  # 设置需要的字段

    def factor_definition(self):
        """
        收集派发指标
        :return:
        """
        s = time.time()
        needData = self.needData                                # 计算所需数据
        
        adjX = needData[t.PB]
        
        tmp1 = adjX-self.calculator.Min(adjX,3)
        tmp2 = adjX-self.calculator.Min(adjX,6)
        tmp3 = adjX-self.calculator.Min(adjX,12)
        tmp4 = adjX-self.calculator.Min(adjX,24)
        tmp = 4*(self.calculator.Max(adjX,24)-self.calculator.Min(adjX,24))
        
        factor = (tmp1+tmp2+tmp3+tmp4)/tmp
        
        print('factor {0} done with {1} seconds'.format(self.factorName, time.time() - s))
        return factor

    def run_factor(self):
        self.run()



fct = Factor()
fct.run_factor()