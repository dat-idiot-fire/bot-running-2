import discord
from itertools import cycle
from discord.ext import commands, tasks
import math
import random
from discord.ext.commands import CommandNotFound
import asyncio
import sys
import traceback
from async_timeout import timeout
from functools import partial 
import json 
from discord.ext.commands.cooldowns import BucketType
from discord.utils import get
import datetime
import os
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient

epoch = datetime.datetime.utcfromtimestamp(0)
bot = commands.Bot(command_prefix = "$")
status = cycle(['$help'])
howgay_rate   = [10, 69, 15, 13, 32, 23, 75, 26, 45, 92, 87, 78, 65, 2, 14, 53, 90, 43]
START_BAL     = 100 
START_HEALTH  = 100
BALANCES_FILE = 'balances.json'
balances      = {} 
SHEEPS_FILE   = 'sheeps.json'
sheeps        = {}
WOOL_FILE     = 'wools.json'
wools         = {}
RICE_FILE     = 'rices.json'
rices         = {}
WHEAT_FILE    = 'wheats.json'
wheats        = {}
PIG_FILE      = 'pigs.json'
pigs          = {}
MEAT_FILE     = 'meats.json'
meats         = {}
HEALTH_FILE   = 'healths.json'
healths       = {}  
AMBULANCES_FILE = 'ambulances.json'
ambulances    = {}
BUFFALOS_FILE = 'buffalos.json'
buffalos      = {}
STOVES_FILE   = 'stoves.json'
stoves        = {}
SALADS_FILE   = 'salads.json'
salads        = {}
UNCOOKED_CHICKENS_FILE = 'uncooked_chickens.json'
uncooked_chickens = {}
COOKED_CHICKENS_FILE = 'cooked_chickens.json'
cooked_chickens = {}

@bot.event
async def on_ready():
  change_status.start()
  print(f'{bot.user.name} is ready to kick some ass')
  global balances, wools, sheeps, rices, wheats, pigs, meats, healths, ambulances, buffalos, stoves, uncooked_chickens, cooked_chickens, salads
  
  try:
    with open(BALANCES_FILE, 'r') as fp: 
      balances = json.load(fp) 
  except FileNotFoundError: 
    print(f'In on_ready(): File {BALANCES_FILE} not found. Starting off with an empty balances dictionary.') 
    balances = {} 

  try:
    with open(SHEEPS_FILE, 'r') as fp:
      sheeps = json.load(fp)
  except FileNotFoundError:
    print(f'In on_ready(): File {SHEEPS_FILE} not found. Starting off with an empty dictionary')
    sheeps = {}

  try:
    with open(WOOL_FILE, 'r') as fp:
      wools = json.load(fp)
  except FileNotFoundError:
    print(f'In on_ready(): File {WOOL_FILE} not found. Starting off with an empty dictionary')
    wools = {}

  try:
    with open(RICE_FILE, 'r') as fp:
      rices = json.load(fp)
  except FileNotFoundError:
    print(f'In on_ready(): File {RICE_FILE} not found. Starting off with an empty dictionary')
    rices = {}

  try:
    with open(WHEAT_FILE, 'r') as fp:
      wheats = json.load(fp)
  except FileNotFoundError:
    print(f'In on_ready(): File {WHEAT_FILE} not found. Starting off with an empty dictionary')
    wheats = {}

  try:
    with open(PIG_FILE, 'r') as fp:
      pigs = json.load(fp)
  except FileNotFoundError:
    print(f'In on_ready(): File {PIG_FILE} not found. Starting off with an empty dictionary')
    pigs = {}

  try:
    with open(MEAT_FILE, 'r') as fp:
      meats = json.load(fp)
  except FileNotFoundError:
    print(f'In on_ready(): File {MEAT_FILE} not found. Starting off with an empty dictionary')
    meats = {}

  try:
    with open(HEALTH_FILE, 'r') as fp:
      healths = json.load(fp)
  except FileNotFoundError:
    print(f'In on_ready(): File {HEALTH_FILE} not found. Starting off with an empty dictionary')
    healths = {}

  try:
    with open(AMBULANCES_FILE, 'r') as fp:
      ambulances = json.load(fp)
  except FileNotFoundError:
    print(f'In on_ready(): File {AMBULANCES_FILE} not found. Starting off with an empty dictionary')
    ambulances = {}

  try:
    with open(BUFFALOS_FILE, 'r') as fp:
      buffalos = json.load(fp)
  except FileNotFoundError:
    print(f'In on_ready(): File {BUFFALOS_FILE} not found. Starting off with an empty dictionary')
    buffalos = {}

  try:
    with open(STOVES_FILE, 'r') as fp:
      stoves = json.load(fp)
  except FileNotFoundError:
    print(f'In on_ready(): File {STOVES_FILE} not found. Starting off with an empty dictionary')
    stoves = {}

  try:
    with open(UNCOOKED_CHICKENS_FILE, 'r') as fp:
      uncooked_chickens = json.load(fp)
  except FileNotFoundError:
    print(f'In on_ready(): File {UNCOOKED_CHICKENS_FILE} not found. Starting off with an empty dictionary')
    uncooked_chickens = {}

  try:
    with open(COOKED_CHICKENS_FILE, 'r') as fp:
      cooked_chickens = json.load(fp)
  except FileNotFoundError:
    print(f'In on_ready(): File {COOKED_CHICKENS_FILE} not found. Starting off with an empty dictionary')
    cooked_chickens = {}

  try:
    with open(SALADS_FILE, 'r') as fp:
      salads = json.load(fp)
  except FileNotFoundError:
    print(f'In on_ready(): File {SALADS_FILE} not found. Starting off with an empty dictionary')
    salads = {}


@tasks.loop(seconds=20)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))  

@bot.command()
async def join(ctx):
   channel = ctx.author.voice.channel
   await channel.connect()
   await ctx.send('LOL i joined')

@bot.command()
async def thotsbegone(ctx):
  await ctx.send('thots')
  await asyncio.sleep(1.5)
  await ctx.send('be')
  await asyncio.sleep(1.5)
  await ctx.send('GONE')

# @bot.command()
# async def info(ctx):
#   embed

@bot.command()
async def yo(ctx):
    await ctx.send('yo whattup')

@bot.command()
async def howgay(ctx):  
    embed = discord.Embed(title="gay boi determiner", description=f"You are {random.choice(howgay_rate)}% gay", color=0xeee657)
    await ctx.send(embed=embed)

