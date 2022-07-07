#!/usr/bin/python3
import csv
import sys
from decimal import Decimal
sys.path.append('/root/kosmic/python-bindings/kosmic')
import kosmic

f=open("tsh.csv","r")
data=list(csv.reader(f))
#print(data)

final_data=()

for each_data in data[0:1000]:
  #print(each_data)
  final_data=final_data+(float(each_data[0]),) 
#  print(final_data)

result = kosmic.kosmic(final_data, decimals=1)
print(result)
# Estimated reference interval:
print (kosmic.percentile(result, 0.025))
print (kosmic.percentile(result, 0.975))
