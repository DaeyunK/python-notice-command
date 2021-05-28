import discord
from discord.ext import commands

app = commands.Bot(command_prefix=";", help_command=None, intents=discord.Intents.all())

@app.command()
@commands.has_permissions(manage_messages=True)
async def 공지(ctx, *,  msg: str = None):
    notice_ch = app.get_channel() #공지가 전송 될 채널 아이디를 적으세요 !

    noti_emb = discord.Embed(title="**공지사항**", description=f"{msg}", color=0x36393F)
    await ctx.reply("메시지 전송이 완료되었습니다.")
    await notice_ch.send(embed=noti_emb)

@공지.error
async def notice_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(title="``❌``  명령어 오류 **(Command Error)** \n\n **사용된 명령어 : 공지**", description="사용 권한이 없습니다.", color=0x36393F)
        await ctx.reply(embed=embed, mention_author=False)


app.run("token_here")