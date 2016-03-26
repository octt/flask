from database import db_session
from models import User
from pprint import pprint

u = User('admin', 'admin@localhost')

pprint(u)

try:
    u = User.query.filter(User.name == 'admin').first()
except:
    u = User.query.filter(User.name == 'admin').first()
    print u.email
    u.email = 'korben@kirscht.com'
    db_session.commit()
    print u.email

print("%s" % (User.query.all()))
print("%s" % (User.query.filter(User.name == 'admin').first().name))

try:
    u = User.query.filter(User.name == 'admin').first()
except:
    pass
else:
    db_session.delete(u)
    db_session.commit()