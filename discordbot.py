from cmath import log
from distutils.sysconfig import PREFIX
from dotenv import load_dotenv
import os
load_dotenv()
import discord, asyncio
from discord.ext import commands
import time 
from youtube_dl import YoutubeDL
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from discord.utils import get 
from discord import FFmpegPCMAudio
from random import *
import urllib.request
from datetime import datetime
import requests
import subprocess
import pytube as pt
import glob


PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

intents = discord.Intents().all()
client = commands.Bot(command_prefix=PREFIX, intents = intents)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("나 벌써 2.0이야!"))


## commands ##



@client.command(aliases = ['마키마소환', 'akzlakthghks'])
async def enter_voice(ctx):
    global voice
    voice = await ctx.author.voice.channel.connect()
    await ctx.reply(embed = discord.Embed(description = "지배의 악마, 두둥등장", color = 0xa53939))
    print(f"{logtimeline} : {str(ctx.author)} issued command /마키마소환")


@client.command(aliases = ['마키마클라이언트', 'akzlakzmffkdldjsxm'])
async def check_client(ctx) :
    embed_client = discord.Embed(color = 0xa53939, title = "이건 내 클라이언트 정보야")
    embed_client.set_author(name = "마키마(マキマ) 봇")
    embed_client.set_footer(text = "from makima API 마키마 봇(made by ruki) copyright form shueisha 「チェンソーマン」")
    embed_client.add_field(name = "클라이언트 버전", value = "1.3b")
    embed_client.add_field(name = "개발언어", value = "Python(Interpreter[Visual Studio Code])")
    embed_client.add_field(name = "개발자", value = "천태성")
    embed_client.add_field(name = "사용 라이브러리", value = "discord.py")
    embed_client.add_field(name = "사용 라이브러리", value = "discord.ext")
    embed_client.add_field(name = "사용 라이브러리", value = "asyncio")
    embed_client.add_field(name = "사용 라이브러리", value = "Ffmpeg")
    embed_client.add_field(name = "사용 라이브러리", value = "pytube")
    embed_client.add_field(name = "사용 라이브러리", value = "time")
    embed_client.add_field(name = "사용 라이브러리", value = "random")
    embed_client.add_field(name = "사용 라이브러리", value = "glob")
    embed_client.add_field(name = "사용 라이브러리", value = "os")
    embed_client.add_field(name = "사용 라이브러리", value = "datetime")
    embed_client.add_field(name = "사용 라이브러리", value = "hangul")
    embed_client.add_field(name = "사용 라이브러리", value = "selenium")
    embed_client.add_field(name = "사용 라이브러리", value = "subprocess")
    embed_client.add_field(name = "사용 라이브러리", value = "request")
    embed_client.add_field(name = "사용 라이브러리", value = "BeautifulSoup4 as bs4")
    embed_client.add_field(name = "사용 라이브러리", value = "urllib.requests")
    embed_client.add_field(name = "사용 라이브러리", value = "webdriver")
    embed_client.add_field(name = "사용 라이브러리", value = "discord.utills.options.webdriver")
    embed_client.add_field(name = "사용 라이브러리", value = "discord.command")
    embed_client.add_field(name = "사용 라이브러리", value = "YoutubeDL")
    embed_client.add_field(name = "현재시간", value = f"{logtimeline}")
    await ctx.send("클라이언트 정보를 불러오는 중입니다 잠시 기다려주세요")
    await asyncio.sleep(randint(1,5))
    await ctx.reply(embed=embed_client)



@client.command(aliases = ['마키마봉인', 'akzlakqhddls'])
async def exit_voice(ctx):
    try :
        await client.voice_clients[0].disconnect()
        await ctx.reply(embed = discord.Embed(description = "나 갈게~", color = 0xa53939))
        print(f"{logtimeline} : {str(ctx.author)} issued command /마키마봉인")
    except :
        await ctx.reply("음성채널에서 이미 나갔어~")
        print(f"{logtimeline} : {str(ctx.author)} issued command /마키마봉인 but failed cause client already off from voice channel")

@client.command(aliases = ['마키마노래', 'akzlakshfo'])
async def makima_play_url(ctx, url):
    if ctx.author.voice is None:
        await ctx.reply("나에게 노래를 부르게 하고 싶으면 먼저 음성채널에 접속해 줘")
        return
    else :
        
        voice = await ctx.author.voice.channel.connect()
        yt = pt.YouTube(url)
        stream = yt.streams.filter(only_audio=True).first()
        stream.download()
        source = await discord.FFmpegOpusAudio.from_probe(stream.default_filename)
        voice.play(source)
        if 'https://www.youtube.com/watch?v=' in url :
            response = requests.get(url)
        elif 'https://youtu.be/' in url :
            results = url.replace('https://youtu.be/', '')
            link = 'https://www.youtube.com/watch?v=' + results
            response = requests.get(link)
        html = response.content
        bs = BeautifulSoup(html, "html.parser")
        title = bs.find('title').text
        embed = discord.Embed(color = 0xa53939, description = f"지금 이 노래! {title.replace('YouTube', '')} 을(를) 불러줄게~")
        embed.set_footer(text = f"영상 : {url}")
        await ctx.reply(embed=embed)
        await asyncio.sleep(0.5)
        await ctx.message.delete()
        while voice.is_playing() :
            await asyncio.sleep(1)
        
        await voice.disconnect()
            



@client.command(aliases = ['마키마정지', '마키마스탑', 'akzlakwjdwl', 'akzlaktmxkq'])
async def makima_stop(ctx) :
    voice_client = ctx.guild.voice_client
    if voice_client.is_playing() :
        voice_client.stop()
        await ctx.reply(embed = discord.Embed(color = 0xa53939, description = "방금 까지 부르던 노래 이제 그만할게~"))
    else :
        await ctx.reply(embed = discord.Embed(color = 0xa53939, description = "응? 아무것도 안 부르고 있는데?"))

@client.command(aliases = ['마키마일시정지', '마키마퍼즈', '마키마일시중지', 'akzlakdlftlwjdwl', 'akzlakdlftlwndwl', 'akzlakvjwm'])
async def makima_pause(ctx) :
    voice_client = ctx.guild.voice_client
    if voice_client.is_playing():
        voice_client.pause()
        await ctx.reply(embed = discord.Embed(color = 0xa53939, description = "잠시 쉬다 올게!"))
    else :
        await ctx.reply(embed = discord.Embed(color = 0xa53939, description = "응? 아무것도 안 부르고 있는데?"))

@client.command(aliases = ['마키마다시재생', '마키마재생', 'akzlakwotod', 'akzlakektlwotod'])
async def makima_resume(ctx):
    voice_client = ctx.guild.voice_client
    if voice_client.is_paused():
        voice_client.resume()
        await ctx.reply(embed = discord.Embed(color = 0xa53939, description = "쉴만큼 쉬었으니 마저 불러볼까~?"))
    else :
        await ctx.reply(embed = discord.Embed(color = 0xa53939, description = "아무것도 멈춘 기억이 없고 부른 기억도 없는데?"))

@client.command(aliases = ['마키마묵찌빠', 'akzlakanrWLQK'])
async def makima_rock_scissor_paper(ctx, msg) :
    if msg == "가위":
        await ctx.channel.send("바위")
    elif msg == "주먹":
        await ctx.channel.send("보자기")
    elif msg == "보자기":
        await ctx.channel.send("가위")
    elif msg == "묵":
        await ctx.channel.send("보자기")
    elif msg == "빠":
        await ctx.channel.send("가위")
    elif msg == "찌":
        await ctx.channel.send("바위")
    elif msg == "바위":
        await ctx.channel.send("보자기")
    elif msg == "보":
        await ctx.channel.send("가위")
    else :
        await ctx.channel.send("너는 날 이길 수 없다!")
    print(f"{logtimeline} : {str(ctx.author)} issued command /마키마묵찌빠 of {msg}")

