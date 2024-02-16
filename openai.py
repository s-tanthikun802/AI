import requests
import json

def get_hostname(url, payload):
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            hostname = response.url.split('//')[-1].split('/')[0]
            return hostname
        else:
            print(f"Failed to fetch URL: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=<ENTER YOUR API KEY>"
    payload = {"contents":[{"parts":[{"text":"You are an AI and now Let play 2D tictactoe. You go first."}]}]}  # Modify this dictionary to match your JSON body
    hostname = get_hostname(url, payload)
    if hostname:
        print(f"The hostname for {url} is: {hostname}")

