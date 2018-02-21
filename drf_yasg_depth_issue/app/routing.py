from channels.routing import URLRouter, ProtocolTypeRouter
from django.conf.urls import url
from channelsexample.consumer import HelloConsumer

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        url("^hello/", HelloConsumer),
    ]),
})
