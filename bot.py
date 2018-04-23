
#!/usr/bin/python3 

import time
import telepot
from telepot.loop import MessageLoop
from commandline import main
import pprint
import os

pp = pprint.PrettyPrinter(indent=2)

def handle(msg):
    chat_id = msg['chat']['id']
    message = msg['text'].split(" ")
    try:
        if(len(message)==2):
            bot.sendMessage(chat_id, "Aguarde enquanto nosso gerador de Inutilidades procura no Reddit")
            command = message[0]
            args  = message[1]           
            if command == '/NadaPraFazer':
                process_crawler(args,chat_id)            
            else:                
                bot.sendMessage(chat_id, "Não entendi, digite /NadaPraFazer [+ Lista de subrredits separados por ;] para obter lista do que fazer")
        elif(len(message)==1):
            command = message[0]
            if command == '/NadaPraFazer':
                process_crawler("news;cats",chat_id)                  
            elif command == '/start':
                bot.sendMessage(chat_id, "Olá eu sou o seu buscador de Inutilidades digite /NadaPraFazer [+ Lista de subrredits separados por ;] para obter lista do que fazer")
            else:                
                bot.sendMessage(chat_id, "Não entendi, digite /NadaPraFazer [+ Lista de subrredits separados por ;] para obter lista do que fazer")
        else:
            bot.sendMessage(chat_id, "Não entendi, digite /NadaPraFazer [+ Lista de subrredits separados por ;] para obter lista do que fazer")
    except Exception as e:
         print(e)
         bot.sendMessage(chat_id, "OPS: Não entendi, digite /NadaPraFazer [+ Lista de subrredits separados por ;] para obter lista do que fazer")



def process_crawler(args,chat_id):
    results = []
    reddits = args.split(';')
    for reddit in reddits: 
        cur_result = main("/r/"+reddit,False)
        #print(reddit)
        #print(cur_result)
        if(len(cur_result)!=0):
            results.extend(cur_result) 
    if(len(results)==0):              
        bot.sendMessage(chat_id,"Infelizmente não houve respostas para este tópico, tente gatinhos(cats)")
    #pp.pprint(results)
    for result in results:
        bot.sendMessage(chat_id,"De uma olhada na Thread: "+ result['title'] + " Link: "+ result['link'] + " No subreddit: https://www.reddit.com" +result['subreddit'] + " Veja os comentários em: https://www.reddit.com/" + result['comments'] + " Ela tem  "+ result['upvotes']+" upvotes")
key = os.environ['BOOT_KEY_REDDIT']
print(key)
bot = telepot.Bot(key)



MessageLoop(bot, handle).run_as_thread()
print('I am listening ...')
while 1:
    time.sleep(1)