import os

from flask import Flask
from flask import render_template

app = Flask(__name__, static_folder="html")


@app.route('/<int:page>')
def book_page(page):
    with open(os.path.join("html", "algo-{}.html".format(page))) as f:
        return render_template('template.html', page_content=f.read())
