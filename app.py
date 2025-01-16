from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.route('/') 
def index(): 
    return render_template('index.html')

@app.route('/manage')
def manage():
    return render_template('manage.html')

@app.route('/add_submit', methods=['POST'])
def add_submit():
    used = request.form.get('is-used')
    return redirect(request.referrer)


if __name__ == '__main__': 
    app.run(host='0.0.0.0')