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
import random

from flask import Flask, request, session

from model import Message


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():

    """
    Code for home page of message board app.
    """

    # If the session does not include a CSRF token, add one
    if "csrf_token" not in session:
        session["csrf_token"] = str(random.randint(10000000, 99999999))

    if request.method == 'POST':

        # Only save the message if the form submission includes a CSRF token and it matches the
        # token in the session
        if request.form.get("csrf_token", None) == session["csrf_token"]:
            m = Message(content=request.form['content'])
            m.save()

    body = f"""
        <html>
        <body>
        <h1>Class Message Board</h1>
        <h2>Contribute to the Knowledge of Others</h2>
        <form method="POST">
            <textarea name="content"></textarea>
            <input type="submit" value="Submit">
            <input type="hidden" name="csrf_token" value={session["csrf_token"]}
        </form>

        <h2>Wisdom From Your Fellow Classmates</h2>
        """

    for m in Message.select():
        body += f"""
            <div class="message">
            {html.escape(m.content)}
            </div>
            """
            # m.content.replace("<", "&lt;").replace(">", "&gt;")

    return body


if __name__ == "__main__":

    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)
