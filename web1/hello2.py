#!/Users/korbenk/octt/flask/web1/bin/python

from flask import Flask, make_response

app = Flask(__name__)

@app.route('/string/')
def return_string():
    return 'Hello, world!'

@app.route('/object/')
def return_object():
    headers = {'Content-Type': 'text/plain'}
    return make_response('Hello, world!', status=200, headers=headers)

@app.route('/tuple/')
def return_tuple():
    return 'Hello, world!', 200, {'Content-Type':
                                      'text/plain'}

if __name__ == '__main__':
    app.run()