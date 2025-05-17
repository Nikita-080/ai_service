from flask import Flask, request
from ollama import Client
import json

class Resource():
    def __init__(self):
        with open('./resources.json', 'r') as file:
            data = json.load(file)
        self.version = data['version']
        self.system_prompt = data['system_prompt']
        self.template = data['template']

class Config():
    def __init__(self):
        with open('./config.json', 'r') as file:
            data = json.load(file)
        self.ollama_host = data['ollama_host']
        self.model_name = data['model_name']

resource = Resource()
config = Config()

client = Client(host=config.ollama_host)

app = Flask(__name__)

@app.route('/api/GetAnswer', methods=['GET'])
def get_answer():
    question = request.args.get('question')

    system_message = {'role': 'system', 'content': resource.system_prompt}
    user_message = {'role': 'user', 'content': question}
        
    answer = client.chat(config.model_name,   
                         messages=[syste_message, user_message])
    
    return answer.message.content

@app.route('/api/GetVersion', methods=['GET'])
def get_version():
    return resource.version

if __name__ == '__main__':
   app.run(host='0.0.0.0')
