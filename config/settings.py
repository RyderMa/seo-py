import os

mysql_url = os.getenv('mysqlUrl')
port = int(os.getenv('port')) or 8001
