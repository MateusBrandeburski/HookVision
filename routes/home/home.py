from flask import Blueprint, render_template, redirect, url_for, session, jsonify, request
from classes.dashboard.tabela import Tabela

home = Blueprint('home', __name__)

@home.route('/home')
def index():
    language = session.get('lang')
    return render_template('home/dashboard/dashboard.html', lang=language)
