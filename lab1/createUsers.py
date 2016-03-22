#!/Users/korbenk/octt/flask/lab1/bin/python

from User import *
admin = User('admin', 'admin@example.com')
guest = User('guest', 'guest@example.com')
db.session.add(admin)
db.session.add(guest)
db.session.commit()
users = User.query.all()
print users

#  http://my.safaribooksonline.com/book/web-development/9781782169628/1dot-instant-flask-web-development/ch01s05_html