from flask import Flask, render_template, request

app = Flask(__name__)

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
        return render_template('processed.html')

if __name__ == '__main__':
    app.debug = True             # Server reloads after each save/change
    app.run()