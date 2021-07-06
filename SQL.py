import mysql.connector
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="weatherdb"
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE weatherdb")
#mycursor.execute("SHOW DATABASES")
#mycursor.execute("DROP DATABASE weatherdb")

#mycursor.execute("CREATE TABLE Forecast (Time datetime, Temperature DECIMAL(4,2), MinPercipitation DECIMAL(6,1), MeanPercipitation DECIMAL(6,1), MaxPercipitation DECIMAL(6,1), TypePercipitation CHAR(20), FrozenPercipitation TINYINT)")
mycursor.execute("CREATE TABLE Station (Time datetime, Temperature DECIMAL(4,2),Percipitation DECIMAL(5,2))")
#mycursor.execute("SHOW TABLES")
mycursor.execute("DESCRIBE Station")
#mycursor.execute("DROP TABLE Station")

#now = datetime.now()
#mycursor.execute("INSERT INTO Home (time, temperature) VALUES (%s,%s)", (now,20.1))
#mydb.commit()

#mycursor.execute("SELECT * FROM Home")

for x in mycursor:
  print(x)
  #time.append(x[0])
  #degC.append(x[1])
  
#plt.plot(time,degC)
#plt.show()