#!/usr/bin/env Python
#思路： wma(-(X-X.shift(5))*Y/Z.shift(5))
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
        self.needFields = [t.VWAP, t.NETASSET, t.VOLUME]  # 设置需要的字段

    def factor_definition(self):
        """
        收集派发指标
        :return:
        """
        s = time.time()
        needData = self.needData  #计算所需数据

        Vwap = needData[t.VWAP] 
        adjVwap = Vwap - Vwap.shift(5)
        Neta = needData[t.NETASSET]
        vol = needData[t.VOLUME]
        factor = - adjVwap * vol / Neta
        print('factor {0} done with {1} seconds'.format(self.factorName, time.time() - s))
        return factor

    def run_factor(self):
        self.run()



fct = Factor()
fct.run_factor()