@bot.command()
async def meme(ctx):
  meme_generator = [

    "https://imgflip.com/i/2xt9op",

    "https://imgflip.com/i/3fromx",

    "https://imgflip.com/i/3ffiq7",

    "https://imgflip.com/i/3f4b9t",

    "https://imgflip.com/i/3fkhhv",

    "https://imgflip.com/i/3fhbuj",

    "https://imgflip.com/i/3fcqsw",

    "https://imgflip.com/i/3fmtla",

    "https://imgflip.com/i/3fcum2",

    "https://imgflip.com/i/3frpkv",

    "https://imgflip.com/i/3fnxiz",

    "https://imgflip.com/i/25pypz",

    "https://imgflip.com/i/3fkzwn",

    "https://imgflip.com/i/3fcshx",

    "https://imgflip.com/i/3fgnlj",

    "https://imgflip.com/i/3filv4",

    "https://imgflip.com/i/3fl2tm",

    "https://imgflip.com/i/2y09tm",

    "https://imgflip.com/i/2hp9ev",

    "https://imgflip.com/i/3fglhy",

    "https://imgflip.com/i/3ftez0"
  
  ]
  await ctx.send(random.choice(meme_generator))

#------------------------
#------------------------
#MOD COMMANDS
#------------------------
#------------------------ 

# @bot.command()
# async def mission(ctx):
#   await ctx.send('A man with a briefcase approaches you, desperate for money.')
#   await asyncio.sleep(2.5)
#   await ctx.send('**Businessman**: I have an opportunity for you...')
#   await asyncio.sleep(2.5)
#   await ctx.send('**You**: the fuck you want, rich boy?')
#   await asyncio.sleep(2.5)
#   await ctx.send('**Businessman**: Give me 25000 meat and i will grant you a fortune...')
#   await asyncio.sleep(2.5)
#   await ctx.send('**You**: fuck off with your bullshit scams mate')
#   await asyncio.sleep(2.5)
#   await ctx.send('**Businessman**: Son of a- You know what?')
#   await asyncio.sleep(2.5)
#   await ctx.send('**You**: What, douchebag?')
#   await asyncio.sleep(2.5)
#   await ctx.send('**Businessman**: Get to work or you\'re gonna get deported!')
#   await asyncio.sleep(2.5)
#   await ctx.send('**You**: OH SHI- i gotchu fam')
#   await asyncio.sleep(2.5)
#   await ctx.send('**Mission**: give the businessman his meat with `$complete` or just don\'t do it LOL.')

@bot.command()
async def credits(ctx):
  await ctx.send('My Creator: Crypto#5318\nLead Programmer: Crypto#5318\nSupporters and Dev: Gay Potato#4928 and Detective#5368')

@bot.command()
async def userinfo(ctx, member: discord.Member, *args):
  if member == None:
    await ctx.send('oi gimme someone to get info on')
  else:
    roles = [role for role in member.roles]

    embed=discord.Embed(colour=member.color, timestamp=ctx.message.created_at)

    embed.set_author(name=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)

    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Guild name:", value=member.display_name)
    embed.add_field(name="Created at:", value=member.created_at.strftime("%a, %d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Joined at:", value=member.joined_at.strftime("%a, %d %B %Y, %I:%M %p UTC"))

    embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]))
    embed.add_field(name="Top role:", value=member.top_role.mention)

    embed.add_field(name="Bot?", value=member.bot)
    embed.add_field(name="Idiot?", value="True")

    await ctx.send(embed=embed) 

@bot.command()
@commands.has_any_role("Moderator")
async def ban(ctx, member: discord.Member=None, *, reason=None, guild: discord.Guild):
  if member == None or member == ctx.message.author:
    await ctx.send("oi stupid ya can\'t ban yourself")
    return
  elif reason == None:
    reason = "No reason given"
    await member.ban(reason=reason)
    await ctx.send(f"```{member} was banned for {reason}```")
  else:
    await member.ban(reason=reason)
    await ctx.send(f"```{member} was banned for {reason}```")

@bot.command()
@commands.has_any_role("Moderator")
async def kick(ctx, member: discord.Member = None, *, reason = None, guild: discord.Guild):
  if member == None or member == ctx.message.author:
    await ctx.send('You cant kick yourself')
    return
  elif reason == None:
    reason = "No reason given"
    await member.kick(reason=reason)
    await ctx.send(f'```{member} was kicked for {reason}')
  else:
    await member.kick(reason = reason)
    await ctx.send(f'```{member} was kicked for {reason}')


@bot.command()
async def warn(ctx, member: discord.Member = None, reason = None):
  if member == None or member == ctx.message.author:
    await ctx.send("oi stupid ya can\'t warn yourself")
    return
  elif reason == None:
    message = "This is a test"
    reason = "No reason given"
    await ctx.send(f"```{member} was warned\nReason: {reason}```")
    await member.send(message)
  else:
    message = "This is a test"
    await member.send(message)
    await ctx.send(f"```{member} was warned\nReason: {reason}```")

#------------------------
#------------------------
#CURRENCY COMMANDS
#------------------------
#------------------------

# @bot.command()
# async def lol(ctx):
#   await ctx.send('cheydaye is gay she luv adam and joshua')

@bot.command()
async def notebook(ctx):
  embed = discord.Embed(title = "Grandma Esther's notebook", description = "only boomers keep recipes in a notebook")
  embed.add_field(name = ":salad: Salad", value = "Ingredients | 5 Chicken, 9 Rice")
  await ctx.send(embed = embed)


