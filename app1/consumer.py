from channels.generic.websocket import WebsocketConsumer
import json
from asgiref.sync import async_to_sync

class TestConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = "test_consumer"
        self.room_group_name = "test_consumer_group"
        # Add the consumer to the group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        # Accept the WebSocket connection
        self.accept()
        # Send a message to the client indicating successful connection
        self.send(text_data=json.dumps({"status": "connected"}))

    def receive(self, text_data):
        self.send(text_data=text_data)
        # Handle incoming messages from the client
        pass

    def disconnect(self, *args, **kwargs):
        # Remove the consumer from the group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
        print("Disconnected")
        # Perform any necessary cleanup
        pass