@client.command(aliases = ['마키마운세', 'akzlakdnstp'])
async def makima_l(ctx, content) :
    await ctx.message.delete()
    await ctx.channel.send(embed = discord.Embed(title = "모든 운세는 순수히 랜덤한 결과로 결정 됩니다. 너무 맹신하지 마세요", color = 0xa53939))
    애정 = ['무난할 것 같지만, 매우 큰 이별을 맞이하고 절망에 빠집니다', '정말 좋네요, 진심으로 사랑하는 사람과 만나 영원히 살게 됩니다', '애인에게 배신을 당하고서 헤어지는 안좋은 결말이네요', '마치 자기 자신인듯 마음이 척척 잘맞는 애인과 결혼하여 무난한 생활을 살게 됩니다', '응 모솔 ㅋ', '거울을 봐라']
    재물 = ['돈은 많지만, 쓸데가 없네요 펑펑 벌게됩니다', '거지는 아니지만 살아갈 수 있을 만큼 벌게 됩니다', '돈이 거의 없어 빚에 시달리며 살게 됩니다', '남부럽지 않게 더도말고 덜도말고 적당히 벌고 하고픈 일 할수  있는 만큼 법니다', '누더기 옷을 입고, 꿰멘 양말을 겨우 신는 힘든 생활이 됩니다']
    장래 = ['원하는 꿈을 이루고 평생직장을 가져 살아가게 됩니다', '원하는 꿈을 이루진 못하였지만 남부럽지 않은 삶을 살아가게 됩니다', '자신이 자신있는 분야에서 크게 성공하여 이름을 남기며 살아갑니다', '주식과 도박에 빠져 우울한 삶을 살게 됩니다', '안좋은 길로 걸어 남을 괴롭히며 사는 삶이 됩니다', '해외에서는 유명한 사업가가 됩니다']   
    행운 = ['운이 지지리도 없어서 매번 벌칙내기 하면 걸리기만 하는 운', '운이 나쁜 편은 아닌데 매번 내기만 하면 지는 운', '운이 겁나 좋아서 3연 로또 당첨은 식은 죽 먹기인 운', '운이 딱 반반인 운 그냥 무난함', '운이 더럽게 안좋아서 도박같은거만 하면 돈 다잃고 파산할 운', '운이 좋아 하는 일 족족 해낼 수 있는 운']
    if content == '애정' :
        await ctx.channel.send(embed = discord.Embed(color = 0xa53939, title = '당신의 애정운은?',description = choice(애정)))
        print(f"{logtimeline} : {str(ctx.author)} issued command /마키마운세 of {content}")
    elif content == '재물' :
        await ctx.channel.send(embed = discord.Embed(color = 0xa53939, title = '당신의 재물운은?',description = choice(재물)))
        print(f"{logtimeline} : {str(ctx.author)} issued command /마키마운세 of {content}")
    elif content == '장래' :
        await ctx.channel.send(embed = discord.Embed(color = 0xa53939, title = "당신의 장래운은?", description = choice(장래)))
        print(f"{logtimeline} : {str(ctx.author)} issued command /마키마운세 of {content}")
    elif content == '행운' :
        await ctx.channel.send(embed = discord.Embed(color = 0xa53939, title = "당신의 행운은?", description = choice(행운)))
        print(f"{logtimeline} : {str(ctx.author)} issued command /마키마운세 of {content}")
    else :
        await ctx.channel.send("이상한 운세는 안봐줘~")
        print(f"{logtimeline} : {str(ctx.author)} issued command /마키마운세 of {content} but failed cause unexpected exception occurred")
    
        
