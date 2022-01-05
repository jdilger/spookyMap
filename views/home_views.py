import flask

from spookyMap.infrastructure.view_modifiers import response
from spookyMap.viewmodels.home.index_viewmodel import IndexViewModel
from spookyMap.viewmodels.shared.viewmodelbase import ViewModelBase

blueprint = flask.Blueprint("home", __name__, template_folder="templates")


@blueprint.route("/")
@response(template_file="home/index.html")
def index():
    # vm = IndexViewModel()
    # return vm.to_dict()
    return {}


@blueprint.route("/about")
@response(template_file="home/about.html")
def about():
    vm = ViewModelBase()
    return vm.to_dict()


# # todo: figure this out
@blueprint.route("/api/inthedb/<lngW>/<lngE>/<latS>/<latN>", methods=["GET"])
def ghosts(lngW, lngE, latN, latS):
    vm = IndexViewModel(lngW, latS, lngE, latN)
    # https://stackoverflow.com/questions/5022066/how-to-serialize-sqlalchemy-result-to-json
    return flask.jsonify(vm.ghosts_list)

