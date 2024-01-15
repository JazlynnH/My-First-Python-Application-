# Importing the Flask class and the render_template function from the Flask module which will allow flask to read html.
from flask import Flask, render_template

# Creating an instance of the Flask class with the name of the current module as the argument
app = Flask(__name__)

# Creating a route for the root URL ('/')
@app.route('/')
def index():
    # Creating a variable 'msg' and assigning the string "Hello World" to it
    msg = "Hello World"
    
    # Rendering the 'tutorial.html' template with the 'msg' variable
    return render_template('tutorial.html', message=msg)

# Running the Flask app if the script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
