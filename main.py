# main.py

from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from . import db
from .models import UrlList
from .src.script import track

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name, subscribed=False)

@main.route('/subscribe', methods=['POST'])
def subscribe():
    url = request.form.get('url')
    price = request.form.get('price')
    
    # if the above check passes, then we know the user has the right credentials
    new_url = UrlList(user_id=current_user.id, url=url, price=price)

    db.session.add(new_url)
    db.session.commit()
    curr_url = UrlList.query.filter_by(user_id=current_user.id).first()
    print(curr_url)
    return render_template('profile.html', name=current_user.name, subscribed=True)

@main.route('/dashboard')
def dashboard():
    
    can_purchase = True
    url_list = UrlList.query.filter_by(user_id=current_user.id).all()
    print(url_list)
    print(url_list[0].price)
    thumbnail_lst = []
    actual_prices_lst = []
    can_buy = []
    """ Track will update the above lists with the links to the 
        respective images and prices of the products
    """
    can_purchase = True
    can_purchase = track(url_list, thumbnail_lst, actual_prices_lst, can_buy)
    print(actual_prices_lst)
    print(can_buy)

    for t in thumbnail_lst:
        print(t)
    return render_template('dashboard.html', name=current_user.name, url_list=url_list, thumbnail_lst=thumbnail_lst,
     actual_prices_lst=actual_prices_lst, can_buy=can_buy, length=len(url_list))