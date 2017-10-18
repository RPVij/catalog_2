from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Sports, Base, SportsPlayer

engine = create_engine('sqlite:///sports.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Sports Badminton
sports1 = Sports(name="Badminton")

session.add(sports1)
session.commit()

sportsplayer1 = SportsPlayer(name="Viktor AXELSEN", description="Viktor Axelsen (born January 4, 1994) is a Danish badminton player and the current"
       " men's singles world champion. He was the 2010 World Junior Champion, beating Korea's Kang Ji-wook in the "
       "final to become the first ever European player to hold the title. In 2011, he lost the world junior title to Malaysia's Zulfadli Zulkiffli,"
       "coming in second place. In the 2017 BWF World Championships held in Glasgow, Scotland, he became the World Champion by beating Lin Dan in straight games.",
                     rank="1", country="Denmark", sports=sports1)

session.add(sportsplayer1)
session.commit()


sportsplayer2 = SportsPlayer(name="SON Wan Ho", description="Son Wan-ho is a South Korean badminton player. He competed in the singles event at the "
       "2012 Summer Olympics. He competed at the 2016 Rio Olympics, but was defeated by Chen Long from China in quarter-finals",
                     rank="2", country="S.Korea", sports=sports1)

session.add(sportsplayer2)
session.commit()

sportsplayer3 = SportsPlayer(name="LIN Dan", description="Lin Dan is a Chinese professional badminton player. He is a two-time Olympic champion, "
       "five-time World champion, as well as a six-time All England champion",
                     rank="3", country="China", sports=sports1)

session.add(sportsplayer3)
session.commit()

sportsplayer4 = SportsPlayer(name="SHI Yuqi", description="Shi Yuqi is a Chinese male badminton player. He won the France SuperSeries 2016 champion"
       " on 30 October 2016 by beating Lee Hyun Il from Korea with 21-16, 21-19.",
                     rank="4", country="China", sports=sports1)

session.add(sportsplayer4)
session.commit()

sportsplayer5 = SportsPlayer(name="CHOU Tien Chen", description="Chou Tien-chen is a male badminton player from Taiwan, representing Chinese Taipei."
       " He became the first local shuttler after 17 years in 2016 to win the Chinese Taipei Open GP men’s singles title since Indonesian-born Fung Permadi won it in ",
                     rank="5", country="Chinese Taepei", sports=sports1)

session.add(sportsplayer5)
session.commit()

sportsplayer6 = SportsPlayer(name="CHEN Long", description="Chen Long, nicknamed 'Junior Lin Dan / Little Dan', is a Chinese professional badminton player. He is the "
       "reigning Olympic champion and two-time World champion and All England champion",
                     rank="6", country="China", sports=sports1)

session.add(sportsplayer6)
session.commit()

sportsplayer7 = SportsPlayer(name="LEE Chong Wei", description="Dato' Lee Chong Wei DSPN DB DCSM PJN is a Chinese-Malaysian professional badminton player. As a singles"
       " player, Lee was ranked first worldwide for 199 consecutive weeks from 21 August 2008 to 14 June 2012, despite not winning a major title.",
                     rank="7", country="Malaysia", sports=sports1)

session.add(sportsplayer7)
session.commit()

sportsplayer8 = SportsPlayer(name="KIDAMBI Srikanth", description="Srikanth Kidambi is an Indian badminton player. He shot to prominence by defeating Olympic Champion"
       " Lin Dan in 2014 China Open Super Series Premier by 21–19 21–17 in the final round, thus becoming the first Indian to win a Super Series Premier Men's title.",
                     rank="8", country="India", sports=sports1)

session.add(sportsplayer8)
session.commit()

sportsplayer9 = SportsPlayer(name="NG Ka Long Angus", description="Angus Ng Ka Long is a badminton player from Hong Kong. He has a career-high ranking of 9 in Men's "
       "Singles, and has beaten other top 10 players like Lin Dan, Chen Long, Chou Tien Chen, Jan O Jorgensen, and Son Wan Ho.",
                     rank="9", country="HongKong", sports=sports1)

session.add(sportsplayer9)
session.commit()


# Chess
sports2 = Sports(name="Chess")

session.add(sports2)
session.commit()


sportsplayer1 = SportsPlayer(name="Carlsen, Magnus", description=" Norwegian chess grandmaster and the current World Chess Champion. A chess prodigy, Carlsen earned his "
       "grandmaster title at the age of 13 years and 148 days.",
                     rank="1", country="Entree", sports=sports2)

session.add(sportsplayer1)
session.commit()

sportsplayer2 = SportsPlayer(name="Aronian, Levon", description=" Levon Grigori Aronian is an Armenian chess Grandmaster. On the March 2014 FIDE rating list,"
 "he was ranked number two in the world and had an Elo rating of 2830, making him the fourth highest rated player in history.", rank="2", country="Armenian", sports=sports2)

session.add(sportsplayer2)
session.commit()

sportsplayer3 = SportsPlayer(name="Vachier-Lagrave, Maxime", description="Maxime Vachier-Lagrave is a French chess grandmaster. He was World Junior Champion in "
       "2009 and is a three-time French Champion. He is the No. 1 ranked French player as of October 2017. ",
                     rank="3", country="France", sports=sports2)

session.add(sportsplayer3)
session.commit()

sportsplayer4 = SportsPlayer(name="Caruana, Fabiano", description="Fabiano Luigi Caruana is an Italian-American chess grandmaster. He played for the United States until 2005, "
       "when he switched to Italy, and he subsequently switched back to the U.S. in 2015. He was the 2016 U.S. Chess Champion.",
                     rank="4", country="USA", sports=sports2)

session.add(sportsplayer4)
session.commit()

sportsplayer5 = SportsPlayer(name="Kramnik, Vladimir", description="Vladimir Borisovich Kramnik is a Russian chess grandmaster. He was the Classical World Chess Champion from "
       "2000 to 2006, and the undisputed World Chess Champion from 2006 to 2007.",
                     rank="5", country="Russia", sports=sports2)

session.add(sportsplayer5)
session.commit()

sportsplayer6 = SportsPlayer(name="Anand, Viswanathan", description="Viswanathan "Vishy" Anand is an Indian chess grandmaster and a former World "
       "Chess Champion. Anand became India's first grandmaster in 1988. He held the FIDE World Chess Championship from 2000 to 2002.",
                     rank="9", country="India", sports=sports2)

session.add(sportsplayer6)
session.commit()


# Table Tennis
sports3 = Sports(name="Table Tennis")

session.add(sports3)
session.commit()


sportsplayer1 = SportsPlayer(name="MA Long", description="aMa Long is a Chinese table tennis player. The current Olympic and World Champion, he is"
       " ranked number 1 in the world by the International Table Tennis Federation, a ranking he has held for a total of 62 months, the most by any male player.",
                     rank="1", country="China`", sports=sports3)

session.add(sportsplayer1)
session.commit()

sportsplayer2 = SportsPlayer(name="FAN Zhendong", description="Fan Zhendong is a Chinese table tennis player. He is ranked number 2 in the official ITTF world rankings as of January 2017.",
                     rank="2", country="China", sports=sports3)

session.add(sportsplayer2)
session.commit()

sportsplayer3 = SportsPlayer(name="XU Xin", description="Xu Xin is a Chinese table tennis player and is currently the No. 3 ranked player in the world, as of July 2016.",
                     rank="3", country="China", sports=sports3)

session.add(sportsplayer3)
session.commit()

sportsplayer4 = SportsPlayer(name="OVTCHAROV Dimitrij", description="Dimitrij Ovtcharov or Dmytro Ovtcharov is a Ukrainian-born German table"
       " tennis player. His father Mikhail, a Soviet table tennis champion in 1982, moved his family to Germany shortly after Dimitrij was born.",
                     rank="4", country="Germany", sports=sports3)

session.add(sportsplayer4)
session.commit()

sportsplayer5 = SportsPlayer(name="BOLL Timo", description="Timo Boll is a German professional table tennis player who currently plays with "
       "Borussia Düsseldorf and is ranked second in the German Table Tennis National League.",
                     rank="5", country="Germany", sports=sports3)

session.add(sportsplayer5)
session.commit()


# Cricket Players
sports4 = Sports(name="Cricket")

session.add(sports4)
session.commit()


sportsplayer1 = SportsPlayer(name="AB de Villiers", description="AB de Villiers is a South African cricketer, who plays all formats and"
       " also a former captain in all formats. He has been rated as the number one batsman in Tests and ODIs on several occasions.",
                     rank="1", country="South Africa", sports=sports4)

session.add(sportsplayer1)
session.commit()

sportsplayer2 = SportsPlayer(name="Virat Kohli", description="Pan Indian international cricketer who currently captains the India national team."
       "A right-handed batsman, often regarded as one of the best batsmen in the world, Kohli was ranked eighth in ESPN's list of world's most"
       " famous athletes in 2016. He plays for the Royal Challengers Bangalore in the Indian Premier League (IPL), and has been the team's captain since 2013.",
                     rank="2", country="India", sports=sports4)

session.add(sportsplayer2)
session.commit()

sportsplayer3 = SportsPlayer(name="Kane Williamson", description="Kane Stuart Williamson is a professional cricketer and currently the captain of New Zealand."
       " Considered as one of the most innovative batsman in the modern era, he is a right-handed batsman and occasional off-spinner",
                     rank="3", country="New Zealand", sports=sports4)

session.add(sportsplayer3)
session.commit()

sportsplayer4 = SportsPlayer(name="Tillekeratne Dilshan", description="Tillakaratne Mudiyanselage Dilshan, popularly known as Tillakaratne Dilshan, is a former"
       " Sri Lankan cricketer and a former captain of the Sri Lanka national cricket team.",
                     rank="4", country="Srilanka", sports=sports4)

session.add(sportsplayer4)
session.commit()

sportsplayer5 = SportsPlayer(name="Hashim Amla", description="Hashim Muhammad Amla is a South African cricketer who plays for South Africa in all "
       "three formats of the game. He is also a former captain of the Proteas and is a right-handed batsman and occasional off-break bowler.",
                     rank="5", country="South Africa", sports=sports4)

session.add(sportsplayer5)
session.commit()

sportsplayer6 = SportsPlayer(name="MS Dhoni", description="Mahendra Singh Dhoni is an Indian cricketer who captained the Indian team in limited-overs"
       " formats from 11th of September 2007 to 4th of January 2017 and in Test cricket from 2008 to 28th of December 2014.",
                     rank="6", country="India", sports=sports4)

session.add(sportsplayer6)
session.commit()




print "added Sports and Players !!"