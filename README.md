# Isabelle

Isabelle is a fork of tiktok-tts-discord, a bot that uses the TikTok TTS API to talk in Discord voice channels.

It can use any (documented) voice, as well as repeat anything a user says in a specific channel.

### Running

Ensure you have all the dependencies listed in `requirements.txt`.

Isabelle requires a TikTok Session ID to run. [See this wiki page for how to obtain yours.](https://github.com/oscie57/tiktok-voice/wiki/Obtaining-SessionID)

Create a `.env` file containing:

```
TIKTOK-TTS-DISCORD-TOKEN=<your Discord token>
TIKTOK-SESSION-ID=<your TikTok session ID>
```

And then run `python3 tiktok-tts-discord.py`. The bot will throw an error if you're missing either value.

### Commands

- `/listen <speaker>`<br>
*Tells the bot to repeat anything you send in the current channel in your current voice call. `speaker` specifies voice.*

- `/dismiss`<br>
*Undoes `/listen`. The bot will automatically disconnect if it has no one else it's copying.*

- `/shush`<br>
*Interrupts the current voice message. Will announce who ran it.*

- `/list`<br>
*Sends a direct message containing all available voices.*

- `/say <script> <speaker>`<br>
*Says one thing in the current voice call. Can't be ran if the bot is in a different channel. `script` is the message, `speaker` specifies voice.*

- `/tts <script> <speaker>`<br>
*Generates a .MP3 file from text. `script` is the message, `speaker` specifies voice.*

### Credits

eviemaybe for the name suggestion and for helping me find some early bugs,

[oscie57](https://github.com/oscie57/tiktok-voice) for documenting the TikTok TTS API and implementing it in Python,

[m4xic](https://github.com/m4xic/tiktok-tts-discord/tree/main) for creating tiktok-tts-discord,

as well as everyone credited in the original README, which can be found below:

* * *

# tiktok-tts-discord

Leverages the TikTok TTS API to send voice messages to Discord.

## With credit and thanks to

[oscie57/tiktok-voice](https://github.com/oscie57/tiktok-voice) for providing the TikTok text-to-speech API in a Python module

[interactions-py](https://github.com/interactions-py) and [pycord](https://dev.pycord.dev) for the endlessly useful `interactions` and `pycord` modules respectively

[Armster15](https://github.com/Rapptz/discord.py/issues/5192#issuecomment-669515571) for the fixed version of FFmpegPCMAudio.py

## Running

Create a `.env` file with the following ⬇️

```sh
TIKTOK-TTS-DISCORD-TOKEN=<your Discord token>
```

Then just run `python3 tiktok-tts-discord.py` 🚀

## Commands

- `/tts script:<script> hide:<True/False>`
  Post a message to the channel with the chosen script. You can spoiler the text message by setting `hide:True`.

- `/say script:<script>`
  Join the current voice channel and say the script out loud.

