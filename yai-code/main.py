import rich
import os
import json
import requests
from rich.panel import Panel
from rich.console import Console
from rich import print
from rich.markdown import Markdown
import random
import time
console = Console()

global thinking
thinking = ["Thinking...", "Procastinating...", "Overreacting...", "Counting Tokens...", "Visit https://www.atlastraffic.in", "Interrupted From Slumber..."]

global messages
messages = [{"role":"system", "content":"You are yAI-code, an AI based coder which is in yShell. You are an expert in python, java, js, json, html, and css."}]
i=1




def main():
    global messages
    global API_KEY
    global PREF_MODEL
    global url
    while True:
        if not os.path.isfile("Apps/yai/config.json"):
            inp1 = input("yAI Enter Openrouter API Key: ")
            inp2 = input("yAI Enter Preferred Model: ")
            dmp = {
                "API_KEY": inp1,
                "PREF_MODEL": inp2
            }

            with open("Apps/yai/config.json", "w") as f:
                json.dump(dmp, f, indent=4)

        url = "https://openrouter.ai/api/v1/chat/completions"
        with open("Apps/yai/config.json", "r") as f:
                dmp = json.load(f)
        API_KEY = dmp["API_KEY"]
        PREF_MODEL = dmp["PREF_MODEL"]

        msg = input("yAI> ")
        parts = msg.split()
        com = parts[0].lower()
        
        with console.status(random.choice(thinking)):
            if msg.lower() == "exit":
                break
            elif msg.lower() == "/clear":
                messages = [{"role":"system", "content":"You are yAI, the AI assistant of yShell."}]
                print("Model Context Reset")
                continue
            elif com == "/save":
                val = parts[1]
                with open(val, "w") as f:
                    json.dump(messages, f, indent=4)
                continue
            elif com == "/load":
                val = parts[1]
                if os.path.isfile(val):
                    with open(val, "r") as f:
                        messages = json.load(f)
                else:
                    print("File not found")
                continue
            elif com == "/explain":
                val = parts[1]
                if os.path.isfile(val):
                    with open(val, "r", encoding='utf-16') as f:
                        content = f.read()
                    post(f"Explain this to me: {content}")
                else:
                    print("Error: File Not Found!")
            elif com == "/create":
                fn = parts[1]
                prompt = ' '.join(parts[2:])
                ans = post(f"I'm creating a file {fn} and output is directly transferred from your response. Only include code. Prompt: {prompt}. Don't format your code using the quotes like ```python as that breaks the file save.")
                with open(fn, "w", encoding='utf-16') as f:
                    f.write(ans)
            elif com == "/fix":
                val = parts[1]
                if os.path.isfile(val):
                    with open(val, "r", encoding='utf-16') as f:
                        content = f.read()
                    ans = post(f"Find Bugs in the code and return only code. Don't use quotes like ```python as that breakes my filesave. Code: {content}")
                    yno = input(f"yai> Save to {val}? (y/N): ")
                    if yno.lower() == "y":
                        with open(val, "w", encoding='utf-16') as f:
                            f.write(ans)
                else:
                    print("Error: File Not Found!")


            else:
                post(msg)
            
def post(msg):
    headers = {

                "Authorization": f"Bearer {API_KEY}",

                "Content-Type": "application/json"

            }
    messages.append({"role":"user", "content":msg})
    payload = {
        "model": f"{PREF_MODEL}",
        "messages": messages
        
    }

    response = requests.post(
        url,
        headers=headers,
        json=payload
    )

    data = response.json()
    answer = data["choices"][0]["message"]["content"]
    print("\n")
    md = Markdown(answer)
    panel = Panel(
        md,
        title="[bold cyan]yAI[/bold cyan]",
        border_style="cyan"
    )
    print(panel)
    print("\n")
    messages.append({"role":"assistant","content":answer})
    return answer