@client.command(aliases = ['마키마게임', 'akzlakrpdla'])
async def makimagame1(ctx, mode, diff) :
    global timeouts
    if mode == '타자게임' or mode == 'xkwkdustmq' :
        if diff == "초보" or diff == 'chqh' :
            timeouts = 10
        elif diff == "중수" or diff == 'wndtn':
            timeouts = 7
        elif diff == "고수" or diff == 'rhtn':
            timeouts = 5
        ranges = 10
        picked_sent = ''
        picked_sent1 = ''
        sentances = ['냉수 먹고 속 차려라', '논을 사려면 두렁을 보라', '닭의 갈비 먹을 것 없다', '가까이 앉아야 정이 두터워진다', '담화는 마음의 보다 즐거운 향연이다', '건넛산 보고 꾸짖기', '고기 보고 부럽거든 가서 그물을 떠라', '기회는 하느님의 또 다른 별명이다', '나라 상감님도 늙은이 대접은 한다', '밑빠진 가마에 물 붓기', '바늘 구멍으로 하늘 보기', '산에서 우는 작은 새여, 꽃이 좋아 산에서 사노라네', '아첨은 비굴의 표시이다', '정이월에 큰항아리 터진다', '중이 제 머리 못 깎는다', '가난과 거지는 사촌간이다', '가는 말이 고와야 오는 말이 곱다', '가마 속의 콩도 삶아야 먹는다', '금일 충청도 명일 경상도', '까마귀 제 소리 하면 온다', '나는 세계 시민이다', '낮말은 지게문이 듣는다', '내 것도 내 것 네 것도 내 것', '내 배가 불러야 남의 배도 부르다']
        points = 000
        for ranges in range(1, ranges+1, 1) :
            picked_sent = choice(sentances)
            if picked_sent != picked_sent1 :
                await ctx.channel.send(embed = discord.Embed(title = "타자 게임 %d" % ranges, description = str(picked_sent), color = 0xa53939))
                
                timeout = timeouts
                def check(m) :
                    return m.author == ctx.message.author and m.channel == ctx.message.channel

                try :
                    
                    msg = await client.wait_for('message', check=check, timeout=timeout)
                        
                except asyncio.TimeoutError :
                    await ctx.send("넌 지배의 악마를 이길 수 없다![-50점]")
                    points -= 50
                else :
                    if msg.content == "마키마중지" or msg.content == "akzlakwndwl":
                        await ctx.channel.send(embed = discord.Embed(color = 0xa53939, description = '게임을 중지합니다. 변경 정보는 저장되지 않습니다'))
                        break
                    elif msg.content == picked_sent:
                        await ctx.send("이 녀석 좀 하는데?[+50점]")
                        points += 50
                    elif msg.content != picked_sent:
                        await ctx.send("이정돈 해야지![-25점]")
                        points -= 25

            embed = discord.Embed(color = 0xa53939, title = "결과")           
            embed.add_field(name = "네 점수는?", value = "%d점!" % points)
            if points >= 325 :
                embed.add_field(name = "티어", value = "챌린저")
                embed.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/challenger.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
            elif points >= 300 :
                embed.add_field(name = "티어", value = "그랜드 마스터")
                embed.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/grandmaster.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
            elif points >= 275 :
                embed.add_field(name = "티어", value = "마스터")
                embed.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/master.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
            elif points >= 250 :
                embed.add_field(name = "티어", value = "다이아")
                embed.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/diamond.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
            elif points>= 200 :
                embed.add_field(name = "티어", value = "플레티넘")
                embed.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/platinum.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
            elif points >= 150 :
                embed.add_field(name = "티어", value = "골드")
                embed.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/gold.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
            elif points >= 100 :
                embed.add_field(name = "티어", value = "실버")
                embed.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/silver.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
            elif points >= 75 :
                embed.add_field(name = "티어", value = "브론즈")
                embed.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/bronze.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
            elif points >= 50 :
                embed.add_field(name = "티어", value = "아이언")
                embed.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/iron.png?image=q_auto,f_webp,w_144&amp;v=1675751623531')
            elif points >= 0 :
                embed.add_field(name = "티어", value = "튀르이")
            await ctx.channel.send(embed = embed)


    elif mode == '암산게임' or mode == 'dkatksrpdla' :
        point_socre = 0
        if diff == '초보' or diff == 'chqh':
            times = 15
            index = 7
            for index in range(1, index+1, 1) :
                random_number = [randint(1, 20), randint(30, 65)]
                await ctx.channel.send(embed = discord.Embed(color = 0xa53939, title = f"암산게임 {index}", description = f"{random_number[0]} + {random_number[1]} = ?"))
                
                def check(m) :
                    return m.author == ctx.message.author and m.channel == ctx.message.channel

                try :
                    msg = await client.wait_for('message', check=check, timeout=times)
                except asyncio.TimeoutError :
                    await ctx.channel.send(embed = discord.Embed(color = 0xa53939, description = f"그것도 못해? 정답({random_number[0] + random_number[1]}) [-50]"))
                    point_socre -= 50
                else :
                    if msg.content == "마키마중지" or msg.content == "akzlakwndwl" :
                        break
                    elif int(msg.content) != int(random_number[0] + random_number[1]) :
                        await ctx.channel.send(embed = discord.Embed(color = 0xa53939, description = f"아쉽지만 틀렸네 ㅋ 정답({random_number[0] + random_number[1]}) [-25]"))
                        point_socre -= 25
                    elif int(msg.content) == int(random_number[0] + random_number[1]) :
                        await ctx.channel.send(embed = discord.Embed(color = 0xa53939, description = f"오 좀 하는데? 정답({random_number[0] + random_number[1]}) [+50]"))
                        point_socre += 50
                    elif msg.content == "마키마중지" :
                        await ctx.channel.send(embed = discord.Embed(color = 0xa53939, description = '게임을 중지합니다. 변경 정보는 저장되지 않습니다'))
                        break
            embed = discord.Embed(color = 0xa53939, title = "결과")           
            embed.add_field(name = "네 점수는?", value = "%d점!" % point_socre)
            if point_socre >= 325 :
                embed.add_field(name = "티어", value = "챌린저")
                embed.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/challenger.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
            elif point_socre >= 300 :
                embed.add_field(name = "티어", value = "그랜드 마스터")
                embed.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/grandmaster.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
            elif point_socre >= 275 :
                embed.add_field(name = "티어", value = "마스터")
                embed.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/master.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
            elif point_socre >= 250 :
                embed.add_field(name = "티어", value = "다이아")
                embed.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/diamond.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
            elif point_socre >= 200 :
                embed.add_field(name = "티어", value = "플레티넘")
                embed.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/platinum.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
            elif point_socre >= 150 :
                embed.add_field(name = "티어", value = "골드")
                embed.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/gold.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
            elif point_socre >= 100 :
                embed.add_field(name = "티어", value = "실버")
                embed.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/silver.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
            elif point_socre >= 75 :
                embed.add_field(name = "티어", value = "브론즈")
                embed.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/bronze.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
            elif point_socre >= 50 :
                embed.add_field(name = "티어", value = "아이언")
                embed.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/iron.png?image=q_auto,f_webp,w_144&amp;v=1675751623531')
            elif point_socre >= 0 :
                embed.add_field(name = "티어", value = "튀르이")
            await ctx.channel.send(embed = embed)

        if diff == '중수' or diff == 'wndtn' :
            times = 15
            index = 7
            for index in range(1, index+1, 1) :
                random_number = [randint(1, 10), randint(3, 17)]
                await ctx.channel.send(embed = discord.Embed(color = 0xa53939, title = f"암산게임 {index}", description = f"{random_number[0]} x {random_number[1]} = ?"))
                
                def check(m) :
                    return m.author == ctx.message.author and m.channel == ctx.message.channel

                try :
                    msg = await client.wait_for('message', check=check, timeout=times)
                except asyncio.TimeoutError :
                    await ctx.channel.send(embed = discord.Embed(color = 0xa53939, description = f"그것도 못해? 정답({random_number[0] * random_number[1]}) [-50]"))
                    point_socre -= 50
                else :
                    if msg.content == "마키마중지" or msg.content == "akzlakwndwl" :
                        await ctx.channel.send(embed = discord.Embed(color = 0xa53939, description = '게임을 중지합니다. 변경 정보는 저장되지 않습니다'))
                        break
                    elif int(msg.content) != int(random_number[0] * random_number[1]) :
                        await ctx.channel.send(embed = discord.Embed(color = 0xa53939, description = f"아쉽지만 틀렸네 ㅋ 정답({random_number[0] * random_number[1]}) [-25]"))
                        point_socre -= 25
                    elif int(msg.content) == int(random_number[0] * random_number[1]) :
                        await ctx.channel.send(embed = discord.Embed(color = 0xa53939, description = f"오 좀 하는데? 정답({random_number[0] * random_number[1]}) [+50]"))
                        point_socre += 50
                    
            embed = discord.Embed(color = 0xa53939, title = "결과")           
            embed.add_field(name = "네 점수는?", value = "%d점!" % point_socre)
            if point_socre >= 275 :
                embed.add_field(name = "티어", value = "챌린저")
                embed.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/challenger.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
            elif point_socre >= 225 :
                embed.add_field(name = "티어", value = "그랜드 마스터")
                embed.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/grandmaster.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
            elif point_socre >= 200 :
                embed.add_field(name = "티어", value = "마스터")
                embed.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/master.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
            elif point_socre >= 175 :
                embed.add_field(name = "티어", value = "다이아")
                embed.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/diamond.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
            elif point_socre >= 150 :
                embed.add_field(name = "티어", value = "플레티넘")
                embed.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/platinum.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
            elif point_socre >= 125 :
                embed.add_field(name = "티어", value = "골드")
                embed.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/gold.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
            elif point_socre >= 100 :
                embed.add_field(name = "티어", value = "실버")
                embed.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/silver.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
            elif point_socre >= 75 :
                embed.add_field(name = "티어", value = "브론즈")
                embed.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/bronze.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
            elif point_socre >= 50 :
                embed.add_field(name = "티어", value = "아이언")
                embed.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/iron.png?image=q_auto,f_webp,w_144&amp;v=1675751623531')
            elif point_socre >= 0 :
                embed.add_field(name = "티어", value = "튀르이")
            await ctx.channel.send(embed = embed)

        if diff == '고수' or diff == 'rhtn' :
            times = 20
            index = 7
            for index in range(1, index+1, 1) :
                random_number = [randint(1, 15), randint(1, 15), randint(999, 9999)]
                await ctx.channel.send(embed = discord.Embed(color = 0xa53939, title = f"암산게임 {index}", description = f"{random_number[0]} x {random_number[1]} + {random_number[2]}= ?"))
                
                def check(m) :
                    return m.author == ctx.message.author and m.channel == ctx.message.channel

                try :
                    msg = await client.wait_for('message', check=check, timeout=times)
                except asyncio.TimeoutError :
                    await ctx.channel.send(embed = discord.Embed(color = 0xa53939, description = f"그것도 못해? 정답({random_number[0] * random_number[1] + random_number[2]}) [-50]"))
                    point_socre -= 50
                else :
                    if msg.content == "마키마중지" or msg.content == "akzlakwndwl":
                        await ctx.channel.send(embed = discord.Embed(color = 0xa53939, description = '게임을 중지합니다. 변경 정보는 저장되지 않습니다'))
                        break
                    elif int(msg.content) != int(random_number[0] * random_number[1] + random_number[2]) :
                        await ctx.channel.send(embed = discord.Embed(color = 0xa53939, description = f"아쉽지만 틀렸네 ㅋ 정답({random_number[0] * random_number[1] + random_number[2]}) [-25]"))
                        point_socre -= 25
                    elif int(msg.content) == int(random_number[0] * random_number[1] + random_number[2]) :
                        await ctx.channel.send(embed = discord.Embed(color = 0xa53939, description = f"오 좀 하는데? 정답({random_number[0] * random_number[1] + random_number[2]}) [+50]"))
                        point_socre += 50
                    
            embed = discord.Embed(color = 0xa53939, title = "결과")           
            embed.add_field(name = "네 점수는?", value = "%d점!" % point_socre)
            if point_socre >= 275 :
                embed.add_field(name = "티어", value = "챌린저")
                embed.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/challenger.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
            elif point_socre >= 225 :
                embed.add_field(name = "티어", value = "그랜드 마스터")
                embed.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/grandmaster.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
            elif point_socre >= 200 :
                embed.add_field(name = "티어", value = "마스터")
                embed.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/master.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
            elif point_socre >= 175 :
                embed.add_field(name = "티어", value = "다이아")
                embed.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/diamond.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
            elif point_socre >= 150 :
                embed.add_field(name = "티어", value = "플레티넘")
                embed.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/platinum.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
            elif point_socre >= 125 :
                embed.add_field(name = "티어", value = "골드")
                embed.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/gold.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
            elif point_socre >= 100 :
                embed.add_field(name = "티어", value = "실버")
                embed.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/silver.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
            elif point_socre >= 75 :
                embed.add_field(name = "티어", value = "브론즈")
                embed.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/bronze.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
            elif point_socre >= 50 :
                embed.add_field(name = "티어", value = "아이언")
                embed.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/iron.png?image=q_auto,f_webp,w_144&amp;v=1675751623531')
            elif point_socre >= 0 :
                embed.add_field(name = "티어", value = "튀르이")
            await ctx.channel.send(embed = embed)
    
    elif mode == '한자게임' or mode == 'gkswkrpdla' :
        await ctx.channel.send(embed = discord.Embed(color = 0xa53939, title = "게임을 플레이 하기 전 ! 명심 해 주세요. 한자의 훈과 음은 모두 Windows 한자 기본 표시 기준입니다"))
        if diff == '초보' or diff == 'chqh' :
            noobcharacter = {'雨' : '비 우', '王' : '임금 왕', '主' : '주인 주', '中' : '가운데 중', '七' : '일곱 칠', '下' : '아래 하', '上' : '위 상', '工' : '장인 공', '公' : '공변될 공', '月' : '달 월', '心' : '마음 심', '生' : '날 생', '以' : '써 이', '來' : '올 래', '目' : '눈 목', '木' : '나무 목', '母' : '어미 모', '不' : '아닐 불', '西' : '서녘 서', '二' : '두 이', '順' : '순할 순', '海' : '바다 해', '三' : '석 삼', '五' : '다섯 오', '白' : '흰 백', '百' : '일백 백', '千' : '일천 천', '十' : '열 십', '金' : '쇠 금', '土' : '흙 토', '日' : '날 일', '水' : '물 수', '子' : '아들 자', '人' : '사람 인', '家' : '집 가', '氷' : '얼음 빙', '男' : '사내 남', '女' : '여자 녀', '未' : '아닐 미', '力' : '힘 력', '刀' : '칼 도'}
            point_noob = 0
            inn = 12
            timen = 15
            for inn in range(1, inn+1, 1) :
                lists_keys = list(noobcharacter.keys())
                question = choice(lists_keys)
                await ctx.channel.send(embed = discord.Embed(color = 0xa53939, title = f"한자게임 {inn}", description = f"{question}"))

                def check(m) :
                    return m.author == ctx.message.author and m.channel == ctx.message.channel
                
                try :
                    msg = await client.wait_for('message', check=check, timeout=timen)
                except asyncio.TimeoutError :
                    await ctx.channel.send(embed = discord.Embed(color = 0xa53939, description = f'뭐해? (정답 : {noobcharacter[question]}) [-50]'))
                    point_noob -= 50
                else :
                    if msg.content == "마키마중지" or msg.content == "akzlakwndwl" :
                        await ctx.channel.send(embed = discord.Embed(color = 0xa53939, description = '게임을 중지합니다. 변경 정보는 저장되지 않습니다'))
                        break
                    elif msg.content != noobcharacter[question] :
                        await ctx.channel.send(embed = discord.Embed(color = 0xa53939, description = f'아쉽네 ~ (정답 : {noobcharacter[question]}) [-25]'))
                        point_noob -= 25
                    elif msg.content == noobcharacter[question] :
                        await ctx.channel.send(embed = discord.Embed(color = 0xa53939, description = f'너 ! 한자 공부 했었지 ! (정답 : {noobcharacter[question]}) [+50]'))
                        point_noob += 50

            embed = discord.Embed(color = 0xa53939, title = "결과")           
            embed.add_field(name = "네 점수는?", value = "%d점!" % point_noob)
            if point_noob >= 550 :
                embed.add_field(name = "티어", value = "챌린저")
                embed.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/challenger.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
            elif point_noob >= 500 :
                embed.add_field(name = "티어", value = "그랜드 마스터")
                embed.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/grandmaster.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
            elif point_noob >= 450 :
                embed.add_field(name = "티어", value = "마스터")
                embed.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/master.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
            elif point_noob >= 425 :
                embed.add_field(name = "티어", value = "다이아")
                embed.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/diamond.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
            elif point_noob >= 375 :
                embed.add_field(name = "티어", value = "플레티넘")
                embed.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/platinum.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
            elif point_noob >= 350 :
                embed.add_field(name = "티어", value = "골드")
                embed.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/gold.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
            elif point_noob >= 300 :
                embed.add_field(name = "티어", value = "실버")
                embed.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/silver.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
            elif point_noob >= 250 :
                embed.add_field(name = "티어", value = "브론즈")
                embed.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/bronze.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
            elif point_noob >= 200 :
                embed.add_field(name = "티어", value = "아이언")
                embed.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/iron.png?image=q_auto,f_webp,w_144&amp;v=1675751623531')
            elif point_noob >= 175 :
                embed.add_field(name = "티어", value = "튀르이")
            await ctx.channel.send(embed = embed)
             
        elif diff == '중수' or diff == 'wndtn' :
            skilledcharacter = {'閉' : '닫을 폐', '開' : '열 개', '問' : '물을 문', '熙' : '기쁠 희', '殺' : '죽일 살', '語' : '말씀 어', '英' : '꽃부리 영', '聚' : '모일 취', '走' : '달릴 주', '福' : '복 복', '暴' : '햇빛 쪼일 폭', '찢을 렬' : '裂', '移' : '옮길 이', '마루 종' : '宗', '象' : '코끼리 상', '線' : '줄 선', '善' : '착할 선', '羊' : '양 양', '陽' : '볕 양', '漁' : '고기 잡을 어', '技' : '재주 기', '乘' : '탈 승', '顔' : '얼굴 안', '戾' : '어그러질 려', '銅' : '구리 동', '種' : '씨 종', '重' : '무거울 중', '江' : '큰 내 강', '戰' : '싸울 전', '電' : '번개 전', '露' : '이슬 로', '富' : '부자 부', '州' : '고을 주', '新' : '새 신', '神' : '귀신 신', '政' : '정사 정', '精' : '정할 정', '報' : '갚을 보', '寶' : '보배 보', '數' : '셈 수', '胸' : '가슴 흉', '必' : '반드시 필', '筆' : '붓 필', '雄' : '수컷 웅', '眞' : '참 진', '淚' : '눈물 루', '設' : '베풀 설', '雪' : '눈 설', '全' : '온전할 전', '酒' : '술 주', '場' : '마당 장', '舜' : '순임금 순', '理' : '다스릴 리', '痲' : '저릴 마', '汚' : '더러울 오', '撒' : '뿌릴 살', '愛' : '사랑 애', '貶' : '떨어트릴 폄', '紫' : '자줏빛 자', '字' : '글자 자', '學' : '배울 학', '鶴' : '학 학', '判' : '판단할 판', '群' : '무리 군', '盡' : '다할 진', '殘' : '잔인할 잔', '泳' : '헤엄칠 영', '龍' : '용 용', '勇' : '날랠 용', '美' : '아름다울 미', '忍' : '참을 인', '龜' : '손 얼어터질 균'}
            point_skilled = 0
            ins = 20
            timesk = 15
            for ins in range(1, ins+1, 1) :
                lists_keys_ = list(skilledcharacter.keys())
                question_ = choice(lists_keys_)
                await ctx.channel.send(embed = discord.Embed(color = 0xa53939, title = f"한자게임 {ins}", description = f"{question_}"))

                def check(m) :
                    return m.author == ctx.message.author and m.channel == ctx.message.channel
                
                try :
                    msg = await client.wait_for('message', check=check, timeout=timesk)

                except asyncio.TimeoutError :
                    await ctx.channel.send(embed = discord.Embed(color = 0xa53939, description = f'뭐해? (정답 : {skilledcharacter[question_]}) [-50]'))
                    point_skilled -= 50
                else :
                    if msg.content == "마키마중지" or msg.content == "akzlakwndwl" :
                        await ctx.channel.send(embed = discord.Embed(color = 0xa53939, description = '게임을 중지합니다. 변경 정보는 저장되지 않습니다'))
                        break
                    elif msg.content != skilledcharacter[question_] :
                        await ctx.channel.send(embed = discord.Embed(color = 0xa53939, description = f'아쉽네 ~ (정답 : {skilledcharacter[question_]}) [-25]'))
                        point_skilled -= 25
                    elif msg.content == skilledcharacter[question_] :
                        await ctx.channel.send(embed = discord.Embed(color = 0xa53939, description = f'너 ! 한자 공부 했었지 ! (정답 : {skilledcharacter[question_]}) [+50]'))
                        point_skilled += 50

            embed = discord.Embed(color = 0xa53939, title = "결과")           
            embed.add_field(name = "네 점수는?", value = "%d점!" % point_skilled)
            if point_skilled >= 950 :
                embed.add_field(name = "티어", value = "챌린저")
                embed.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/challenger.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
            elif point_skilled >= 875 :
                embed.add_field(name = "티어", value = "그랜드 마스터")
                embed.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/grandmaster.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
            elif point_skilled >= 850 :
                embed.add_field(name = "티어", value = "마스터")
                embed.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/master.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
            elif point_skilled >= 750 :
                embed.add_field(name = "티어", value = "다이아")
                embed.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/diamond.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
            elif point_skilled >= 725 :
                embed.add_field(name = "티어", value = "플레티넘")
                embed.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/platinum.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
            elif point_skilled >= 675 :
                embed.add_field(name = "티어", value = "골드")
                embed.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/gold.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
            elif point_skilled >= 600 :
                embed.add_field(name = "티어", value = "실버")
                embed.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/silver.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
            elif point_skilled >= 550 :
                embed.add_field(name = "티어", value = "브론즈")
                embed.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/bronze.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
            elif point_skilled >= 500 :
                embed.add_field(name = "티어", value = "아이언")
                embed.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/iron.png?image=q_auto,f_webp,w_144&amp;v=1675751623531')
            elif point_skilled >= 475 :
                embed.add_field(name = "티어", value = "튀르이")
            await ctx.channel.send(embed = embed)

        elif diff == "고수" or diff == 'rhtn':
            mastercharacter = {'戾' : '어그러질 려', '俊' : '준걸 준', '然' : '그러할 연', '養' : '기를 양', '隱' : '숨을 은', '歡' : '기뻐할 환', '龜' : '손 얼어터질 균', '歸' : '돌아올 귀', '瞳' : '눈동자 동', '空' : '빌 공', '命' : '목숨 명', '散' : '흩을 산', '密' : '빽빽할 밀', '淵' : '못 연', '巖' : '바위 암', '智' : '지혜 지', '慧' : '지혜 혜', '勝' : '이길 승', '顔' : '얼굴 안', '騎' : '탈 기', '矯' : '바로잡을 교', '所' : '바 소', '了' : '마칠 료', '尿' : '오줌 뇨', '漏' : '샐 루', '壽' : '목숨 수', '鬼' : '귀신 귀', '餘' : '남을 여'} 
            index_master = 25
            point_master = 0
            timem = 10
            for index_master in range(1, index_master+1, 1) :
                list_keys_master = list(mastercharacter.keys())
                question_m = choice(list_keys_master)
                await ctx.channel.send(embed = discord.Embed(color = 0xa53939, title = f"한자게임 {index_master}", description = f"{question_m}"))

                def check(m) :
                        return m.author == ctx.message.author and m.channel == ctx.message.channel
                    
                try :
                    msg = await client.wait_for('message', check=check, timeout=timem)

                except asyncio.TimeoutError :
                    await ctx.channel.send(embed = discord.Embed(color = 0xa53939, description = f'뭐해? (정답 : {mastercharacter[question_m]}) [-50]'))
                    point_master -= 50
                else :
                    if msg.content == "마키마중지" or msg.content == "akzlakwndwl" :
                        await ctx.channel.send(embed = discord.Embed(color = 0xa53939, description = '게임을 중지합니다. 변경 정보는 저장되지 않습니다'))
                        break
                    elif msg.content != mastercharacter[question_m] :
                        await ctx.channel.send(embed = discord.Embed(color = 0xa53939, description = f'아쉽네 ~ (정답 : {mastercharacter[question_m]}) [-25]'))
                        point_master -= 25
                    elif msg.content == mastercharacter[question_m] :
                        await ctx.channel.send(embed = discord.Embed(color = 0xa53939, description = f'너 ! 한자 공부 했었지 ! (정답 : {mastercharacter[question_m]}) [+50]'))
                        point_master += 50

            embed = discord.Embed(color = 0xa53939, title = "결과")           
            embed.add_field(name = "네 점수는?", value = "%d점!" % point_master)
            if point_master >= 1225 :
                embed.add_field(name = "티어", value = "챌린저")
                embed.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/challenger.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
            elif point_master >= 1100 :
                embed.add_field(name = "티어", value = "그랜드 마스터")
                embed.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/grandmaster.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
            elif point_master >= 1050 :
                embed.add_field(name = "티어", value = "마스터")
                embed.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/master.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
            elif point_master >= 1000 :
                embed.add_field(name = "티어", value = "다이아")
                embed.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/diamond.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
            elif point_master >= 975 :
                embed.add_field(name = "티어", value = "플레티넘")
                embed.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/platinum.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
            elif point_master >= 925 :
                embed.add_field(name = "티어", value = "골드")
                embed.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/gold.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
            elif point_master >= 850 :
                embed.add_field(name = "티어", value = "실버")
                embed.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/silver.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
            elif point_master >= 800 :
                embed.add_field(name = "티어", value = "브론즈")
                embed.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/bronze.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
            elif point_master >= 775 :
                embed.add_field(name = "티어", value = "아이언")
                embed.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/iron.png?image=q_auto,f_webp,w_144&amp;v=1675751623531')
            elif point_master >= 725 :
                embed.add_field(name = "티어", value = "튀르이")
            await ctx.channel.send(embed = embed)

    else :
        await ctx.reply(embed = discord.Embed(color = 0xa53939, description = "해당 모드는 현재 지원하지 않습니다(타자게임, 암산게임, 한자게임)"))
