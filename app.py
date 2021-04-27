from flask import Flask, render_template

app = Flask(__name__)
files = {
    'Home' : 'index.html'
}

@app.route('/', methods = ['GET', 'POST'])
def home():
    return render_template(files['Home'])

if __name__ == "__main__":
    app.debug = True
    app.run(port=8141)
