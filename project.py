# Minimum flask application structure

from flask import Flask  # import a Flask class from the flask library
app = Flask(__name__)  # creates a new instance passing the name of the application __name__, anytime an application is run in python a variable __name__ is created which holds all its imports


@app.route('/')  # Declarator... routes
# Declarator... it will call the function that matches the route.
@app.route('/hello')
def HelloWorld():
    return 'Hello World!'


if __name__ == '__main__':  # the application run by the python interpreter gets an __main__ variable
    # only run if script is executed directly from the interpreter, sets debugging to true (will restart server with each modification, by default the host is only available from the hosting machine, to change it change the host address below(CORS), setting the ip to 0.0.0.0 tells the interpreter to listen to all public ip adresses)
    app.debug = True
    app.run('', port=3000)
