from PySide6 import QtWidgets, QtSql

class Data:
    def __init__(self):
        super(Data, self).__init__()

    def create_connection(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('links_db.db')
        if not db.open():
            QtWidgets.QMessageBox.critical(None, 'Database Error', 'Database Error', QtWidgets.QMessageBox.Cancel)
            return False

        query = QtSql.QSqlQuery()
        query.exec("CREATE TABLE IF NOT EXISTS links (ID integer primary key  AUTOINCREMENT, LongLink  VARCHAR(255), ShortLink  VARCHAR(255))")
        return True

    def execute_query_with_params(self, sql_query, query_values=None):
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)
        if query_values is not None:
            for query_value in query_values:
                query.addBindValue(query_value)
        query.exec()
        return query

    def add_new_link(self, shortlink,longlink):
        sql_query = "INSERT INTO links (LongLink, ShortLink) VALUES (?, ?)"
        self.execute_query_with_params(sql_query, [longlink, shortlink])

    def delete_link_query(self, id):
        sql_query = "DELETE FROM links WHERE ID = ?"
        self.execute_query_with_params(sql_query, [id])

    def get_longlink_query(self, shortlink):
        sql_query = "SELECT LongLink FROM links WHERE ShortLink = ?"
        query = self.execute_query_with_params(sql_query, [shortlink])
        if query.next():
            return query.value(0)
        return None