@client.command(aliases = ['마키마지배', 'akzlakwlqo'])
async def kill(ctx, nickname: discord.Member) :
    urllib.request.urlretrieve("https://i.ytimg.com/vi/G1hMtZlVKv4/hqdefault.jpg", "explain.jpg")
    img = discord.File("explain.jpg", filename="img_.jpg")
    if str(ctx.author) == "米津玄師(よねづけんし)#9185" or str(ctx.author) == "카직스 장인#6332" or str(ctx.author) == "박희영#5169" :

        times = 10
        await ctx.channel.send(embed = discord.Embed(color = 0xa53939, title = f"『{nickname}』이라고 말해, 어서"))
        def check (m) :
            return m.author == ctx.message.author and m.channel == ctx.message.channel
        try :
                msg = await client.wait_for('message', check=check, timeout=times)
        except asyncio.TimeoutError :
            await ctx.send("에이 모야 시시하게")
            print(f"{logtimeline} : {str(ctx.author)} issued command /마키마지배 to {nickname} but timesouts")
        else :
            print(f"{logtimeline} : {str(ctx.author)} issued command /마키마지배 to {nickname}")
            embed = discord.Embed(color = 0xa53939)
            embed.set_image(url = "attachment://img.jpg")
            await ctx.channel.send(file=img)
            await nickname.edit(mute=True)
            await asyncio.sleep(120)
            await nickname.edit(mute=False)
    else :
        await ctx.channel.send(embed = discord.Embed(color = 0xa53939, description = "나보다 약한 자의 말 따윈 듣지 않아"))
        print(f"{logtimeline} : {str(ctx.author)} issued command /마키마지배 to {nickname} but failed cause missing permissions")


