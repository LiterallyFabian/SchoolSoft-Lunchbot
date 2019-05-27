import discord
from bs4 import BeautifulSoup
import requests
import datetime
import re
from datetime import date
import keys


now = datetime.datetime.now()
today = datetime.datetime.today().weekday()
weekNumber = date.today().isocalendar()[1]
day = ['måndag', 'tisdag', 'onsdag', 'torsdag', 'fredag']

class AuthFailure(Exception):
    pass

class SchoolSoft(object):
    def __init__(self, school, username, password, usertype = 1):
        self.school = school
        self.username = username
        self.password = password
        self.usertype = usertype
        self.cookies = {}

        _login_page_re = r"https://sms(\d*).schoolsoft.se/%s/html/redirect_login.htm"
        self._login_page_re = re.compile(_login_page_re % school)

        # Might not be needed, still gonna leave it here
        self.login_page = "https://sms5.schoolsoft.se/{}/jsp/Login.jsp".format(school)

    def try_get(self, url, attempts = 0):
        """
        Tries to get URL info using
        self.username && self.password
        Mainly for internal calling;
        however can be used to fetch from pages not yet added to API.
        """
        r = requests.get(url, cookies=self.cookies)

        login_page_match = self._login_page_re.match(r.url)
        if login_page_match:
            server_n = login_page_match.groups()
            if attempts < 1:
                # Sends a post request with self.username && self.password
                loginr = requests.post(self.login_page, data = {
                    "action": "login",
                    "usertype": self.usertype,
                    "ssusername": self.username,
                    "sspassword": self.password
                    }, cookies=self.cookies, allow_redirects=False)

                # Saves login cookie for faster access after first call
                self.cookies = loginr.cookies

                return self.try_get(url, attempts+1)
            else:
                raise AuthFailure("Invalid username or password")
        else:
            return r

    def fetch_lunch_menu(self):
        """
        Fetches the lunch menu for the entire week
        Returns an ordered list with days going from index 0-4
        This list contains all the food on that day
        """
        menu_html = self.try_get("https://sms5.schoolsoft.se/{}/jsp/student/right_student_lunchmenu.jsp?menu=lunchmenu".format(self.school))
        menu = BeautifulSoup(menu_html.text, "html.parser")

        lunch_menu = []

        for div in menu.find_all("td", {"style": "word-wrap: break-word"}):
            food_info = div.get_text(separator=u"<br/>").split(u"<br/>")
            lunch_menu.append(food_info)

        return lunch_menu

if __name__ == "__main__":
    api = SchoolSoft(keys.school, keys.username, keys.password)
    lunch = api.fetch_lunch_menu()

bot = discord.Client()

@bot.event
async def on_ready():
    print('started')

    if today <= 5:
        await bot.change_presence(activity=discord.Game(name=lunch[today][0], type=0))
    else:
        await bot.change_presence(activity=discord.Game(name='-lunch', type=0))

@bot.event
async def on_message(message):

    if message.content in ('-lunch', '-food', '-lunch day'):
        if today < 5:
            food = ['\n🥗 '.join(item) for item in lunch]
            await message.channel.send('🍽**Skolmat ' + day[today] + ' ' + now.strftime("%d/%m") + '**\n\n🍖 ' + food[today])
        else:
            await message.channel.send('Ingen lunch idag!')

    if message.content in ('-wlunch', '-wfood', '-lunch week'):
        food = ['\n🥗 '.join(item) for item in lunch]
        await message.channel.send('🍽**Skolmat vecka ' + str(weekNumber) + '**\n\n' + ("**Måndag:**\n🍖 {}\n\n**Tisdag:**\n🍖 {}\n\n**Onsdag:**\n🍖 {}\n\n**Torsdag:**\n🍖 {}\n\n**Fredag:**\n🍖 {}".format(*food)))


bot.run(keys.bottoken)
