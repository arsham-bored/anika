# Anika: useless group manager bot

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)

## About <a name = "about"></a>

**Anika** aims to add some flexibility to PySpider's community on Telegram, [link](https://t.me/pyspy).<br>
features:
- `score system`
- `spam message detection`
- `member flow manager`

`score system` : a feature which users can give score to each other, members will get promoted in this way.<br>

this happens by replying symbols `+` or `-` for target user.<br>
also with some emojis, but special users can have it.


## Getting Started <a name = "getting_started"></a>

you need to sign into your Telegram developer account, define new application and
copy both your `api_id` and `api_hash`.<br>
paste those into `.env` file in the root directory

now you need to install required dependency with command: <br>`pip install -r requirements.txt`<br>

then you're ready to start project with command: <br>`python -m src.app`