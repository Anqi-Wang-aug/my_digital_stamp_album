from flask import Flask, request, render_template, redirect, url_for
import redis
import base64
from PIL import Image

app = Flask(__name__)

@app.route('/') 
def index(): 
    return render_template('index.html')

@app.route('/manage')
def manage():
    return render_template('manage.html')

@app.route('/add_submit', methods=['POST'])
def add_submit():
    #r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    file = request.files.get('img')
    file_content = base64.b64encode(file.read())
    year = request.form['year']
    country = request.form['country']
    theme = request.form['theme']
    form = request.form['stamp-format']
    printing = request.form['printings']
    descp = request.form['descrip']
    used = request.form['is-used']
    #img_str = base64.bsencode(img.read())
    #print(f'img: {img_str}, year: {year}')
    return redirect(url_for('manage'))



if __name__ == '__main__': 
    app.run(debug=True)