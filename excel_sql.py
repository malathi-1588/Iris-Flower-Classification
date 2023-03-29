import pymysql as pms
import pandas as pd
import xlrd
import sys

conn = pms.connect(host = 'localhost', port = 3306, user = 'root', password = 'Malathi5*', db = 'iris')
cursor = conn.cursor()

iris_table = "CREATE TABLE IF NOT EXISTS iris_data(SepalLength float, SepalWidth float, PetalLength float, PetalWidth float, Species varchar(100))"
cursor.execute(iris_table)

data = pd.read_csv(r"D:\College Files\Flask Codes\IRIS\Iris.csv")
import csv

with open(r"D:\College Files\Flask Codes\IRIS\Iris.csv", mode='r') as csv_file:
    #read csv using reader class
    csv_reader = csv.reader(csv_file)
    #skip header
    header = next(csv_reader)
    #Read csv row wise and insert into table
    for row in csv_reader:
        sql = "INSERT INTO iris_data (SepalLength, SepalWidth, PetalLength, PetalWidth, Species) VALUES (%s,%s,%s,%s,%s)"
        cursor.execute(sql, tuple(row))
        print("Record inserted")
 
conn.commit()
cursor.close()

    