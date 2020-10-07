import string

from flask import Blueprint, render_template, request
import linvie.adapters.repository as repo
from linvie.domainmodel.genre import Genre
from linvie.form.search_form import SearchForm

index_blueprint = Blueprint('index_bp', __name__)


@index_blueprint.route("/index")
def index():
    form = SearchForm()
    keyword = request.args.get('keyword')
    return render_template(
        "General/index.html",
        form=form,
        alphabet=repo.database.search_index(),
        dictionary=repo.database.sorted_dictionary(keyword=keyword)
    )
