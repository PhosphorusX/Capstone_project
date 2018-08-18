#msg = "hello world"
#print(msg)

import csv

#with open('~/Desktop/SpringBoard_Project_CharlesDam_Aug2018/diabetic_data.csv', newline='') as csvfile:
 
#df_import = csv.reader(open('diabetic_data.csv','r'))
#for row in df_import:
#    print(row)

import pandas as pd
import numpy as np
from pandas import DataFrame as df
from scipy.stats import trim_mean, kurtosis
from scipy.stats.mstats import mode, gmean, hmean

df = pd.read_csv('diabetic_data.csv')
#print(df)
list(df.columns.values)
print(list(df))


df1 = df[['race', 'gender', 'age', 'weight', 'time_in_hospital', 'payer_code', 'medical_specialty', 'num_lab_procedures',
#omitted: 'encounter_id', 'admission_type_id', 'discharge_disposition_id','admission_source_id', 'patient_nbr',
'num_procedures', 'num_medications', 'number_outpatient', 'number_emergency', 'number_inpatient', 'diag_1', 'diag_2', 'diag_3', 
'number_diagnoses', 'max_glu_serum', 'A1Cresult', 'metformin', 'repaglinide', 'nateglinide', 'chlorpropamide', 'glimepiride', 
'acetohexamide', 'glipizide', 'glyburide', 'tolbutamide', 'pioglitazone', 'rosiglitazone', 'acarbose', 'miglitol', 'troglitazone', 
'tolazamide', 'examide', 'citoglipton', 'insulin', 'glyburide-metformin', 'glipizide-metformin', 'glimepiride-pioglitazone', 
'metformin-rosiglitazone', 'metformin-pioglitazone', 'change', 'diabetesMed', 'readmitted']] 

data = df1.describe(include ='all')

print(data)

data.to_csv('DiabetiesSummaryStats.tsv', sep='\t', encoding='utf-8')

import matplotlib.pyplot as plt

corrmat = plt.matshow(data.corr())

corrmat.show()


#labels, levels = pd.factorize(df.Race)

#data.Race = labels

