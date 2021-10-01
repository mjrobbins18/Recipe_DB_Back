from channels.routing import ProtocolTypeRouter, URLRouter
from django.conf.urls import url
from channels.security.websocket import AllowedHostsOriginValidator
from recipe_db_app.consumers import BoardConsumer


application = ProtocolTypeRouter({
    'websocket': AllowedHostsOriginValidator(
        [
            url("", BoardConsumer)
        ]
    )
})

# from channels.routing import route
# from recipe_db_app.consumers import ws_connect, ws_diconnect

# channel_routing = [
#     url('websocket.connect', ws_connect),
#     url('websocket.disconnect', ws_diconnect),
# ]