#!/user/bin/env/python
# v0.1 Grinberg tutorial - notes and commentary. 

from flask import Flask, render_template

# object of flask package, passing the dunder name variable is the module name that is running. Flask uses this to find the module and the files and all the others relative to it.

app = Flask(__name__)
guesses =['Python', 'Java', 'C++']
# decorator modifies a fx, creates a mapping between a URL and the function defined. 

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/guess/<int:id>')
# when flask receives this url with the guess number as an integer, it will map it to this function.
def guess(id):
    return ('<h1> Guess the Language!</h1>'
            '<p> My Guess: {0}</p>').format(guesses[id])

# Starts application - starts web server - it is the working component that is listening for requests from browsers and other clients. 

if __name__ == '__main__':
    app.run(debug=True)  # debug mode enabled = True. Other server will be used with a real webserver -- it will use if statement.
    
    