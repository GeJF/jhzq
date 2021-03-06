#!/usr/bin/env Python
#思路： wma(COrr(findrank(decaylinear(delay(Z,5)/Z,3),15),findRank(decaylinear(delay(X+Y,3)/(X+Y),3),15)),3)
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
        self.needFields = [t.ADJOPEN,t.ADJLOW,t.VWAP]  # 设置需要的字段

    def factor_definition(self):
        """
        收集派发指标
        :return:
        """
        s = time.time()
        needData = self.needData                                # 计算所需数据
        
        adjX = needData[t.ADJOPEN]
        adjY = needData[t.ADJLOW]
        adjZ = needData[t.VWAP]
        
        tmp1 = self.calculator.Delay(adjX+adjY,3)/(adjX+adjY)
        tmp2 = self.calculator.Delay(adjZ,5)/adjZ
        tmp3 = self.calculator.Decaylinear(tmp1,3)
        tmp4 = self.calculator.Decaylinear(tmp2,3)

        factor = self.calculator.Corr(self.calculator.FindRank(tmp3,15),self.calculator.FindRank(tmp4,15),15)
        factor = self.calculator.Wma(factor,3)
        print('factor {0} done with {1} seconds'.format(self.factorName, time.time() - s))
        return factor

    def run_factor(self):
        self.run()



fct = Factor()
fct.run_factor()