@client.command(aliases = ['마키마빵', 'akzlakQkd'])
async def mute(ctx, nickname: discord.Member) :
    urllib.request.urlretrieve("https://ih1.redbubble.net/image.2219450953.2470/bg,f8f8f8-flat,750x,075,f-pad,750x1000,f8f8f8.jpg", "explain1.jpg")
    img1 = discord.File("explain1.jpg", filename="image.png")
    if str(ctx.author) == "米津玄師(よねづけんし)#9185" or str(ctx.author) == "카직스 장인#6332" or str(ctx.author) == "박희영#5169" :
        times = 10
        await ctx.channel.send(embed = discord.Embed(color = 0xa53939, title = "네가 문을 열어, 내가 죽일게"))
        def check (m) :
            return m.author == ctx.message.author and m.channel == ctx.message.channel
        try :
                msg = await client.wait_for('message', check=check, timeout=times)
        except asyncio.TimeoutError :
            await ctx.send("에이 모야 시시하게")
            print(f"{logtimeline} : {str(ctx.author)} issued command /마키마빵 to {nickname} but timeouts")
        else :
            print(f"{logtimeline} : {str(ctx.author)} issued command /마키마빵 to {nickname}")
            embed1 = discord.Embed(color = 0xa53939)
            embed1.set_image(url = "attachment://explain1.jpg")
            await ctx.channel.send(file=img1)
            await asyncio.sleep(1)
            await nickname.edit(voice_channel=None)
    else :
        await ctx.channel.send(embed = discord.Embed(color = 0xa53939, description = "나 보다 약한 자의 말 따윈 듣지 않아"))
        print(f"{logtimeline} : {str(ctx.author)} issued command /마키마빵 but failed cuase missing permissions")



