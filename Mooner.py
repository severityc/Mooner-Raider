import requests
import time
import threading
import os
import colorama
import webbrowser
import logging
import ctypes
from pystyle import Write, Colors
from colorama import Fore

# Colours
purple_light = colorama.Fore.LIGHTMAGENTA_EX
purple_dark = colorama.Fore.LIGHTMAGENTA_EX
yellow = colorama.Fore.YELLOW
red = colorama.Fore.RED
green = colorama.Fore.GREEN

# Errors
Locked = f"{red} [LOCKED]? {red}"
Invalid = f"{red} [INVALID]? {red}"
Valid = f"{colorama.Fore.GREEN} [VALID] {colorama.Fore.GREEN}"
NoAcces = f"{red} [NO ACCESS]? {red}"
Succes = f"{colorama.Fore.GREEN} [SUCCESS] {colorama.Fore.GREEN}"
RateLimit = f"{colorama.Fore.YELLOW} [RATELIMIT] {colorama.Fore.YELLOW}"
Banned = f"{red} [BANNED]? {red}"

# Error codes
# 401 Api?
# 403 Locked/Banned
# 50001 No access
# 40007 Banned from a server

# Getting fingerprint
finger_fail = False
session = requests.Session()

headers = {
        'Accept': '*/*',
        'Referer': 'https://discord.com/',
        'User-Agent': 'Mozilla/5.0'
}
response = session.get('https://discord.com/api/v9/experiments', headers=headers)

if response.status_code == 200:
    data = response.json()
    fingerprint = data["fingerprint"]
else:
    finger_fail = True

# Making data folder
if not os.path.exists("data"):
    os.makedirs("data")

# Making tokens.txt
file_path = os.path.join("data", "tokens.txt")
if not os.path.exists(file_path):
    with open(file_path, 'w'):
        pass

# Making webhooks.txt
file_pathWB = os.path.join("data", "webhooks.txt")
if not os.path.exists(file_pathWB):
    with open(file_pathWB, 'w'):
        pass

# Making logs.txt
file_path_logs = os.path.join("data", "logs.txt")
if not os.path.exists(file_path_logs):
    with open(file_path_logs, 'w'):
        pass

# VARIABLES
discord = "https://discord.com/invite/auaX4vqZra"
youtube = "https://www.youtube.com/@_R3CI_"
discord_acc = "_r3ci_"
file_path_tokens = "data/tokens.txt"
file_path_webhooks = "data/webhooks.txt"
file_path_logs = "data/logs.txt"

#Logging
log_file_path = "data/logs.txt"

logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
msg_sent = 0
msg_failed = 0
msg_ratelimited = 0
def main_program():
    while True:            
        # Cleaning ocnsole
        os.system('cls')
        logging.info("console was cleared")
        
        def title():
            ctypes.windll.kernel32.SetConsoleTitleW(f"Mooner | Sent ~ {msg_sent} | Failed ~ {msg_failed} | Ratelimited ~ {msg_ratelimited} | Made by _r3ci_")
        
        # Counting tokens
        def count_lines(file_path):
            with open(file_path, 'r') as file:
                line_count = 0
                for _ in file:
                    line_count += 1
            return line_count
        
        # Print mooner logo with gradient effect
        Write.Print("""
                                        ███╗   ███╗ ██████╗  ██████╗ ███╗   ██╗███████╗██████╗ 
                                        ████╗ ████║██╔═══██╗██╔═══██╗████╗  ██║██╔════╝██╔══██╗
                                        ██╔████╔██║██║   ██║██║   ██║██╔██╗ ██║█████╗  ██████╔╝
                                        ██║╚██╔╝██║██║   ██║██║   ██║██║╚██╗██║██╔══╝  ██╔══██╗
                                        ██║ ╚═╝ ██║╚██████╔╝╚██████╔╝██║ ╚████║███████╗██║  ██║
                                        ╚═╝     ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝  
        """, Colors.blue_to_purple, interval=0.000)
        logging.info("printed mooner logo")
        
        # token count shit i dont know 
        token_count = "{0}".format(count_lines(file_path))
        
        # Options text with gradient effect
        Write.Print("""
                                                            <0> Socials                                                                               
                                            |    <1>  Joiner           <6> Is typing...    |      
                                            |    <2>  Leaver           <7> Checker         |  
                                            |    <3>  Spammer          <8> Token locker    |
                                            |    <4>  Reactor          <9>  soon           |
                                            |    <5>  Webhook spammer  <10> Exit           |
        """, Colors.blue_to_purple, interval=0.000)
        logging.info("printed options")
        if finger_fail == True:
            print("")
            Write.Print("Failed getting fingerprint some features may not work", Colors.blue_to_purple, interval=0.000)
        
        # Choice
        print(" ")
        choice = int(input(purple_dark + "[>>>]: "), )
        logging.info("printed option chooser")
       
        # Socials
        if choice == 0:
            logging.info("chose socials (0)")
            Write.Print('''
<1> Discord server
<2> Youtube    
<3> Discord acc                
                  ''', Colors.blue_to_purple, interval=0.000)
            logging.info("printed social options")
            choice_socials = int(input(purple_dark + 
"[>>>]: "))
            logging.info("printed option choser for socials")
            if choice_socials == 1:
                webbrowser.open(discord)
                logging.info("chose discord (socials) (1)")
            elif choice_socials == 2:
                webbrowser.open(youtube)
                logging.info("chose youtube (socials) (2)")
            elif choice_socials == 3:
                print(discord_acc)
                logging.info("chose discord_acc (socials) (3)")
            else:
                print ("no such option")
                logging.info("put in a option that doesnt exist (socials)")
                
            
        elif choice == 1:
            # Skidded joiner why? Ended the project and i just want yall to enjoy it
            import concurrent.futures
            import random
            import string
            import tls_client
            from colorama import Fore, Style
            import dtypes


            class Joiner:
                def __init__(self, data: dtypes.Instance) -> None:
                    self.session = data.client
                    self.session.headers = data.headers
                    self.get_cookies()
                    self.instance = data

                def rand_str(self, length: int) -> str:
                    return ''.join(random.sample(string.ascii_lowercase + string.digits, length))

                def get_cookies(self) -> None:
                    site = self.session.get("https://discord.com")
                    self.session.cookies = site.cookies

                def join(self) -> None:
                    self.session.headers.update({"Authorization": self.instance.token})
                    result = self.session.post(f"https://discord.com/api/v9/invites/{self.instance.invite}", json={
                        'session_id': self.rand_str(32),
                    })

                    if result.status_code == 200:
                       Write.Print(f'Joined\n', Colors.blue_to_purple, interval=0.000)

                    else:
                        Write.Print('Something went wrong captcha?\n', Colors.blue_to_purple, interval=0.000)

            class logger:
                colors_table = dtypes.OtherInfo.colortable

                @staticmethod
                def printk(text) -> None:
                    print(f"{text}")

                @staticmethod
                def convert(color):
                    return color if color.__contains__("#") else logger.colors_table[color]

                @staticmethod
                def color(opt, obj):
                    return f"{logger.convert(opt)}{obj}{Style.RESET_ALL}"

            class intilize:
                @staticmethod
                def start(i):
                    Joiner(i).join()

            if __name__ == '__main__':
                with open("data/tokens.txt") as file:
                    tokens = [line.strip() for line in file]

                instances = []
                max_threads = 5
                invite = input("Discord invite: ")
                invite = invite.replace("https://discord.gg/", "").replace("https://discord.com/invite/", "").replace("discord.gg/", "").replace("https://discord.com/invite/", "")
                invite_parts = invite.split("/")

                for token_ in tokens:
                    header = dtypes.OtherInfo.headers
                    instances.append(
                        dtypes.Instance(
                            client=tls_client.Session(
                                client_identifier=f"chrome_{random.randint(110, 115)}",
                                random_tls_extension_order=True,
                            ),
                            token=token_,
                            headers=header,
                            invite=invite,
                        )
                    )

                with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
                    for i in instances:
                        executor.submit(intilize.start, i)
        
        
        # LEAVER
        elif choice == 2:
            logging.info("chose leaver (2)")
            with open(file_path_tokens, "r") as file:
                tokens = file.read().splitlines()

            guild_id = Write.Input("Guild ID: ", Colors.blue_to_purple, interval=0.000)
            logging.info("put in guild id (leaver)")

            def leaver(token):
                header = {'Authorization': token}

                url = f"https://discord.com/api/v9/users/@me/guilds/{guild_id}"

                response = requests.delete(url, headers=header)

                if response.status_code == 204:
                    print(Succes, purple_light + token[:-5] + "*****", yellow, response)
                    logging.info("leaver succes")
                elif response.status_code == 401:
                    print(Invalid, purple_light + token[:-5] + "*****", yellow, response)
                    logging.info("leaver invalid token")
                elif response.status_code == 403:
                    print(Locked, purple_light + token[:-5] + "*****", yellow, response)
                    logging.info("leaver locked token")
                else:
                    print(Invalid, purple_light + token[:-5] + "*****", yellow, response)
                    logging.info("leaver invalid token")

            threads = []
            for token in tokens:
                thread = threading.Thread(target=leaver, args=(token,))
                thread.start()
                threads.append(thread)
                
            for thread in threads:
                thread.join()

        # SPAMMER
        elif choice == 3:
            global msg_sent
            logging.info("chose spammer (3)")
            with open(file_path_tokens, "r") as file:
                tokens = file.read().splitlines()

            channel_id = input("Channel ID: ")
            logging.info("put in channel id")
            message_content = input("Message: ")
            logging.info("put in message content")
            repeat_count = int(input("Repeat count (How many times): "))
            logging.info("put in repeat count")
        
            def spammer(token):
                url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
                headers = {'Authorization': token}
                payload = {'content': message_content}

                for _ in range(repeat_count):
                    response = requests.post(url, json=payload, headers=headers)
                    if response.status_code == 200:
                        print(Succes, purple_light + token[:-5] + "*****", yellow, response)
                        logging.info("spammer succes")
                        msg_sent =+ 1
                        title()
                    elif response.status_code == 401:
                        print(Invalid, purple_light + token[:-5] + "*****", yellow, response)
                        logging.info("spammer invalid token")
                        msg_failed =+ 1
                        title()
                    elif response.status_code == 429:
                        print(RateLimit, purple_light + token[:-5] + "*****", yellow, response)
                        logging.info("spammer ratelimit (use proxies to bypass)")
                        msg_ratelimited =+ 1
                        title()
                    elif response.status_code == 403:
                        print(Invalid, "/", Banned, purple_light + token[:-5] + "*****", yellow, response)
                        logging.info("spammer invalid or banned token")
                        msg_failed =+ 1
                        title()
                    else:
                        print("Unknown Error", purple_light + token[:-5] + "*****", yellow, response)
                        logging.info("spammer unknown error")

            threads = []
            for token in tokens:
                thread = threading.Thread(target=spammer, args=(token,))
                thread.start()
                threads.append(thread)
                
            for thread in threads:
                thread.join()

        # Reactor
        elif choice == 4:
            logging.info("chose reactor (4)")
            with open(file_path_tokens, "r") as file:
                tokens = file.read().splitlines()

            channel_id = Write.Input("Channel ID: ", Colors.blue_to_purple, interval=0.000)
            logging.info("put in channel id")
            message_id = Write.Input("Message ID: ", Colors.blue_to_purple, interval=0.000)
            logging.info("put in message id")
            emoji = Write.Input("Emoji (use win + .): ", Colors.blue_to_purple, interval=0.000)
            logging.info("put in emoji")

            def reactor(token):
                headers = {'Authorization': token}
                url = f"https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}/reactions/{emoji}/@me"

                response = requests.put(url, headers=headers)
                if response.status_code == 204:
                    print(Succes, purple_light + token[:-5] + "*****", yellow, response)
                    logging.info("reactor succes")
                elif response.status_code == 401:
                    print(Invalid, purple_light + token[:-5] + "*****", yellow, response)
                    logging.info("reactor invalid token")
                elif response.status_code == 403:
                    print(Locked, purple_light + token[:-5] + "*****", yellow, response)
                    logging.info("reactor locked token")
                else:
                    print(Invalid, purple_light + token[:-5] + "*****", yellow, response)
                    logging.info("reactor invalid token")

            threads = []
            for token in tokens:
                thread = threading.Thread(target=reactor, args=(token,))
                thread.start()
                threads.append(thread)
                
            for thread in threads:
                thread.join()

        # Webhook spammer
        elif choice == 5:
            logging.info("chose webhook spammer (5)")
            with open(file_path_webhooks, "r") as file:
                webhooks = file.read().splitlines()

            message = Write.Input("Message: ", Colors.blue_to_purple, interval=0.000)
            logging.info("put in message")
            repeat_count_str = Write.Input("Repeat count: ", Colors.blue_to_purple, interval=0.000)
            repeat_count = int(repeat_count_str)
            logging.info("put in repeat count")

            def webhook_spammer(webhook_url, message, repeat_count):
                for _ in range(repeat_count):
                    
                    payload = {'content': message}
                    
                    response = requests.post(webhook_url, json=payload)

                    if response.status_code == 204:
                        print(Succes, purple_light + webhook_url[:-5] + "*****", yellow, response)
                        logging.info("webhook spammer succes")
                    elif response.status_code == 401:
                        print(Invalid, purple_light + webhook_url[:-5] + "*****", yellow, response)
                        logging.info("webhook spammer invalid webhook")
                    else:
                        print(Invalid, purple_light + webhook_url[:-5] + "*****", yellow, response)
                        logging.info("webhook spammer invalid webhook")

            threads = []
            for webhook_url in webhooks:
                thread = threading.Thread(target=webhook_spammer, args=(webhook_url, message, repeat_count))
                thread.start()
                threads.append(thread)

            for thread in threads:
                thread.join()

        # Is typing...
        elif choice == 6:
            logging.info("chose is typing (6)")
            with open(file_path_tokens, "r") as file:
                tokens = file.read().splitlines()

            channel_id = Write.Input("Channel ID: ", Colors.blue_to_purple, interval=0.000)
            logging.info("put in channel id")
            logging.info("put in deleay")
            url = f"https://discord.com/api/v9/channels/{channel_id}/typing"

            def is_typing(token):
                headers = {'Authorization': token}
                response = requests.post(url, headers=headers)

                if response.status_code == 204:
                    print(Succes, purple_light + token[:-5] + "*****", yellow, response)
                    logging.info("is typing succes")
                elif response.status_code == 401:
                    print(Invalid, purple_light + token[:-5] + "*****", yellow, response)
                    logging.info("is typing invalid token")
                elif response.status_code == 403:
                    print(Locked, purple_light + token[:-5] + "*****", yellow, response)
                    logging.info("is typing locked token")
                else:
                    print(Invalid, purple_light + token[:-5] + "*****", yellow, response)
                    logging.info("is typing invalid token")

            threads = []
            for token in tokens:
                thread = threading.Thread(target=is_typing, args=(token,))
                thread.start()
                threads.append(thread)
                
            for thread in threads:
                thread.join()

        # Checker
        elif choice == 7:
            logging.info("chose checker (7)")
            with open(file_path_tokens, "r") as file:
                tokens = file.read().splitlines()

            def checker(token):
                url = "https://discord.com/api/v9/users/@me/affinities/guilds"
                headers = {'Authorization': token}
                response = requests.get(url, headers=headers)

                if response.status_code == 200:
                    print(Valid, purple_light + token[:-5] + "*****", yellow, response)
                    logging.info("checker valid token")
                elif response.status_code == 401:
                    print(Invalid, purple_light + token[:-5] + "*****", yellow, response)
                    logging.info("checker invalid token")
                elif response.status_code == 403:
                    print(Locked, purple_light + token[:-5] + "*****", yellow, response)
                    logging.info("checker locked token")
                else:
                    print(Invalid, purple_light + token[:-5] + "*****", yellow, response)
                    logging.info("checker invalid token")

            threads = []
            for token in tokens:
                thread = threading.Thread(target=checker, args=(token,))
                thread.start()
                threads.append(thread)
                
            for thread in threads:
                thread.join()

        # Token locker
        elif choice == 8:
            logging.info("chose token locker (8)")
            with open(file_path_tokens, "r") as file:
                tokens = file.read().splitlines()
            Write.Print("ARE U SURE U WANT TO **LOCK** ALL THE TOKENS IN TOKENS.TXT? y/n", Colors.blue_to_purple, interval=0.000)
            token_locker_confirm = Write.Input("[>>>]: ", Colors.blue_to_purple, interval=0.000)
            
            def token_locker(token):
                if token_locker_confirm == "y" or "Y":
                    logging.info("Token locker was confirmed")
                    logging.info("token locking has started")
                    Write.Print("Reccomend using like 2-3 times to make sure tokens are locked", Colors.blue_to_purple, interval=0.000)
                    payload = {"bio": "."}
                    headers = {'Authorization': token}
                    url = "https://discord.com/api/v9/users/%40me/profile"
                    response = requests.patch(url, json=payload, headers=headers)

                    if response.status_code == 200:
                        print(Succes, purple_light + token[:-5] + "*****", yellow, response)
                        logging.info("token locker succes")
                    elif response.status_code == 401:
                        print(Invalid, purple_light + token[:-5] + "*****", yellow, response)
                        logging.info("token locker invalid token")
                    elif response.status_code == 403:
                        print(Locked, purple_light + token[:-5] + "*****", yellow, response)
                        logging.info("token locker locked token")
                    else:
                        print(Invalid, purple_light + token[:-5] + "*****", yellow, response)
                        logging.info("token locker invalid token")

                    threads = []
                    for token in tokens:
                        thread = threading.Thread(target=token_locker, args=(token,))
                        thread.start()
                        threads.append(thread)
                        
                    for thread in threads:
                        thread.join()
                
        elif choice == 10:
            logging.info("exited (10)")
            exit()
        elif choice == 100:
            logging.info("entered the TEST SPACE")
            Write.Print("This is a testing space for me (R3CI) wired stuff can be here so I recommend re-opening",Colors.blue_to_purple, interval=0.000)
            print("")
            print(f"tkns {token_count}")

        else:
            print("No such option")
            logging.info("put in an option that doesn't exist")

        Write.Print("Returning in 3s", Colors.blue_to_purple, interval=0.000)
        time.sleep(3)
        logging.info("returned")


if __name__ == "__main__":
    main_program()
