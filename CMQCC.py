# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 10:18:54 2019

@author: Michelle Pressly
"""

import math as m
import numpy as np
import scipy as sp
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


Cat={'CMQCC High','CMQCC Med','CMQCC Low','CMQCC Category','CMQCC Recommendation'}
CMQCC=pd.DataFrame(columns =Cat)
MAP=pd.DataFrame()

#High Criteria 
CMQCC_high=np.zeros([6, 1])
print('')
print('High-Risk Checks: ')
CMQCC_high[0]=input('1: Placenta previa or low lying placenta (1: yes, 0: no, 0: unsure): ')
CMQCC_high[1]=input('2: Suspected placenta accreta/percreta (1: yes, 0: no, 0: unsure): ')
CMQCC_high[2]=input('3: Hematocrit < 30 (1: yes, 0: no, 0: unsure): ')
CMQCC_high[3]=input('4: Active bleeding (greater than show) on admission (1: yes, 0: no, 0: unsure): ')
CMQCC_high[4]=input('5: Platelet count less than 100,000 (1: yes, 0: no, 0: unsure): ')
CMQCC_high[5]=input('6: Known coagulopathy (1: yes, 0: no, 0: unsure): ')

CMQCC['CMQCC High'] = sum(CMQCC_high[0:5])

#Medium Criteria 
CMQCC_med=np.zeros([8, 1])
print('')
print('Medium-Risk Checks: ')
CMQCC_med[0]=input('1: Previous cesarean delivery or uterine surgery (1: yes, 0: no, 0: unsure): ')
CMQCC_med[1]=input('2: Multiple gestation (1: yes, 0: no, 0: unsure): ')
CMQCC_med[2]=input('3: > 4 previous vaginal deliveries (1: yes, 0: no, 0: unsure): ')
CMQCC_med[3]=input('4: Chorioamnionitis (1: yes, 0: no, 0: unsure): ')
CMQCC_med[4]=input('5: History of peripartum hemorrhage (1: yes, 0: no, 0: unsure): ')
CMQCC_med[5]=input('6: Large uterine leiomyoma (1: yes, 0: no, 0: unsure): ')
CMQCC_med[6]=input('7: Macrosomia - estimated feal weight > 4 kg (1: yes, 0: no, 0: unsure): ')            
CMQCC_med[7]=input('8: Morbid Obesity - BMI greater than 35 kg/m^2 ( (1: yes, 0: no, 0: unsure): ')

CMQCC['CMQCC Med'] = sum(CMQCC_med[0:7])

#Low Criteria 
CMQCC_low=np.zeros([5, 1])

if CMQCC_med[0]==0:
    CMQCC_low[0]=1
else:
    CMQCC_low[0]=0
    
if CMQCC_med[1]==0:
    CMQCC_low[1]=1
else:
    CMQCC_low[1]=0    

if CMQCC_med[2]==0:
    CMQCC_low[2]=1
else:
    CMQCC_low[2]=0

if CMQCC_high[5]==0:
    CMQCC_low[3]=1
else:
    CMQCC_low[3]=0

if CMQCC_med[4]==0:
    CMQCC_low[4]=1
else:
    CMQCC_low[4]=0
 
CMQCC['CMQCC Low'] = sum(CMQCC_low[0:4])

if sum(CMQCC_high[0:5]) >0: 
    CMQCC['CMQCC Category'] = 'High'
    CMQCC['CMQCC Recommendation'] = '2 Units RBC Cross-Matched'
elif sum(CMQCC_med[0:7]) >0:
    CMQCC['CMQCC Category'] = 'Medium'
    CMQCC['CMQCC Recommendation'] = 'Prenatal Type & Screen Performed, No RBC Units Cross-Matched'
elif sum(CMQCC_low[0:4]) == 5:
    CMQCC['CMQCC Category'] = 'Low, All Checks Indicate Low Risk'
    CMQCC['CMQCC Recommendation'] = 'No Prenatal Prestransfusion Testing Required'
else:
    CMQCC['CMQCC Category'] = 'Low'
    CMQCC['CMQCC Recommendation'] = 'No Prenatal Prestransfusion Testing Required'    
 
#CMQCC=CMQCC.transpose()
CMQCC_Scores={"Score":[float(sum(CMQCC_low[0:4])/5),float(sum(CMQCC_med[0:7])/8),float(sum(CMQCC_high[0:5])/6)]}
Score_Index= ["Low","Medium","High"];
plot_CMQCC=pd.DataFrame(data=CMQCC_Scores,index=Score_Index)
plot_CMQCC.plot.bar();
plt.text(1,
  0.5,
  str(CMQCC['CMQCC Category'].iloc[0]).format(d),
  transform=plt.gca().transAxes)
plot.show(block=True);