@client.command(aliases = ['마키마공지', 'akzlakrhdwl'])
async def announcement (ctx, tit, cont) :
    role = discord.utils.get(ctx.roles, name="개발자👨‍💻") 
    if role is not None :

        await ctx.message.delete()
        result = cont.replace('_',' ')
        chann = client.get_channel(1066219293995438170)
        await chann.send(embed = discord.Embed(title = str(tit), description = str(result), color = 0xa53939))
        print(f"{logtimeline} : {str(ctx.author)} issued command /마키마공지 to Announce Channel contain {result}")
    else :
        await ctx.reply("나 보다 약한 녀석의 말 따윈 듣지 않아")

@client.command(aliases = ['마키마알림', 'akzlakdkffla'])
async def announce(ctx, chanid, tit, cont) :
    if str(ctx.author) == '米津玄師(よねづけんし)#9185' :

        await ctx.message.delete()
        re = cont.replace('_', ' ')
        titles = tit.replace('_', ' ')
        cha = client.get_channel(int(chanid))
        await cha.send(embed = discord.Embed(title = titles, description = re, color = 0xa53939))
        print(f"{logtimeline} : {str(ctx.author)} issued command /마키마알림 to {chanid} contains {re}")
    else :
        await ctx.reply('지배의 악마에게 이런 잡일 시키지 마라!')


@client.command(aliases = ['마키마메세지', 'akzlakaptpwl'])
async def annou(ctx, chanid, cont) :
    if str(ctx.author) == '米津玄師(よねづけんし)#9185' :

        await ctx.message.delete()
        re = cont.replace('_', ' ')
        cha = client.get_channel(int(chanid))
        await cha.send(re)
        print(f"{logtimeline} : {str(ctx.author)} issued command /마키마알림 to {chanid} contains {re}")
    else :
        await ctx.reply('지배의 악마에게 이런 잡일 시키지 마라!')


@client.command(aliases = ['마키마도움', 'akzlakehdna'])
async def helps (ctx) :
    embed = discord.Embed(title = "접두사 : /마키마", color = 0xa53939)
    embed.add_field(name = "/마키마지배 [@mention.member]", value = "지정한 대상을 지배하여 어떤 말도 할 수 없게 만듭니다", inline = False)
    embed.add_field(name = "/마키마빵 [@mention.member]", value = "지정한 대상을 총으로 쏴 보내버립니다", inline = False)
    embed.add_field(name = "/마키마게임 [game: 타자게임,암산게임,한자게임] [difficulty: 초보,중수,고수]", value = "마키마와 게임을 합니다", inline = False)
    embed.add_field(name = "/마키마소환", value = "현재 접속해 있는 음성 채널에 마키마를 불러냅니다", inline = False)
    embed.add_field(name = "/마키마봉인", value = "음성 채널에 있는 마키마를 내보냅니다", inline = False)
    embed.add_field(name = "/마키GG [game: 롤,배그] [playername]", value = "해당 유저의 롤 정보를 보여줍니다", inline = False)
    embed.add_field(name = "/마키마별명변경 [@mention.member] [newname]", value = "해당하는 유저의 별명을 변경합니다", inline = False)
    embed.add_field(name = "/마키마노래차트 [value: jpop,kpop,pop]", value = "해당하는 종류의 노래 차트를 보여줍니다(Bugs!)", inline = False)
    embed.add_field(name = "/마키마활동점수 [@mention.member]", value = "해당 멤버의 활동 점수를 보여줍니다", inline = False)
    embed.add_field(name = "/마키마노래 [urllink]", value = "해당하는 유튜브링크의 노래를 재생해줍니다", inline = False)
    embed.add_field(name = "/마키마정지", value = "노래를 재생하고 있다면, 즉시 종료합니다", inline = False)
    embed.add_field(name = "/마키마일시정지", value = "노래를 재생하고 있다면, 즉시 일시징지합니다", inline = False)
    embed.add_field(name = "/마키마다시재생", value = "노래를 일시정지 했다면, 정지했던 부분에서 마저 재생합니다", inline = False)
    embed.add_field(name = "/마키마운세 [애정, 재물, 장래, 행운]", value = "마키마가 운세를 봐 줍니다", inline = False)
    embed.add_field(name = "/마키마뽑기 [number: int]", value = "행운의 인물을 뽑습니다", inline = False)
    embed.add_field(name = "/마키마사다리타기 [number: int] [numbers: list]", value = "지정된 횟수 만큼 랜덤한 숫자를 뽑습니다", inline = False)
    await ctx.reply(embed=embed)
    print(f"{logtimeline} : {str(ctx.author)} issued command /마키마도움")
   
