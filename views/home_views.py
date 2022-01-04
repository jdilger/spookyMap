import flask

from spookyMap.infrastructure.view_modifiers import response
from spookyMap.viewmodels.home.index_viewmodel import IndexViewModel
from spookyMap.viewmodels.shared.viewmodelbase import ViewModelBase

blueprint = flask.Blueprint("home", __name__, template_folder="templates")


@blueprint.route("/")
@response(template_file="home/index.html")
def index():
    vm = IndexViewModel()
    return vm.to_dict()


@blueprint.route("/about")
@response(template_file="home/about.html")
def about():
    vm = ViewModelBase()
    return vm.to_dict()


# # todo: figure this out
# @blueprint.route('/api/inthedb',methods=['GET'])
# @response(template_file='home/index.html')
# def hello_get():
#     if request.method == 'GET':
#         f = Haunts.query.all()
#         results = [
#             {
#                 "description": i.description,
#                 'latitude': i.latitude,
#                 'longitude': i.longitude
#                 # "comments": i.comments
#             } for i in f]


#         return {'count': len(results), "apibb": results}

