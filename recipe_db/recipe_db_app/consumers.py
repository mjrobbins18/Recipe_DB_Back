import asyncio
import json
from asgiref.sync import async_to_sync
from channels.consumer import AsyncConsumer
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):


    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive messages from websocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # send message to websocket
        await self.send(text_data=json.dumps({
            'message': message
        }))


# class BoardConsumer(AsyncConsumer):
#     async def websocket_connect(self, event):
#         print('connected', event)
#         board_room = "boardroom"
#         self.board_room = board_room
#         await self.channel_layer.group_add(
#             board_room,
#             self.channel_name
#         )
#         await self.send({
#             "type": "websocket.accept"
#         })

#     async def websocket_receive(self, event):
#         drawing_data = event.get('text', None)
#         await self.channel_layer.group_send(
#             self.board_room,
#             {
#                 "type": "board_message",
#                 "text": drawing_data
#             }
#         )

#     async def board_message(self, event):
#         await self.send({
#             "type": "websocket.send",
#             "text": event['text']
#         })
#     async def websocket_disconnect(self, event):
#         print('disconnected', event)
