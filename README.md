# SchoolSoft lunchbot (via Discord.py)
Simple Discord bot made in Python using [discord.py](https://github.com/Rapptz/discord.py) and the [Unofficial SchoolSoft API](https://github.com/lnus/schoolsoft-api) for showing the current lunch in schools using Schoolsoft.



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

- The bot will have a game status with the current primary dish
  - Will at the moment only update when the bot gets restarted, that will be changed in the future
  
![Bot status](https://cdn.discordapp.com/attachments/520168552687206400/576809571167764500/unknown.png)
