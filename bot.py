import discord
import random
from discord.ext import commands
bot = commands.Bot(command_prefix='!')
TOKEN = 'ODI0NTAzOTAxNzIxMTk4NTky.YFwVGA.4tVkVn-YuTOp_bXOYgayIuX-ibo'
welcomes = ['씨, 안녕하세요.' , '.좋은 아침에요. 아침 맞죠?' , '.좋은 저녁일수도 있겠네요.' , '... 다들 인사하는 걸 좋아하시네요, 그렇죠?' , '씨, 네, 네. 안녕하세요.' , '님... 전 안녕봇이 아니에요. 그래도, 어, 안녕하세요.' ,'야, 안녕! ...농담이에요. 안녕하세요?']
callsf = ['씨, 부르셨나요?' , '. 저 여기 있어요.' , ',풀 네임은 정중해서 기분 좋네요.' , '0-S1-R1-S, ONLINE. Systems Almost Green.']
callsgood = [', 애칭인가요? 나쁘지 않아요.', '가까워 진 것 같아 기뻐요. 무슨 일인가요?','응, 여기 도착했어. ...요. ','나 불렀어? ...요?']
callsneh = ['그렇게 부르지 말라니까요.', '왔어요.' , '듣고 있어요.' , '....' , '계속 그렇게 부르면 대답 안 할 거에요.' , '짜증나...! 요.']
callsrude = ['그런 식으로 말하면 저도 화 낼 거에요.', '욕설...욕설...아, 그래. 조까요.', '...뭔가 불만이라도 있나요?', '네, 네. 제 얼굴 보기 싫다 이거죠.' , '...저 진짜 상처받았어요. 사라져 드릴게요.']
callsfriendly = ['넹?', '히읗이응! 그러니까, ㅎㅇ!' ]
muyaho = ['무~야~호~~!' , '무~야~호~~!', '무~야~호~~!' ,'무~야~호~~!' , '무~야~호~~!' , '무~야~호~~!' ,  '무~야~...콜록. 이거 언제까지 해요?' ]
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('새로운 환경에 적응 '))
    print('0-S1-R1-S ONLINE. SYSTEM ALMOST GREEN')

@bot.event
async def on_message(msg):
    if msg.author.bot: return None
    await bot.process_commands(msg)

@bot.command()
async def 안녕(ctx):
    await ctx.channel.send(f'{ctx.message.author.mention} {random.choice(welcomes)}', reference=ctx.message)

@bot.command()
async def 오시리스(ctx):
    await ctx.channel.send(f'{ctx.message.author.mention} {random.choice(callsf)}', reference=ctx.message)

@bot.command()
async def 시리(ctx):
    await ctx.channel.send(f'{ctx.message.author.mention} {random.choice(callsgood)}', reference=ctx.message)

@bot.command()
async def 리스(ctx):
    await ctx.channel.send(f'{ctx.message.author.mention} {random.choice(callsgood)}', reference=ctx.message)

@bot.command()
async def 시스(ctx):
    await ctx.channel.send(f'{ctx.message.author.mention} {random.choice(callsgood)}', reference=ctx.message)
@bot.command()
async def 오스(ctx):
    await ctx.channel.send(random.choice(callsneh))

@bot.command()
async def 오리(ctx):
    await ctx.channel.send(random.choice(callsneh))

@bot.command()
async def 깡통(ctx):
    await ctx.channel.send(random.choice(callsrude))

@bot.command()
async def 씨발(ctx):
    await ctx.channel.send(random.choice(callsrude))

@bot.command()
async def 니미(ctx):
    await ctx.channel.send(random.choice(callsrude))

@bot.command()
async def 병신(ctx):
    await ctx.channel.send(random.choice(callsrude))
@bot.command()
async def 도움말(ctx):
    embed = discord.Embed(title='오시리스입니다. 시리, 리스, 시스, 오시리스. 편하신 대로 부르세요.',
                          description='현재 준비된 명령어는 다음과 같습니다 : 직접, 알아내, 보세요. 계속해서 대화를 배워나갈 예정이에요.',
                          colour=0xff7676)

    await ctx.channel.send(embed=embed)
@bot.command()
async def 명령어(ctx):
    embed = discord.Embed(title='오시리스입니다. 시리, 리스, 시스, 오시리스. 편하신 대로 부르세요.',
                          description='현재 준비된 명령어는 다음과 같습니다 : 직접, 알아내, 보세요. 계속해서 대화를 배워나갈 예정이에요.',
                          colour=0xff7676)

    await ctx.channel.send(embed=embed)


bot.run(TOKEN)
