from flask import Flask, flash, redirect, render_template, request, session, abort
import hello

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template('layout.html')

@app.route('/generate')
def generate(name=None):
    hello.main()
    return render_template('process.html',name=name)

if __name__ == "__main__":
    app.run()
