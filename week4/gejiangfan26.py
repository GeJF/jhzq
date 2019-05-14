#!/usr/bin/env Python
#思路： (X.mean(3)+X.mean(6)+X.mean(12)+X.mean(24))/4*X
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
        adjX3 = self.calculator.Mean(adjX,3)
        adjX6 = self.calculator.Mean(adjX,5)
        adjX12 = self.calculator.Mean(adjX,15)
        adjX24 = self.calculator.Mean(adjX,30)

        factor = (adjX3+adjX6+adjX12+adjX24)/(4*adjX)

        print('factor {0} done with {1} seconds'.format(self.factorName, time.time() - s))
        return factor

    def run_factor(self):
        self.run()



fct = Factor()
fct.run_factor()