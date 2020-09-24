from flask import Blueprint, render_template
import flix.adapters.repository as repo
from flix.domainmodel.genre import Genre
from flix.form.search_form import SearchForm

home_blueprint = Blueprint('home_bp', __name__)


@home_blueprint.route('/', methods=['GET', 'POST'])
def home():

    form = SearchForm()
    if form.validate_on_submit():
        keyword = form.keyword.data
        lis = repo.database.find(keyword)
        if len(lis) == 0:
            return render_template(
                'movie_list.html',
                MovieList=None,
                form=form
            )
        else:
            return render_template(
                'movie_list.html',
                MovieList=lis,
                form=form
            )
    print(form.errors)
    return render_template(
        'home.html',
        MovieList=repo.database.random_movie([Genre("Sci-Fi")]),
        form=form
    )
