from twisted.web import resource
from event_handler import EventHandler

#LISTENING FOR REQUEST
#AND RETURN HTTPRESPONSE FROM EVENTHANDLER

class MyGreatResource(resource.Resource):
    def render_GET(self, request):
        return EventHandler(request)

resource = MyGreatResource()
