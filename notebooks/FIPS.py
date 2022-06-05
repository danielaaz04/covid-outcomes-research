a = 1001
b = 10501
c = ""
d = 24052

a = str(a).zfill(5)
print(a)
#print(str(b).zfill(5))
#print(str(c).zfill(5))

import pandas as pd
data = {'Name':['Karan','Rohit','Sahil','Aryan'],'FIPS':[a,b,c,d]}
df = pd.DataFrame(data)
for i in df['FIPS']:
	df['FIPS'].loc[i] = str(i).zfill(5)
print(df)