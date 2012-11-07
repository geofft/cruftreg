#!/usr/bin/env python

from flask import Flask

import index
import password

app = Flask(__name__)

app.add_url_rule("/", "index", index.index)
app.add_url_rule("/password", "password", password.password, methods=['GET', 'POST'])

if __name__ == "__main__":
    app.debug = True
    app.run()
