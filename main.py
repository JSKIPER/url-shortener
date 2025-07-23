import sys
import random
import string
import threading
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtSql import QSqlTableModel
from ui_main import Ui_MainWindow
from connection import Data
from flask_server import FlaskServer

class URLShortenerApp(QMainWindow):
    def __init__(self):
        super(URLShortenerApp,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.conn = Data()
        self.conn.create_connection()
        self.view_data()
        self.ui.btn_delete.clicked.connect(self.deleteLink)
        self.ui.btn_generatelink.clicked.connect(self.generateLink)

    def view_data(self):
        self.model = QSqlTableModel(self)
        self.model.setTable('links')
        self.model.select()
        self.ui.tableView.setModel(self.model)

    def deleteLink(self):
        index = self.ui.tableView.selectedIndexes()[0]
        id = str(self.ui.tableView.model().data(index))
        self.conn.delete_link_query(id)
        self.view_data()

    def generate_short_url(self, length=6):
        chars = string.ascii_letters + string.digits
        short_link = ''.join(random.choice(chars) for _ in range(length))
        return short_link

    def generateLink(self):
        long_link = self.ui.line_for_link.text()
        short_link = self.generate_short_url()
        self.conn.add_new_link(short_link, long_link)
        self.view_data()
        self.ui.line_for_link.clear()


def run_flask():
    flask_app = FlaskServer()
    flask_app.run()





if __name__ == "__main__":
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()
    app = QApplication(sys.argv)
    window = URLShortenerApp()
    window.show()
    sys.exit(app.exec())