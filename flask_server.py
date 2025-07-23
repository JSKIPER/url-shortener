from flask import Flask, redirect
import sqlite3

class FlaskServer:
    def __init__(self):
        self.app = Flask(__name__)
        self.setup_routes()

    def setup_routes(self):
        @self.app.route('/<short_code>')
        def redirect_short_url(short_code):
            conn = sqlite3.connect("links_db.db")
            cursor = conn.cursor()
            cursor.execute("SELECT LongLink FROM links WHERE ShortLink = ?", (short_code,))
            row = cursor.fetchone()
            if row:
                return redirect(row[0])
            else:
                return "Shortened URL not found", 404

    def run(self):
        self.app.run(port=5000, debug=False)
