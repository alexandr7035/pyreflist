from flask import Flask
from flask import render_template
from flask import request
from flask import json
app = Flask(__name__)

import form_func

# used to prevent chaching images and css
@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


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


@app.route('/form_handler', methods=['POST'])
def form_handler():
    print(request.data)
    data = json.loads(request.data.decode('utf-8'))
    print('>>> REQUEST: ', data, '\n')

    # Decide which func to call depending on the 'form_name'
    func_to_call = getattr(form_func, data['form_name'])

    reply = func_to_call(data)
    print(reply)

    return(json.dumps(reply))

if __name__ == '__main__':
    app.run()