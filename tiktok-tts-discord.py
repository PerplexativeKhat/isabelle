import dotenv
from os import getenv
import requests
import base64
# Uses pycord, not discord.py (docs.pycord.dev)
import discord
from io import BytesIO
from FFmpegPCMAudio import FFmpegPCMAudio
import asyncio

from resources import speakers, messages

dotenv.load_dotenv()
intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True
activity = discord.Activity(type=discord.ActivityType.listening, name="and repeating what you say!")
bot = discord.Bot(intents=intents, activity=activity)

ENDPOINT_URL = "https://api16-normal-v6.tiktokv.com/media/api/text/speech/invoke//?text_speaker={}&req_text={}&speaker_map_type=0&aid=1233"
USER_AGENT = "com.zhiliaoapp.musically/2022600030 (Linux; U; Android 7.1.2; es_ES; SM-G988N; Build/NRD90M;tt-ok/3.12.13.1)"
SESSION_ID = getenv("TIKTOK-SESSION-ID")

speakers_autocomplete = discord.utils.basic_autocomplete(speakers)
echos = dict()

# TODO: use aiohttp instead of requests
def get_tts(script, speaker):
    script = script.replace("\n", " ").replace(
        " ", "+").replace("&", "and")
    # TikTok API found by https://github.com/oscie57/tiktok-voice
    r = requests.post(
        ENDPOINT_URL.format(speaker, script),
        headers={"User-Agent": USER_AGENT, "Cookie": f"sessionid={SESSION_ID}"})
    vstr = [r.json()["data"]["v_str"]][0]
    b64d = base64.b64decode(vstr)
    return b64d

@bot.slash_command(description = messages["desc_listen"])
async def listen(
    ctx,
    speaker: discord.Option(str, messages["desc_opt_speaker"], autocomplete=speakers_autocomplete, default="English US - Female 1")):
    if ctx.author.voice:
        if ctx.voice_client and ctx.author.voice.channel != ctx.voice_client.channel:
            await ctx.respond(messages["err_diff_channel"].format(ctx.voice_client.channel.mention), ephemeral = True)
        else:
            try: await ctx.author.voice.channel.connect()
            except discord.ClientException: pass
            echos[ctx.author.id] = {"speaker": speakers[speaker], "channel": ctx.channel}
            await ctx.respond(messages["rsp_listen"].format(ctx.channel.mention, speaker), ephemeral = True)
    else:
        await ctx.respond(messages["err_no_channel"], ephemeral = True)

@bot.slash_command(description = messages["desc_dismiss"])
async def dismiss(ctx):
    if ctx.author.id in echos:
        del echos[ctx.author.id]
        await ctx.respond(messages["rsp_dismiss"], ephemeral = True)
        if len(echos) == 0:
            ctx.voice_client.disconnect()
    else:
        await ctx.respond(messages["err_not_listening"], ephemeral = True)

@bot.slash_command(description = messages["desc_shush"])
async def shush(ctx):
    if ctx.voice_client and ctx.author.voice.channel == ctx.voice_client.channel:
        await ctx.voice_client.stop()
        await ctx.respond(messages["rsp_shush"].format(ctx.author.mention), ephemeral = True)
    else:
        await ctx.respond(messages["err_diff_channel"], ephemeral = True)


@bot.slash_command(description = messages["desc_list"])
async def list(ctx):
    rsp = str()
    for i in speakers:
        rsp = rsp + i + "\n"
    await ctx.author.send(rsp)
    await ctx.respond(messages["rsp_list"], ephemeral = True)

# handles repeating messages for /listen
@bot.listen()
async def on_message(message):
    if message.author.id in echos and message.channel == echos[message.author.id]["channel"]:
        if len(message.content) < 200:
            vc = message.guild.voice_client
            while vc.is_playing(): await asyncio.sleep(1)
            vc.play(FFmpegPCMAudio(BytesIO(get_tts(message.content, echos[message.author.id]["speaker"])).getvalue(), pipe=True))
        else:
            await message.reply(messages["err_char_cap"].format(len(message.content)))


# handles cleaning up echos dict and auto disconnect
@bot.listen()
async def on_voice_state_update(member, before, after):
    if member.id in echos and after.channel == None:
        await asyncio.sleep(30)
        if member.voice == None:
            del echos[member.id]
        if len(echos) == 0:
            await before.channel.guild.voice_client.disconnect()

@bot.slash_command(description="say something!")
async def say(
    ctx,
    script: discord.Option(str, messages["desc_opt_script"]),
    speaker: discord.Option(str, messages["desc_opt_speaker"], autocomplete=speakers_autocomplete, default="English US - Female 1")
    ):
    if ctx.author.voice:
        if ctx.voice_client and ctx.author.voice.channel != ctx.voice_client.channel:
            ctx.respond(messages["err_diff_channel"].format(ctx.voice_client.channel.mention), ephemeral = True)
        else:
            try: await ctx.author.voice.channel.connect()
            except discord.ClientException: pass
            ctx.voice_client.play(FFmpegPCMAudio(BytesIO(get_tts(script, speakers[speaker])).getvalue(), pipe=True))
            while ctx.voice_client.is_playing(): await asyncio.sleep(1)
            if len(echos) == 0:
                await ctx.voice_client.disconnect()
    else:
        await ctx.respond(messages["err_no_channel"], ephemeral = True)

@bot.slash_command(description = messages["desc_tts"])
async def tts(
    ctx,
    script: discord.Option(str, messages["desc_opt_script"]),
    speaker: discord.Option(str, messages["desc_opt_speaker"], autocomplete=speakers_autocomplete, default="English US - Female 1")
    ):
    if len(script) > 200:
        await ctx.respond(messages["err_char_cap"].format(len(ctx.message.content)))
    else:
        await ctx.respond(file=discord.File(BytesIO(get_tts(script, speakers[speaker])), filename="script.mp3"))

bot.run(getenv("TIKTOK-TTS-DISCORD-TOKEN"))
