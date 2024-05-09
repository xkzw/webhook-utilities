import os
import socket
import requests
import platform
from pystyle import *
import json
import re

hostname = socket.gethostname()

def clear_screen():
    try:
        if platform.system() == 'Linux':
            os.system("clear")
        elif platform.system() == 'Windows':
            os.system("cls")
    except Exception as e:
        Write.Print(f"An error occurred while clearing the screen: {e}\nPress ENTER to go back to menu", Colors.red, interval=0.000)
        input()
        main()

def validate_webhook(url):
    try:
        response = requests.head(url)
        return response.status_code in range(200, 300)
    except requests.RequestException:
        return False

def is_valid_url(url):
    url_pattern = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9-]+\.)+[A-Z]{2,}|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or IP
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return bool(url_pattern.match(url))

def is_image_url(url):
    try:
        response = requests.head(url)
        content_type = response.headers.get('Content-Type')
        return content_type.startswith('image/')
    except requests.RequestException:
        return False

def main():
    try:
        clear_screen()
        Write.Print("""
                        $$\       $$\                           $$\                           $$\     $$\ $$\           
                        $$ |      $$ |                          $$ |                          $$ |    \__|$$ |          
$$\  $$\  $$\  $$$$$$\  $$$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\  $$ |  $$\         $$\   $$\ $$$$$$\   $$\ $$ | $$$$$$$\  
$$ | $$ | $$ |$$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$ | $$  |$$$$$$\ $$ |  $$ |\_$$  _|  $$ |$$ |$$  _____| 
$$ | $$ | $$ |$$$$$$$$ |$$ |  $$ |$$ |  $$ |$$ /  $$ |$$ /  $$ |$$$$$$  / \______|$$ |  $$ |  $$ |    $$ |$$ |\$$$$$$\  
$$ | $$ | $$ |$$   ____|$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$  _$$<          $$ |  $$ |  $$ |$$\ $$ |$$ | \____$$\ 
\$$$$$\$$$$  |\$$$$$$$\ $$$$$$$  |$$ |  $$ |\$$$$$$  |\$$$$$$  |$$ | \$$\         \$$$$$$  |  \$$$$  |$$ |$$ |$$$$$$$  |
 \_____\____/  \_______|\_______/ \__|  \__| \______/  \______/ \__|  \__|         \______/    \____/ \__|\__|\_______/ \n
""", Colors.blue_to_white, interval=0.0000)
 
        Write.Print("                                                      Created by lv8\n                                          Follow my github: github.com/nosztalgia\n", Colors.blue_to_white, interval=0.0001)

        Write.Print("[1] Webhook spammer\n[2] Webhook deleter\n\n", Colors.blue_to_white, interval=0.000)

        selection = Write.Input("(" + "lv8" + "@" + hostname + ")-[~]$> ", Colors.blue_to_white, interval=0.000)

        if selection == "1":
            webhook_spam()
        elif selection == "2":
            webhook_delete()
        else:
            Write.Print("\nInvalid selection, press ENTER to go back to selection menu", Colors.red, interval=0.000)
            input()
            main()
    except Exception as e:
        Write.Print(f"\nAn error occurred: {e}\nPress ENTER to go back to menu", Colors.red, interval=0.000)
        input()
        main()

def webhook_delete():
    try:
        while True:
            webhook_url = Write.Input("(" + "lv8" + "@" + hostname + ")-[~/webhook-deleter/webhook_url]$> ", Colors.blue_to_white, interval=0.000)
            
            if validate_webhook(webhook_url):
                break
            else:
                Write.Print("\n[ERROR] - Invalid webhook URL\n\n", Colors.red, interval=0.000)

        response = requests.delete(webhook_url)

        if response.status_code == 204:
            Write.Input('\n[SUCCESS] - Webhook deleted successfully\n\nPress ENTER to go back to menu', Colors.blue_to_white, interval=0.000)
        else:
            Write.Input('\n[ERROR] - Failed to delete webhook\n\nPress ENTER to go back to menu', Colors.blue_to_white, interval=0.000)
        main()
    except Exception as e:
        Write.Print(f"\nAn error occurred: {e}\nPress ENTER to go back to menu", Colors.red, interval=0.000)
        input()
        main()

def webhook_spam():
    try:
        while True:
            webhook_url = Write.Input("(" + "lv8" + "@" + hostname + ")-[~/webhook-spammer/webhook_url]$> ", Colors.blue_to_white, interval=0.000)
            
            if validate_webhook(webhook_url):
                break
            else:
                Write.Print("\n[ERROR] - Invalid webhook URL\n\n", Colors.red, interval=0.000)

        message_payload = {
            'content': Write.Input("(" + "lv8" + "@" + hostname + ")-[~/webhook-spammer/message_content]$> ", Colors.blue_to_white, interval=0.000),
            'username': Write.Input("(" + "lv8" + "@" + hostname + ")-[~/webhook-spammer/username]$> ", Colors.blue_to_white, interval=0.000),
            'avatar_url': ''
        }

        while True:
            avatar_url = Write.Input("(" + "lv8" + "@" + hostname + ")-[~/webhook-spammer/avatar_url]$> ", Colors.blue_to_white, interval=0.000)
            if avatar_url == '':
                break
            if is_valid_url(avatar_url) and is_image_url(avatar_url):
                message_payload['avatar_url'] = avatar_url
                break
            else:
                Write.Print("\n[ERROR] - Invalid or non-image avatar URL\n\n", Colors.red, interval=0.000)

        while True:
            try:
                num_messages = int(Write.Input("(" + "lv8" + "@" + hostname + ")-[~/webhook-spammer/messages_number]$> ", Colors.blue_to_white, interval=0.000))
                print("\n")
                break
            except ValueError:
                Write.Print("\n[ERROR] - Invalid number of messages. Please enter a valid integer.\n\n", Colors.red, interval=0.000)
                

        for i in range(num_messages):
            response = requests.post(webhook_url, json=message_payload)

            if response.status_code == 204:
                Write.Print(f'[LOGS] Message {i+1} sent successfully\n', Colors.blue_to_white, interval=0.000)
            else:
                Write.Print(f'[ERROR] Failed to send message {i+1}\n', Colors.red, interval=0.000)

        Write.Input(f'\n[SUCCESS] {num_messages} messages sent successfully\n\nPress ENTER to go back to menu', Colors.blue_to_white, interval=0.000)
        main()
    except Exception as e:
        Write.Print(f"\nAn error occurred: {e}\nPress ENTER to go back to menu", Colors.red, interval=0.000)
        input()
        main()

main()
