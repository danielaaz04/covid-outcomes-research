import pandas as pd
import datetime

#read csv file
df = pd.read_csv('C:/Users/chris/Desktop/covidintervention/intervention.csv', sep = ',', header =0)

#fill null and create second dataframe
df=df.fillna(1)
df2=df.copy()

#drop non date columns
df2.drop(columns=['STATE','AREA_NAME'], inplace = True)


dfnew =df.copy()
#print(df.loc[:,['FIPS','STATE','AREA_NAME']])

#Loop each cell
for column in df2:
    for i in range(len(df2)):

        test=df2[column][i]
        date = datetime.date.fromordinal(int(test))
        df2.at[i,column]=date
#combine first by columns
dfnew = df.loc[:,['FIPS','STATE','AREA_NAME']].combine_first(df2)
#print(dfnew)

#write to csv
dfnew.to_csv('C:/Users/chris/Desktop/covidintervention/interventionDates.csv')