from flask import Blueprint, render_template, request
import linvie.adapters.repository as repo
from linvie.domainmodel.genre import Genre
from linvie.form.search_form import SearchForm

movie_blueprint = Blueprint('movie_bp', __name__)


@movie_blueprint.route('/movie')
def movie():
    form=SearchForm()
    keyword=request.args.get('keyword')
    movie=repo.database.find_movie(keyword)


    return render_template(
        'MovieObject/movie.html',
        form=form,
        movie=movie
    )
