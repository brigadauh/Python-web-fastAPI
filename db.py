import pymysql

mysqlConfig = {
  'user': 'sapi_admin',
  'password': '',
  'host': '192.168.1.3',
  'database': 'sapi'
  #'raise_on_warnings': False ,
  #'pool_name': 'sapi_pool',
  #'pool_size':5
}
def pyTest():
  conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='mysql')
  cur = conn.cursor()
  cur.execute("SELECT Host,User FROM user")
  print(cur.description)
  print()
  for row in cur:
    print(row)

  cur.close()
  conn.close()


def open():
    ##subsequent calls to this will return connections from the same pool
    #cnx = mysql.connector.connect(**mysqlConfig)
    #cnx = pymysql.connect(**mysqlConfig)
    cnx = pymysql.connect(host='192.168.1.3', port=3306, user='sapi_admin', passwd='123456', db='sapi')
    return cnx
def close(cnx):
    cnx.close()