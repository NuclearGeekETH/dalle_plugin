import openai
import quart
import quart_cors
from quart import request
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("openai_key")

app = quart_cors.cors(quart.Quart(__name__), allow_origin="https://chat.openai.com")

@app.post("/draw")
async def draw():
    try:
        data = await request.get_json(force=True)
        prompt = data.get("prompt")
        if not prompt:
            return quart.Response("Prompt missing in request data", status=400)
        response = openai.Image.create(prompt=prompt, n=1, size="1024x1024", response_format="url")
        image_url = response['data'][0]['url']
        return quart.Response(response=image_url, status=200)
    except Exception as e:
        return quart.Response(str(e), status=500)

@app.get("/logo.png")
async def plugin_logo():
    filename = 'logo.png'
    return await quart.send_file(filename, mimetype='image/png')

@app.get("/.well-known/ai-plugin.json")
async def plugin_manifest():
    host = request.headers['Host']
    with open("./.well-known/ai-plugin.json") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/json")

@app.get("/openapi.yaml")
async def openapi_spec():
    host = request.headers['Host']
    with open("openapi.yaml") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/yaml")

def main():
    app.run(debug=True, host="0.0.0.0", port=5003)

if __name__ == "__main__":
    main()
