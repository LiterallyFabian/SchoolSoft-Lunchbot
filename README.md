# SchoolSoft lunch bot (via Discord.py) 

Simple Discord bot made in Python using [discord.py](https://github.com/Rapptz/discord.py) and the [Unofficial SchoolSoft API](https://github.com/lnus/schoolsoft-api) for showing the current lunch in schools using Schoolsoft. 

**⚠ Note that this project is not maintained and will most likely no longer work as SchoolSoft have updated their login systems.**


## Setup
Fill in your information in the keys.py file and run bot.py.

## Features
- **-lunch**: Shows the current lunch
  - You can also do -food or -lunch day
  - Updates every weekday at 12 am CEST

![-lunch command](https://media.discordapp.net/attachments/520168552687206400/576808899059908618/unknown.png)

- **-wlunch**: Shows the lunch menu for the whole week
  - You can also do -wfood or -lunch week
  - Will only update on Mondays at 12 am CEST
  
![-wlunch command](https://cdn.discordapp.com/attachments/520168552687206400/576808397832454184/unknown.png)

- **Game status**
  - The bot will have a game status with the current primary dish
  - Will at the moment only update when the bot gets restarted.
  
![Bot status](https://cdn.discordapp.com/attachments/520168552687206400/576809571167764500/unknown.png)
