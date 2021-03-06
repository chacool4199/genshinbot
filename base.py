# -*- coding:utf-8 -*-
# 위에 구문은 # 빼버리시면 문제 생깁니다.
# 가끔가다 애가 인코딩을 잘못 읽어서 오류를 냅니다. 그것을 대비하기 위해 'utf-8'으로 읽으라고 선언합니다.

import discord, asyncio # 디스코드 모듈과, 보조 모듈인 asyncio를 불러옵니다.
import os
import random

#import urllib
#from urllib.request import Request
#import bs4
#from bs4 import BeautifulSoup

#import selenium
#from selenium import webdriver
# 아까 메모해 둔 토큰을 입력합니다

client = discord.Client() # discord.Client() 같은 긴 단어 대신 client를 사용하겠다는 선언입니다.

#charactorData = [(4, '엠버'), (4, '베넷'), (5, '다이루크'), (5, '클레'), (4, '향릉'), (4, '신염'), (5, '호두'), (4, '바바라'), (5, '모나'), (4, '행추'), (5, '타르탈리아'), (4, '북두'), (4,'피슬'),
#(5, '각청'), (4, '리사'), (4, '레이저'), (4, '중운'), (4, '케이아'), (5, '치치'), (4, '디오나'), (5, '감우'), (5, '진'), (4, '설탕'), (5, '벤티'), (5, '소'), (4, '응광'), (4, '노엘'), (5, '종려'),
#(5, '알베도')]
#weaponData = []
#charactorData5 = []
#charactorData4 = []

cmdData = [(0, '엠버'), (0, '베넷'), (0, '다이루크'), (0, '클레'), (0, '향릉'), (0, '신염'), (0, '호두'), (0, '바바라'), (0, '모나'), (0, '행추'), (0, '타르탈리아'), (0, '북두'), (0,'피슬'),
(0, '각청'), (0, '리사'), (0, '레이저'), (0, '중운'), (0, '케이아'), (0, '치치'), (0, '디오나'), (0, '감우'), (0, '진'), (0, '설탕'), (0, '벤티'), (0, '소'), (0, '응광'), (0, '노엘'), (0, '종려'),
(0, '알베도'), (1, '매의검'), (1, '천공의검'), (1, '참봉의칼날'), (1, '반암결록'), (1, '천공의긍지'), (1, '늑대의말로'), (1, '무공의검'), (1, '천공의두루마리'), (1, '사풍원서'), (1, '속세의자물쇠'), 
(1, '천공의날개'), (1, '아모스의활'), (1, '화박연'), (1, '천공의마루'), (1, '관홍의창'), (1, '호마의지팡이')]
# charactorData_water = ['바바라', '모나', '행추', '타르탈리아']
# charactorData_electric = ['북두', '피슬', '각청']

global standardGachaStack
standardGachaStack = [[0, 0]]

global standardGachaCharactor4 
standardGachaCharactor4 = [16, "신염", "설탕", "디오나", "중운", "노엘", "베넷", "피슬", "응광", "행추", "북두", "향릉", "엠버", "레이저", "케이아", "바바라", "리사"]

global standardGachaCharactor5 
standardGachaCharactor5 = [5, "각청", "치치", "진", "모나", "다이루크"]

global standardGachaWeapon3
standardGachaWeapon3 = [13, "탄궁", "신궁의서약", "까마귀깃활", "비취오브", "드래곤슬레이어영웅담", "마도서론", "흑술창", "훌륭한대화수단", "드래곤블러드소드", "강철의그림자",
                        "비천어검", "여명신검", "차가운칼날"]

global standardGachaWeapon4 
standardGachaWeapon4 = [18, "녹슨활", "제례활", "절현", "페보니우스활", "소심", "제례의악장", "음유시인의악장", "페보니우스비전", "페보니우스장창", "용학살창", "빗물베기", "제례대검",
                        "시간의검", "페보니우스대검", "용의포효", "제례검", "피리검", "페보니우스검"]

global standardGachaWeapon5 
standardGachaWeapon5 = [10, "천공의날개", "천공의두루마리", "천공의마루", "천공의긍지", "천공의검", "아모스의활", "사풍원서", "화박연", "늑대의말로", "매의검"]

global standardGachaList
standardGachaList = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]

global standardGachaResult
standardGachaResult = [ ]

@client.event
async def on_ready(): # 봇이 준비가 되면 1회 실행되는 부분입니다.

    await client.change_presence(status=discord.Status.online, activity=discord.Game("<!도움> 야근.."))
# 봇이 "반갑습니다"를 플레이 하게 됩니다.
# 눈치 채셨을지 모르곘지만, discord.Status.online에서 online을 dnd로 바꾸면 "다른 용무 중", idle로 바꾸면 "자리 비움"으로 바뀝니다.

print("I'm Ready!") # I'm Ready! 문구를 출력합니다.
# print(client.user.name) # 봇의 이름을 출력합니다.
# print(client.user.id) # 봇의 Discord 고유 ID를 출력합니다.

@client.event
async def on_message(message): # 메시지가 들어 올 때마다 가동되는 구문입니다.

    if message.author.bot: # 채팅을 친 사람이 봇일 경우
        return None # 반응하지 않고 구문을 종료합니다.

    if message.content == "!도움": # !명령어 라는 채팅을 친다면

# 메시지 전송이 두가지 방법이 있습니다. 상황에 맞는 구문을 사용하시면 됩니다.

