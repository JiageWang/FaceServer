from . import web
from flask import render_template, send_file


@web.route('/')
def main():
    return send_file('../templates/version1.html')
