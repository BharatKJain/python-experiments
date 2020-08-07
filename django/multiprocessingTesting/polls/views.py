from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import pyodbc
from concurrent.futures import ProcessPoolExecutor

def check(query):
    try:
        server = 'tcp:pythonmultiprocessing.database.windows.net' 
        database = 'testingdatabaseforpython' 
        username = 'bharat-server' 
        password = 'Admin112358' 
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        cursor = cnxn.cursor()
        print("executing query")
        cursor.execute(query)
        cursor.commit()
        cnxn.close()
    except Exception as error:
        print(error)

def index(request):
    query="INSERT INTO accounts (id, username, password, email) VALUES (1, 'test', 'test', 'test@test.com')"
    with ProcessPoolExecutor(max_workers=5) as executor:
        for index in range(0,200):
            print("Executing")
            executor.submit(check,query)
    return HttpResponse("Hello, world. Inserted data")