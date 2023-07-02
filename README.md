# DALL-E Image Generator ChatGPT Plugin Quickstart

This quickstart guide will help you set up and run a ChatGPT plugin that utilizes OpenAI’s DALL-E model to generate images based on the user’s prompts in less than 5 minutes. This plugin has been made in alliance with the [ChatGPT plugins documentation](https://platform.openai.com/docs/plugins). If you do not already have plugin developer access, please [join the waitlist](https://openai.com/waitlist/plugins).

## Setup locally

To install the required packages for this plugin, run the following command:

```bash
pip install -r requirements.txt
```

Setup your .env file:

1. In your project root, create a new file and name it .env.
2. Open the .env file.
3. Add your OpenAI API Key in the following way:

```bash
openai_key="YOUR_OPENAI_KEY"
```
4. Make sure you replace YOUR_OPENAI_KEY with your actual OpenAI Key.
5. Save the .env file.

To run the plugin, enter the following command:

```bash
python main.py
```

Once the local server is running:

1. Navigate to https://chat.openai.com. 
2. In the Model drop down, select "Plugins" (note, if you don't see it there, you don't have access yet).
3. Select "Plugin store"
4. Select "Develop your own plugin"
5. Enter in `localhost:5003` since this is the URL the server is running on locally, then select "Find manifest file".

Voila! Your DALL-E Image Generator plugin should now be installed and enabled. You can test it by asking it to “Draw a blue apple” or any other image prompt.

## Setup remotely

### Cloudflare workers

### Code Sandbox

### Replit

## Getting help

If you run into issues or have questions building a plugin, please join our [Developer community forum](https://community.openai.com/c/chat-plugins/20).
