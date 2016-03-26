#  http://flask.pocoo.org/docs/0.10/patterns/sqlalchemy/
#  http://flask-sqlalchemy.pocoo.org/2.1/queries/
#  http://flask.pocoo.org/docs/0.10/tutorial/templates/
#  http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ii-templates
from yourapplication.database import db_session

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()