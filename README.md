# tiktok-tts-discord

Leverages the TikTok TTS API to send voice messages to Discord.

## With credit and thanks to

[oscie57/tiktok-voice](https://github.com/oscie57/tiktok-voice) for providing the TikTok text-to-speech API in a Python module

[interactions-py](https://github.com/interactions-py) for the endlessly useful `interactions` module

## Running

Create a `.env` file with the following ⬇️

````sh
TIKTOK-TTS-DISCORD-TOKEN=<your Discord token>```
````

Then just run `python3 tiktok-tts-discord.py` 🚀

## Commands

- `/tts script:<script> hide:<True/False>`  
  Post a message to the channel with the chosen script. You can spoiler the text message by setting `hide:True`.

- **Coming soon...** ~~`/say script:<script>`~~  
  Join the current voice channel and say the script out loud.
