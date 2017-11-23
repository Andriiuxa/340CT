from twisted.web import resource
from ./shop import EventHandler
class MyGreatResource(resource.Resource):
    def render_GET(self, request):
        return EventHandler(request)

resource = MyGreatResource()
