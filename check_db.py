import psycopg2

db_DATABASE = "d2a9hjf0j9oiik"
db_USER = "qxxuwbttvvdpcu"
db_PASSWORD = "37f22e5a6aecdfed7d7f126404a53726d58dbfacc765906e410b2a5edc39ca53"
db_HOST = "ec2-46-51-190-87.eu-west-1.compute.amazonaws.com"

conn = psycopg2.connect(database = db_DATABASE,
                        user = db_USER,
                        password = db_PASSWORD,
                        host = db_HOST,
                        port = "5432")
cur = conn.cursor()
cur.execute("SELECT _ip_, first_visit, last_visit from DB_IP_test")

try:
    txt = ''
    for i in cur.fetchall():
        txt += f'{i}\n'
    print(txt)
    conn.close()
    
except Exception as e:
    
    print('>>>>>GETSKEY<<<<<',e)