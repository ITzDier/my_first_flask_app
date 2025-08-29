from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
# def home():
#    return render_template('home.html')

# def dashboard():
#    return render_template('dashboard.html')

# def dashboard_gestionable():
#    return render_template('dashboard_gestionable.html')

def dashboard_pro():
    return render_template('dashboard_pro.html')