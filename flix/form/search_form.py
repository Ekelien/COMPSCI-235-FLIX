from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Length



class SearchForm(FlaskForm):
    keyword = StringField('keyword')
    submit = SubmitField("Search")

    def validate_keyword(self,keyword):
        keyword=keyword.data
        print(keyword)
        if not keyword:
            raise ValidationError
        if keyword == "":
            raise ValidationError
        if all([i == " " for i in keyword]):
            raise ValidationError("You cannot search with only spaces!")
        if len(keyword) < 3:
            raise ValidationError("Please enter more information!")
