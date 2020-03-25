# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 10:18:54 2019

@author: Michelle Pressly
Copyright: Michelle Pressly 2019
"""

import math as m
import numpy as np
import scipy as sp
import pandas as pd
#import seaborn as sns
from matplotlib import pyplot as plt


Cat={'CMQCC High','CMQCC Med','CMQCC Low','CMQCC Category','CMQCC Recommendation'}
CMQCC=pd.DataFrame(columns =Cat)
MAP=pd.DataFrame()

#High Criteria 
CMQCC_high=np.zeros([6, 1])
print('')
print('High-Risk Checks: ')
CMQCC_high[0]=input('1: Placenta previa or low lying placenta (1: yes, 0: no, 0: unsure): ')
PREV01=CMQCC_high[0]
CMQCC_high[1]=input('2: Suspected placenta accreta/percreta (1: yes, 0: no, 0: unsure): ')
CRET01=CMQCC_high[1]
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
PCES01=float(CMQCC_med[0])
CMQCC_med[1]=input('2: Multiple gestation (1: yes, 0: no, 0: unsure): ')
MGEST01=float(CMQCC_med[1])
CMQCC_med[2]=input('3: > 4 previous vaginal deliveries (1: yes, 0: no, 0: unsure): ')
PAR401=float(CMQCC_med[3])
CMQCC_med[3]=input('4: Suspected or known chorioamnionitis (1: yes, 0: no, 0: unsure): ')
CHOR01=float(CMQCC_med[3])
CMQCC_med[4]=input('5: History of peripartum hemorrhage (1: yes, 0: no, 0: unsure): ')
CMQCC_med[5]=input('6: Large uterine leiomyoma (1: yes, 0: no, 0: unsure): ')
LEIO01=float(CMQCC_med[5])
CMQCC_med[6]=input('7: Macrosomia - estimated feal weight > 4 kg (1: yes, 0: no, 0: unsure): ')            
MACR01=float(CMQCC_med[6])
CMQCC_med[7]=input('8: Morbid Obesity - BMI greater than 35 kg/m^2 (1: yes, 0: no, 0: unsure): ')
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
    CMQCC['CMQCC Category'] = 'Low, All Checks'
    CMQCC['CMQCC Recommendation'] = 'No Prenatal Prestransfusion Testing Required'
else:
    CMQCC['CMQCC Category'] = 'Low'
    CMQCC['CMQCC Recommendation'] = 'No Prenatal Prestransfusion Testing Required'    
 
print('')
print('Additional Antepartum Checks: ')
print('Transfusion:')
SMOKE01=float(input('MAP1: Smoking - Maternal smoking history (1: yes, 0: no, 0: unsure): '))
CAUC01=float(input('MAP2: Caucasian race (1: yes, 0: no, 0: unsure): '))
ARR01=float(input('MAP3: Arrythmia (1: yes, 0: no, 0: unsure): '))            
AGE40=float(input('MAP4: Maternal age > 40 (1: yes, 0: no, 0: unsure): '))                        
DIAB01=float(input('MAP5: Any form of diabetes (1: yes, 0: no, 0: unsure): '))            
DEP01=float(input('MAP6: Clinical depression (1: yes, 0: no, 0: unsure): '))            
ENDO01=float(input('MAP7: Endometriosis (1: yes, 0: no, 0: unsure): '))       
HF01=float(input('MAP8: Heart failure (1: yes, 0: no, 0: unsure): '))       
HD01=float(input('MAP9: Heart disease (1: yes, 0: no, 0: unsure): '))       
HYP01=float(input('MAP10: Hypertension (1: yes, 0: no, 0: unsure): '))       
LUP01=float(input('MAP11: Lupus (1: yes, 0: no, 0: unsure): '))       
MINFERT01=float(input('MAP12: Maternal infertility (1: yes, 0: no, 0: unsure): '))       
PLAC01=float(input('MAP13: Placental abruption (1: yes, 0: no, 0: unsure): '))       
POLY01=float(input('MAP14: Polyhydramnios (1: yes, 0: no, 0: unsure): '))       
PREC01=float(input('MAP15: Preeclampsia (1: yes, 0: no, 0: unsure): '))             
RENF01=float(input('MAP16: Renal failure (1: yes, 0: no, 0: unsure): '))       
RENINS01=float(input('MAP17: Renal insufficiency (1: yes, 0: no, 0: unsure): '))       
RENALA01=float(input('MAP18: Renal abnormality (1: yes, 0: no, 0: unsure): '))       
UTI01=float(input('MAP19: Urinary tract infection (1: yes, 0: no, 0: unsure): '))       
SICKL01=float(input('MAP20: Sickle cell trait (1: yes, 0: no, 0: unsure): '))
print('Hemorrhage:')                         
CERC01=float(input('MAP21: Cervical cerclage (1: yes, 0: no, 0: unsure): '))
ASTH01=float(input('MAP22: Asthma (1: yes, 0: no, 0: unsure): '))

if PAR401==1:
    FIRSTDEL01=0.0
else:
    FIRSTDEL01=float(input('MAP23: First delivery (1: yes, 0: no, 0: unsure): '))                  
      
Ante_h_coef= -3.1603 + AGE40*0.3511 + ARR01*0.6196 + ASTH01*0.1999 + CERC01*0.1836 + CRET01*2.1030 + DIAB01*0.1620 + ENDO01*1.1456 + HF01*1.6663 + HD01*0.0601 + HYP01*0.4057 + MGEST01*0.8440 + PAR401*0.4142 + PCES01*0.0443 + PLAC01*0.9229 + POLY01*0.5494 + PREC01*0.6010 + PREV01*1.9011 + RENF01*1.2820 + SICKL01*0.1667 + RENALA01*0.3970 + MINFERT01*0.0623 + FIRSTDEL01*0.0985
P_Ante_hem=1/(1 + np.exp(-Ante_h_coef))
 
Ante_t_coef= -4.6539 + AGE40*0.4059 + ARR01*1.1942 - CAUC01*0.7825 + CRET01*1.8715 + DIAB01*0.2520 + DEP01*0.2533 + ENDO01*1.6078 + HF01*2.8316 + HD01*0.8696 + HYP01*0.5883 + LUP01*0.9537 + MGEST01*0.8752 + MINFERT01*0.6413 + PAR401*0.3655 + PCES01*0.5721 + PLAC01*1.7958 + POLY01*0.7421 + PREC01*0.7474 + PREV01*2.8248 + RENF01*2.0824 + RENINS01*1.1250 + SICKL01*0.7939 + RENALA01*0.4343 - SMOKE01*0.1454 + UTI01*0.9345   
P_Ante_trans=1/(1 + np.exp(-Ante_t_coef))

if P_Ante_hem>0.287:
    MAP_hem_cat='Hem: High ' #+ str(round(P_Ante_hem[0],4))
elif P_Ante_hem>0.05:
    MAP_hem_cat='Hem: Medium ' #+ str(round(P_Ante_hem[0],4))
else:
    MAP_hem_cat='Hem: Low ' #+ str(round(P_Ante_hem[0],4))

if P_Ante_trans>0.202:
    MAP_trans_cat='Trans: High ' #+ str(round(P_Ante_trans[0],4))
elif P_Ante_trans>0.03:
    MAP_trans_cat='Trans: Medium '# + str(round(P_Ante_trans[0],4))
else:
    MAP_trans_cat='Trans: Low ' #+ str(round(P_Ante_trans[0],4))

CMQCC
#CMQCCplot=CMQCC.transpose()
Scores={"Score":[float(sum(CMQCC_low[0:5])/5),float(sum(CMQCC_med[0:8])/8),float(sum(CMQCC_high[0:6])/6),P_Ante_hem[0],P_Ante_trans[0]]}
Score_Index= ["Low","Medium","High","Hem","Trans"];
plot_CMQCC=pd.DataFrame(data=Scores,index=Score_Index)
plot_CMQCC.plot(rot=0,legend=None,kind='bar');
plt.text(0.1, 1.08, str('CMQCC:'), transform=plt.gca().transAxes, fontsize=18)
plt.text(0.1, 1.02, str(CMQCC['CMQCC Category'].iloc[0]), transform=plt.gca().transAxes, fontsize=18)
plt.text(0.45, 1.08, str('MAP Risk Categories:'), transform=plt.gca().transAxes, fontsize=18)
plt.text(0.45, 1.02, str(MAP_hem_cat) + '  ' + str(MAP_trans_cat), transform=plt.gca().transAxes, fontsize=18)
plt.text(2.75,P_Ante_hem[0]+0.01,  str(round(P_Ante_hem[0],4)))
plt.text(2.75,P_Ante_hem[0]+0.05,  str(round((P_Ante_hem[0]*100),1))+'%', fontsize=14)
plt.text(3.75,P_Ante_trans[0]+0.01,  str(round(P_Ante_trans[0],4)))
plt.text(3.75,P_Ante_trans[0]+0.05,  str(round((P_Ante_trans[0]*100),1))+'%', fontsize=14)
plt.ylabel('Fraction of Indications in Risk Category', fontsize=18)
plt.rc('ytick',labelsize=18)
plt.rc('xtick',labelsize=16)
plt.axis([-.5,4.5,0,1.1])
#plt.rc('legend',fontsize=18)
#plt.legend.set_visible(False)
plt.show(block=True); 


print('')
print('Peripartum Additions:')                         
CES01=float(input('PERI1: Cesarian section (1: yes, 0: no, 0: unsure): '))
SICKLCR01=float(input('PERI2: Sickle cell crisis (1: yes, 0: no, 0: unsure): '))
RDIS01=float(input('PERI3: Respiratory distress (1: yes, 0: no, 0: unsure): '))
PRE01=float(input('PERI4: Preterm Labor (1: yes, 0: no, 0: unsure): '))
PROL01=float(input('PERI5: Prolonged labor (1: yes, 0: no, 0: unsure): '))

Peri_h_coef= -3.1746 + CES01*0.2309 + SICKLCR01*2.9207 + RDIS01*2.1455 + AGE40*0.3353 + ARR01*0.5598 + CRET01*2.1364 + DIAB01*0.1496 + ENDO01*1.1395 + HF01*1.3378 - HD01*0.0696 + HYP01*0.4054 + LUP01*0.2516 + MGEST01*0.7902 + PAR401*0.4235 - PCES01*0.0626 + PLAC01*0.9057 + POLY01*0.5464 + PREC01*0.5904 + PREV01*1.7961 + RENF01*1.1439 + SICKL01*0.2245 + ASTH01*0.1797 + RENALA01*0.2710 + CERC01*0.1502 + MINFERT01*0.0232 + FIRSTDEL01*0.06899
P_Peri_hem=1/(1 + np.exp(-Peri_h_coef))
 
Peri_t_coef= -4.7460 + CES01*0.6601 + SICKLCR01*4.1838 + RDIS01*2.8958 + PRE01*0.2446 + PROL01*0.3382 + AGE40*0.3848 + ARR01*1.0910 - CAUC01*0.9574 + CRET01*1.8715 + DIAB01*0.2271 + DEP01*0.3339 + ENDO01*1.6325 + HF01*2.2475 + HD01*0.5755 + HYP01*0.5521 + LUP01*1.0643 + MGEST01*0.6645 + MINFERT01*0.5750 + PAR401*0.3670 + PCES01*0.3826 + PLAC01*1.6409 + POLY01*0.7333 + PREC01*0.6578 + PREV01*2.4739 + RENF01*1.9658 + RENINS01*1.0121 + SICKL01*0.8921 + RENALA01*0.09861 - SMOKE01*0.1085 + UTI01*0.9807   
P_Peri_trans=1/(1 + np.exp(-Peri_t_coef))

if P_Peri_hem>0.350:
    MAP_hem_peri_cat='Hem: High ' #+ str(round(P_Ante_hem[0],4))
elif P_Peri_hem>0.05:
    MAP_hem_peri_cat='Hem: Medium ' #+ str(round(P_Ante_hem[0],4))
else:
    MAP_hem_peri_cat='Hem: Low ' #+ str(round(P_Ante_hem[0],4))

if P_Peri_trans>0.224:
    MAP_trans_peri_cat='Trans: High ' #+ str(round(P_Ante_trans[0],4))
elif P_Peri_trans>0.03:
    MAP_trans_peri_cat='Trans: Medium '# + str(round(P_Ante_trans[0],4))
else:
    MAP_trans_peri_cat='Trans: Low ' #+ str(round(P_Ante_trans[0],4))


Scores_peri={"Score":[float(sum(CMQCC_low[0:5])/5),float(sum(CMQCC_med[0:8])/8),float(sum(CMQCC_high[0:6])/6),P_Peri_hem[0],P_Peri_trans[0]]}
Score_peri_Index= ["Low","Medium","High","Hem","Trans"];
plot_CMQCC_peri=pd.DataFrame(data=Scores_peri,index=Score_peri_Index)
plot_CMQCC_peri.plot(rot=0,legend=None,kind='bar');
plt.text(0.1, 1.08, str('CMQCC:'), transform=plt.gca().transAxes, fontsize=18)
plt.text(0.1, 1.02, str(CMQCC['CMQCC Category'].iloc[0]), transform=plt.gca().transAxes, fontsize=18)
plt.text(0.45, 1.08, str('MAP Risk Categories:'), transform=plt.gca().transAxes, fontsize=18)
plt.text(0.45, 1.02, str(MAP_hem_peri_cat) + '  ' + str(MAP_trans_peri_cat), transform=plt.gca().transAxes, fontsize=18)
plt.text(2.75,P_Peri_hem[0]+0.01,  str(round(P_Peri_hem[0],4)))
plt.text(2.75,P_Peri_hem[0]+0.05,  str(round((P_Peri_hem[0]*100),1))+'%', fontsize=14)
plt.text(3.75,P_Peri_trans[0]+0.01,  str(round(P_Peri_trans[0],4)))
plt.text(3.75,P_Peri_trans[0]+0.05,  str(round((P_Peri_trans[0]*100),1))+'%', fontsize=14)
plt.ylabel('Fraction of Indications in Risk Category', fontsize=18)
plt.rc('ytick',labelsize=18)
plt.rc('xtick',labelsize=16)
plt.axis([-.5,4.5,0,1.1])
#plt.rc('legend',fontsize=18)
#plt.legend.set_visible(False)
plt.show(block=True); 



print('')
print('Postpartum Checks (updating):')                         
FD01=float(input('POST1: Fetal death (1: yes, 0: no, 0: unsure): '))
VENT01=float(input('POST2: Ventalation needed (1: yes, 0: no, 0: unsure): '))
CHOR01=float(input('POST3: Chorioamnionitis (1: yes, 0: no, 0: unsure): '))
MACR01=float(input('POST4: Macrosomia (1: yes, 0: no, 0: unsure): '))
DYST01=float(input('POST5: Shoulder dystocia (1: yes, 0: no, 0: unsure): '))
GENANEST01=float(input('POST6: General anesthesia (1: yes, 0: no, 0: unsure): '))
GENANEST2014_01=1 # assuming delivery is occuring after 2014
UR01=float(input('POST7: Uterine rupture (1: yes, 0: no, 0: unsure): '))
VLAC01=float(input('POST8: Vaginal Laceration (1: yes, 0: no, 0: unsure): '))
APGAR1=float(input('POST9: APGAR score at 1 minute after delivery (1: yes, 0: no, 0: unsure): '))
APGAR5=float(input('POST10: APGAR score at 5 minutes after delivery (1: yes, 0: no, 0: unsure): '))
FORC01=float(input('POST11: Forceps used (1: yes, 0: no, 0: unsure): '))
UMBPROLPS01=float(input('POST12: Umbilical prolapse (1: yes, 0: no, 0: unsure): '))
NUCH01=float(input('POST13: Nuchal cord (1: yes, 0: no, 0: unsure): '))


Post_h_coef= -3.02985 + FD01*0.43808 + VENT01*0.84586 + CHOR01*65797 + MACR01*0.38285 - DYST01*0.75882 - NUCH01*0.10911 + GENANEST01*1.37334 - GENANEST2014_01*0.25946 + UR01*1.41467 - VLAC01*0.12942 - APGAR1*0.01337 + CES01*0.03101 + SICKLCR01*2.92559 + RDIS01*1.45473 + AGE40*0.33424 + ARR01*0.58037 + CRET01*2.08379 + DIAB01*0.14156 + ENDO01*0.97174 + HF01*1.17893 - HD01*0.05113 + HYP01*0.39009 + LUP01*0.27232 + MGEST01*0.77894 + PAR401*0.38961 - PCES01*0.04310 + PLAC01*0.79849 + POLY01*0.44380 + PREC01*0.59339 + PREV01*1.79582 + RENF01*0.94382 + SICKL01*0.17190 + ASTH01*0.17586 + RENALA01*0.24827 + CERC01*0.18180 + MINFERT01*0.03672 + FIRSTDEL01*0.07478
P_Post_hem=1/(1 + np.exp(-Post_h_coef))
 
Post_t_coef= -4.44838 + FD01*1.38366 + FORC01*0.83971 + UMBPROLPS01*0.05890 + VENT01*1.40721 + CHOR01*1.13413 - NUCH01*0.37081 + GENANEST01*1.36420 + GENANEST2014_01*0.22678 + UR01*2.35799 - VLAC01*0.76758 - APGAR1*0.10669 + APGAR5*0.02950 + CES01*0.46474 + SICKLCR01*3.96529 + RDIS01*1.74196 - PRE01*0.07449 + PROL01*0.16787 + AGE40*0.34876 + ARR01*1.15955 - CAUC01*0.55088 + CRET01*1.86736 + DIAB01*0.20394 + DEP01*0.17366 + ENDO01*1.19943 + HF01*2.12654 + HD01*0.67161 + HYP01*0.47624 + LUP01*1.16271 + MGEST01*0.60166 + MINFERT01*0.68830 + PAR401*0.36252 + PCES01*0.33535 + PLAC01*1.34198 + POLY01*0.44641 + PREC01*0.67364 + PREV01*2.40411 + RENF01*1.53724 + RENINS01*0.74476 + SICKL01*0.69743 + RENALA01*0.14280 - SMOKE01*0.12492 + UTI01*0.74954   
P_Post_trans=1/(1 + np.exp(-Post_t_coef))

if P_Post_hem>0.385:
    MAP_hem_post_cat='Hem: High ' #+ str(round(P_Ante_hem[0],4))
elif P_Post_hem>0.05:
    MAP_hem_post_cat='Hem: Medium ' #+ str(round(P_Ante_hem[0],4))
else:
    MAP_hem_post_cat='Hem: Low ' #+ str(round(P_Ante_hem[0],4))

if P_Post_trans>0.306:
    MAP_trans_post_cat='Trans: High ' #+ str(round(P_Ante_trans[0],4))
elif P_Post_trans>0.03:
    MAP_trans_post_cat='Trans: Medium '# + str(round(P_Ante_trans[0],4))
else:
    MAP_trans_post_cat='Trans: Low ' #+ str(round(P_Ante_trans[0],4))


Scores_post={"Score":[float(sum(CMQCC_low[0:5])/5),float(sum(CMQCC_med[0:8])/8),float(sum(CMQCC_high[0:6])/6),P_Post_hem[0],P_Post_trans[0]]}
Score_post_Index= ["Low","Medium","High","Hem","Trans"];
plot_CMQCC_post=pd.DataFrame(data=Scores_post,index=Score_post_Index)
plot_CMQCC_post.plot(rot=0,legend=None,kind='bar');
plt.text(0.1, 1.08, str('CMQCC:'), transform=plt.gca().transAxes, fontsize=18)
plt.text(0.1, 1.02, str(CMQCC['CMQCC Category'].iloc[0]), transform=plt.gca().transAxes, fontsize=18)
plt.text(0.45, 1.08, str('MAP Risk Categories:'), transform=plt.gca().transAxes, fontsize=18)
plt.text(0.45, 1.02, str(MAP_hem_post_cat) + '  ' + str(MAP_trans_post_cat), transform=plt.gca().transAxes, fontsize=18)
plt.text(2.75,P_Post_hem[0]+0.01,  str(round(P_Post_hem[0],4)))
plt.text(2.75,P_Post_hem[0]+0.05,  str(round((P_Post_hem[0]*100),1))+'%', fontsize=14)
plt.text(3.75,P_Post_trans[0]+0.01,  str(round(P_Post_trans[0],4)))
plt.text(3.75,P_Post_trans[0]+0.05,  str(round((P_Post_trans[0]*100),1))+'%', fontsize=14)
plt.ylabel('Fraction of Indications in Risk Category', fontsize=18)
plt.rc('ytick',labelsize=18)
plt.rc('xtick',labelsize=16)
plt.axis([-.5,4.5,0,1.1])
#plt.rc('legend',fontsize=18)
#plt.legend.set_visible(False)
plt.show(block=True); 