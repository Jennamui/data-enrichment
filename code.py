#import packages
import pandas as pd
import tabulate

#load in data
patients = pd.read_csv('data/Hospital_Inpatient_Discharges__SPARCS_De-Identified___2015.csv')
neighborhood = pd.read_csv('data/NY_2015_ADI_9 Digit Zip Code_v3.1.csv')

list(patients)
list(neighborhood)

patients.columns = patients.columns.str.replace('[^A-Za-z0-9]+', '_')

df_patients_small = patients[['Zip_Code_3_digits','CCS_Diagnosis_Code','CCS_Diagnosis_Description','Total_Charges','Total_Costs']]
print(df_patients_small.sample(10).to_markdown())
list(df_patients_small)
df_patients_small.shape

df_neighborhood_small = [['ZIPID','ADI_NATRANK','ADI_STATERNK']]
print(df_neighborhood_small.sample(10).to_markdown())
list(df_neighborhood_small)
df_neighborhood_small.shape 
