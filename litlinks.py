from flask import Flask
from flask import render_template
from flask import request
from flask import json
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/form', methods=['POST', 'GET'])
def form():
    if request.method == 'POST':
        data = json.loads(request.data.decode('utf-8'))
        print(data['selected_link'])
    
    return render_template('form.html')


if __name__ == '__main__':
    app.run()
