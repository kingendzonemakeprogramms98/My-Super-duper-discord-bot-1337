import discord
from discord.ext import commands

gateway = True

client = commands.Bot(command_prefix = "_")
client.remove_command('help')

PREFIX = '_'

@client.event
async def on_ready():
    print("Connected")

    await client.change_presence(status=discord.Status.online, activity = discord.Game('Префикс \'_\' | Топ бот для топового сервера'))

@client.command()
async def test(ctx):
    await ctx.send(f'Привет, {ctx.author.mention}!')
#clear
@client.command()
@commands.has_permissions(manage_messages = True)
async def clear(ctx, amount : int):
	await ctx.channel.purge(limit = amount)

#kick
@client.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member, *, reason = "КИКНУТ САМЫМ ТОПОВЫМ БОТОМ!!!111"):
	await ctx.channel.purge(limit = 1)

	await member.kick(reason = reason)
	await ctx.send(f'{ctx.author.mention} кикнул {member.mention}!')
#ban
@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = "ЗАБАНЕН САМЫМ ТОПОВЫМ БОТОМ!!!111"):
	await ctx.channel.purge(limit = 1)

	await member.ban(reason = reason)
	await ctx.send(f'{ctx.author.mention} забанил {member.mention}!')

@client.command()
async def help(ctx):
	emb = discord.Embed(title = 'Команды САМОГО ТОПОВОГО БОТА')

	emb.add_field(name = '{}clear'.format(PREFIX), value = 'Чистит чат!')
	emb.add_field(name = '{}ban'.format(PREFIX), value = 'Банит')
	emb.add_field(name = '{}kick'.format(PREFIX), value = 'Кикает')
	emb.add_field(name = '{}test'.format(PREFIX), value = '404 404 404')
	emb.add_field(name = '{}news'.format(PREFIX), value = 'Сообщение с новостями (Эмбед) (Бета)')
	emb.add_field(name = '{}giverole'.format(PREFIX), value = 'Даёт роль по её ID (Бета)')

	await ctx.send(embed=emb)

#filter
@client.event
async def on_message(message):
	await client.process_commands(message)\

	msg = message.content.lower()

	if msg in bad_words:
		await message.delete()
		await message.channel.send(f'{message.author.mention} : Вы сказали плохое слово!')

#news
@client.command()
@commands.has_permissions(administrator = True)
async def news(ctx, title='Внимание!', *, desc='Текст не указан'):
	emb = discord.Embed(title = title, description = desc)

	await ctx.send(embed=emb)

#Give role
@client.command()
@commands.has_permissions(administrator = True)
async def giverole(ctx, role : str , member : discord.Member):
	
	role2 = discord.utils.get(member.guild.roles, id = role)

	await member.add_roles(role2)

	await ctx.send(f'{ctx.author.mention}, успешно дана роль участнику {member.mention}!')

#connect
token = open('token.txt', 'r').readline()

client.run(token)

    
