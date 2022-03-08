from flask import render_template,request,redirect,url_for
from . import main
from flask_login import login_required
from ..models import Users

@main.route('/pitches/review/new/<int:id>', nethods = ['GET', 'POST'])
@login_required
# def new_review(id):