# 이 구문은 메시지가 보내진 채널에 메시지를 보내는 구문입니다.
        # await message.channel.send("일이 아직 끝나지 않았어요..")

        embed = discord.Embed(title="당신과의 계약에 따를게요..", description="지령을 내려주세요\n\000\n\000\n(수행 가능한 지령)", color=0xd6616a) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
        # embed.set_thumbnail(url="링크")
        embed.set_thumbnail(url="https://i.imgur.com/LqSl4LI.jpg")
        embed.add_field(name=":closed_book: Characters", value="!캐릭터 = 캐릭터 목록을 확인합니다\n !검색 (캐릭터명) = 해당 캐릭터의 상세정보를 확인합니다", inline=False)
        embed.add_field(name=":green_book: Weapon", value="!무기 = 무기 목록을 확인합니다\n !검색 (무기명) = 해당 무기의 상세정보를 확인합니다", inline=False)
        embed.add_field(name=":blue_book: 가챠시뮬", value="!가챠 = 가챠 목록을 확인합니다", inline=False)
        embed.add_field(name=":orange_book: 편의기능", value="!편의 = 편의기능 목록을 확인합니다", inline=False)

        # embed.set_footer(text="슬슬 끝내도 되겠군요") # 하단에 들어가는 조그마한 설명을 잡아줍니다
        await message.channel.send(embed=embed) # embed를 포함 한 채로 메시지를 전송합니다.
        # await message.channel.send("할 말", embed=embed) # embed와 메시지를 함께 보내고 싶으시면 이렇게 사용하시면 됩니다.
    
    if message.content == "!캐릭터":
        embed = discord.Embed(title="캐릭터 리스트\000\000\000\000\000\
            \000\000\000\000\000\000\000\000\000\000\
            \000\000\000\000\000\000\000\000\000\000\
            \000\000\000\000\000\000\000\000\000\000\
            ", description="\000", color=0x8989a5)

        #embed.set_thumbnail(url="https://i.imgur.com/cJH3kph.jpg")

        embed.add_field(name=":red_circle:불 속성", value="[★★★★★]\n다이루크, 클레, 호두\n\
            [★★★★]\n엠버, 베넷, 향릉, 신염\n\000", inline=True)

        embed.add_field(name=":blue_circle:물 속성", value="[★★★★★]\n모나, 타르탈리아\n\
            [★★★★]\n바바라, 행추\n\000", inline=True)

        embed.add_field(name=":purple_circle:번개 속성", value="[★★★★★]\n각청\n\
            [★★★★]\n북두, 피슬, 리사, 레이저\n\000", inline=True)

        embed.add_field(name=":white_circle:얼음 속성", value="[★★★★★]\n치치, 감우\n\
            [★★★★]\n중운, 케이아, 디오나\n\000", inline=True)

        embed.add_field(name=":green_circle:바람 속성", value="[★★★★★]\n진, 벤티, 소\n\
            [★★★★]\n설탕\n\000", inline=True)

        embed.add_field(name=":yellow_circle:땅 속성", value="[★★★★★]\n종려, 알베도\n\
            [★★★★]\n응광, 노엘\n\000", inline=True)
       
        await message.channel.send(embed=embed)

        #embed = discord.Embed(title=":star::star::star::star:\
        #                \000\000\000\000\000\000\000\000\000\000\
        #                \000\000\000\000\000\000\000\000\000\000\n4성 캐릭터 목록\n", description="\000\n\000\n", color=0x8989a5)

        #embed.set_thumbnail(url="https://i.imgur.com/cJH3kph.jpg")

        #embed.add_field(name="불 속성", value="엠버, 베넷, 향릉, 신염\n\000", inline=False)
        #embed.add_field(name="물 속성", value="바바라, 행추\n\000", inline=False)
        #embed.add_field(name="번개 속성", value="북두, 피슬, 리사, 레이저\n\000", inline=False)
        #embed.add_field(name="얼음 속성", value="중운, 케이아, 디오나\n\000", inline=False)
        #embed.add_field(name="바람 속성", value="설탕\n\000", inline=False)
        #embed.add_field(name="땅 속성", value="응광, 노엘\n\000", inline=False)
       
        #await message.channel.send(embed=embed)

    if message.content.startswith("!검색"):
        target = message.content[4:]
        targetNoneblank = target.replace(" ","")
        # await message.channel.send("검색중...")
        findsuccess = False

        for (dataType, data) in cmdData:

            if dataType == 0 and data == targetNoneblank:
                # await message.channel.send("캐릭터 정보를 찾고 있습니다...")
                # await message.channel.send(data+"_targetData를 찾았습니다")
                if targetNoneblank == "엠버":
                    findsuccess = True
                    embed = discord.Embed(title=":star::star::star::star:\
                        \000\000\000\000\000\000\000\000\000\000\
                        \000\000\000\000\000\000\000\000\000\000\n비행 챔피언 · 엠버\n", description="\000\n\000\n정찰 기사 엠버, 준비 완료!", color=0x8989a5)

                    embed.set_thumbnail(url="https://i.imgur.com/cJH3kph.jpg")
                    embed.add_field(name="신의 눈", value="불", inline=True)
                    embed.add_field(name="생일", value="8월 10일", inline=True)
                    embed.add_field(name="별자리", value="토끼자리", inline=True)

                    embed.add_field(name="사용 무기", value="토끼백작", inline=True)
                    embed.add_field(name="돌파 스텟", value="공격력%", inline=True)
                    embed.add_field(name="성우", value="いわみ まなか\n\000", inline=True)

                    embed.add_field(name="특성소재", value="자유의 철학 <월,목,일>\n동풍의 숨결 <드발린>\n역전의 화살촉\n\000", inline=False)
                    embed.add_field(name="무기추천", value="있는대로 쓰세요ㅋ\n\000", inline=False)
                    embed.add_field(name="성유물 추천", value="있는대로 쓰세요ㅋ\n\000", inline=False)
       
                    await message.channel.send(embed=embed)

                elif targetNoneblank == "베넷":
                    findsuccess = True
                    embed = discord.Embed(title=":star::star::star::star::star:\
                        \000\000\000\000\000\000\000\000\000\000\
                        \000\000\000\000\000\000\000\000\n운명의 시금석 · 베넷\n", description="\000\n\000\n보켄다! 보켄!", color=0x8989a5)

                    embed.set_thumbnail(url="https://i.imgur.com/uxMayD1.jpg")
                    embed.add_field(name="신의 눈", value="불", inline=True)
                    embed.add_field(name="생일", value="2월 29일", inline=True)
                    embed.add_field(name="별자리", value="험로자리", inline=True)

                    embed.add_field(name="사용 무기", value="한손검", inline=True)
                    embed.add_field(name="돌파 스텟", value="원소 충전 효율%", inline=True)
                    embed.add_field(name="성우", value="おおさか りょうた\n\000", inline=True)

                    embed.add_field(name="특성소재", value="투쟁의 철학 <화,금,일>\n동풍의 깃털 <드발린>\n골드 까마귀 휘장\n\000", inline=False)
                    embed.add_field(name="무기추천", value="천공의 검, 용의 포효, 페보니우스 검, 부식의 검\n\000", inline=False)
                    embed.add_field(name="성유물 추천", value="마녀4셋(6돌), 소녀4셋, 왕실4셋\n\000", inline=False)
       
                    await message.channel.send(embed=embed)

                elif targetNoneblank == "다이루크":
                    findsuccess = True
                    embed = discord.Embed(title=":star::star::star::star::star:\
                        \000\000\000\000\000\000\000\000\000\000\
                        \000\000\000\000\000\000\000\000\n새벽의 어둠 · 다이루크\n", description="\000\n\000\n지금, 선고한다!", color=0x8989a5)

                    embed.set_thumbnail(url="https://i.imgur.com/ryONXxj.jpg")
                    embed.add_field(name="신의 눈", value="불", inline=True)
                    embed.add_field(name="생일", value="4월 30일", inline=True)
                    embed.add_field(name="별자리", value="밤올빼미자리", inline=True)

                    embed.add_field(name="사용 무기", value="행추", inline=True)
                    embed.add_field(name="돌파 스텟", value="치명타 확률%", inline=True)
                    embed.add_field(name="성우", value="おの けんしょう\n\000", inline=True)

                    embed.add_field(name="특성소재", value="투쟁의 철학 <화,금,일>\n동풍의 깃털 <드발린>\n위관의 휘장\n\000", inline=False)
                    embed.add_field(name="무기추천", value="늑대의 말로, 천공의 긍지, 이무기 검, 고화 프로토타입\n\000", inline=False)
                    embed.add_field(name="성유물 추천", value="마녀4셋\n\000", inline=False)
       
                    await message.channel.send(embed=embed)

                elif targetNoneblank == "클레":
                    findsuccess = True
                    embed = discord.Embed(title=":star::star::star::star::star:\
                        \000\000\000\000\000\000\000\000\000\000\
                        \000\000\000\000\000\000\000\000\n도망치는 태양 · 클레\n", description="\000\n\000\n다다다~ 클레가 도와줄게!", color=0x8989a5)

                    embed.set_thumbnail(url="https://i.imgur.com/5MaVxnF.jpg")
                    embed.add_field(name="신의 눈", value="태양", inline=True)
                    embed.add_field(name="생일", value="7월 27일", inline=True)
                    embed.add_field(name="별자리", value="네잎클로버자리", inline=True)

                    embed.add_field(name="사용 무기", value="법구", inline=True)
                    embed.add_field(name="돌파 스텟", value="불 원소피해 보너스%", inline=True)
                    embed.add_field(name="성우", value="くの みさき\n\000", inline=True)

                    embed.add_field(name="특성소재", value="자유의 철학 <월,목,일>\n북풍의 고리 <안드리우스>\n금주의 두루마리\n\000", inline=False)
                    embed.add_field(name="무기추천", value="사풍 원서, 천공의 두루마리, 일월의 정수, 음유시인의 악장\n\000", inline=False)
                    embed.add_field(name="성유물 추천", value="마녀4셋, 현인4셋\n\000", inline=False)
       
                    await message.channel.send(embed=embed)
                    
                elif targetNoneblank == "향릉":
                    findsuccess = True
                    embed = discord.Embed(title=":star::star::star::star:\
                        \000\000\000\000\000\000\000\000\000\000\
                        \000\000\000\000\000\000\000\000\000\000\n만민백미 · 향릉\n", description="\000\n\000\n달리기 시합하자아~~~", color=0x8989a5)

                    embed.set_thumbnail(url="https://i.imgur.com/Ni6fy51.jpg")
                    embed.add_field(name="신의 눈", value="불", inline=True)
                    embed.add_field(name="생일", value="11월 2일", inline=True)
                    embed.add_field(name="별자리", value="국자자리", inline=True)

                    embed.add_field(name="사용 무기", value="장병기", inline=True)
                    embed.add_field(name="돌파 스텟", value="원소 마스터리", inline=True)
                    embed.add_field(name="성우", value="おざわ あり\n\000", inline=True)

                    embed.add_field(name="특성소재", value="근면의 철학 <화,금,일>\n동풍의 발톱 <드발린>\n슬라임 원액\n\000", inline=False)
                    embed.add_field(name="무기추천", value="화박연, 천공의 마루, 결투의 창, 용학살창\n\000", inline=False)
                    embed.add_field(name="성유물 추천", value="검투사4셋, 마녀4셋\n\000", inline=False)
       
                    await message.channel.send(embed=embed)
                    
                elif targetNoneblank == "신염":
                    findsuccess = True
                    embed = discord.Embed(title=":star::star::star::star:\
                        \000\000\000\000\000\000\000\000\000\000\
                        \000\000\000\000\000\000\000\000\000\000\n폭열 멜로디 · 신염\n", description="\000\n\000\n롸큰롤다운 선택이야!", color=0x8989a5)

                    embed.set_thumbnail(url="https://i.imgur.com/DjTQPuP.jpg")
                    embed.add_field(name="신의 눈", value="불", inline=True)
                    embed.add_field(name="생일", value="10월 16일", inline=True)
                    embed.add_field(name="별자리", value="홍단사현자리", inline=True)

                    embed.add_field(name="사용 무기", value="양손검", inline=True)
                    embed.add_field(name="돌파 스텟", value="공격력%", inline=True)
                    embed.add_field(name="성우", value="たかはし ちあき\n\000", inline=True)

                    embed.add_field(name="특성소재", value="황금의 철학 <수,토,일>\n하늘을 삼킨 고래·뿔 <마왕 타르탈리아>\n골드 까마귀 휘장\n\000", inline=False)
                    embed.add_field(name="무기추천", value="무공의 검, 백영검, 이무기 검, 제례 대검\n\000", inline=False)
                    embed.add_field(name="성유물 추천", value="기사2셋+왕실2셋, 검투사4셋\n\000", inline=False)
       
                    await message.channel.send(embed=embed)
                    
                elif targetNoneblank == "호두":
                    findsuccess = True
                    embed = discord.Embed(title=":star::star::star::star::star:\
                        \000\000\000\000\000\000\000\000\000\000\
                        \000\000\000\000\000\000\000\000\n눈 그친 뒤의 매화향 · 호두\n", description="\000\n\000\n배도 채웠으니, 편히가렴~", color=0x8989a5)

                    embed.set_thumbnail(url="https://i.imgur.com/LtsRXSc.png")
                    embed.add_field(name="신의 눈", value="불", inline=True)
                    embed.add_field(name="생일", value="7월 15일", inline=True)
                    embed.add_field(name="별자리", value="나비자리", inline=True)

                    embed.add_field(name="사용 무기", value="호마창", inline=True)
                    embed.add_field(name="돌파 스텟", value="치명타 피해%", inline=True)
                    embed.add_field(name="성우", value="たかはし りえ\n\000", inline=True)

                    embed.add_field(name="특성소재", value="근면의 철학 <화,금,일>\n마왕의 칼날·조각 <마왕 타르탈리아>\n원소 꽃꿀\n\000", inline=False)
                    embed.add_field(name="무기추천", value="호마의 지팡이, 화박연, 용학살창\n\000", inline=False)
                    embed.add_field(name="성유물 추천", value="마녀4셋, 유성4셋\n\000", inline=False)
       
                    await message.channel.send(embed=embed)
                    
                elif targetNoneblank == "바바라":
                    findsuccess = True
                    embed = discord.Embed(title=":star::star::star::star:\
                        \000\000\000\000\000\000\000\000\000\000\
                        \000\000\000\000\000\000\000\000\000\000\n빛나는 아이돌 · 바바라\n", description="\000\n\000\n공연 시작~!", color=0x8989a5)

                    embed.set_thumbnail(url="https://i.imgur.com/zzSWKNe.jpg")
                    embed.add_field(name="신의 눈", value="물", inline=True)
                    embed.add_field(name="생일", value="7월 5일", inline=True)
                    embed.add_field(name="별자리", value="황금잔자리", inline=True)

                    embed.add_field(name="사용 무기", value="법구", inline=True)
                    embed.add_field(name="돌파 스텟", value="HP%", inline=True)
                    embed.add_field(name="성우", value="きとう あかり\n\000", inline=True)

                    embed.add_field(name="특성소재", value="자유의 철학 <월,목,일>\n북풍의 고리 <안드리우스>\n금주의 두루마리\n\000", inline=False)
                    embed.add_field(name="무기추천", value="드래곤 슬레이어 영웅담, 황금 호박 프로토타입, 페보니우스 비전\n\000", inline=False)
                    embed.add_field(name="성유물 추천", value="소녀4셋\n\000", inline=False)
       
                    await message.channel.send(embed=embed)
                    
                elif targetNoneblank == "모나":
                    findsuccess = True
                    embed = discord.Embed(title=":star::star::star::star::star:\
                        \000\000\000\000\000\000\000\000\000\000\
                        \000\000\000\000\000\000\000\000\n별하늘의 물거울 · 모나\n", description="\000\n\000\n운명이여, 드러나거라!", color=0x8989a5)

                    embed.set_thumbnail(url="https://i.imgur.com/ILnNhF7.jpg")
                    embed.add_field(name="신의 눈", value="물", inline=True)
                    embed.add_field(name="생일", value="8월 31일", inline=True)
                    embed.add_field(name="별자리", value="영천자리", inline=True)

                    embed.add_field(name="사용 무기", value="법구", inline=True)
                    embed.add_field(name="돌파 스텟", value="원소 충전 효율%", inline=True)
                    embed.add_field(name="성우", value="こはら このみ\n\000", inline=True)

                    embed.add_field(name="특성소재", value="투쟁의 철학 <화,금,일>\n북풍의 고리 <안드리우스>\n원소 꽃꿀\n\000", inline=False)
                    embed.add_field(name="무기추천", value="음유시인의 악장, 천공의 두루마리, 사풍 원서, 드래곤 슬레이어 영웅담\n\000", inline=False)
                    embed.add_field(name="성유물 추천", value="왕실2셋+몰락2셋, 왕실4셋\n\000", inline=False)
       
                    await message.channel.send(embed=embed)
                    
                elif targetNoneblank == "행추":
                    findsuccess = True
                    embed = discord.Embed(title=":star::star::star::star:\
                        \000\000\000\000\000\000\000\000\000\000\
                        \000\000\000\000\000\000\000\000\000\000\n의기충천 · 행추\n", description="\000\n\000\n고 화 신 비!", color=0x8989a5)

                    embed.set_thumbnail(url="https://i.imgur.com/MBj96Ga.jpg")
                    embed.add_field(name="신의 눈", value="물", inline=True)
                    embed.add_field(name="생일", value="10월 9일", inline=True)
                    embed.add_field(name="별자리", value="금직자리", inline=True)

                    embed.add_field(name="사용 무기", value="한손검", inline=True)
                    embed.add_field(name="돌파 스텟", value="공격력%", inline=True)
                    embed.add_field(name="성우", value="みながわ じゅんこ\n\000", inline=True)

                    embed.add_field(name="특성소재", value="황금의 철학 <수,토,일>\n북풍의 꼬리 <안드리우스>\n불길한 가면\n\000", inline=False)
                    embed.add_field(name="무기추천", value="제례검, 천공의 검, 페보니우스 검, 부식의 검\n\000", inline=False)
                    embed.add_field(name="성유물 추천", value="몰락4셋, 왕실4셋\n\000", inline=False)
       
                    await message.channel.send(embed=embed)
                    
                elif targetNoneblank == "타르탈리아":
                    findsuccess = True
                    embed = discord.Embed(title=":star::star::star::star::star:\
                        \000\000\000\000\000\000\000\000\000\000\
                        \000\000\000\000\000\000\000\000\n귀공자 · 타르탈리아\n", description="\000\n\000\n나 타르탈리아는 매순간 강해지고 있다고?ㅋ", color=0x8989a5)

                    embed.set_thumbnail(url="https://i.imgur.com/aVuou1L.jpg")
                    embed.add_field(name="신의 눈", value="물", inline=True)
                    embed.add_field(name="생일", value="7월 20일", inline=True)
                    embed.add_field(name="별자리", value="경천자리", inline=True)

                    embed.add_field(name="사용 무기", value="아마 활", inline=True)
                    embed.add_field(name="돌파 스텟", value="물 원소피해 보너스%", inline=True)
                    embed.add_field(name="성우", value="きむら りょうへい\n\000", inline=True)

                    embed.add_field(name="특성소재", value="자유의 철학 <월,목,일>\n마왕의 칼날·조각 <마왕 타르탈리아>\n위관의 휘장\n\000", inline=False)
                    embed.add_field(name="무기추천", value="천공의 날개, 청록의 사냥활, 녹슨 활, 절현\n\000", inline=False)
                    embed.add_field(name="성유물 추천", value="몰락4셋, 몰락2셋+왕실2셋\n\000", inline=False)
       
                    await message.channel.send(embed=embed)
                    
                elif targetNoneblank == "북두":
                    findsuccess = True
                    embed = discord.Embed(title=":star::star::star::star:\
                        \000\000\000\000\000\000\000\000\000\000\
                        \000\000\000\000\000\000\000\000\000\000\n무관의 용왕 · 북두\n", description="\000\n\000\n이게, 해산을 멸하는 힘이다!", color=0x8989a5)

                    embed.set_thumbnail(url="https://i.imgur.com/qOQkfoK.jpg")
                    embed.add_field(name="신의 눈", value="번개", inline=True)
                    embed.add_field(name="생일", value="2월 14일", inline=True)
                    embed.add_field(name="별자리", value="남천해산자리", inline=True)

                    embed.add_field(name="사용 무기", value="양손검", inline=True)
                    embed.add_field(name="돌파 스텟", value="번개 원소피해 보너스%", inline=True)
                    embed.add_field(name="성우", value="こしみず あみ\n\000", inline=True)

                    embed.add_field(name="특성소재", value="황금의 철학 <수,토,일>\n동풍의 숨결 <드발린>\n골드 까마귀 휘장\n\000", inline=False)
                    embed.add_field(name="무기추천", value="늑대의 말로, 천공의 긍지, 이무기 검, 고화 프로토타입\n\000", inline=False)
                    embed.add_field(name="성유물 추천", value="검투사4셋, 번분4셋\n\000", inline=False)
       
                    await message.channel.send(embed=embed)
                    
                elif targetNoneblank == "피슬":
                    findsuccess = True
                    embed = discord.Embed(title=":star::star::star::star:\
                        \000\000\000\000\000\000\000\000\000\000\
                        \000\000\000\000\000\000\000\000\000\000\n단죄의 황녀!! · 피슬\n", description="\000\n\000\n나와라, 오즈!", color=0x8989a5)

                    embed.set_thumbnail(url="https://i.imgur.com/FKSga7s.jpg")
                    embed.add_field(name="신의 눈", value="번개", inline=True)
                    embed.add_field(name="생일", value="5월 27일", inline=True)
                    embed.add_field(name="별자리", value="환상까마귀자리", inline=True)

                    embed.add_field(name="사용 무기", value="활", inline=True)
                    embed.add_field(name="돌파 스텟", value="공격력%", inline=True)
                    embed.add_field(name="성우", value="うちだ まあや\n\000", inline=True)

                    embed.add_field(name="특성소재", value="시문의 철학 <수,토,일>\n북풍의 영혼상자 <안드리우스>\n역전의 화살촉\n\000", inline=False)
                    embed.add_field(name="무기추천", value="천공의 날개, 녹슨 활, 절현, 강철궁\n\000", inline=False)
                    embed.add_field(name="성유물 추천", value="검투2셋+번분2셋, 뇌명4셋, 번분4셋\n\000", inline=False)
       
                    await message.channel.send(embed=embed)
                    
                elif targetNoneblank == "각청":
                    findsuccess = True
                    embed = discord.Embed(title=":star::star::star::star::star:\
                        \000\000\000\000\000\000\000\000\000\000\
                        \000\000\000\000\000\000\000\000\n질뢰쾌우 · 각청\n", description="\000\n\000\n옥형성 등장! ㅇㅈㄹㅋㅋ", color=0x8989a5)

                    embed.set_thumbnail(url="https://i.imgur.com/3OAkXsG.jpg")
                    embed.add_field(name="신의 눈", value="ㅈ개", inline=True)
                    embed.add_field(name="생일", value="11월 20일", inline=True)
                    embed.add_field(name="별자리", value="금자정수자리", inline=True)

                    embed.add_field(name="사용 무기", value="한솜검", inline=True)
                    embed.add_field(name="돌파 스텟", value="치명타 피해%", inline=True)
                    embed.add_field(name="성우", value="きたむら えり\n\000", inline=True)

                    embed.add_field(name="특성소재", value="번영의 철학 <월,목,일>\n북풍의 고리 <안드리우스>\n원소 꽃꿀\n\000", inline=False)
                    embed.add_field(name="무기추천", value="매의 검, 천공의 검, 칠흑검, 용의 포효\n\000", inline=False)
                    embed.add_field(name="성유물 추천", value="번분4셋, 번분2셋+왕실2셋\n\000", inline=False)
       
                    await message.channel.send(embed=embed)
                    
                elif targetNoneblank == "리사":
                    findsuccess = True
                    embed = discord.Embed(title=":star::star::star::star:\
                        \000\000\000\000\000\000\000\000\000\000\
                        \000\000\000\000\000\000\000\000\000\000\n장미 마녀 · 리사\n", description="\000\n\000\n누나가~ 도와줄게", color=0x8989a5)

                    embed.set_thumbnail(url="https://i.imgur.com/waik67J.jpg")
                    embed.add_field(name="신의 눈", value="번개", inline=True)
                    embed.add_field(name="생일", value="6월 9일", inline=True)
                    embed.add_field(name="별자리", value="모래시계자리", inline=True)

                    embed.add_field(name="사용 무기", value="법구", inline=True)
                    embed.add_field(name="돌파 스텟", value="원소 마스터리", inline=True)
                    embed.add_field(name="성우", value="たなか りえ\n\000", inline=True)

                    embed.add_field(name="특성소재", value="시문의 철학 <수,토,일>\n동풍의 발톱 <드발린>\n슬라임 원액\n\000", inline=False)
                    embed.add_field(name="무기추천", value="음유시인의 악장, 천공의 두루마리, 사풍 원서, 페보니우스 비전\n\000", inline=False)
                    embed.add_field(name="성유물 추천", value="뇌명4셋, 번분4셋\n\000", inline=False)
       
                    await message.channel.send(embed=embed)
                    
                elif targetNoneblank == "레이저":
                    findsuccess = True
                    embed = discord.Embed(title=":star::star::star::star:\
                        \000\000\000\000\000\000\000\000\000\000\
                        \000\000\000\000\000\000\000\000\000\000\n늑대소년 · 레이저\n", description="\000\n\000\n안가? 배고파. 고깃덩어리. 좋아.", color=0x8989a5)

                    embed.set_thumbnail(url="https://i.imgur.com/rVwdmIu.jpg")
                    embed.add_field(name="신의 눈", value="번개", inline=True)
                    embed.add_field(name="생일", value="9월 9일", inline=True)
                    embed.add_field(name="별자리", value="이리자리", inline=True)

                    embed.add_field(name="사용 무기", value="양손검", inline=True)
                    embed.add_field(name="돌파 스텟", value="물리피해 보너스%", inline=True)
                    embed.add_field(name="성우", value="うちやま こうき\n\000", inline=True)

                    embed.add_field(name="특성소재", value="투쟁의 철학 <화,금,일>\n동풍의 발톱 <드발린>\n불길한 가면\n\000", inline=False)
                    embed.add_field(name="무기추천", value="늑대의 말로, 천공의 긍지, 이무기 검, 고화 프로토타입\n\000", inline=False)
                    embed.add_field(name="성유물 추천", value="검투사4셋, 뇌명4셋\n\000", inline=False)
       
                    await message.channel.send(embed=embed)
                    
                elif targetNoneblank == "중운":
                    findsuccess = True
                    embed = discord.Embed(title=":star::star::star::star:\
                        \000\000\000\000\000\000\000\000\000\000\
                        \000\000\000\000\000\000\000\000\000\000\n얼어붙은 정열 · 중운\n", description="\000\n\000\n내겐 악귀를 퇴치하는 주문이 있어!", color=0x8989a5)

                    embed.set_thumbnail(url="https://i.imgur.com/uVuHDWU.jpg")
                    embed.add_field(name="신의 눈", value="얼음", inline=True)
                    embed.add_field(name="생일", value="9월 7일", inline=True)
                    embed.add_field(name="별자리", value="건곤봉자리", inline=True)

                    embed.add_field(name="사용 무기", value="양손검", inline=True)
                    embed.add_field(name="돌파 스텟", value="공격력%", inline=True)
                    embed.add_field(name="성우", value="さいとう そうま\n\000", inline=True)

                    embed.add_field(name="특성소재", value="근면의 철학 <화,금,일>\n동풍의 숨결 <드발린>\n불길한 가면\n\000", inline=False)
                    embed.add_field(name="무기추천", value="늑대의 말로, 제례 대검, 페보니우스 대검, 고화 프로토타입\n\000", inline=False)
                    embed.add_field(name="성유물 추천", value="얼음바람4셋, 왕실4셋\n\000", inline=False)
       
                    await message.channel.send(embed=embed)
                    
                elif targetNoneblank == "케이아":
                    findsuccess = True
                    embed = discord.Embed(title=":star::star::star::star:\
                        \000\000\000\000\000\000\000\000\000\000\
                        \000\000\000\000\000\000\000\000\000\000\n한풍의 검사 · 케이아\n", description="\000\n\000\n정말 평화롭군! 하지만, 이게 얼마나 갈까?", color=0x8989a5)

                    embed.set_thumbnail(url="https://i.imgur.com/kTb9BXV.jpg")
                    embed.add_field(name="신의 눈", value="얼음", inline=True)
                    embed.add_field(name="생일", value="11월 30일", inline=True)
                    embed.add_field(name="별자리", value="공작깃털자리", inline=True)

                    embed.add_field(name="사용 무기", value="한손검", inline=True)
                    embed.add_field(name="돌파 스텟", value="원소 충전 효율%", inline=True)
                    embed.add_field(name="성우", value="とりうみ こうすけ\n\000", inline=True)

                    embed.add_field(name="특성소재", value="시문의 철학 <수,토,일>\n북풍의 영혼상자 <안드리우스>\n골드 까마귀 휘장\n\000", inline=False)
                    embed.add_field(name="무기추천", value="매의 검, 천공의 검, 부식의 검, 참암 프로토타입\n\000", inline=False)
                    embed.add_field(name="성유물 추천", value="얼음바람4셋, 검투사4셋\n\000", inline=False)
       
                    await message.channel.send(embed=embed)
                    
                elif targetNoneblank == "치치":
                    findsuccess = True
                    embed = discord.Embed(title=":star::star::star::star::star:\
                        \000\000\000\000\000\000\000\000\000\000\
                        \000\000\000\000\000\000\000\000\n차가운 환혼의 밤 · 치치\n", description="\000\n\000\n코코넛 밀크..! (치치야사랑해)", color=0x8989a5)

                    embed.set_thumbnail(url="https://i.imgur.com/uN1Cz9m.jpg")
                    embed.add_field(name="신의 눈", value="얼음", inline=True)
                    embed.add_field(name="생일", value="3월 3일", inline=True)
                    embed.add_field(name="별자리", value="삼청령자리", inline=True)

                    embed.add_field(name="사용 무기", value="한손검", inline=True)
                    embed.add_field(name="돌파 스텟", value="치유 보너스%", inline=True)
                    embed.add_field(name="성우", value="たむら ゆかり\n\000", inline=True)

                    embed.add_field(name="특성소재", value="번영의 철학 <월,목,일>\n북풍의 꼬리 <안드리우스>\n금주의 두루마리\n\000", inline=False)
                    embed.add_field(name="무기추천", value="제례검, 천공의 검, 페보니우스 검, 부식의 검\n\000", inline=False)
                    embed.add_field(name="성유물 추천", value="소녀4셋, 왕실4셋\n\000", inline=False)
       
                    await message.channel.send(embed=embed)
                    
                elif targetNoneblank == "디오나":
                    findsuccess = True
                    embed = discord.Embed(title=":star::star::star::star:\
                        \000\000\000\000\000\000\000\000\000\000\
                        \000\000\000\000\000\000\000\000\000\000\n캐츠라인 칵테일 · 디오나\n", description="\000\n\000\n잡았다~ 냥~", color=0x8989a5)

                    embed.set_thumbnail(url="https://i.imgur.com/8kuMuna.jpg")
                    embed.add_field(name="신의 눈", value="얼음", inline=True)
                    embed.add_field(name="생일", value="1월 18일", inline=True)
                    embed.add_field(name="별자리", value="고양이자리", inline=True)

                    embed.add_field(name="사용 무기", value="활", inline=True)
                    embed.add_field(name="돌파 스텟", value="얼음 원소피해 보너스%", inline=True)
                    embed.add_field(name="성우", value="いざわ しおり\n\000", inline=True)

                    embed.add_field(name="특성소재", value="자유의 철학 <월,목,일>\n마왕의 칼날·조각 <마왕 타르탈리아>\n역전의 화살촉\n\000", inline=False)
                    embed.add_field(name="무기추천", value="제례활, 페보니우스 활, 절현\n\000", inline=False)
                    embed.add_field(name="성유물 추천", value="왕실4셋, 소녀4셋\n\000", inline=False)
       
                    await message.channel.send(embed=embed)
                    
                elif targetNoneblank == "감우":
                    findsuccess = True
                    embed = discord.Embed(title=":star::star::star::star::star:\
                        \000\000\000\000\000\000\000\000\000\000\
                        \000\000\000\000\000\000\000\000\n리월의 수호자 · 감우\n", description="\000\n\000\n저와 함께... 야근하실래요?", color=0x8989a5)

                    embed.set_thumbnail(url="https://i.imgur.com/RkwH7GU.png")
                    embed.add_field(name="신의 눈", value="얼음", inline=True)
                    embed.add_field(name="생일", value="12월 2일", inline=True)
                    embed.add_field(name="별자리", value="선린자리", inline=True)

                    embed.add_field(name="사용 무기", value="아모스활", inline=True)
                    embed.add_field(name="돌파 스텟", value="치명타 피해%", inline=True)
                    embed.add_field(name="성우", value="うえだ れいな\n\000", inline=True)

                    embed.add_field(name="특성소재", value="근면의 철학 <화,금,일>\n무예의 혼·고영 <마왕 타르탈리아>\n원소 꽃꿀\n\000", inline=False)
                    embed.add_field(name="무기추천", value="아모스의 활, 흑암 배틀 보우, 담월 프로토타입, 천공의 날개\n\000", inline=False)
                    embed.add_field(name="성유물 추천", value="얼음4셋, 얼음2셋+악단2셋, 악단4셋, 왕실4셋\n\000", inline=False)
       
                    await message.channel.send(embed=embed)
                    
                elif targetNoneblank == "진":
                    findsuccess = True
                    embed = discord.Embed(title=":star::star::star::star::star:\
                        \000\000\000\000\000\000\000\000\000\000\
                        \000\000\000\000\000\000\000\000\n민들레 기사 · 진\n", description="\000\n\000\n바람의 신이여, 우릴 인도하소서!", color=0x8989a5)

                    embed.set_thumbnail(url="https://i.imgur.com/eyn6137.jpg")
                    embed.add_field(name="신의 눈", value="바람", inline=True)
                    embed.add_field(name="생일", value="3월 14일", inline=True)
                    embed.add_field(name="별자리", value="새끼사자자리", inline=True)

                    embed.add_field(name="사용 무기", value="한손검", inline=True)
                    embed.add_field(name="돌파 스텟", value="치유 보너스%", inline=True)
                    embed.add_field(name="성우", value="さいとう ちわ\n\000", inline=True)

                    embed.add_field(name="특성소재", value="투쟁의 철학 <화,금,일>\n동풍의 깃털 <드발린>\n불길한 가면\n\000", inline=False)
                    embed.add_field(name="무기추천", value="매의 검, 천공의 검, 피리검, 부식의 검\n\000", inline=False)
                    embed.add_field(name="성유물 추천", value="검투2셋+청록2셋, 소녀4셋, 왕실4셋\n\000", inline=False)
       
                    await message.channel.send(embed=embed)
                    
                elif targetNoneblank == "설탕":
                    findsuccess = True
                    embed = discord.Embed(title=":star::star::star::star:\
                        \000\000\000\000\000\000\000\000\000\000\
                        \000\000\000\000\000\000\000\000\000\000\n무해한 달콤함 · 설탕\n", description="\000\n\000\n무상의 바람, 복제", color=0x8989a5)

                    embed.set_thumbnail(url="https://i.imgur.com/mr1m0fr.jpg")
                    embed.add_field(name="신의 눈", value="바람", inline=True)
                    embed.add_field(name="생일", value="11월 26일", inline=True)
                    embed.add_field(name="별자리", value="플라스크자리", inline=True)

                    embed.add_field(name="사용 무기", value="법구", inline=True)
                    embed.add_field(name="돌파 스텟", value="바람 원소피해 보너스%", inline=True)
                    embed.add_field(name="성우", value="ふじた あかね\n\000", inline=True)

                    embed.add_field(name="특성소재", value="자유의 철학 <월,목,일>\n북풍의 영혼상자 <안드리우스>\n원소 꽃꿀\n\000", inline=False)
                    embed.add_field(name="무기추천", value="제례의 악장, 드래곤 슬레이어 영웅담, 페보니우스 비전, 만국 항해용해도\n\000", inline=False)
                    embed.add_field(name="성유물 추천", value="청록4셋, 왕실4셋\n\000", inline=False)
       
                    await message.channel.send(embed=embed)
                    
                elif targetNoneblank == "벤티":
                    findsuccess = True
                    embed = discord.Embed(title=":star::star::star::star::star:\
                        \000\000\000\000\000\000\000\000\000\000\
                        \000\000\000\000\000\000\000\000\n바람의 시인 · 벤티\n", description="\000\n\000\n계속 듣고싶다면~ 내게 사과 하나만 줘", color=0x8989a5)

                    embed.set_thumbnail(url="https://i.imgur.com/mqjZuGg.jpg")
                    embed.add_field(name="신의 눈", value="바람", inline=True)
                    embed.add_field(name="생일", value="6월 16일", inline=True)
                    embed.add_field(name="별자리", value="가선자리", inline=True)

                    embed.add_field(name="사용 무기", value="활", inline=True)
                    embed.add_field(name="돌파 스텟", value="원소 충전 효율%", inline=True)
                    embed.add_field(name="성우", value="むらせ あゆむ\n\000", inline=True)

                    embed.add_field(name="특성소재", value="시문의 철학 <수,토,일>\n북풍의 꼬리 <안드리우스>\n슬라임 원액\n\000", inline=False)
                    embed.add_field(name="무기추천", value="천공의 날개, 아모스의 활, 절현, 페보니우스 활\n\000", inline=False)
                    embed.add_field(name="성유물 추천", value="청록4셋\n\000", inline=False)
       
                    await message.channel.send(embed=embed)
                    
                elif targetNoneblank == "소":
                    findsuccess = True
                    embed = discord.Embed(title=":star::star::star::star::star:\
                        \000\000\000\000\000\000\000\000\000\000\
                        \000\000\000\000\000\000\000\000\n호법야차 · 소\n", description="\000\n\000\n무능하군! 무능하군! 무능하군!", color=0x8989a5)

                    embed.set_thumbnail(url="https://i.imgur.com/29SKUZX.png")
                    embed.add_field(name="신의 눈", value="바람", inline=True)
                    embed.add_field(name="생일", value="4월 17일", inline=True)
                    embed.add_field(name="별자리", value="황금날개천붕왕자리", inline=True)

                    embed.add_field(name="사용 무기", value="장병기", inline=True)
                    embed.add_field(name="돌파 스텟", value="치명타 확률%", inline=True)
                    embed.add_field(name="성우", value="まつおか よしつぐ\n\000", inline=True)

                    embed.add_field(name="특성소재", value="번영의 철학 <월,목,일>\n무예의 혼·고영 <마왕 타르탈리아>\n슬라임 원액\n\000", inline=False)
                    embed.add_field(name="무기추천", value="화박연, 호마의 지팡이, 관홍의 창\n\000", inline=False)
                    embed.add_field(name="성유물 추천", value="청록2셋+검투사2셋\n\000", inline=False)
       
                    await message.channel.send(embed=embed)
                    
                elif targetNoneblank == "응광":
                    findsuccess = True
                    embed = discord.Embed(title=":star::star::star::star:\
                        \000\000\000\000\000\000\000\000\000\000\
                        \000\000\000\000\000\000\000\000\000\000\n엄월천권 · 응광\n", description="\000\n\000\n어쨌든, 모라는 많을수록 좋으니까", color=0x8989a5)

                    embed.set_thumbnail(url="https://i.imgur.com/Pub9P1j.jpg")
                    embed.add_field(name="신의 눈", value="바위", inline=True)
                    embed.add_field(name="생일", value="8월 26일", inline=True)
                    embed.add_field(name="별자리", value="기형의자리", inline=True)

                    embed.add_field(name="사용 무기", value="법구", inline=True)
                    embed.add_field(name="돌파 스텟", value="바위 원소피해 보너스%", inline=True)
                    embed.add_field(name="성우", value="おおはら さやか\n\000", inline=True)

                    embed.add_field(name="특성소재", value="번영의 철학 <월,목,일>\n북풍의 영혼상자 <안드리우스>\n위관의 휘장\n\000", inline=False)
                    embed.add_field(name="무기추천", value="사풍 원서, 천공의 두루마리, 속세의 자물쇠, 일월의 정수\n\000", inline=False)
                    embed.add_field(name="성유물 추천", value="유성4셋, 검투2셋+반암2셋\n\000", inline=False)
       
                    await message.channel.send(embed=embed)
                    
                elif targetNoneblank == "노엘":
                    findsuccess = True
                    embed = discord.Embed(title=":star::star::star::star:\
                        \000\000\000\000\000\000\000\000\000\000\
                        \000\000\000\000\000\000\000\000\000\000\n수여받지 못한 꽃 · 노엘\n", description="\000\n\000\n전장을 청소해야 겠군요!", color=0x8989a5)

                    embed.set_thumbnail(url="https://i.imgur.com/Y2NI8nM.jpg")
                    embed.add_field(name="신의 눈", value="바위", inline=True)
                    embed.add_field(name="생일", value="3월 21일", inline=True)
                    embed.add_field(name="별자리", value="심호자리", inline=True)

                    embed.add_field(name="사용 무기", value="양손검", inline=True)
                    embed.add_field(name="돌파 스텟", value="방어력%", inline=True)
                    embed.add_field(name="성우", value="たかお かのん\n\000", inline=True)

                    embed.add_field(name="특성소재", value="투쟁의 철학 <화,금,일>\n동풍의 발톱 <드발린>\n불길한 가면\n\000", inline=False)
                    embed.add_field(name="무기추천", value="늑대의 말로, 천공의 긍지, 백영검, 무공의 검\n\000", inline=False)
                    embed.add_field(name="성유물 추천", value="검투사4셋, 유성4셋\n\000", inline=False)
       
                    await message.channel.send(embed=embed)
                    
                elif targetNoneblank == "종려":
                    findsuccess = True
                    embed = discord.Embed(title=":star::star::star::star::star:\
                        \000\000\000\000\000\000\000\000\000\000\
                        \000\000\000\000\000\000\000\000\n속세 한유 · 종려\n", description="\000\n\000\n아쉽게도 까먹었어..", color=0x8989a5)

                    embed.set_thumbnail(url="https://i.imgur.com/1B4u2YQ.jpg")
                    embed.add_field(name="신의 눈", value="바위", inline=True)
                    embed.add_field(name="생일", value="12월 31일", inline=True)
                    embed.add_field(name="별자리", value="암왕제군자리", inline=True)

                    embed.add_field(name="사용 무기", value="장병기", inline=True)
                    embed.add_field(name="돌파 스텟", value="바위 원소피해 보너스%", inline=True)
                    embed.add_field(name="성우", value="まえの ともあき\n\000", inline=True)

                    embed.add_field(name="특성소재", value="황금의 철학 <수,토,일>\n하늘을 삼킨 고래·뿔 <마왕 타르탈리아>\n슬라임 원액\n\000", inline=False)
                    embed.add_field(name="무기추천", value="호마의 지팡이, 화박연, 관홍의 창\n\000", inline=False)
                    embed.add_field(name="성유물 추천", value="유성4셋, 왕실2셋+반암2셋\n\000", inline=False)
       
                    await message.channel.send(embed=embed)
                    
                elif targetNoneblank == "알베도":
                    findsuccess = True
                    embed = discord.Embed(title=":star::star::star::star::star:\
                        \000\000\000\000\000\000\000\000\000\000\
                        \000\000\000\000\000\000\000\000\n백악의 아이 · 알베도\n", description="\000\n\000\n생명, 창조의 법칙", color=0x8989a5)

                    embed.set_thumbnail(url="https://i.imgur.com/WAMUxDq.jpg")
                    embed.add_field(name="신의 눈", value="바위", inline=True)
                    embed.add_field(name="생일", value="9월 13일", inline=True)
                    embed.add_field(name="별자리", value="백악의아이자리", inline=True)

                    embed.add_field(name="사용 무기", value="한손검", inline=True)
                    embed.add_field(name="돌파 스텟", value="바위 원소피해 보너스%", inline=True)
                    embed.add_field(name="성우", value="のじま けんじ\n\000", inline=True)

                    embed.add_field(name="특성소재", value="시문의 철학 <수,토,일>\n하늘을 삼킨 고래·뿔 <마왕 타르탈리아>\n금주의 두루마리\n\000", inline=False)
                    embed.add_field(name="무기추천", value="반암결록, 여명신검, 부식의 검, 천공의 검\n\000", inline=False)
                    embed.add_field(name="성유물 추천", value="반암4셋, 유성4셋\n\000", inline=False)
       
                    await message.channel.send(embed=embed)

            elif dataType == 1 and data == targetNoneblank:
                if targetNoneblank == "매의검":
                    findsuccess = True
                    #a = str(target)
                    #print(a)
                    #targetlen = len(a)
                    #await message.channel.send(a)
                    #await message.channel.send(target[0]+"\n타겟의 0번째 인덱스 출력")
                    #await message.channel.send(target[1]+"\n타겟의 1번째 인덱스 출력")
                    #await message.channel.send(target[2]+"\n타겟의 2번째 인덱스 출력")
                    #await message.channel.send(target[3]+"\n타겟의 3번째 인덱스 출력")
                    #await message.channel.send(target[4]+"\n타겟의 4번째 인덱스 출력")
                    #await message.channel.send(targetlen)
                    #await message.channel.send("target_len")
                    embed = discord.Embed()
                    embed.set_image(url="https://i.imgur.com/nkJkn6G.png")
                    await message.channel.send(embed=embed)

                if targetNoneblank == "천공의검":
                    findsuccess = True
                    
                    embed = discord.Embed()
                    embed.set_image(url="https://i.imgur.com/yeopYXL.png")
                    await message.channel.send(embed=embed)

                if targetNoneblank == "참봉의칼날":
                    findsuccess = True
                    
                    embed = discord.Embed()
                    embed.set_image(url="https://i.imgur.com/Z4uyWC4.png")
                    await message.channel.send(embed=embed)

                if targetNoneblank == "반암결록":
                    findsuccess = True
                    
                    embed = discord.Embed()
                    embed.set_image(url="https://i.imgur.com/NF6sA4D.png")
                    await message.channel.send(embed=embed)

                if targetNoneblank == "천공의긍지":
                    findsuccess = True
                    
                    embed = discord.Embed()
                    embed.set_image(url="https://i.imgur.com/WIYctKq.png")
                    await message.channel.send(embed=embed)

                if targetNoneblank == "늑대의말로":
                    findsuccess = True
                    
                    embed = discord.Embed()
                    embed.set_image(url="https://i.imgur.com/ZHZyC6I.png")
                    await message.channel.send(embed=embed)

                if targetNoneblank == "무공의검":
                    findsuccess = True
                    
                    embed = discord.Embed()
                    embed.set_image(url="https://i.imgur.com/DvVTOvb.png")
                    await message.channel.send(embed=embed)

                if targetNoneblank == "천공의두루마리":
                    findsuccess = True
                    
                    embed = discord.Embed()
                    embed.set_image(url="https://i.imgur.com/4cgrxvc.png")
                    await message.channel.send(embed=embed)

                if targetNoneblank == "사풍원서":
                    findsuccess = True
                    
                    embed = discord.Embed()
                    embed.set_image(url="https://i.imgur.com/aTNb5Xr.png")
                    await message.channel.send(embed=embed)

                if targetNoneblank == "속세의자물쇠":
                    findsuccess = True
                    
                    embed = discord.Embed()
                    embed.set_image(url="https://i.imgur.com/HQ9H41e.png")
                    await message.channel.send(embed=embed)

                if targetNoneblank == "천공의날개":
                    findsuccess = True
                    
                    embed = discord.Embed()
                    embed.set_image(url="https://i.imgur.com/cYQHPAm.png")
                    await message.channel.send(embed=embed)

                if targetNoneblank == "아모스의활":
                    findsuccess = True
                    
                    embed = discord.Embed()
                    embed.set_image(url="https://i.imgur.com/jEUupRP.png")
                    await message.channel.send(embed=embed)

                if targetNoneblank == "화박연":
                    findsuccess = True
                    
                    embed = discord.Embed()
                    embed.set_image(url="https://i.imgur.com/D4gwRAp.png")
                    await message.channel.send(embed=embed)

                if targetNoneblank == "천공의마루":
                    findsuccess = True
                    
                    embed = discord.Embed()
                    embed.set_image(url="https://i.imgur.com/XQ0PblV.png")
                    await message.channel.send(embed=embed)

                if targetNoneblank == "관홍의창":
                    findsuccess = True
                    
                    embed = discord.Embed()
                    embed.set_image(url="https://i.imgur.com/8MPA7c8.png")
                    await message.channel.send(embed=embed)

                if targetNoneblank == "호마의지팡이":
                    findsuccess = True
                    
                    embed = discord.Embed()
                    embed.set_image(url="https://i.imgur.com/C25nok6.png")
                    await message.channel.send(embed=embed)

          
        if findsuccess == False:

            await message.channel.send("일치하는 정보를 찾지 못했어요..")
            await message.channel.send("4성 무기는 준비중입니다..")
            await message.channel.send("!도움 을 입력해 주세요")

        

    if message.content == "!무기":
        embed = discord.Embed(title="무기 리스트\000\000\000\000\000\
            \000\000\000\000\000\000\000\000\000\000\
            \000\000\000\000\000\000\000\000\000\000\
            ", description="\000", color=0x8989a5)

        embed.add_field(name="한손검", value="[★★★★★]\n매의 검, 천공의 검, 참봉의 칼날, 반암결록\n\
            [★★★★]\n페보니우스 검, 피리검, 제례검, 왕실의 장검, 용의 포효, 참암 프로토타입, 강철 벌침, 흑암 장검, 칠흑검, 강림의 검, 부식의 검, 뒷골목의 섬광\n\000", inline=False)

        embed.add_field(name="양손검", value="[★★★★★]\n천공의 긍지, 늑대의 말로, 무공의 검\n\
            [★★★★]\n페보니우스 대검, 시간의 검, 제례 대검, 왕실의 대검, 빗물 베기, 고화 프로토타입, 백영검, 흑암참도, 이무기 검, 설장의 성은, 천암고검\n\000", inline=False)

        embed.add_field(name="법구", value="[★★★★★]\n천공의 두루마리, 사풍 원서, 속세의 자물쇠\n\
            [★★★★]\n페보니우스 비전, 음유시인의 악장, 제례의 악장, 왕실의 비전록, 일월의 정수, 황금 호박 프로토타입, 만국 항해용해도, 흑암 홍옥, 소심, 인동의 열매, 뒷골목의 술과 시\n\000", inline=False)

        embed.add_field(name="활", value="[★★★★★]\n천공의 날개, 아모스의 활, 종말 탄식의 노래\n\
            [★★★★]\n페보니우스 활, 절현, 제례활, 왕실의 장궁, 녹슨 활, 담월 프로토타입, 강철궁, 흑암 배틀 보우, 청록의 사냥활, 바람 꽃의 노래, 뒷골목 사냥꾼\n\000", inline=False)

        embed.add_field(name="장병기", value="[★★★★★]\n화박연, 천공의 마루, 관홍의 창, 호마의 지팡이\n\
            [★★★★]\n용학살창, 별의 낫 프로토타입, 유월창, 흑암창, 결투의 창, 페보니우스 장창, 왕실의 장창, 용의 척추, 천암 장창\n\000", inline=False)
       
        await message.channel.send(embed=embed)

    if message.content == "!가챠":
        embed = discord.Embed()
        embed.add_field(name="!상시", value="상시 10연차 시뮬레이션\n\000", inline=False)
        embed.add_field(name="!한정", value="한정 10연차 시뮬레이션\n현재 픽업: 벤티, 노엘, 설탕, 레이저(준비중)\n\000", inline=False)
        embed.add_field(name="!무기", value="무기 10연차 시뮬레이션\n현재 픽업: 종말 탄식의 노래, 천공의 검(준비중)", inline=False)
        await message.channel.send(embed=embed)

    def StandardWishStackCounter(user):

        global standardGachaStack
        # global oderNumber
        a = 0

        for x, y in standardGachaStack:   

            if y == user:
                
                if x < 8:
                    x = x + 1
                    standardGachaStack[a][0] = x

                    return 0

                if x >= 8:
                    x = 0
                    standardGachaStack[a][0] = x

                    return 1

            a = a + 1

        standardGachaStack.append([1, user])

        return 0

    def gacha(percent): # 확률을 퍼센트로 받아, 확률에 따라 참과 거짓을 반환하는 함수를 선언한다.

        prob = percent * 0.01 # 퍼센트 값을 0과 1 사이의 숫자로 바꾼다.
        rand = random.random() # 의사난수 모듈을 사용하여, 0과 1 사이의 난수 하나를 뽑는다.

        if prob >= rand: # 확률보다 난수가 작거나 같으면 참(True)을 반환한다. 아니면 거짓(False)이다.
            return True

        else:
            return False

    def standardWish(user, count):

        global standardGachaStack
        global standardGachaList
        global standardGachaResult
        
        # 천장발동
        if count == 1:
            for i in standardGachaList:
                get = gacha(0.6)

                if get == True:
                    standardGachaList[i] = 5

            for i in standardGachaList:
                get = gacha(5.1)

                if get == True:
                    if standardGachaList[i] != 5:
                        standardGachaList[i] = 4

            a = 0
            for i in standardGachaList:
                
                if i == 3:

                    standardGachaList[a] = 5

                    b = 0
                    for x, y in standardGachaStack:
                        
                        if y == user:
                            x = 0
                            standardGachaStack[b][0] = x

                            standardGachaList.sort(reverse=True)

                            for i in standardGachaList:
                                if i == 3:
                                    j = standardGachaWeapon3[0]
                                    getItem = random.randint(1, j)
                                    standardGachaResult.append(standardGachaWeapon3[getItem])

                                if i == 4:
                                    item = True
                                    rItem = random.randint(0,1)

                                    if rItem == 0:
                                        item = False
                                    elif rItem == 1:
                                        item = True

                                    j = standardGachaWeapon4[0]
                                    k = standardGachaCharactor4[0]

                                    if item == True:
                                        getItem = random.randint(1, j)
                                        standardGachaResult.append(standardGachaWeapon4[getItem])

                                    if item == False:
                                        getItem = random.randint(1, k)
                                        standardGachaResult.append(standardGachaCharactor4[getItem])
                    

                                if i == 5:
                                    item = True
                                    rItem = random.randint(0,1)

                                    if rItem == 0:
                                        item = False
                                    elif rItem == 1:
                                        item = True

                                    j = standardGachaWeapon5[0]
                                    k = standardGachaCharactor5[0]

                                    if item == True:
                                        getItem = random.randint(1, j)
                                        standardGachaResult.append(standardGachaWeapon5[getItem])

                                    if item == False:
                                        getItem = random.randint(1, k)
                                        standardGachaResult.append(standardGachaCharactor5[getItem])


                            return standardGachaResult

                    b = b + 1

                a = a + 1

        # 기본확률
        if count == 0:
            gacha5 = 0
            gacha4 = 0
            
            for i in standardGachaList:
                get = gacha(0.6)

                if get == True:
                    standardGachaList[i] = 5

            for i in standardGachaList:
                get = gacha(5.1)

                if get == True:
                    standardGachaList[i] = 4

            for i in standardGachaList:

                if i == 5:
                    gacha5 = gacha5 + 1

                elif i == 4:
                    gacha4 = gacha4 + 1

            #4성 5성 모두 획득실패시 4성 하나 확정
            if gacha4 == 0 and gacha5 == 0:
                standardGachaList[0] = 4

            #5성 획득시 스택초기화
            if gacha5 >= 1:
                a = 0
                for x, y in standardGachaStack:
                    if y == user:
                        x = 0
                        standardGachaStack[a][0] = x
                
                    a = a + 1

            standardGachaList.sort(reverse=True)

            for i in standardGachaList:
                if i == 3:
                    j = standardGachaWeapon3[0]
                    getItem = random.randint(1, j)
                    standardGachaResult.append(standardGachaWeapon3[getItem])

                if i == 4:
                    item = True
                    rItem = random.randint(0,1)

                    if rItem == 0:
                        item = False
                    elif rItem == 1:
                        item = True

                    j = standardGachaWeapon4[0]
                    k = standardGachaCharactor4[0]

                    if item == True:
                        getItem = random.randint(1, j)
                        standardGachaResult.append(standardGachaWeapon4[getItem])

                    if item == False:
                        getItem = random.randint(1, k)
                        standardGachaResult.append(standardGachaCharactor4[getItem])
                    

                if i == 5:
                    item = True
                    rItem = random.randint(0,1)

                    if rItem == 0:
                        item = False
                    elif rItem == 1:
                        item = True

                    j = standardGachaWeapon5[0]
                    k = standardGachaCharactor5[0]

                    if item == True:
                        getItem = random.randint(1, j)
                        standardGachaResult.append(standardGachaWeapon5[getItem])

                    if item == False:
                        getItem = random.randint(1, k)
                        standardGachaResult.append(standardGachaCharactor5[getItem])


            return standardGachaResult

        return -1

    if message.content == "!상시":

        global standardGachaList
        global standardGachaResult

        user = message.author.id

        count = StandardWishStackCounter(user)

        result = standardWish(user, count)

        if result == -1:
            await message.channel.send("ERROR1001 확인요망")

        #await message.channel.send(result)

        result01 = str(standardGachaList[0])+"성"
        result02 = str(standardGachaList[1])+"성"
        result03 = str(standardGachaList[2])+"성"
        result04 = str(standardGachaList[3])+"성"
        result05 = str(standardGachaList[4])+"성"
        result06 = str(standardGachaList[5])+"성"
        result07 = str(standardGachaList[6])+"성"
        result08 = str(standardGachaList[7])+"성"
        result09 = str(standardGachaList[8])+"성"
        result10 = str(standardGachaList[9])+"성"
        result11 = ""
        for x, y in standardGachaStack:   

            if y == user:
                result11 = "현재스택은 총 "+str(x*10)+"스택으로 천장까지 "+str(90-x*10)+"스택 남았습니다"
                break

        #최종 결과화면 정리
        msg = "<@{}>".format(message.author.id)
        await message.channel.send(msg+"님에 가챠결과")
        await message.channel.send(msg+"님에 "+result11)

        embed = discord.Embed(title="", description="", color=0x4169E1)

        #embed.set_thumbnail(url="https://i.imgur.com/cJH3kph.jpg")
        embed.add_field(name=result01+"\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000", value=result[0], inline=False)
        embed.add_field(name=result02, value=result[1], inline=False)
        embed.add_field(name=result03, value=result[2], inline=False)
        embed.add_field(name=result04, value=result[3], inline=False)
        embed.add_field(name=result05, value=result[4], inline=False)
        embed.add_field(name=result06, value=result[5], inline=False)
        embed.add_field(name=result07, value=result[6], inline=False)
        embed.add_field(name=result08, value=result[7], inline=False)
        embed.add_field(name=result09, value=result[8], inline=False) 
        embed.add_field(name=result10, value=result[9], inline=False) 

        await message.channel.send(embed=embed)  

        standardGachaList = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
        standardGachaResult = [ ]

        
    if message.content == "!편의":
        await message.channel.send("일이 아직 끝나지 않았어요..")

# 이 아래 구문은 메시지를 보낸 사람의 DM으로 메시지를 보냅니다.
# await message.author.send("응답")

# 여기 token에는 토큰을 넣지 않고 그대로 옮겨 쓰시면 됩니다.
# client.run('token') # 아까 넣어놓은 토큰 가져다가 봇을 실행하라는 부분입니다. 이 코드 없으면 구문이 아무리 완벽해도 실행되지 않습니다.
# client.run(os.environ['token'])
access_token = os.environ["token"]
client.run(access_token)
