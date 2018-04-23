# redditcrawler

## Command Line Version
This Reddit crawler was created using Python3 and has two options, to run as a command line:
- First install it's dependencies:
```
pip install urllib
pip install bs4
```
- The you can query it:
```
python commandline.py "/r/cats;/r/worldnews"
```
It only takes one argument which is the subreddits that you wanna query separated by ';' and return it's hot topics of the day (above 5000 upvotes)

## Bot Version
- First install it's dependencies:
```
pip install telepot
```
- Then set environment variable with you BootKey:
    - export BOOT_KEY_REDDIT="597001235:AAFuetAcfvJ09r4Cc7fbtOJKeCj_SPAu7aY"   

- The you can run it:
```
python bot.py"
```

- After that add "personalredditcrawler_bot" to your Telegram Contacts and start to do queries:
    - digite /NadaPraFazer [+ Lista de subrredits separado por virgulas]
