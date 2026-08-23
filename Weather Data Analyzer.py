import numpy as np
city=(["Kathmandu","Pokhara","Chitwan"])
months=(["Jan","Feb","March"])

temptatures=np.array([[10,12,16],[12,14,18],[18,21,25]])
overall_mean=np.mean(temptatures)
print("The overall mean is\n",overall_mean)

city_avg=np.average(temptatures,axis=1)
print("The city avg is\n" ,city_avg)

monthly_avg=np.average(temptatures,axis=0)
print("The monthly avg is\n",monthly_avg)

max_temp=np.argmax(city_avg)
print("The maximum temprature is",max_temp)
print("The city with maximun temptature is\n",city[max_temp])

collest_temp=np.argmin(city_avg)
print("The collest temprature is",collest_temp)
print("The city with collest temprature is\n",city[collest_temp])

hottest_month=np.argmax(monthly_avg)
print("The month with hotest temprature is\n",months[hottest_month])

collest_month=np.argmin(monthly_avg)
print("The moth with collest temprature is\n",months[collest_month])

city_maxtemp=np.max(temptatures,axis=1)
city_min=np.min(temptatures,axis=0)

diff=np.argmax(city_maxtemp-city_min)
print("Largest variation city\n",city[diff])

boolean=np.where(temptatures>0)

rows,col=np.where(temptatures>0)
print("Temprature above 20")
for r, c in zip(rows,col):
     print(f"City: {city[r]} | Month: {months[c]} | Temp: {temptatures[r, c]}°C")

temp_dillf=np.diff(temptatures,axis=1)
print("Month to Month temprature difference is: ")
print(temptatures)
