from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
#from email import send_email

app = Flask(__name__)


#------------------------------------------------------------#
# Development/Production Mode

ENV = 'dev'

if ENV == 'dev':
    app.debug = True             # Server reloads after each save/change
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:****pw goes here****@localhost/mlh-app'        # For local development database
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False     # Warning in console


#------------------------------------------------------------#

# Database
db = SQLAlchemy(app)


# Model
class info_storage(db.Model):
    __tablename__ = 'person'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    score = db.Column(db.Integer)
    adjective = db.Column(db.String(30))

    def __init__(self, first_name, last_name, score, adjective):
        self.first_name = first_name
        self.last_name = last_name
        self.score = score
        self.adjective = adjective

#------------------------------------------------------------#

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        score = request.form['score']
        adjective = request.form['adjective']
                #print(first_name, last_name, score, adjective)

        # Message that prompts user to fill form
        if first_name == '' or last_name == '':
            return render_template('index.html', message="Please enter the minimum fields for processing")

        # Prevents duplicate first_name
        if db.session.query(info_storage).filter(info_storage.first_name == first_name).count() == 0:
            data = info_storage(first_name, last_name, score, adjective)
            db.session.add(data)
            db.session.commit()
#            send_email(first_name, last_name, score, adjective)
            return render_template('processed.html')

        return render_template('index.html', message="Unfortunately the first name has already been taken, enter another")

#------------------------------------------------------------#

if __name__ == '__main__':
    app.run()