from json.encoder import ESCAPE
import random
import os 
import uuid

from optparse import Option
from tokenize import String

from typing import Optional

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#Get the content needed



@app.get("/write_code/", response_class=HTMLResponse)
def write_code( code: str):
    link_len = 15
    cur_str = []
    for i in range(link_len):
        c = random.choice(letters)
        cur_str.append(c)
    print(code)
    cur_str_s = str(uuid.uuid4())

    fh = open(f'/var/www/html/q/{cur_str_s}.txt', 'w')
    fh.write(code)
    fh.close()

    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Paste/Code Link</title>
</head>
<body>
    Your link: http://leefamily.site/q/{cur_str_s}.txt
</body>
</html>
"""
