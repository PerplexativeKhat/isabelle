import interactions
import dotenv
from os import getenv
import requests
import base64

dotenv.load_dotenv()
bot = interactions.Client(token=getenv("TIKTOK-TTS-DISCORD-TOKEN"))
bot.load("interactions.ext.files")

ENDPOINT_URL = "https://api16-normal-useast5.us.tiktokv.com/media/api/text/speech/invoke/?text_speaker=en_us_001&req_text=%TEXT%&speaker_map_type=0"

# TODO: Add /say command


@bot.command(
    name="tts",
    description="Get the TikTok text-to-speech lady to say something.",
    options=[
                interactions.Option(
                    name="script",
                    description="What do you want her to say?",
                    type=interactions.OptionType.STRING,
                    required=True,
                ),
        interactions.Option(
                    name="hide",
                    description="Do you want to spoiler the text?",
                    type=interactions.OptionType.BOOLEAN,
                    required=False,
                ),
        # TODO: Add other voice options
    ]
)
async def tts(ctx: interactions.CommandContext, script: str, hide: bool = False):
    orig = str(script)
    script = script.replace("\n", " ").replace(" ", "+").replace("&", "and")
    # TikTok API found by https://github.com/oscie57/tiktok-voice
    # TODO: Replace with aiohttp, requests is blocking!
    r = requests.post(ENDPOINT_URL.replace("%TEXT%", script))
    vstr = [r.json()["data"]["v_str"]][0]
    b64d = base64.b64decode(vstr)
    file = interactions.File(filename="script.mp3", fp=b64d)
    await ctx.send(f"> {f'||' if hide else ''}{orig}{'||' if hide else ''}", files=file)

bot.start()
