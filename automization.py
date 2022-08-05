import pandas as pd
import discord
from discord.ext import commands
from discord.utils import get
from module import *

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!',intents=intents)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------------')


@bot.command()
async def 정회원(ctx):
    f = open("serverId.txt","r")
    serverId = int(f.readline())
    f.close()
    server = bot.get_guild(serverId)
    await ctx.send("-------------------------------------------")
    await ctx.send("=접속 서버 정보=")
    await ctx.send(f'이름: {server}')
    await ctx.send(f'서버 id: {server.id}')

    nameOfDepositorList = saveNameOfDepositorList()
    await ctx.send("-------------------------------------------")
    await ctx.send("입금자 명단 :")
    await ctx.send(nameOfDepositorList)

    await ctx.send("-------------------------------------------")
    listOfGoogleFormWriter = saveListOfGoogleFormWriter()
    await ctx.send("입금 확인 폼 작성자: ")
    await ctx.send(listOfGoogleFormWriter)
    await ctx.send("-------------------------------------------")

    militaryLeaveMemberList = readMilitaryLeaveMemberList()
    await ctx.send("기존 회원 중 군휴학자: ")
    await ctx.send(militaryLeaveMemberList)
    await ctx.send("-------------------------------------------")

    checkMemberList = []

    for i in range(len(listOfGoogleFormWriter)):
        name = listOfGoogleFormWriter.loc[i,'(2자리)  학번이름 (띄어쓰기 하지말아주세요!)']
        discriminator = listOfGoogleFormWriter.loc[i,'디스코드 사용자번호']
        if name in nameOfDepositorList.loc[:,'내용'].values:
            checkMemberList.append((name, discriminator))

    for i in range(len(server.members)):
        member = server.members[i]
        name = member.name
        nickname = member.nick
        discriminator = member.discriminator
        role = get(server.roles, name="정회원")
        if role in member.roles: # 이미 정회원인 사람은 생략
            continue
        for j in range(len(checkMemberList)):
            checkName = checkMemberList[j][0][2:]
            checkDiscriminator = checkMemberList[j][1][1:]
            if checkDiscriminator == discriminator:
                if nickname == None:
                    if name == checkName:
                        await member.add_roles(role)
                        await ctx.send(f'사용자번호 #{discriminator} {checkName} 님이 정회원이 되었습니다')
                        break
                else:
                    if nickname == checkName:
                        await member.add_roles(role)
                        await ctx.send(f'사용자번호 #{discriminator} {checkName} 님이 정회원이 되었습니다')
                        break 

        # 군휴학
        for j in range(len(militaryLeaveMemberList)):
           checkName = militaryLeaveMemberList.values[j][0]
           checkDiscriminator = militaryLeaveMemberList.values[j][2][len(militaryLeaveMemberList.values[j][2]) - 4:] 
           if checkDiscriminator == discriminator:
               if nickname == None:
                   if name == checkName:
                       await member.add_roles(role)
                       await ctx.send(f'사용자번호 #{discriminator} {checkName} 님이 정회원이 되었습니다')
                       break
               else:
                   if nickname == checkName:
                       await member.add_roles(role)
                       await ctx.send(f'사용자번호 #{discriminator} {checkName} 님이 정회원이 되었습니다')
                       break
    await ctx.send("-------------------------------------------")
    await ctx.send("FINISH")

@bot.command()
async def 준회원(ctx):
    await ctx.send("-------------------------------------------")
    await ctx.send("준회원 목록")
    await ctx.send("-------------------------------------------")

    f = open("serverId.txt","r")
    serverId = int(f.readline())
    f.close()
    server = bot.get_guild(serverId)

    for i in range(len(server.members)):
        member = server.members[i]
        name = member.name
        nickname = member.nick
        discriminator = member.discriminator
        if len(member.roles) == 1:
            await ctx.send(f'이름 : {name}, 닉네임 : {nickname}, 사용자번호 : {discriminator}')
    await ctx.send("FINISH")

# 보안 때문에 봇 token 값은 다른 파일에 보관 + gitignore 파일에 해당 txt 파일을 추가해서 깃허브에 올라가지 않도록
f = open("token.txt","r")
TOKEN = f.readline()
f.close()

bot.run(TOKEN)