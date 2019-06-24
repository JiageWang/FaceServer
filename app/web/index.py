from . import web
from flask import render_template


@web.route('/')
def main():
    return render_template('index.html')
