from flask import Flask
app = Flask(__name__)
from flask import render_template
@app.route("/")
def hello():
    return render_template('mouseover.html')
    
if __name__ == "__main__":
    app.run()