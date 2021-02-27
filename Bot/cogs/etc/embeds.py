import discord


thumbnail = 'https://i.imgur.com/GKPAp4q.png'


class Embeds:

    Help = discord.Embed(title=':ticket: HiyobiBot 명령어 목록', color=0xababab)
    Help.set_thumbnail(url=thumbnail)
    Help.add_field(name=';정보 N', value='망가 정보를 불러옵니다.', inline=False)
    Help.add_field(name=';최신', value='최신 망가 15개를 불러옵니다.', inline=False)
    Help.add_field(
        name=';페이지 N', value='최신 망가 리스트 중 N번째 페이지를 불러옵니다.', inline=False)
    Help.add_field(
        name=';검색 K', value='히요비에 키워드를 검색하여 첫 번째 페이지를 불러옵니다.', inline=False)
    Help.add_field(name=';표지 N', value='N번 망가의 표지를 보여줍니다.', inline=False)
    Help.add_field(name=';보기 N N2', value='N번 망가의 N2페이지를 불러옵니다.', inline=False)
    Help.add_field(
        name=';청소 N', value='N개의 메세지를 삭제합니다.\n메세지 관리 권한이 있어야 사용 가능합니다.', inline=False)
    Help.add_field(name=';초대', value='HiyobiBot 초대 링크를 불러옵니다.', inline=False)
    Help.add_field(
        name=';지원', value='HiyobiBot 디스코드 서버 링크를 불러옵니다.', inline=False)
    Help.add_field(name=':warning: 경고',
                   value='모든 명령어는 "연령 제한 채널"이 아니어도 정상 작동합니다.', inline=False)

    Wait = discord.Embed(title=':file_folder: 정보를 불러오는 중입니다...',
                         description='잠시만 기다려주세요...', color=0xababab)
    Wait.set_thumbnail(url=thumbnail)

    NoResult = discord.Embed(title=':warning: 오류', color=0xff0000)
    NoResult.set_thumbnail(url=thumbnail)
    NoResult.add_field(name='검색 결과가 없습니다.',
                       value='번호가 정확한지 다시 한번 확인해주세요.', inline=False)

    Error = discord.Embed(title=':warning: 오류', color=0xff0000)
    Error.set_thumbnail(url=thumbnail)
    Error.add_field(name='오류가 발생했습니다.',
                    value='지속적으로 오류 발생 시 ombe#7777으로 문의해주세요.', inline=False)

    PlzInputNum = discord.Embed(
        title=':warning: 오류', description='숫자를 입력해주세요.', color=0xff0000)
    PlzInputNum.set_thumbnail(url=thumbnail)

    WrongNum = discord.Embed(title=':warning: 오류',
                             description='해당 페이지를 찾을 수 없습니다.', color=0xff0000)
    WrongNum.set_thumbnail(url=thumbnail)

    Invite = discord.Embed(title=':inbox_tray: HiyobiBot 초대 링크', url='https://discord.com/oauth2/authorize?client_id=765557137832542208&scope=bot&permissions=2146954615',
                           description='위 링크를 눌러 HiyobiBot을 다른 서버에 초대할 수 있습니다.', color=0xff0000)
    Invite.set_thumbnail(url=thumbnail)

    Support = discord.Embed(title=':envelope: HiyobiBot 지원', url='https://discord.gg/3zSTSNT',
                            description='위 링크를 눌러 HiyobiBot 디스코드 서버에 접속하거나, ombe#7777 DM으로 지원이 가능합니다.', color=0xff0000)
    Support.set_thumbnail(url=thumbnail)

    HowtoClear = discord.Embed(title=':question: 청소 명령어 사용 방법',
                               description=';청소 N 을 입력하여 채팅창을 청소할 수 있습니다.\nN은 1 이상의 정수로 입력해주세요.', color=0xababab)
    HowtoClear.set_thumbnail(url=thumbnail)

    NotReady = discord.Embed(title=':hammer: 아직 개발 중인 기능입니다.',
                             description='곧 완성될 예정이니 조금만 기다려주세요.', color=0xff0000)
    NotReady.set_thumbnail(url=thumbnail)
