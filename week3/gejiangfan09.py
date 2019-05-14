#!/usr/bin/env Python
#思路： -(X-X.shift(6))*Y/X.shift(6)
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
        self.needFields = [ t.CLOSE, t.VOLUME]  # 设置需要的字段

    def factor_definition(self):
        """
        收集派发指标
        :return:
        """
        s = time.time()
        needData = self.needData  #计算所需数据

        Close = needData[t.CLOSE] 
        adjClose = Close - Close.shift(5)
        vol = needData[t.VOLUME]
        factor = - adjClose * vol / Close.shift(5)
        print('factor {0} done with {1} seconds'.format(self.factorName, time.time() - s))
        return factor

    def run_factor(self):
        self.run()



fct = Factor()
fct.run_factor()