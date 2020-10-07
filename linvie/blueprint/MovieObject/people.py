from flask import Blueprint, render_template, request
import linvie.adapters.repository as repo
from linvie.domainmodel.genre import Genre
from linvie.form.search_form import SearchForm

people_blueprint = Blueprint('people_bp', __name__)


@people_blueprint.route('/people')
def people():
    form=SearchForm()
    keyword=request.args.get('keyword')
    person=repo.database.find_people(keyword)


    return render_template(
        'MovieObject/people.html',
        form=form,
        people=person
    )
