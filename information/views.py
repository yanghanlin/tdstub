from rest_framework.decorators import api_view
from rest_framework.views import Request, Response
from .core.entity import normalize
from .core.request import Request as RequestInfo
from .core.environment import Environment

ALL_METHODS = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS', 'HEAD']


@api_view(ALL_METHODS)
def information_view(request: Request) -> Response:
    try:
        status = int(request.query_params['status'])
    except (KeyError, TypeError):
        status = 200
    return Response(normalize({
        'environment': Environment.current(),
        'request': RequestInfo.from_request(request),
    }), status=status)
