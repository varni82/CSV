import csv
import mysql.connector

mydb=mysql.connector.connect(host='localhost',user='root',password='',database='credit')
print("database connected")

cursor=mydb.cursor()
csv_data=csv.reader(open('D:/Grootan_Csv/credit_card.csv'))
for row in csv_data:
    cursor.execute('INSERT INTO creditlist(Card_Code,Type,Issue,Card_Number,CardHolder_Name,Cvv,Issue_Date,Expiry_Date,Billing_Date,Card_PIN,Credit_Limit,Account_Password) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',row)
    print(row)

mydb.commit()
cursor.close()
print("Done")
