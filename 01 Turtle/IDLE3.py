Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> turtle.setup(400, 400, 0, 0)
>>> turtle.cirkel(20)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    turtle.cirkel(20)
AttributeError: module 'turtle' has no attribute 'cirkel'
>>> turtle.circle(20)
>>> turtle.circle(100)
>>> turtle.right(180)
>>> turtle.circle(20)
>>> turtle.circle(100)
>>> turtle.right(90)
>>> turtle.circle(20)
>>> turtle.circle(100)
>>> turtle.right(180)
>>> turtle.circle(20)
>>> turtle.circle(100)
>>> 