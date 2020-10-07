from flask import Blueprint, render_template
import linvie.adapters.repository as repo
from linvie.domainmodel.genre import Genre
from linvie.form.search_form import SearchForm

home_blueprint = Blueprint('home_bp', __name__)


@home_blueprint.route('/', methods=['GET', 'POST'])
def home():
    form = SearchForm()
    if form.validate_on_submit():
        keyword = form.keyword.data

        match, similar = repo.database.find(keyword)
        return render_template(
            'General/search.html',
            match=match,
            similar=similar,
            form=form
        )
    return render_template(
        'General/home.html',
        MovieList=repo.database.random_movie([Genre("Sci-Fi")]),
        form=form
    )
