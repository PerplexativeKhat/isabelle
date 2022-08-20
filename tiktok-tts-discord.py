import dotenv
from os import getenv
import requests
import base64
# Uses pycord, not discord.py (docs.pycord.dev)
import discord
from io import BytesIO
import time
from FFmpegPCMAudio import FFmpegPCMAudio

dotenv.load_dotenv()
bot = discord.Bot()

ENDPOINT_URL = "https://api16-normal-useast5.us.tiktokv.com/media/api/text/speech/invoke/?text_speaker=en_us_001&req_text=%TEXT%&speaker_map_type=0"

# TODO: DRY


@bot.slash_command(
    name="say",
    description="Get the TikTok text-to-speech lady to say something in a voice chat",)
async def say(ctx, script: discord.Option(str, "What would you like her to say?")):
    if not ctx.author.voice:
        await ctx.respond("Join a voice channel first!", ephemeral=True)
    else:
        if len(script) > 200:
            await ctx.respond(f"Shorten your script please! The API struggles if it's longer than 200 characters (yours was {len(script)})")
        else:
            script = script.replace("\n", " ").replace(
                " ", "+").replace("&", "and")
            # TikTok API found by https://github.com/oscie57/tiktok-voice
            # TODO: Replace with aiohttp, requests is blocking!
            r = requests.post(ENDPOINT_URL.replace("%TEXT%", script))
            vstr = [r.json()["data"]["v_str"]][0]
            b64d = base64.b64decode(vstr)
            await ctx.respond(f"I'm joining <#{ctx.author.voice.channel.id}> now...", ephemeral=True)
            vc = await ctx.author.voice.channel.connect()
            vc.play(FFmpegPCMAudio(BytesIO(b64d).getvalue(), pipe=True))
            while vc.is_playing():
                time.sleep(1)
            await vc.disconnect()


@bot.slash_command(
    name="tts",
    description="Get the TikTok text-to-speech lady to say something as an mp3 file",)
# TODO: Add other voice options
async def tts(ctx, script: discord.Option(str, "What would you like her to say?"), hide: discord.Option(bool, "Hide your message?") = False):
    orig = str(script)
    script = script.replace("\n", " ").replace(" ", "+").replace("&", "and")
    if len(script) > 200:
        await ctx.respond(f"Shorten your script please! The API struggles if it's longer than 200 characters (yours was {len(script)})")
    else:
        # TikTok API found by https://github.com/oscie57/tiktok-voice
        # TODO: Replace with aiohttp, requests is blocking!
        r = requests.post(ENDPOINT_URL.replace("%TEXT%", script))
        vstr = [r.json()["data"]["v_str"]][0]
        b64d = base64.b64decode(vstr)
        await ctx.respond(f"> {f'||' if hide else ''}{orig}{'||' if hide else ''}", file=discord.File(BytesIO(b64d), filename="script.mp3"))

bot.run(getenv("TIKTOK-TTS-DISCORD-TOKEN"))
