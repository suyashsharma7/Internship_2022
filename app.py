from flask import Flask, render_template,request
import re

app = Flask(__name__)

@app.route('/')
def index_function():
    return render_template('index.html')

@app.route('/result',methods = ['POST'])
def result_function():
    exp = request.form['in_1']
    st = request.form['in_2']
    pattern = re.compile(exp)
    r = pattern.search(st)
    if not r:
         return render_template('result.html',ans='NOT FOUND')
    while r:
        return render_template('result.html',ans="({0}, {1})".format(r.start(), r.end()))
        r = pattern.search(st,r.start() + 1)
    
if __name__ == '__main__':
    app.run(debug=True)