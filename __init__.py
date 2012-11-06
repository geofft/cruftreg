#!/usr/bin/env python

from flask import Flask, g

import index
import kauth

app = Flask(__name__)

app.add_url_rule("/", "index", index.index)
app.add_url_rule("/register", "register", register.register, methods=['GET', 'POST'])

if __name__ == "__main__":
    app.run()
