from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ContConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add(
            'demo_group',
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            'demo_group',
            self.channel_name
        )
        await self.accept()

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        preamble = text_data_json['preamble']
        value = text_data_json['value']

        await self.channel_layer.group_send(
            'demo_group',
            {
                'type': 'packet',
                'preamble': preamble,
                'value': value
            }
        )

    async def packet(self, event):
        preamble = event['preamble']
        value = event['value']

        await self.send(text_data=json.dumps(
            {
                'preamble': preamble,
                'value': value
            }
        ))