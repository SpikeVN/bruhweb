from pcweb.route import Route
from .index import index

routes = [r for r in locals().values() if isinstance(r, Route)]
