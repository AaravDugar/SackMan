import requests
import json
import os

def main():
    while True:
        if not os.path.isfile("Apps/news/config.json"):
            key = input("Please Enter API Key from https://newsapi.org > ")
            dmp = {"API_KEY": key}
            with open("Apps/news/config.json", "w") as f:
                json.dump(dmp, f, indent=4)

        with open("Apps/news/config.json", "r") as f:
            api = json.load(f)
        API_KEY = api["API_KEY"]
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"
        cmd = input("news> ").lower()
        com = cmd.split()
        rno = 0
        
        if cmd == "list":
            if os.path.isfile("Apps/news/news.json"):
                with open("Apps/news/news.json", "r") as f:
                    data = json.load(f)
                for i in range(10):
                    print(f"[{i+1}] {data["articles"][i]["title"]}")
            else:
                r = requests.get(url)
                data = r.json()
                with open("Apps/news/news.json", "w") as f:
                    json.dump(data, f, indent=4)
                for i in range(10):
                    print(f"[{i+1}] {data["articles"][i]["title"]}")
        elif cmd == "refresh":
            r = requests.get(url)
            data = r.json()
            with open("Apps/news/news.json", "w") as f:
                json.dump(data, f, indent=4)
            print("Refreshed News!")
        elif com[0] == "read":
            rno = int(com[1]) -1
            with open("Apps/news/news.json", "r") as f:
                data = json.load(f)
            print(data["articles"][rno]["content"])
        elif cmd == "exit":
            break
