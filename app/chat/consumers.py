import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
  async def connect(self):
    print('#'*10 + 'connect' + '#'*10)
    self.room_name = self.scope['url_route']['kwargs']['room_name']
    self.room_group_name = f'chat_{self.room_name}'

    await self.channel_layer.group_add(self.room_group_name, self.channel_name)

    await self.accept()

    await self.send(text_data=json.dumps({
      'type': 'connection established',
      'message': 'Successfully connected with Django'
    }))

  async def disconnect(self, code):
    print('#'*10 + 'disconnect' + '#'*10)
    await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

  async def receive(self, text_data):
    print('#'*10 + 'receive' + '#'*10)
    # json.loads で辞書型(object)に変換
    # {
    #  'type': string,
    #  'message: string,
    # }
    json_text = json.loads(text_data)
    # type をフロントに返すように明記（わかりやすくするためだけ）
    # json.dumps でstringにして送る
    message = json_text['message']

    await self.channel_layer.group_send(self.room_group_name, {
      'type': 'chat_message',
      'message': message
    })

  async def chat_message(self, event):
    message = event['message']

    await self.send(text_data=json.dumps({
      'message': message
    }))
