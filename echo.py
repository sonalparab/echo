from flask import Flask,render_template, request

app = Flask(__name__)

@app.route('/', methods = ['POST','GET'])
def root():
    return render_template('form.html')

@app.route('/greeting/', methods = ['POST','GET'])
def greeting():
    username = request.form['name']
    method = request.method
    return render_template('output.html', username=username, method=method)

if __name__ == '__main__':
    app.debug = True
    app.run()
