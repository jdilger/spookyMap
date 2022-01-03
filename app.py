from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os
import sys

folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, folder)

app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost/haunt_test'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost/postgres'
else:
    app.debug = False

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Haunts(db.Model):
    __tablename__ = 'landmarks'
    id = db.Column(db.Integer(), primary_key=True)
    city = db.Column(db.Text())
    country = db.Column(db.Text())
    description = db.Column(db.Text())
    location = db.Column(db.Text())
    state = db.Column(db.Text())
    state_abbrev = db.Column(db.Text())
    latitude = db.Column(db.Float())
    longitude = db.Column(db.Float())
    city_latitude = db.Column(db.Float())
    city_longitude = db.Column(db.Float())

    # def __init__(self,)    
# this is the starting input 
@app.route('/')
def index():
    # tells comp to render the index at start
    return render_template('home/index.html')
 
@app.route('/api/inthedb',methods=['GET'])
def hello_get():
    if request.method == 'GET':
        f = Haunts.query.all()
        results = [
            {  
                "description": i.description,
                'latitude': i.latitude,
                'longitude': i.longitude
                # "comments": i.comments
            } for i in f]
        

        return {'count': len(results), "apibb": results} 
        
if __name__ == '__main__':
    app.run()