@client.command(aliases = ['마키GG', '마키gg', '마킿ㅎ', '마키마GG', 'akzlgg', 'akzlGG'])
async def makigg (ctx, game, username) :
    if game == '롤' or game == '리그오브레전드' or game == '리그 오브 레전드' :
     
        global rankvalue

        ## open urls ##

        profile_lol = urllib.parse.quote(username)
        rankvalue = ''
        profileurl_lol1 = "https://your.gg/ko/kr/profile/" + profile_lol
        profileurl_lol = "https://www.op.gg/summoner/username=" + profile_lol
        html_lol = urllib.request.urlopen(profileurl_lol)
        html_lol1 = urllib.request.urlopen(profileurl_lol1)

        ## set html.parser ##

        bs_lol = BeautifulSoup(html_lol.read(), "html.parser")
        bs_lol1 = BeautifulSoup(html_lol1.read(), "html.parser")

        ## crawling %username%'s recent match data ##

        rank_is_sf = bs_lol.find("div", {"class" : "css-1v663t e1x14w4w1"})
        if 'Unranked' in rank_is_sf.text :
            rankvalue = '자랭'
        elif 'Ranked Solo' in rank_is_sf.text :
            rankvalue = '솔랭'
            
        rank = bs_lol.find("div", {"class" : "tier"})
        ranktxt = rank.text
        
        lepoint = bs_lol.find("div", {"class" : "lp"})
        leaguepoints = lepoint.text

        winrate = bs_lol.find("div", {"class" : "ratio"})
        winratetxt = winrate.text

        userlvl = bs_lol.find("span", {"class" : "level"})
        summonerlvl = userlvl.text

        win_lose = bs_lol.find("div", {"class" : "win-lose"})
        win_lose1 = win_lose.text
        win_lose2 = win_lose1.replace("W", "승")
        win_loset = win_lose2.replace("L", "패")
        champ = bs_lol.find("div", {"class" : "champion-box"})
        champ1 = champ.find("div", {"class" : "info"})
        champ2 = champ1.find("a", {"target" : "_blank"})
        champt = champ2.text

        mainlines = bs_lol1.find("div", {"class" : "sc-18rxd2l-3 klpTdv"})
        mainline1 = mainlines.text
        mainline2 = mainline1.replace(" 경", "경")

        champrate = bs_lol.find("div", {"class" : "count"})
        champrate1 = champrate.text

        ## declaration embed and set fields ##
        embed_lol = discord.Embed(color = 0xa53939, title = f"{username}")

        embed_lol.set_author(name = "League Of Legends")
        embed_lol.set_footer(text = "From Official Riot API")
        embed_lol.add_field(name = "레벨", value = summonerlvl, inline = False)
        embed_lol.add_field(name = "티어", value = ranktxt + f"({rankvalue})")
        embed_lol.add_field(name = "LP", value = leaguepoints, inline = True)
        embed_lol.add_field(name = "승률", value = winratetxt.replace("Win Rate", ""), inline = False)
        embed_lol.add_field(name = "승패비율", value = win_loset, inline = False)
        embed_lol.add_field(name = "챔피언", value = champt, inline = True)
        embed_lol.add_field(name = "사용횟수", value = champrate1, inline = True)
        embed_lol.add_field(name = "주 라인", value = mainline2, inline = False)
        

        ## set embed tier thumbnail ##

        if 'iron' in ranktxt :
            embed_lol.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/iron.png?image=q_auto,f_webp,w_144&amp;v=1675751623531')
        elif 'bronze' in ranktxt :
            embed_lol.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/bronze.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
        elif 'silver' in ranktxt :
            embed_lol.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/silver.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
        elif 'gold' in ranktxt :
            embed_lol.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/gold.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
        elif 'platinum' in ranktxt :
            embed_lol.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/platinum.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
        elif 'diamond' in ranktxt :
            embed_lol.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/diamond.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
        elif 'master' in ranktxt :
            embed_lol.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/master.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
        elif 'grandmaster' in ranktxt :
            embed_lol.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/grandmaster.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
        elif 'challenger' in ranktxt :
            embed_lol.set_thumbnail(url = 'https://opgg-static.akamaized.net/images/medals_new/challenger.png?image=q_auto,f_webp,w_144&amp;v=1675751623266')
        await ctx.reply(embed=embed_lol) # reply embed 
        print(f"{logtimeline} : {str(ctx.author)} issued command /마키GG of {username}") 
    
    elif game == '배그' or game == '배틀그라운드' or game == 'battlegrounds' :
        await ctx.reply(embed = discord.Embed(color = 0xa53939, description = "미안해 아직 지원하지 않는 기능이야"))
        # profileurl_pubg = "https://pubg.op.gg/user/" + username # open urls
        # html_pubg = urllib.request.urlopen(profileurl_pubg)

        # bs_pubg = BeautifulSoup(html_pubg.read(), "html.parser") # set parser
       
        # ## crawling %username%'s recent match data ## 

        # platform = bs_pubg.find("span", {"class" : "player-summary__platform-txt"}).text
        # platform_ = platform.replace("Platform: ", "")
        # avg_rank = bs_pubg.find("div", {"class" : "recent-matches__avg-rank"}).text
        # avg_rank_1 = avg_rank.replace("#", "")
        # avg_rank_ = str(round(float(avg_rank_1))).replace(".0", "")
        # avg_kda = bs_pubg.find("div", {"class" : "recent-matches__stat-value--good"}).text
        # avg_stat = bs_pubg.find_all("div", {"class" : "recent-matches__stat-value"})
        # avg_dmg = avg_stat[1]
        # avg_damage = avg_dmg['data-damage']
        # avg_st = avg_stat[2]
        # avg_survtime = avg_st['data-survive-time']
        # average_damage = str(round(float(avg_damage), 0)).replace(".0", "")
        # average_survivaltime = str(round(float(int(str(round(float(avg_survtime), 0)).replace(".0", "")) / 60), 0)).replace(".0", "")
        # current_players = bs_pubg.find("a", {"class" : "current-user__count"}).text


        # ## declaration embed and set fields ##
        # embed_pubg = discord.Embed(color = 0xa53939, title = "최근 20경기 요약")
        # embed_pubg.set_author(name = f"{username}")
        # embed_pubg.set_thumbnail(url = 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAxODEwMThfMTI3%2FMDAxNTM5ODUyOTMwMzAw.FgvGPP10LjuSUZU4Km3Umb9bS8RszFnwBwWXUNJmFBIg.nVyrHPQxPdARfP9jJ-n_B37xGEYHAeNPnZypyi63LVQg.JPEG.pmsil%2F1668647a6874c329e_png.jpg&type=sc960_832')
        # embed_pubg.add_field(name = "이용 플랫폼", value = f"{platform_}")
        # embed_pubg.add_field(name = " 평균 순위", value = f" {avg_rank_}위")
        # embed_pubg.add_field(name = " 평균 KDA", value = f" {avg_kda}", inline = False)
        # embed_pubg.add_field(name = "평균 피해량", value = f"{average_damage}")
        # embed_pubg.add_field(name = "평균 생존 시간", value = f"{average_survivaltime}분")
        # embed_pubg.set_footer(text = f"From Krafton: PUBG API: [{current_players}]")
        # await ctx.reply(embed = embed_pubg) # reply embed
    elif game == '발로' or game == '발로란트' or game == 'valorant' :
        await ctx.reply(embed = discord.Embed(color = 0xa53939, description = "미안해 아직 지원하지 않는 기능이야"))
    elif game == '옵치' or game == '옵치2' or game == '오버워치' or game == '오버워치2' :
        await ctx.reply(embed = discord.Embed(color = 0xa53939, description = "미안해 아직 지원하지 않는 기능이야"))
    elif game == '이리' or game == '이터널리턴' :
        await ctx.reply(embed = discord.Embed(color = 0xa53939, description = "미안해 아직 지원하지 않는 기능이야"))


