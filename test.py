import os
import numpy
from datetime import datetime
import matplotlib.pyplot as plt

#os.system('python --version')
dateStr1 = "2021-07-05T10:00:00Z"
#dateStr = "2021-07-05 10:00:00"
dateStr = dateStr1[:10] + ' ' + dateStr1[11:19] 
#date_time_obj = datetime.strptime(dateStr, '%Y-%m-%d %H:%M:%S')
print(dateStr)
#print(type(date_time_obj))
#print(date_time_obj)