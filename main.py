import os
import socket
import requests
import platform

hostname = socket.gethostname()
user = os.getlogin()

def main():
    if platform.system() == 'Linux':
        os.system("clear")
    elif platform.system() == 'Windows':
        os.system("cls")
    print("""
 $$$$$$\            
$$  __$$\           
\__/  $$ |$$$$$$$$\ 
 $$$$$$  |\____$$  |
$$  ____/   $$$$ _/ 
$$ |       $$  _/   
$$$$$$$$\ $$$$$$$$\ 
\________|\________|
    
 Created by lv8""")

    print("""\n[1] Webhook spammer
[2] Webhook deleter\n""")

    selection = input("("+user+"@"+hostname+")-[~]$> ")

    if selection == "1":
        webhook_spam()
    elif selection == "2":
        webhook_delete()
    else:
        print("Invalid selection")
        main()

def webhook_delete():
    webhook_url = input("("+user+"@"+hostname+")-[~/webhook-deleter/webhook_url]""$> ")

    response = requests.delete(webhook_url)

    if response.status_code == 204:
        input('[SUCCESS] - Webhook deleted successfully')
    else:
        input('[ERROR] - Failed to delete webhook')
    main()

def webhook_spam():
    webhook_url = input("("+user+"@"+hostname+")-[~/webhook-spammer/webhook_url]""$> ")

    # Define the message payload
    message_payload = {
        'content': input("("+user+"@"+hostname+")-[~/webhook-spammer/message_content]""$> "),
        'username': input("("+user+"@"+hostname+")-[~/webhook-spammer/username]""$> "),  # Set the username
        'avatar_url': input("("+user+"@"+hostname+")-[~/webhook-spammer/avatar_url]""$> ")  # Set the avatar URL
    }

    # Get the number of messages to send
    num_messages = int(input("("+user+"@"+hostname+")-[~/webhook-spammer/messages_number]""$> "))

    # Send the messages
    for i in range(num_messages):
        response = requests.post(webhook_url, json=message_payload)

        if response.status_code == 204:
            print(f'[LOGS] Message {i+1} sent successfully')
        else:
            print(f'[ERROR] Failed to send message {i+1}')

    input(f'[SUCCESS] {num_messages} messages sent successfully')
    main()

main()