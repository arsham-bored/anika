# Anika
![image](https://i.pinimg.com/originals/25/bf/ae/25bfae315cda928ecd8e03cb8ca57da1.png)

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)

## About <a name = "about"></a>
**Anika** is group manager bot designed for [Telegram platfrom](telegram.org).<br>
powered by [Telethon](https://github.com/LonamiWebs/Telethon).

## Getting Started <a name = "getting_started"></a>
[Telethon's documentation](Telethon's documentation) would be useful.
- `git clone https://github.com/arsham-bored/anika.git` and `cd anika`
- Create _.env_ file: `touch .env`. <br>
<small> all necessary variables will be pasted there.</small>
- [Login into your Telegram account](https://my.telegram.org/)
- Create new application window will appear. Fill in your application details. There is no need to enter any URL, and only the first two fields (App title and Short name) can currently be changed later.<br>

- Click on Create application at the end. Remember that your API hash is secret and Telegram won’t let you revoke it. Don’t post it anywhere!<br>

- Paste your *OWN* `api_id` and `api_hash` into _.env_ file. like,
```
api_id=12345
api_hash=0123456789abcdef0123456789abcdef
```

- Install all required dependencies: `pip install -r requirements.txt`

- You are ready to go ! run project by `python -m src.app`.<br> <small>`python src/app.py` may cause error</small>
