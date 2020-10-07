from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    keyword=StringField('keyword',[DataRequired()],render_kw={'style':"width: 99%;height: 99%;background-color: rgb(255, 255, 255);border:0px;font-size:20px;"})
    submit=SubmitField("Search",render_kw={'style':"width: 99%;height: 99%;background-color: rgb(255, 255, 255);border:0px;font-size:16px;line-height:24px;"})