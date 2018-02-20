from channels.consumer import SyncConsumer


class HelloConsumer(SyncConsumer):
    def websocket_connect(self, event):
        self.send({
            "type": "websocket.accept",
        })
        self.send({
            "type": "websocket.send",
            "text": "Connected"
        })

    def websocket_receive(self, event):
        self.send({
            "type": "websocket.send",
            "text": "Yo",
        })

    def websocket_disconnect(self, event):
        self.send({
            "type": "websocket.close",
            'text': "closing"
        })
