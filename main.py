# Ioana A Mititean
# 1/11/22
# UWPCE Course 3 - Internet Programming in Python
# Lesson 08 - Web Security and Class-Based Views

"""
Code for a simple class message board application.

This app allows the user to input a text message, which will then be displayed on that page.
"""

import os
import html

from flask import Flask, request

from model import Message


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():

    """
    Code for home page of message board app.
    """

    if request.method == 'POST':
        m = Message(content=request.form['content'])
        m.save()

    body = """
        <html>
        <body>
        <h1>Class Message Board</h1>
        <h2>Contribute to the Knowledge of Others</h2>
        <form method="POST">
            <textarea name="content"></textarea>
            <input type="submit" value="Submit">
        </form>

        <h2>Wisdom From Your Fellow Classmates</h2>
        """

    for m in Message.select():
        body += """
            <div class="message">
            {}
            </div>
            """.format(html.escape(m.content))
            #.format(m.content.replace("<", "&lt;").replace(">", "&gt;"))

    return body


if __name__ == "__main__":

    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)
