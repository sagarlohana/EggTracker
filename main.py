# main.py

from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from . import db
from .src.script import track

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    update = False
    if current_user.url or current_user.price:
        update = True
    print("Update:{0}".format(update))
    return render_template('profile.html', name=current_user.name, url=current_user.url, price=current_user.price, update=update)

@main.route('/subscribe', methods=['POST'])
def subscribe():
    url = request.form.get('url')
    price = request.form.get('price')
    
    # if the above check passes, then we know the user has the right credentials
    current_user.url = url
    current_user.price = price
    db.session.commit()
    return redirect(url_for('main.profile'))

@main.route('/dashboard')
def dashboard():
    can_purchase = track(current_user.url, current_user.price)
    if can_purchase:
        valid = "You can purchase this item!"
    else:
        valid = "You cannot currently purchase this item!"
    return render_template('dashboard.html', name=current_user.name, url=current_user.url, price=current_user.price, valid=valid)