from tkinter import *
from tkinter import ttk, messagebox, scrolledtext

import os
import re
import json
from urllib.request import Request, urlopen

def send():
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
    }
    url = str(webhook_url.get())
    content = str(webhook_content.get())
    payload = json.dumps({'content': content})
    req = Request(url, data=payload.encode(), headers=headers)
    urlopen(req)


root = Tk()
root.title("Discord Webhook Sender")
root.geometry("410x130")

frame = ttk.Frame(root, padding=(5))
frame.grid(rowspan=3, sticky=(N, W, E, S))

webhook_url = StringVar()
webhook_content = StringVar()

label_1 = ttk.Label(frame, text="URL").grid(row=0, column=0,  sticky=(W))
label_2 = ttk.Label(frame, text="Content").grid(row = 2, column=0, sticky=(W, E))
entry_1 = ttk.Entry(frame, textvariable=webhook_url, width=65).grid(row = 1, column=0, sticky=(W, E))
entry_2 = ttk.Entry(frame, textvariable=webhook_content, width=65).grid(column=0, row=3, sticky=(W, E))
button_1 = ttk.Button(frame, text="Send", command=send).grid(row = 4, column=0, pady=10, sticky=(E))

if __name__ == "__main__":
    root.bind("<Return>", send)
    root.mainloop()
