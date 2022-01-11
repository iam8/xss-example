# Ioana A Mititean
# 1/11/22
# UWPCE Course 3 - Internet Programming in Python
# Lesson 08 - Web Security and Class-Based Views

"""
Database setup script for class message board app.
"""

from model import db, Message

db.connect()
db.create_tables([Message])
