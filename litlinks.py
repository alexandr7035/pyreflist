from flask import Flask
from flask import render_template
from flask import request
from flask import json
app = Flask(__name__)

import form_func

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/link_form_selector', methods=['POST','GET'])
def link_form_selector():

    if request.method == 'POST':
        data = json.loads(request.data.decode('utf-8'))
        print(data)
        selected_source = data['selected_source']
        print(selected_source)

    return(json.dumps(render_template('forms/' + selected_source + '.html')))

# call function form form_func.py to hadle the request
def call_form_func(frontend_request):
    func_to_call = getattr(form_func, frontend_request['form_name'])
    func_to_call(frontend_request)

@app.route('/form_handler', methods=['POST'])
def form_handler():
    print(request.data)
    data = json.loads(request.data.decode('utf-8'))
    print('>>> REQUEST: ', data, '\n')

    reply = call_form_func(data)

    return ''

if __name__ == '__main__':
    app.run()
