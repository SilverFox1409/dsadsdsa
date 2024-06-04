
import disnake
from disnake.ext import commands


bot = commands.Bot(command_prefix="!", help_command=None, intents=disnake.Intents.all(), test_guilds=[1245768304174301204])
bot.remove_command("help")


@bot.event
async def on_ready():
    print(f"Bot {bot.user} Начинает работу!")

    await bot.change_presence(status=disnake.Status.online, activity=disnake.Game("Counter-Strike 2"))





@bot.slash_command(
    description="Список правил."
)
@commands.has_permissions(kick_members=True, administrator=True)
async def правила(ctx):
    emb = disnake.Embed(title = "Правила сервера Pureshka CS2",
                        color=0xffff00,
                        description="**--ПРАВИЛА ТЕКСТОВИХ КАНАЛІВ--**",
                       )
# Команда /rules для вывода списка правил.

# Список правил
    emb.add_field(name="", inline=False, value="**1.2 Заборонено відправляти шок/18+ контент у всіх каналах.**")
    emb.add_field(name="", inline=False, value="**1.4 Заборонена будь-яка реклама будь-яких сторонніх ресурсів.**")
    emb.add_field(name="", inline=False, value="**1.5 Заборонені будь-які шкідливі посилання для сервера і для користувачів.**")
    emb.add_field(name="", inline=False, value="**1.6 Заборонено спам/флуд.**")
    emb.add_field(name="", inline=False, value="**1.7 Заборонена будь-яка комерційна діяльність.**")
    emb.add_field(name="", inline=False, value="**1.8 Заборонена провокація на порушення правил.**")
    emb.add_field(name="", inline=False, value="**1.9 Заборонено розпалювати конфлікти.**")
    emb.add_field(name="", inline=False, value="**2.1 Заборонено перешкодження роботи адміністрації.**")

    emb.add_field(name="**--ПРАВИЛА ГОЛОСОВИХ КАНАЛІВ--**", inline=False, value="")

    emb.add_field(name="", inline=False, value="**1.1 Заборонено зловживати матом у всіх голосових каналах.**")
    emb.add_field(name="", inline=False, value="**1.2 Заборонено показувати шок/18+ контент у всіх голосових каналах.**")
    emb.add_field(name="", inline=False, value="**1.3 Заборонено ображати рідних, релігію тощо у голосових каналах.**")
    emb.add_field(name="", inline=False, value="**1.4 Заборонена будь-яка реклама будь-яких сторонніх ресурсів у голосових каналах.**")
    emb.add_field(name="", inline=False, value="**1.5 Заборонені будь-які шкідливі посилання для сервера і для користувачів у голосових каналах.**")
    emb.add_field(name="", inline=False, value="**1.8 Заборонено провокацію на порушення правил у голосових каналах.**")

    emb.add_field(name="**--ПРАВИЛА ПРОФІЛІВ--**", inline=False, value="")

    emb.add_field(name="", inline=False, value="**1.9 Заборонено передачу акаунта третім особам.**")
    emb.add_field(name="", inline=False, value="**2.1 Заборонено обходити покарання лівим акаунтом або використовувати твінк у злісних цілях.**")
    emb.add_field(name="", inline=False, value="**2.2 Нікнейм не повинен складатися з образ користувача.**")
    emb.add_field(name="", inline=False, value="**2.3 Аватарка не повинна містити шок/18+.**")
    emb.add_field(name="", inline=False, value="**2.4 Заборонено прикидатися іншою людиною, змінюючи нікнейм і аву.**")
    emb.add_field(name="", inline=False, value="**2.5 Нік не повинен бути таким, що не копіюється.**")
    emb.add_field(name="------------------------", inline=False, value="@everyone  СЛАВА УКРАЇНІ!🇺🇦")
# Список правил

    await ctx.send(embed=emb)




@bot.event
async def member_join(ctx):
    channel = bot.get_channel(993793910331691090)
    emb = disnake.Embed(title = "Правила сервера Pureshka CS2",
                        color=0xffff00,
                        description="**--ПРАВИЛА ТЕКСТОВИХ КАНАЛІВ--**",
                       )


    emb.add_field(name="", inline=False, value="**1.1 Заборонено зловживати матом у всіх каналах.**")
    emb.add_field(name="", inline=False, value="**1.2 Заборонено відправляти шок/18+ контент у всіх каналах.**")
    emb.add_field(name="", inline=False, value="**1.3 Заборонено ображати рідних, релігію тощо.**")
    emb.add_field(name="", inline=False, value="**1.4 Заборонена будь-яка реклама будь-яких сторонніх ресурсів.**")
    emb.add_field(name="", inline=False, value="**1.5 Заборонені будь-які шкідливі посилання для сервера і для користувачів.**")
    emb.add_field(name="", inline=False, value="**1.6 Заборонено спам/флуд.**")
    emb.add_field(name="", inline=False, value="**1.7 Заборонена будь-яка комерційна діяльність.**")
    emb.add_field(name="", inline=False, value="**1.8 Заборонена провокація на порушення правил.**")
    emb.add_field(name="", inline=False, value="**1.9 Заборонено розпалювати конфлікти.**")
    emb.add_field(name="", inline=False, value="**2.1 Заборонено перешкодження роботи адміністрації.**")

    emb.add_field(name="**--ПРАВИЛА ГОЛОСОВИХ КАНАЛІВ--**", inline=False, value="")

    emb.add_field(name="", inline=False, value="**1.1 Заборонено зловживати матом у всіх голосових каналах.**")
    emb.add_field(name="", inline=False, value="**1.2 Заборонено показувати шок/18+ контент у всіх голосових каналах.**")
    emb.add_field(name="", inline=False, value="**1.3 Заборонено ображати рідних, релігію тощо у голосових каналах.**")
    emb.add_field(name="", inline=False, value="**1.4 Заборонена будь-яка реклама будь-яких сторонніх ресурсів у голосових каналах.**")
    emb.add_field(name="", inline=False, value="**1.5 Заборонені будь-які шкідливі посилання для сервера і для користувачів у голосових каналах.**")
    emb.add_field(name="", inline=False, value="**1.8 Заборонено провокацію на порушення правил у голосових каналах.**")

    emb.add_field(name="**--ПРАВИЛА ПРОФІЛІВ--**", inline=False, value="")

    emb.add_field(name="", inline=False, value="**1.9 Заборонено передачу акаунта третім особам.**")
    emb.add_field(name="", inline=False, value="**2.1 Заборонено обходити покарання лівим акаунтом або використовувати твінк у злісних цілях.**")
    emb.add_field(name="", inline=False, value="**2.2 Нікнейм не повинен складатися з образ користувача.**")
    emb.add_field(name="", inline=False, value="**2.3 Аватарка не повинна містити шок/18+.**")
    emb.add_field(name="", inline=False, value="**2.4 Заборонено прикидатися іншою людиною, змінюючи нікнейм і аву.**")
    emb.add_field(name="", inline=False, value="**2.5 Нік не повинен бути таким, що не копіюється.**")
    emb.add_field(name="------------------------", inline=False, value="@everyone  СЛАВА УКРАЇНІ!🇺🇦")

    await channel.send(embed=emb)





bot.run("MTI0NjgwMzgyMDg1NjczNzgxMw.G-6E5g.wLs9PKaTePua0VQBn2UJnWnZ5ivBR9s-492OoA")