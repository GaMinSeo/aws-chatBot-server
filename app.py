import serverless_wsgi
from flask import Flask
from flask_restful import Api

from resources.chat import ChatBotResource

app = Flask(__name__)
app.config.from_object('config.Config')


api = Api(app)

api.add_resource(ChatBotResource,'/chat')

def handler(event, context):
    return serverless_wsgi.handle_request(app,event,context)
if __name__== '__main__':
    app.run(debug=True)