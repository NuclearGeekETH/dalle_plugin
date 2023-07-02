import openai
from dotenv import load_dotenv
import os


load_dotenv()

openai_key = os.environ["openai_key"]

openai.api_key = openai_key

def gen_image(prompt):
    try:
        response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024",
        response_format="url"
        )
        image_url = response['data'][0]['url']
        # image_url = response
        return(image_url)
    except openai.error.OpenAIError as e:
        return(e.error)

if __name__ == "__main__" :
    prompt = "a beautiful painting of a princess"
    image = gen_image(prompt)
    print(image)