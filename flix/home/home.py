from flask import Blueprint,render_template

home_blueprint=Blueprint('',__name__)

@home_blueprint.route('/',method=['GET'])
def home():
    return render_template(
        'home.html'
    )