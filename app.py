from flask import Flask, render_template, request
from translator import translator
app = Flask(__name__)



@app.route('/', methods=['POST', 'GET'])

def hello_world():
    if request.method == 'POST':
        transform = request.form['transform']
        value = translator(str(transform))
        return render_template('index.html', value=value)
    return render_template('index.html')
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4869)