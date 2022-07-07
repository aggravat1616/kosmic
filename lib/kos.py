#!/usr/bin/python3
import csv
import sys
sys.path.append('/root/kosmic/python-bindings/kosmic')
import kosmic

datafile=input("Give name of file . If in different folder, give full path:")
f=open(datafile,"r")
data=list(csv.reader(f))
#print(data)

final_data=()

#for each_data in data[0:1000]:
for each_data in data:
  final_data=final_data+(round(float(each_data[0]),1),)

print(final_data)

result = kosmic.kosmic(final_data, decimals=1)
print(result)
# Estimated reference interval:
print ("Lower reference limit(2.5% cut-off):{}".format(kosmic.percentile(result, 0.025)))
print ("Upper reference limit(97.5% cut-off):{}".format(kosmic.percentile(result, 0.975)))
