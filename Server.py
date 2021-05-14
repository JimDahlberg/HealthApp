import mysql.connector as mysql

class Server:
    def __init__(self):
        """Class establishes connection with the SQL-server. Requires Tunnel.py to be running."""

        MYSQL_USER =  '' #ACRONYM
        MYSQL_PASS =  '' #MYSQL_PASS
        MYSQL_DATABASE = MYSQL_USER #ACRONYM
        MYSQL_PORT = open("port.txt", "r")

        self._connection = mysql.connect(
            host='127.0.0.1', 
            user=MYSQL_USER,
            passwd=MYSQL_PASS, 
            db=MYSQL_DATABASE,
            port=MYSQL_PORT.read()
        )
        self._cnx = self._connection.cursor(dictionary=True, buffered=True)

    # def __del__(self):
    #     self._cnx.close()

    @property
    def cnx(self):
        return self._cnx.fetchall()

    def execute(self, str_to_sql):
        self._cnx.execute(str_to_sql)

    def fetchall(self):
        return self._cnx.fetchall()

    def commit(self):
        self._connection.commit()