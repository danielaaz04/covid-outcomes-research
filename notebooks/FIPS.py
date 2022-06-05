a = 1001
b = 501
c = ""
d = 24052

#a = str(a).zfill(5)
#print(a)
#print(str(b).zfill(5))
#print(str(c).zfill(5))

import pandas as pd
data = {'Name':['Karan','Rohit','Sahil','Aryan'],'FIPS':[a,b,c,d]}
df = pd.DataFrame(data)
k=0
for i in df['FIPS']:
    #print(df['FIPS'].iloc[k])
    df['FIPS'].loc[k] = str(i).zfill(5)
    k += 1
print(df)