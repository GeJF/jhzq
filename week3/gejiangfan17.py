#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# author: gejiangfan

import time
import math
import numpy as np
import pandas as pd
from FactorModule.FactorBase import FactorBase
from DataReaderModule.Constants import ALIAS_FIELDS as t

class Factor(FactorBase):

    def __init__(self):
        super(Factor,self).__init__()
        self.neutral = False
        self.factorName = __name__.split('.')[-1]
        self.needFields = [ t.CLOSE, t.OPEN,t.HIGH,t.LOW, t.VOLUME]  # 设置需要的字段

    def factor_definition(self):
        """
        收集派发指标
        :return:
        """
        s = time.time()
        needData = self.needData  #计算所需数据

        adjClose = needData[t.CLOSE]
        adjLow = needData[t.LOW]
        adjHigh = needData[t.HIGH]
        ret = (2*adjClose-adjHigh - adjLow) / (adjClose - adjLow)
        vol = needData[t.VOLUME] ** 0.5
        factor =  1/math.pi*np.arctan(self.calculator.Decaylinear(- (ret * vol),5))
        print('factor {0} done with {1} seconds'.format(self.factorName, time.time() - s))
        return factor

    def run_factor(self):
        self.run()



fct = Factor()
fct.run_factor()