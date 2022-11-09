"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

# Below is the solution for the letter P provided by one of your classmates.

import turtle

# Name your turtle something creative, maybe casper instead of t below
t = turtle.Turtle()

# Write your code and comments below
t.right(90)
t.fd(40)
# I had to start with going down because the shape would be cut off by the screen otherwise
t.left(90)
t.fd(40)
t.left(90)
t.fd(100)
t.right(90)
t.fd(40)
t.left(90)
t.fd(70)
t.left(90)
t.fd(80)
t.left(90)
t.fd(140)
t.penup()
# This prevents the pen from being used
t.right(180)
t.fd(90)
t.right(90)
t.fd(30)
t.pendown()
# This allows for the pen to be used again
t.fd(30)
t.left(90)
t.fd(30)
t.left(90)
t.fd(30)
t.left(90)
t.fd(30)
# The shape is complete