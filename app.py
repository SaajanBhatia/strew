from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    return 'welcome to strew'

if __name__ == "__main__":
    app.run(port=8141)
