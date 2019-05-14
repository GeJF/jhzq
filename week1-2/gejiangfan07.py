#!/usr/bin/env Python
#思路： Decay((X1-Y1)/Z)*Decay((X2-Y2)/Z)
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
        self.needFields = [t.MKTCAPFL, t.BUY_VALUE_LARGE_ORDER,t.BUY_VALUE_SMALL_ORDER,
                           t.SELL_VALUE_LARGE_ORDER,t.SELL_VALUE_SMALL_ORDER]  # 设置需要的字段

    def factor_definition(self):
        """
        收集派发指标
        :return:
        """
        s = time.time()
        needData = self.needData  #计算所需数据

        buyL = needData[t.BUY_VALUE_LARGE_ORDER]
        sellL = needData[t.SELL_VALUE_LARGE_ORDER]
        buyS = needData[t.BUY_VALUE_SMALL_ORDER]
        sellS = needData[t.SELL_VALUE_SMALL_ORDER]
        MKT =  needData[t.MKTCAPFL]
        ret1 =  self.calculator.Decaylinear((buyL-buyS)/MKT,5)
        ret2 = self.calculator.Decaylinear((sellL-sellS)/MKT,5)
        factor = - ret1 * ret2
        print('factor {0} done with {1} seconds'.format(self.factorName, time.time() - s))
        return factor

    def run_factor(self):
        self.run()



fct = Factor()
fct.run_factor()