from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/info')
def info():
    return render_template('info.html')

if __name__ == '__main__':
    app.run()
