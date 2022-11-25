from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/arvore1')
def arvore1():
    return render_template('arvore b.html')

@app.route('/arvore2')
def arvore2():
    return render_template('arvore b+.html')

@app.route('/arvore3')
def arvore3():
    return render_template('arvore b*.html')

@app.route('/arvore4')
def arvore4():
    return render_template('arvore vermelhoepreto.html')

@app.route('/alunos')
def alunos():
    return render_template('alunos.html')