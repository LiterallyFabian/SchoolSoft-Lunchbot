
# SchoolSoft lunchbot (via Discord.py) (Swedish)
Simpel discord bot gjord i Python med [discord.py](https://github.com/Rapptz/discord.py) och den [Inoficiella SchoolSoft APIn](https://github.com/lnus/schoolsoft-api) för att visa den nuvarande maträtten i skolor som använder SchoolSoft. Koden är inte jättebra struktuerad/kommenterad än men allting bör fungera som det ska

## Setup
Skriv all information i filen keys.py och kör bot.py.

Om du vill ha en bot för Cybergymnasiets lunch så kan du invitea [denna](https://discordapp.com/api/oauth2/authorize?client_id=571758785115324427&permissions=0&scope=bot) som är hostad av mig.

## Funktioner
- **-lunch**: Visar dagens maträtt
  - Du kan även skriva -food eller -lunch day
  - Fungerar ej på helger
  - Uppdateras varje veckodag vid midnatt (CEST)

![-lunch command](https://media.discordapp.net/attachments/520168552687206400/576808899059908618/unknown.png)

- **-wlunch**: Visar menyn för hela veckan
  - Du kan även skriva -wfood eller -lunch week
  - Uppdateras på natten till måndagar
  
![-wlunch command](https://cdn.discordapp.com/attachments/520168552687206400/576808397832454184/unknown.png)

- **Spel status**
  - Botten kommer ha en spelstatus som visar den nuvarande huvudrätten
  - Vid tillfället så uppdateras statusen bara när botten startar vilket kan bli lite missledande, detta kommer ändras.
  
![Bot status](https://cdn.discordapp.com/attachments/520168552687206400/576809571167764500/unknown.png)

# SchoolSoft lunchbot (via Discord.py) (English)

Simple Discord bot made in Python using [discord.py](https://github.com/Rapptz/discord.py) and the [Unofficial SchoolSoft API](https://github.com/lnus/schoolsoft-api) for showing the current lunch in schools using Schoolsoft. The code isn't very well structured, but everything should work fine

## Setup
Fill in your information in the keys.py file and run bot.py.

If you want a bot for Cybergymnasiet, feel free to invite [this one hosted by me](https://discordapp.com/api/oauth2/authorize?client_id=571758785115324427&permissions=0&scope=bot).

## Features
- **-lunch**: Shows the current lunch
  - You can also do -food or -lunch day
  - The command does not work on weekends yet
  - Updates every weekday at 12 am CEST

![-lunch command](https://media.discordapp.net/attachments/520168552687206400/576808899059908618/unknown.png)

- **-wlunch**: Shows the lunch menu for the whole week
  - You can also do -wfood or -lunch week
  - Will only update on Mondays at 12 am CEST at the moment
  
![-wlunch command](https://cdn.discordapp.com/attachments/520168552687206400/576808397832454184/unknown.png)

- **Game status**
  - The bot will have a game status with the current primary dish
  - Will at the moment only update when the bot gets restarted which may be a bit misleading. That will be changed in the future
  
![Bot status](https://cdn.discordapp.com/attachments/520168552687206400/576809571167764500/unknown.png)


