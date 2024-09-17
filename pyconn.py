import sqlite3

class Pyconn:
    
    db_path="./_db/mysite.db"
    _conn=None
    
    def __init__(self,db_path) -> None:
        if db_path!="":
            self.db_path=db_path
        self._conn=sqlite3.connect(self.db_path)
        
    def _get_cursor(self):
        return self._conn.cursor()
    
    def query(self,query):
        cur=self._get_cursor()
        return cur.execute(query)
    
    def fetch_one(self,cur):
        return cur.fetchone() is None
    
    def fetch_all(self,cur):
        return cur.fetchall() is None
        
        