@bot.command()
async def combine(ctx, arg1, arg2):
  global rices, cooked_chickens, salads
  user = str(ctx.message.author.id)
  if arg1 == "chicken" and arg2 == "rice" or arg1 == "rice" and arg2 == "chicken":
    cooked_chickens[user] = cooked_chickens[user] if user in cooked_chickens else 0
    rices[user] = rices[user] if user in rices else 0
    salads[user] = salads[user] if user in salads else 0
    if rices[user] > 9 and cooked_chickens[user] > 5:
      rices[user] -= 9
      cooked_chickens[user] -= 5
      await ctx.send(f'{ctx.message.author.mention} has just combined his chicken and his rice to get....')
      await asyncio.sleep(1)
      await ctx.send(f'{ctx.message.author.mention} got A SALAD!!')
      salads[user] += 1
    else:
      await ctx.send('You don\'t got enough ingredients for this!')
  else:
    await ctx.send('Error ocurred. Either you put the ingredients the wrong order or you can\'t combine these.')

  print(f'In sell(): Saving rices = {rices}')
  try: 
    with open(RICE_FILE, 'w') as fp: 
      json.dump(rices, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {RICE_FILE} not found! Not sure what to do here!') 

  print(f'In sell(): Saving salads = {salads}')
  try: 
    with open(SALADS_FILE, 'w') as fp: 
      json.dump(salads, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {SALADS_FILE} not found! Not sure what to do here!') 

  print(f'In sell(): Saving cooked chicken = {cooked_chickens}')
  try: 
    with open(COOKED_CHICKENS_FILE, 'w') as fp: 
      json.dump(cooked_chickens, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {COOKED_CHICKENS_FILE} not found! Not sure what to do here!') 

@bot.command()
async def pharmacy(ctx):
  embed = discord.Embed(title = "Crypto's underground pharmacy", description = "`buy <item> <amount>` or `sell <item> <amount>`\n No selling `ambulance` because it is too rare.")
  embed.add_field(name = ":medical_symbol: Meds", value = ":ambulance: Ambulance | Price: :cut_of_meat: 15,200 | Puts your health back to 100\n")
  await ctx.send(embed = embed)

@bot.command()
@commands.cooldown(1, 18000, commands.BucketType.user)
async def rice(ctx):
  global rices, wheats, healths
  user = str(ctx.message.author.id)
  healths[user] = healths[user] if user in healths else 100
  if healths[user] > 5 or healths[user] == 5:
    if user in rices:
      wheats[user] = wheats[user] if user in wheats else 0
      wheat = rices[user] * 4
      wheats[user] += wheat
      healths[user] -= 5  
      embed = discord.Embed(title = f'{ctx.message.author}\'s harvest ', description = f"{ctx.message.author} just recieved :tanabata_tree: {wheat} wheat from his :rice: rice")
      await ctx.send(embed = embed)   
    else:
      await ctx.send('You don\'t have any rice')
  else:
    await ctx.send('You don\'t have enough health for this action!')

  print(f'In sell(): Saving rices = {rices}')
  try: 
    with open(RICE_FILE, 'w') as fp: 
      json.dump(rices, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {RICE_FILE} not found! Not sure what to do here!') 

  print(f'In sell(): Saving wheat = {wheats}')
  try: 
    with open(WHEAT_FILE, 'w') as fp: 
      json.dump(wheats, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {WHEAT_FILE} not found! Not sure what to do here!') 

  print(f'In pigs(): Saving healths = {healths}')
  try: 
    with open(HEALTH_FILE, 'w') as fp: 
      json.dump(healths, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {HEALTH_FILE} not found! Not sure what to do here!') 


@bot.command()
@commands.cooldown(1, 18000, commands.BucketType.user)
async def sheep(ctx):
  global sheep, wools, healths
  user = str(ctx.message.author.id)
  healths[user] = healths[user] if user in healths else 100
  if healths[user] > 5 or healths[user] == 5:
    if user in sheeps:
      wools[user] = wools[user] if user in wools else 0
      wool = sheeps[user] * 3
      wools[user] += wool
      healths[user] -= 5
      embed = discord.Embed(title = f'{ctx.message.author}\'s harvest', description = f"{ctx.message.author} just recieved :scroll: {wool} wool from his :sheep: sheep")
      await ctx.send(embed = embed)   
    else:
      await ctx.send('You don\'t have any sheep')
  else:
    await ctx.send('You don\'t have enough health for this action!')


  print(f'In sell(): Saving sheep = {sheeps}')
  try: 
    with open(SHEEPS_FILE, 'w') as fp: 
      json.dump(sheeps, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {SHEEPS_FILE} not found! Not sure what to do here!') 

  print(f'In sell(): Saving wool = {wools}')
  try: 
    with open(WOOL_FILE, 'w') as fp: 
      json.dump(wools, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {WOOL_FILE} not found! Not sure what to do here!') 

  print(f'In pigs(): Saving healths = {healths}')
  try: 
    with open(HEALTH_FILE, 'w') as fp: 
      json.dump(healths, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {HEALTH_FILE} not found! Not sure what to do here!') 

@bot.command()
@commands.cooldown(1, 18000, commands.BucketType.user)
async def buffalos(ctx):
  global buffalos, meats, wheats, healths
  user = str(ctx.message.author.id)
  healths[user] = healths[user] if user in healths else 100
  if healths[user] > 20 or healths[user] == 20:
    if user in buffalos:
      wheats[user] = wheats[user] if user in wheats else 0
      meats[user] = meats[user] if user in meats else 0
      wheat2 = buffalos[user] * 10000
      wheats[user] += wheat2
      meat2 = buffalos[user] * 10000
      meats[user] += meat2
      healths[user] -= 20
      embed = discord.Embed(title = f'{ctx.message.author}\'s harvest ', description = f"{ctx.message.author} just recieved :cut_of_meat: {meat2} meat and :ear_of_rice: {wheat2} wheat from his :water_buffalo: Buffalos")
      await ctx.send(embed = embed)   
    else:
      await ctx.send('You don\'t have any buffalos!')
  else:
    await ctx.send('You don\'t have enough health for this action!')

  print(f'In sell(): Saving buffalos = {buffalos}')
  try: 
    with open(BUFFALOS_FILE, 'w') as fp: 
      json.dump(buffalos, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {BUFFALOS_FILE} not found! Not sure what to do here!') 

  print(f'In sell(): Saving wheats = {wheats}')
  try: 
    with open(WHEAT_FILE, 'w') as fp: 
      json.dump(wheats, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {WHEAT_FILE} not found! Not sure what to do here!') 
  
  print(f'In sell(): Saving meats = {meats}')
  try: 
    with open(MEAT_FILE, 'w') as fp: 
      json.dump(meats, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {MEAT_FILE} not found! Not sure what to do here!') 

  print(f'In pigs(): Saving healths = {healths}')
  try: 
    with open(HEALTH_FILE, 'w') as fp: 
      json.dump(healths, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {HEALTH_FILE} not found! Not sure what to do here!') 

@bot.command()
@commands.cooldown(1, 18000, commands.BucketType.user)
async def cook(ctx, arg):
  global uncooked_chickens, cooked_chickens, stoves, healths
  user = str(ctx.message.author.id)
  healths[user] = healths[user] if user in healths else 100
  stoves[user] = stoves[user] if user in stoves else 0
  cooked_chickens[user] = cooked_chickens[user] if user in cooked_chickens else 0
  uncooked_chickens[user] = uncooked_chickens[user] if user in uncooked_chickens else 0 
  if arg == "chicken" or arg == "chickens":
    if healths[user] > 10 or healths[user] == 10:
      if user in stoves:
        if stoves[user] > 0:
          if user in uncooked_chickens:
            chicken = uncooked_chickens[user] * 3
            cooked_chickens[user] += chicken
            healths[user] -= 10
            stoves[user] -= 1
            embed = discord.Embed(title = f'{ctx.message.author}\'s harvest ', description = f"{ctx.message.author} just recieved :chicken: {chicken} chickens from his :hatched_chick: Uncooked Chickens!")
            await ctx.send(embed = embed)   
          else:
            await ctx.send('You don\'t have any uncooked chickens!')  
        else:
          await ctx.send('You don\'t have any stoves!')
      else:
        await ctx.send('You don\'t have any stoves!')
    else:
      await ctx.send('You don\'t have enough health for this action!')
  elif arg == None:
    await ctx.send('Specify what to cook!')
  else:
    await ctx.send('Specify what to cook!')

  print(f'In pigs(): Saving healths = {healths}')
  try: 
    with open(HEALTH_FILE, 'w') as fp: 
      json.dump(healths, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {HEALTH_FILE} not found! Not sure what to do here!') 

  print(f'In pigs(): Saving stoves = {stoves}')
  try: 
    with open(STOVES_FILE, 'w') as fp: 
      json.dump(stoves, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {STOVES_FILE} not found! Not sure what to do here!') 

  print(f'In pigs(): Saving uncooked chickens = {uncooked_chickens}')
  try: 
    with open(UNCOOKED_CHICKENS_FILE, 'w') as fp: 
      json.dump(uncooked_chickens, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {UNCOOKED_CHICKENS_FILE} not found! Not sure what to do here!') 

  print(f'In pigs(): Saving cooked chickens = {cooked_chickens}')
  try: 
    with open(COOKED_CHICKENS_FILE, 'w') as fp: 
      json.dump(cooked_chickens, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {COOKED_CHICKENS_FILE} not found! Not sure what to do here!') 

@cook.error
async def cook_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    embed = discord.Embed(title="Slow down dude", description="Stop tryna harvest so much, you look like a big baby.\nYou can have more goods in **{} seconds**.\n (5 hour cooldown)".format(math.ceil(error.retry_after)), color = 0xff0000)
    await ctx.send(embed=embed)
    return

@bot.command()
@commands.cooldown(1, 18000, commands.BucketType.user)
async def pigs(ctx):
  global pigs, meats, healths
  user = str(ctx.message.author.id)
  healths[user] = healths[user] if user in healths else 100
  if healths[user] > 5 or healths[user] == 5:
    if user in pigs:
      meats[user] = meats[user] if user in meats else 0
      meat = pigs[user] * 6
      meats[user] += meat
      healths[user] -= 5
      embed = discord.Embed(title = f'{ctx.message.author}\'s harvest ', description = f"{ctx.message.author} just recieved :cut_of_meat: {meat} meat from his :pig2: pig(s)")
      await ctx.send(embed = embed)   
    else:
      await ctx.send('You don\'t have any pigs')
  else:
    await ctx.send('You don\'t have enought health for this!')

  print(f'In sell(): Saving pigs = {pigs}')
  try: 
    with open(PIG_FILE, 'w') as fp: 
      json.dump(pigs, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {PIG_FILE} not found! Not sure what to do here!') 

  print(f'In sell(): Saving meats = {meats}')
  try: 
    with open(MEAT_FILE, 'w') as fp: 
      json.dump(meats, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {MEAT_FILE} not found! Not sure what to do here!') 

  print(f'In pigs(): Saving healths = {healths}')
  try: 
    with open(HEALTH_FILE, 'w') as fp: 
      json.dump(healths, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {HEALTH_FILE} not found! Not sure what to do here!') 

@rice.error
async def rice_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    embed = discord.Embed(title="Slow down dude", description="Stop tryna harvest so much, you look like a big baby.\nYou can have more goods in **{} seconds**.\n (5 hour cooldown)".format(math.ceil(error.retry_after)), color = 0xff0000)
    await ctx.send(embed=embed)
    return

@sheep.error
async def sheep_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    embed = discord.Embed(title="Slow down dude", description="Stop tryna harvest so much, you look like a big baby.\nYou can have more goods in **{} seconds**.\n (5 hour cooldown)".format(math.ceil(error.retry_after)), color = 0xff0000)
    await ctx.send(embed=embed)
    return

@pigs.error
async def pigs_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    embed = discord.Embed(title="Slow down dude", description="Stop tryna harvest so much, you look like a big baby.\nYou can have more goods in **{} seconds**.\n (5 hour cooldown)".format(math.ceil(error.retry_after)), color = 0xff0000)
    await ctx.send(embed=embed)
    return

# @bot.command()
# @commands.cooldown(1, 18000, commands.BucketType.user)
# async def harvest(ctx, arg):
#   global sheeps, rices, wheats, pigs, wools, meats
#   user = str(ctx.message.author.id)
#   if arg == "sheep":
#     if user in sheeps:
#       wools[user] = wools[user] if user in wools else 0
#       wool = sheeps[user] * 3 
#       wools[user] += wool
#       embed = discord.Embed(title = f'{ctx.message.author}\'s harvest ', description = f"{ctx.message.author} just recieved :scroll: {wool} wool from his :sheep: sheep")
#       await ctx.send(embed = embed)
#     else:
#       await ctx.send('yo u don\'t have any sheep')
#   elif arg == "rice":
#     if user in rices:
#       wheats[user] = wheats[user] if user in wheats else 0
#       wheat = rices[user] * 6
#       wheats[user] += wheat
#       embed = discord.Embed(title = f'{ctx.message.author}\'s harvest ', description = f"{ctx.message.author} just recieved :tanabata_tree: {wheat} wheat from his :rice: rice")
#       await ctx.send(embed = embed)
#     else:
#       await ctx.send('You don\'t have any rice')
#   elif arg == "pig" or arg == "pigs":
#     if user in pigs:
#       meats[user] = meats[user] if user in meats else 0
#       meat = pigs[user] * 4
#       meats[user] += meat
#       embed = discord.Embed(title = f'{ctx.message.author}\'s harvest ', description = f"{ctx.message.author} just recieved :cut_of_meat: {meat} meat from his :pig2: pig(s)")
#       await ctx.send(embed = embed)
#     else:
#       await ctx.send('You don\'t have any pigs to harvest')
#   else:
#     await ctx.send('What do you want to harvest?')

#   print(f'In sell(): Saving sheeps = {sheeps}')
#   try: 
#     with open(SHEEPS_FILE, 'w') as fp: 
#       json.dump(sheeps, fp) 
#   except FileNotFoundError: 
#     print(f'In sell(): File {SHEEPS_FILE} not found! Not sure what to do here!') 

#   print(f'In sell(): Saving rices = {rices}')
#   try: 
#     with open(RICE_FILE, 'w') as fp: 
#       json.dump(rices, fp) 
#   except FileNotFoundError: 
#     print(f'In sell(): File {RICE_FILE} not found! Not sure what to do here!') 

#   print(f'In sell(): Saving wheats = {wheats}')
#   try: 
#     with open(WHEAT_FILE, 'w') as fp: 
#       json.dump(wheats, fp) 
#   except FileNotFoundError: 
#     print(f'In sell(): File {WHEAT_FILE} not found! Not sure what to do here!') 

#   print(f'In sell(): Saving wools = {wools}')
#   try: 
#     with open(WOOL_FILE, 'w') as fp: 
#       json.dump(wools, fp) 
#   except FileNotFoundError: 
#     print(f'In sell(): File {WOOL_FILE} not found! Not sure what to do here!') 
  
#   print(f'In sell(): Saving meats = {meats}')
#   try: 
#     with open(MEAT_FILE, 'w') as fp: 
#       json.dump(meats, fp) 
#   except FileNotFoundError: 
#     print(f'In sell(): File {MEAT_FILE} not found! Not sure what to do here!') 

# @harvest.error
# async def harvest_error(ctx, error):
#   if isinstance(error, commands.CommandOnCooldown):
#     embed = discord.Embed(title="Slow down dude", description="Stop tryna harvest so much, you look like a big baby.\nYou can have more goods in **{} seconds**.\n (5 hour cooldown)".format(math.ceil(error.retry_after)), color = 0xff0000)
#     await ctx.send(embed=embed)
#     return

@bot.command()
async def sell(ctx, arg, amount: int):
  global balances, START_BAL, meats, wools, wheats
  user = str(ctx.message.author.id)
  if arg == "wheats" or arg == "wheat":
    if user in wheats:
      if user in balances:
        if wheats[user] > amount or wheats[user] == amount:
          balances[user] = balances[user] if user in balances else 0
          wheats[user] = wheats[user] if user in wheats else 0
          crypto_for_selling_wheat = amount * 250
          wheats[user] -= amount
          balances[user] += crypto_for_selling_wheat
          await ctx.send(f'{ctx.message.author.mention} just sold {amount} wheat for {crypto_for_selling_wheat} crypto!')
        else:
          await ctx.send('um i don\'t think you have enough wheat for that **SCAMMER**')
      else:
        print(f'In buy(): No record for {user} found. Creating a new record with a starting balance of {START_BAL}') 
        balances[user] = START_BAL 
        await ctx.send(f'hey you don\'t have a bank account yet. I just created one for you and started you off with ${START_BAL}') 
    else:
      await ctx.send('you don\'t have any wheat with you')
  elif arg == "wool" or arg == "wools":
    if user in wools:
      if user in balances:
        if wools[user] > amount or wools[user] == amount:
          balances[user] = balances[user] if user in balances else 0
          wools[user] = wools[user] if user in wools else 0
          crypto_for_selling_wool = amount * 100
          wools[user] -= amount
          balances[user] += crypto_for_selling_wool
          await ctx.send(f'{ctx.message.author.mention} just sold {amount} wool for {crypto_for_selling_wool} crypto!')
        else:
          await ctx.send('um i don\'t think you have enough wool for that **SCAMMER**')
      else:
        print(f'In buy(): No record for {user} found. Creating a new record with a starting balance of {START_BAL}') 
        balances[user] = START_BAL 
        await ctx.send(f'hey you don\'t have a bank account yet. I just created one for you and started you off with ${START_BAL}') 
    else:
      await ctx.send('you don\'t have any wool with you')
  elif arg == "meat" or arg == "meats":
    if user in meats:
      if user in balances:
        if meats[user] > amount or meats[user] == amount:
          balances[user] = balances[user] if user in balances else 0
          meats[user] = meats[user] if user in meats else 0
          crypto_for_selling_meat = amount * 500
          meats[user] -= amount
          balances[user] += crypto_for_selling_meat
          await ctx.send(f'{ctx.message.author.mention} just sold {amount} meat(s) for {crypto_for_selling_meat} crypto!')
        else:
          await ctx.send('um i don\'t think you have enough meat for that **SCAMMER**')
      else:
        print(f'In buy(): No record for {user} found. Creating a new record with a starting balance of {START_BAL}') 
        balances[user] = START_BAL 
        await ctx.send(f'hey you don\'t have a bank account yet. I just created one for you and started you off with ${START_BAL}') 
    else:
      await ctx.send('you don\'t have any meat with you')
  else:
    await ctx.send('Error occured. You maybe missing something in the command or you cannot sell this item')

  print(f'In sell(): Saving wool = {wools}')
  try: 
    with open(WOOL_FILE, 'w') as fp: 
      json.dump(wools, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {WOOL_FILE} not found! Not sure what to do here!') 

  print(f'In sell(): Saving meats = {meats}')
  try: 
    with open(MEAT_FILE, 'w') as fp: 
      json.dump(meats, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {MEAT_FILE} not found! Not sure what to do here!') 

  print(f'In sell(): Saving wheats = {wheats}')
  try: 
    with open(WHEAT_FILE, 'w') as fp: 
      json.dump(wheats, fp) 
  except FileNotFoundError: 
    print(f'In sell(): File {WHEAT_FILE} not found! Not sure what to do here!') 

@bot.command()
async def popeyes(ctx):
  embed = discord.Embed(title = "Crypto's Popeyes", description = "`$buy <item> <amount>` | `$cook <item> <amount>`")
  embed.add_field(name = ":hatched_chick: Uncooked Chicken [ANIMAL]", value = "Price: ¢10000")
  await ctx.send(embed = embed)

@bot.command()
async def shop(ctx):
  embed = discord.Embed(title = "Crypto's secret shop", description = "`$buy <item> <amount>` or `$sell <item> <amount>`\n Goods are not able to be purchased")
  # embed.add_field(name = ":sheep: Sheep [ANIMAL]", value = "Price: ¢100")
  # embed.add_field(name = ":pig2: Pig [ANIMAL]", value = "Price: ¢200")
  # embed.add_field(name = ":rice: Rice [CROP]", value = "Price: ¢30")
  # embed.add_field(name = ":water_buffalo: Buffalo [RARE]", value = "Price ¢10000000")
  # embed.add_field(name = ":cooking: Stove [MATERIAL]", value = "Price ¢19,500")
  embed.add_field(name = "Animals\n", value = "\n:sheep: Sheep | Price: ¢100\n :pig2: Pig | Price: ¢200\n :water_buffalo: Buffalo | Price: ¢10000000", inline = True)
  embed.add_field(name = "Materials\n", value = "\n:cooking: Stove | Price: ¢19,500", inline = False)
  embed.add_field(name = "Crops\n", value = "\n:rice: Rice | Price: ¢30", inline = False)
  await ctx.send(embed=embed)

@bot.command()
@commands.cooldown(1, 600, commands.BucketType.user)
async def grab(ctx):
  global balances
  AIRDROP_LOOT = random.randint(500,1200)
  user = str(ctx.message.author.id)
  if user in balances:
    embed = discord.Embed(title=f'{ctx.message.author} just grabbed an airdrop for ¢{AIRDROP_LOOT}')
    balances[user] += AIRDROP_LOOT
    await ctx.send(embed=embed)
  else:
    print(f'In buy(): No record for {user} found. Creating a new record with a starting balance of {START_BAL}') 
    balances[user] = START_BAL 
    await ctx.send(f'hey you don\'t have a bank account yet. I just created one for you and started you off with ${START_BAL}') 

@bot.command()
@commands.cooldown(1, 28800, commands.BucketType.user)
async def use(ctx, arg):
  global ambulances, healths
  user = str(ctx.message.author.id)
  if arg == "ambulances" or arg == "ambulance":
    if user in ambulances:
      if ambulances[user] > 1 or ambulances[user] == 1:
        if user in healths:
          if healths[user] < 100:
            healths[user] = 100
            ambulances[user] -= 1
            await ctx.send(f'{ctx.message.author.mention} has just healed themselves to 100 health!')
          else:
            await ctx.send('You can\'t dose that, you have full health!')
        else:
          await ctx.send('You don\'t have a health bar! Type in `$health` to register.')
      else:
        await ctx.send('You don\'t have any ambulances with u')
    else:
      await ctx.send('Go buy some ambulances child')
  else:
    await ctx.send('Specify what to use!')

  print(f'In buy(): Saving ambulances = {ambulances}')
  try: 
    with open(AMBULANCES_FILE, 'w') as fp: 
      json.dump(ambulances, fp) 
  except FileNotFoundError: 
    print(f'In pigs(): File {AMBULANCES_FILE} not found! Not sure what to do here!') 

  print(f'In buy(): Saving healths = {healths}')
  try: 
    with open(HEALTH_FILE, 'w') as fp: 
      json.dump(healths, fp) 
  except FileNotFoundError: 
    print(f'In pigs(): File {HEALTH_FILE} not found! Not sure what to do here!') 

@use.error
async def use_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    embed = discord.Embed(title="Slow down dude", description="Stop tryna heal so much, you look like a big baby.\nYou can have more heal in **{} seconds**.\n (8 hour cooldown)".format(math.ceil(error.retry_after)), color = 0xff0000)
    await ctx.send(embed=embed)
    return

@bot.command()
async def farm(ctx):
  global sheeps, wools, rices, wheats, pigs, meats, ambulances, buffalos, stoves, uncooked_chickens, cooked_chickens, salads
  user = str(ctx.message.author.id)
  salads[user] = salads[user] if user in salads else 0
  cooked_chickens[user] = cooked_chickens[user] if user in cooked_chickens else 0
  uncooked_chickens[user] = uncooked_chickens[user] if user in uncooked_chickens else 0
  stoves[user] = stoves[user] if user in stoves else 0
  sheeps[user] = sheeps[user] if user in sheeps else 0
  buffalos[user] = buffalos[user] if user in buffalos else 0
  wools[user] = wools[user] if user in wools else 0
  rices[user] = rices[user] if user in rices else 0
  wheats[user] = wheats[user] if user in wheats else 0
  pigs[user] = pigs[user] if user in pigs else 0
  meats[user] = meats[user] if user in meats else 0
  ambulances[user] = ambulances[user] if user in ambulances else 0
  embed = discord.Embed(title = f"{ctx.message.author}'s Farm", description = "`$<crop/animal>` to harvest the animals or crops\n `$shop` for more")
  embed.add_field(name = "Animals [NOT SELLABLE]\n", value = f":sheep: Sheep | {sheeps[user]}\n :pig2: Pigs | {pigs[user]}\n :water_buffalo: Buffalos | {buffalos[user]}\n :hatched_chick: Uncooked Chickens | {uncooked_chickens[user]}\n", inline = True)
  embed.add_field(name = "\nCrops [NOT SELLABLE]\n", value = f":rice: Rice | {rices[user]}\n", inline = False)
  embed.add_field(name = "\nGoods [SELLABLE]\n", value = f":scroll:  Wool | {wools[user]}\n :tanabata_tree: Wheat | {wheats[user]}\n :cut_of_meat: Meat | {meats[user]}\n :chicken: Chickens | {cooked_chickens[user]}\n", inline = False)
  embed.add_field(name = "\nMeds [SELLABLE]\n", value = f":ambulance: Ambulances | {ambulances[user]}", inline = False)
  embed.add_field(name = "\nMaterials [NOT SELLABLE]\n", value = f':cooking: Stoves | {stoves[user]}', inline = False)
  embed.add_field(name = "\nDishes [NOT SELLABLE]\n", value = f':salad: Salads | {salads[user]}', inline = False)
  await ctx.send(embed=embed)

@bot.command()
async def buy(ctx, arg, amount: int):
  global balances, START_BAL, sheeps, rices, pigs, ambulances, meats, stoves, uncooked_chickens
  user = str(ctx.message.author.id)
  print(f'In buy(): arg = {arg}')
  print(f'In buy(): balances = {balances}')
  print(f'In buy(): args[0] = {arg}')
  

  if arg == "sheep":
    if user in balances:
      if balances[user] > 100 or balances[user] == 100:
        price_for_sheep = amount * 100
        if balances[user] > price_for_sheep:
          sheeps[user] = sheeps[user] + amount if user in sheeps else amount
          balances[user] -= price_for_sheep
          await ctx.send(f'Congratulations {ctx.message.author.mention}! You bought {amount} sheep!') 
        else:
          await ctx.send(f'You don\'t have enough to buy {amount} sheeps')
      else:
        await ctx.send('you don\'t have enough money don\'t try to scam me')
    else:
      print(f'In beg(): No record for {user} found. Creating a new record with a starting balance of {START_BAL}') 
      balances[user] = START_BAL 
      await ctx.send(f'hey you don\'t have a bank account yet. I just created one for you and started you off with ${START_BAL}') 
  elif arg == "rice":
    if user in balances:
      if balances[user] > 30 or balances[user] == 30:
        price_for_rice = amount * 30
        if balances[user] > price_for_rice:
          rices[user] = rices[user] + amount if user in rices else amount
          balances[user] -= price_for_rice
          await ctx.send(f'Congratulations {ctx.message.author.mention}! You bought {amount} rice!') 
        else:
          await ctx.send(f'You don\'t have enough to buy {amount} rice')
      else:
        await ctx.send('you don\'t have enough money don\'t try to scam me')
    else:
      print(f'In beg(): No record for {user} found. Creating a new record with a starting balance of {START_BAL}') 
      balances[user] = START_BAL 
      await ctx.send(f'hey you don\'t have a bank account yet. I just created one for you and started you off with ${START_BAL}') 
  elif arg == "pig" or arg == "pigs":
    if user in balances:
      if balances[user] > 200 or balances[user] == 200:
        price_for_pigs = amount * 200
        if balances[user] > price_for_pigs:
          pigs[user] = pigs[user] + amount if user in pigs else amount
          balances[user] -= price_for_pigs
          await ctx.send(f'Congratulations {ctx.message.author.mention}! You bought {amount} pig(s)!') 
        else:
          await ctx.send(f'You don\'t have enough to buy {amount} pig(s)')
      else:
        await ctx.send('You don\'t have enough money don\'t try to scam me')
    else:
      print(f'In beg(): No record for {user} found. Creating a new record with a starting balance of {START_BAL}') 
      balances[user] = START_BAL 
      await ctx.send(f'hey you don\'t have a bank account yet. I just created one for you and started you off with ${START_BAL}') 
  elif arg == "ambulance" or arg == "ambulances":
    if user in meats:
      if meats[user] > 15200 or meats[user] == 15200:
        price_for_ambulances = amount * 15200
        if meats[user] > price_for_ambulances or meats[user] == price_for_ambulances:
          ambulances[user] = ambulances[user] + amount if user in ambulances else amount
          meats[user] -= price_for_ambulances
          await ctx.send(f'Congratulations {ctx.message.author.mention}! You bought {amount} ambulances')
        else:
          await ctx.send(f'You don\'t have enough to buy {amount} ambulances!')
      else:
        await ctx.send('oi go harvest more pigs to buy this ya **SCAMMER**')
    else:
      await ctx.send('You don\'t have any meat...')
  elif arg == "buffalo" or arg == "buffalos":
    if user in balances:
      if balances[user] > 10000000 or balances[user] == 10000000:
        price_for_buffalos = amount * 10000000
        if balances[user] > price_for_buffalos or balances[user] == price_for_buffalos:
          buffalos[user] = buffalos[user] + amount if user in buffalos else amount
          balances[user] -= price_for_buffalos
          await ctx.send(f'Congratulations {ctx.message.author.mention}! You bought {amount} buffalos')
        else:
          await ctx.send(f'You don\'t have enough to buy {amount} buffalos!')
      else:
        await ctx.send('You don\'t have enough crypto for that **SCAMMER**')
    else:
      await ctx.send('You don\'t have any crypto!')
  elif arg == "stove" or arg == "stoves":
    if user in balances:
      if balances[user] > 19500 or balances[user] == 19500:
        price_for_stoves = amount * 19500
        if balances[user] > price_for_stoves or balances[user] == price_for_stoves:
          stoves[user] = stoves[user] + amount if user in stoves else amount
          balances[user] -= price_for_stoves
          await ctx.send(f'Congratulations {ctx.message.author.mention}! You bought {amount} stoves')
        else:
          await ctx.send(f'You don\'t have enough to buy {amount} stoves!')
      else:
        await ctx.send('You don\'t have enough crypto for that **SCAMMER**')
    else:
      await ctx.send('You don\'t have any crypto!')
  elif arg == "chicken" or arg == "chickens":
    if user in balances:
      if balances[user] > 10000 or balances[user] == 10000:
        price_for_uncooked_chickens = amount * 10000
        if balances[user] > price_for_uncooked_chickens or balances[user] == price_for_uncooked_chickens:
          uncooked_chickens[user] = uncooked_chickens[user] + amount if user in uncooked_chickens else amount
          balances[user] -= price_for_uncooked_chickens
          await ctx.send(f'Congratulations {ctx.message.author.mention}! You just bought {amount} uncooked chicken(s)')
        else:
          await ctx.send(f'You don\'t have enough to buy {amount} uncooked chicken(s)!')
      else:
        await ctx.send('You don\'t have enough crypto for that **SCAMMER**')
    else:
      await ctx.send('You don\'t have any crypto!')
  else:
    await ctx.send('You need to specify what to buy!')

  print(f'In buy(): Saving sheeps = {sheeps}')
  try: 
    with open(SHEEPS_FILE, 'w') as fp: 
      json.dump(sheeps, fp) 
  except FileNotFoundError: 
    print(f'In buy(): File {SHEEPS_FILE} not found! Not sure what to do here!') 

  print(f'In beg(): Saving balances = {balances}')
  try: 
    with open(BALANCES_FILE, 'w') as fp: 
      json.dump(balances, fp) 
  except FileNotFoundError: 
    print(f'In balances(): File {BALANCES_FILE} not found! Not sure what to do here!') 

  print(f'In buy(): Saving rice = {rices}')
  try: 
    with open(RICE_FILE, 'w') as fp: 
      json.dump(rices, fp) 
  except FileNotFoundError: 
    print(f'In rice(): File {RICE_FILE} not found! Not sure what to do here!') 

  print(f'In buy(): Saving pigs = {pigs}')
  try: 
    with open(PIG_FILE, 'w') as fp: 
      json.dump(pigs, fp) 
  except FileNotFoundError: 
    print(f'In pigs(): File {pigs} not found! Not sure what to do here!') 

  print(f'In buy(): Saving ambulances = {ambulances}')
  try: 
    with open(AMBULANCES_FILE, 'w') as fp: 
      json.dump(ambulances, fp) 
  except FileNotFoundError: 
    print(f'In pigs(): File {AMBULANCES_FILE} not found! Not sure what to do here!') 

  print(f'In buy(): Saving buffalos = {buffalos}')
  try: 
    with open(BUFFALOS_FILE, 'w') as fp: 
      json.dump(buffalos, fp) 
  except FileNotFoundError: 
    print(f'In pigs(): File {BUFFALOS_FILE} not found! Not sure what to do here!') 

  print(f'In buy(): Saving stoves = {stoves}')
  try: 
    with open(STOVES_FILE, 'w') as fp: 
      json.dump(stoves, fp) 
  except FileNotFoundError: 
    print(f'In pigs(): File {STOVES_FILE} not found! Not sure what to do here!') 

  print(f'In buy(): Saving uncooked chickens = {uncooked_chickens}')
  try: 
    with open(UNCOOKED_CHICKENS_FILE, 'w') as fp: 
      json.dump(uncooked_chickens, fp) 
  except FileNotFoundError: 
    print(f'In pigs(): File {UNCOOKED_CHICKENS_FILE} not found! Not sure what to do here!') 


@bot.command()
async def health(ctx):
  global healths
  user = str(ctx.message.author.id)
  print(f'In health(): Author Id = {ctx.message.author.id}, Author Name = {user}')
  if user in healths:
    embed = discord.Embed(title = f"{ctx.message.author}'s health :heartpulse:", description = "Your health is deprived everytime you harvest.\nTo regenerate, go to `$pharmacy` to buy meds.\nDose them to regenerate health.")
    embed.add_field(name = "Your health", value = f'{healths[user]}/100')
    await ctx.send(embed = embed)
  else: 
    print(f'In plead(): No record for {user} found. Creating a new record with a starting balance of {START_HEALTH}') 
    healths[user] = START_HEALTH
    await ctx.send(f'hey you don\'t have a health bar yet. I just created you one with {START_HEALTH}') 

  print(f'In health(): Saving healths = {healths}')
  try: 
    with open(HEALTH_FILE, 'w') as fp: 
      json.dump(healths, fp) 
  except FileNotFoundError: 
   print(f'In beg(): File {HEALTH_FILE} not found! Not sure what to do here!') 


@bot.command(name = 'plead')
@commands.cooldown(1, 60, commands.BucketType.user)
async def plead(ctx):
  global balances, START_BAL 
  INCREMENT = random.randint(20, 70)
  user = str(ctx.message.author.id) 
  print(f'In plead(): Author Id = {ctx.message.author.id}, Author Name = {user}')

  if user in balances: 
    # print(f'In plead(): Found record for {user}. Incrementing balance by {random.randint(20,70)}')
    responses = [
      f"**Detective Dank** donated {INCREMENT} coins to {ctx.message.author.mention}!",
      f"**David Dobrik** donated {INCREMENT} coins to {ctx.message.author.mention}!",
      f"**Pewdiepie** donated {INCREMENT} coins to {ctx.message.author.mention}!",
      f"**Kylie Jenner** donated {INCREMENT} coins to {ctx.message.author.mention}!",
      f"**Ur Mom** donated {INCREMENT} coins to {ctx.message.author.mention}!",
      f"**Kanye West** donated {INCREMENT} coins to {ctx.message.author.mention}!",
      f"**Markiplier** donated {INCREMENT} coins to {ctx.message.author.mention}!",
      f"**Mojang** donated {INCREMENT} coins to {ctx.message.author.mention}!",
      f"**Jesus** donated {INCREMENT} coins to {ctx.message.author.mention}!"
    ]
    await ctx.send(random.choice(responses))
    balances[user] += INCREMENT
  else: 
    print(f'In plead(): No record for {user} found. Creating a new record with a starting balance of {START_BAL}') 
    balances[user] = START_BAL 
    await ctx.send(f'hey you don\'t have a bank account yet. I just created one for you and started you off with ${START_BAL}') 

  print(f'In plead(): Saving balances = {balances}')
  try: 
    with open(BALANCES_FILE, 'w') as fp: 
      json.dump(balances, fp) 
  except FileNotFoundError: 
   print(f'In beg(): File {BALANCES_FILE} not found! Not sure what to do here!') 


@plead.error
async def plead_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    embed = discord.Embed(title="Slow down dude", description="Stop pleading so much, you look like a big baby.\nYou can have more coins in **{} seconds**.\n The default cooldown for pleading is `1m`.".format(math.ceil(error.retry_after)), color = 0xff0000)
    await ctx.send(embed=embed)
    return

@bot.command(name = 'bal')
async def bal(ctx): 
  global balances, START_BAL 
  user = str(ctx.message.author.id) 
  print(f'In balance(): Author Id = {ctx.message.author.id}, Author Name = {user}')

  if user in balances: 
    print(f'In balance(): Found record for {user}. User balance = {balances[user]}') 
    embed = discord.Embed(title=f":moneybag: {ctx.message.author}'s balance", description=f"**Bank Account**: ¢{balances[user]}/ꝏ", color=0xeee657)

    await ctx.send(embed=embed)

  else: 
    print(f'In balance(): No record for {user} found. Creating a new record with a starting balance of {START_BAL}') 
    balances[user] = START_BAL 
    await ctx.send(f'hey you don\'t have an account yet. I just created one for you and started you off with ${START_BAL}. To register type in `$plead`') 

  print(f'In balance(): balances = {balances}')





bot.run('haha u thought losers')
