import discord

thumbnail = 'https://i.imgur.com/GKPAp4q.png'


class CreateEmbed:

    def Error(self, e):
        embed = discord.Embed(title=':warning: 오류', color=0xff0000)
        embed.set_thumbnail(url=thumbnail)
        embed.add_field(name='오류가 발생했습니다.',
                        value='지속적으로 오류 발생 시 ombe#7777으로 문의해주세요.', inline=False)
        embed.add_field(name='오류 코드', value=e, inline=False)
        return embed

    def Cleared(self, n):
        embed = discord.Embed(title=':white_check_mark: 청소 완료',
                              description=f'{n}개의 메세지를 삭제했습니다.', color=0xababab)
        embed.set_thumbnail(url=thumbnail)
        return embed
