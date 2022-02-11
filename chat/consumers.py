import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):
  async def connect(self):
    print('#'*10 + 'connect' + '#'*10)
    self.room_name = self.scope['url_route']['kwargs']['room_name']
    self.room_group_name = f'chat_{self.room_name}'

    await sync_to_async(self.channel_layer.group_add(self.room_group_name, self.channel_name))

    await sync_to_async(self.accept())

    await sync_to_async(self.send(text_data=json.dumps({
      'type': 'connection established',
      'message': 'Successfully connected with Django'
    })))

  async def disconnect(self, code):
    print('#'*10 + 'disconnect' + '#'*10)
    await sync_to_async(self.channel_layer.group_discard(self.room_group_name, self.channel_name))

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
    playerName = json_text['playerName']
    playerImg = json_text['playerImg']
    playerId = json_text['playerId']

    sync_to_async(await self.channel_layer.group_send(self.room_group_name, {
      'type': 'chat_message',
      'message': message,
      'playerName': playerName,
      'playerImg': playerImg,
      'playerId': playerId,
      'message': message
    }))

  async def chat_message(self, event):
    # print(event)
    message = event['message']
    playerName = event['playerName']
    playerImg = event['playerImg']
    playerId = event['playerId']

    sync_to_async(await self.send(text_data=json.dumps({
      'message': message,
      'playerName': playerName,
      'playerImg': playerImg,
      'playerId': playerId
    })))
