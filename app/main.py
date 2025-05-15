from flask import Flask
from flask import request
from ollama import Client
import json

class Resource():
    def __init__(self):
        with open("./resources.json", "r") as file:
            data = json.load(file)
        self.version = data["version"]
        self.system_prompt = data["system_prompt"]

client = Client(
  host='http://localhost:11434'
)

resource = Resource()
app = Flask(__name__)

@app.route('/api/GetAnswer', methods=['GET'])
def get_answer():
    question = request.args.get("question")
    answer = client.chat('qwen2.5:0.5b',   
                messages=[  
                    {'role': 'system', 'content': resource.system_prompt},  
                    {'role': 'user', 'content': question}  
                ])  
    return answer.message.content

@app.route('/api/GetVersion', methods=['GET'])
def get_version():
    return resource.version

if __name__ == '__main__':
   app.run(host='0.0.0.0')
