import json

from ryu.app.wsgi import ControllerBase
from ryu.app.wsgi import Response
from ryu.app.wsgi import route
from ryu.app.wsgi import WSGIApplication
from ryu.base import app_manager
from ryu.lib import dpid as dpid_lib
from ryu.topology.api import get_switch, get_link, get_host
from pyramid.view import view_config
from webob_graphql import serve_graphql_request
from schemas import main as schema
from pprint import pprint

class GraphQL(app_manager.RyuApp):
    _CONTEXTS = {
        'wsgi': WSGIApplication
    }

    def __init__(self, *args, **kwargs):
        super(GraphQL, self).__init__(*args, **kwargs)

        wsgi = kwargs['wsgi']
        wsgi.register(GraphQLController, {'graphql_api': self})


class GraphQLController(ControllerBase):
    def __init__(self, req, link, data, **config):
        super(GraphQLController, self).__init__(req, link, data, **config)
        self.graphql_api = data['graphql_api']   

    @route('graphql', '/graphql', methods=['GET', 'POST'])
    @view_config(route_name='graphql')
    def graphql_serve_request(self, request):
        context = {'session': request}
        pprint(request)
        return serve_graphql_request(request, schema.schema, context_value=context)



        



