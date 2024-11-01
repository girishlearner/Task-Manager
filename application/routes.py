from flask import render_template

from application import app

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
