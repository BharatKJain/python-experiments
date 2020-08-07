from concurrent.futures import ProcessPoolExecutor
from time import perf_counter
import pyodbc
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


if __name__ == "__main__":
    server = 'tcp:pythonmultiprocessing.database.windows.net' 
    database = 'testingdatabaseforpython' 
    username = 'bharat-server' 
    password = 'Admin112358' 
    query="INSERT INTO accounts (id, username, password, email) VALUES (1, 'test', 'test', 'test@test.com')"
    # cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    # cursor = cnxn.cursor()
    # cursor.execute(query)
    # cursor.commit()
    # cnxn.close()
    # for row in cursor:
    #     print(row)
    print("Entering process pool executor")
    with ProcessPoolExecutor(max_workers=5) as executor:
        for index in range(0,200):
            print("Executing")
            executor.submit(check,query)