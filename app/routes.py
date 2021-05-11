from app import app
from flask import render_template

@app.route('/')
def index():
    title = 'This is my Index Page. It is Boring. Go to /favefive to see my favorites'
    return render_template('index.html', title=title)

# def index():
#     print ("This is my homepage. It is boring")


@app.route('/favefive')
def favefive():
    context = {
       'items': ['Cherokee Green Tomatoes',  'Kale',  'Zucchini', 'Zinnias','Cosmos']} 
    title = 'Fave Five'
    return render_template('favefive.html', **context)