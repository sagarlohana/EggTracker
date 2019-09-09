# main.py

from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from . import db
from .models import UrlList, User
from .src.script import track

main = Blueprint('main', __name__)

@main.route('/')
def index():
    # If user logged in, find number of products avail and total products
    if current_user.is_authenticated:
        return render_template('index.html', products_available=current_user.products_available, total_products=current_user.total_products)
    else:
        return render_template('index.html', products_available=-2, total_products=-2)

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name, subscribed=False)

@main.route('/subscribe', methods=['POST'])
def subscribe():
    url = request.form.get('url')
    price = request.form.get('price')
    
    # If the above check passes, then we know the user has the right credentials
    new_url = UrlList(user_id=current_user.id, url=url, price=price)

    db.session.add(new_url)
    db.session.commit()

    return render_template('profile.html', name=current_user.name, subscribed=True)

@main.route('/dashboard')
def dashboard():
    
    can_purchase = True
    url_list = UrlList.query.filter_by(user_id=current_user.id).all()
    thumbnail_lst = []
    actual_prices_lst = []
    can_buy = []
    """ Track will update the above lists with the links to the 
        respective images and prices of the products
    """
    num_products = track(url_list, thumbnail_lst, actual_prices_lst, can_buy)

    current_user.products_available = num_products 
    current_user.total_products = len(url_list)
    db.session.commit()

    return render_template('dashboard.html', name=current_user.name, url_list=url_list, thumbnail_lst=thumbnail_lst,
     actual_prices_lst=actual_prices_lst, can_buy=can_buy, length=len(url_list))