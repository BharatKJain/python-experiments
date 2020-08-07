from pg import DB
from unittest.mock import Mock,patch

databaseObject=Mock()

if __name__ == "__main__":
    # databaseObject = DB(dbname= self.databaseName, host= self.hostUrl, port= self.portNumber, user=self.username, passwd=self.password)
    reponse = databaseObject.query("SELECT * FROM weather")