@client.command(aliases = ['마키마노래차트', 'akzlakshfockxm'])
async def makimarank(ctx, value) :
    if value == 'jpop' or value == 'JPOP' :
        daytime = datetime.now()
        jpoprank = 1
        embedjpop = discord.Embed(color = 0xa53939, title = f"현 시간 {daytime.date()} 기준 J-POP 노래차트(1~25)")
        embedjpop.set_footer(text = "Bugs! 음악 랭킹 사이트의 API로, 사이트마다 다를 수 있습니다.")
        embedjpop.set_author(name = "API제공 : https://music.bugs.co.kr/chart/track/day/njpop")
        urljpop = 'https://music.bugs.co.kr/chart/track/day/njpop'
        re = requests.get(urljpop)
        bs = BeautifulSoup(re.text, "html.parser")

        jpopsongs = bs.select(".title")

        for i, item in enumerate(jpopsongs, 1) :
            if i <= 3 :
                pass
            elif i > 3 :
                embedjpop.add_field(name = f"{jpoprank}위", value = item.text)
                jpoprank += 1

        await ctx.channel.send(embed = embedjpop)
        print(f"{logtimeline} : {str(ctx.author)} issued command /마키마노래차트 jpop")

    elif value == 'kpop' or value == 'KPOP':
        daytime = datetime.now()
        kpoprank = 1
        embedkpop = discord.Embed(color = 0xa53939, title = f"현 시간 {daytime.date()} 기준 K-POP 노래 차트(1~25)")
        embedkpop.set_footer(text = "Bugs! 음악 행킹 사이트의 API로, 사이트마다 다를 수 있습니다")
        embedkpop.set_author(name = "API제공 : https://music.bugs.co.kr/genre/chart/kpop/idol/total/day")
        urlkpop = 'https://music.bugs.co.kr/genre/chart/kpop/idol/total/day'
        result = requests.get(urlkpop)
        bs1 = BeautifulSoup(result.text, "html.parser")

        kpopsongs = bs1.select(".title")

        for e, it in enumerate(kpopsongs, 1) :
            if e <= 3 :
                pass
            elif e > 3 :
                embedkpop.add_field(name = f"{kpoprank}위", value = it.text)
                kpoprank += 1      

        await ctx.channel.send(embed = embedkpop)
        print(f"{logtimeline} : {str(ctx.author)} issued command /마키마노래차트 kpop")

    elif value == 'pop' or value == 'POP' :
        daytime = datetime.now()
        poprank = 1
        embedpop = discord.Embed(color = 0xa53939, title = f"현 시간 {daytime.date()} 기준 POP 노래 차트")
        embedpop.set_footer(text = "Bugs! 음악 행킹 사이트의 API로, 사이트마다 다를 수 있습니다")
        embedpop.set_author(name = "https://music.bugs.co.kr/genre/chart/pop/pop/total/day")
        urlpop = 'https://music.bugs.co.kr/genre/chart/pop/pop/total/day'
        req = requests.get(urlpop)
        bes1 = BeautifulSoup(req.text, "html.parser")

        popsongs = bes1.select(".title")

        for j, item1 in enumerate(popsongs, 1) :
            if j <= 3 :
                pass
            elif j > 3 :
                embedpop.add_field(name = f"{poprank}위", value = item1.text)
                poprank += 1
        
        await ctx.channel.send(embed = embedpop)
        print(f"{logtimeline} : {str(ctx.author)} issued command /마키마노래차트 pop")





@client.command(aliases = ['마키마별명변경', 'akzlakqufaudqusrud'])
async def change_nick(ctx, membername: discord.Member, *, newname) :
    members_database = {"米津玄師(よねづけんし)#9185" : "(천태성/공주마이스터고등학교)", "튀르이#7961" : "(박서용/용화중학교)", "박조비#5083" : "(옥은정/온양여자고등학교)", "Aarumida#1311" : "(임우진/충남외국어고등학교)", "민아대가리#5105" : "(이건희/공주마이스터고등학교)", "안태현#1169" : "(안태현/온양고등학교)", "왕쟈.#3901" : "(안세은/고등학교)", "sdttwz#5167" : "(한주희/용화고등학교)", "minhyuk#5083" : "(김민혁/용화고등학교)", "딕코#4641" : "(김남준/온양고등학교)", "메타몽#8158" : "(박희민/용화고등학교)", "박희영#5169" : "(박희영/용화고등학교)", "붉점#0865" : "(최영현/아산고등학교)", "악어고기#5083" : "(이하원/용화고등학교)", "암살장인#9241" : "(유 찬/용화고등학교)", "오민규#7426" : "(오민규/아산고등학교)", "이건희#5624" : "(이건희/온양고등학교)", "찍히지 않았읍니다#6561" : "(김연호/온양고등학교)", "마고가아닙니다#7719" : "(장재성/용화고등학교)", "카직스 장인#6332" : "(정연승/천안제일고등학교)", "할게없어#8500" : "(이헌재/온양고등학교)", "음😕#7004" : "(김영환/온양고등학교)", "김가을#2611" : "(김가을/용화고등학교)"}
    if str(membername) != str(ctx.author) :
        await ctx.channel.send(embed = discord.Embed(color = 0xa53939, description = "자신의 이름만 변경 할 수 있어요"))
    elif str(membername) == str(ctx.author) :
        result_name = newname.replace("_", " ")
        names = list(members_database.keys())
        if str(membername) in names :
            await membername.edit(nick = f"{result_name} {members_database[str(ctx.author)]}")
        else :
            await ctx.reply(embed = discord.Embed(color = 0xa53939, description = "데이터베이스에 등록되어 있지않거나 잘못된 이름입니다. 개발자에게 문의 해 주세요"))
        print(f"{logtimeline} : {str(ctx.author)} issued command /마키마별명변경 of {membername} to {result_name}")



@client.command(aliases = ['마키마활동점수', 'akzlakghkfehdwjatn'])
async def check_actpoint (ctx, member: discord.Member) :
    try :
        embed = discord.Embed(color = 0xa53939, title = f"{member}님의 활동 점수", description = f"{activity_point[str(member)]}점")
        embed.set_footer(text = "1주일 마다 역할을 변경할 때 활동 점수가 높은 순서로 추첨을 합니다")
        await ctx.channel.send(embed = embed)
        print(f"{logtimeline} : {str(ctx.author)} issued command /마키마활동점수 of {member}")
    except :
        embed = discord.Embed(color = 0xa53939, title = f"Error Forbidden 401 : {member} is not logged database or parameter is not assigned.")
        await ctx.channel.send(embed = embed)



@client.command(aliases = ['마키마뽑기'])
async def random_player(ctx, num) :
    database_member = ['米津玄師(よねづけんし)#9185', '카직스 장인#6332', '박조비#5083', 'sdttwz#5167', 'minhyuk#4379', 'ANG#5105', '오민규#7426', 'Aarumida#1311', '김가을#2611', '딕코#4641', '암살장인#9241', '메타몽#8158', '박희영#5169', '붉점#0865', '악어고기#8198', '안태현#1169', '이건희#5624', '찍히지 않았읍니다#6561', '튀르이#7961', '마고가아닙니다#7719', '할게없어#8500', '음😕#7004']
    for member in range(1, int(num)+1, 1) :
        await ctx.channel.send(embed = discord.Embed(color = 0xa53939, title = f"행운의 {member}번째 주인공은..?", description = f"{choice(database_member)}"))
        await asyncio.sleep(0.2)


@client.command(aliases = ['마키마사다리타기'])
async def member(ctx, num, list) :
    ladders = list.split(',')
    for index in range(1, int(num)+1, 1) :
        await ctx.channel.send(embed = discord.Embed(color = 0xa53939, title = f"행운의 주인공 {index}번째는?",  description = f"{choice(ladders)}"))



try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
