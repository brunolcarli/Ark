<table align="center"><tr><td align="center" width="9999">

<img src="https://i.ibb.co/WGq1nBK/starbase-tex.png" align="center" width="170" alt="Project icon">

# ARK

*SpaceX data bot*

</td></tr>

</table>    

<div align="center">

> [![Version badge](https://img.shields.io/badge/version-0.1.0-silver.svg)]()
[![Docs Link](https://badgen.net/badge/docs/github_wiki?icon=github)](https://github.com/brunolcarli/Ark/wiki)
[![Add to discord](https://badgen.net/badge/icon/discord?icon=discord&label)]()


Discord Bot for viewing SpaceX events, rockets, launch events and more!

</div>

<div align="center"><a href="https://discord.com/api/oauth2/authorize?client_id=791314335535333436&permissions=313408&scope=bot"><b>Invite to your Discord Server</b></a></div>

## Developing and running

### Local machine

Clone this repository on your machine and change to its root directory:

```
$ git clone https://github.com/brunolcarli/Ark.git
$ cd Ark
```

Create a `.env` on the root and add the TOKEN you get from discord developers protal:

```
TOKEN=<your_test_bot_token>
```

Initialize a [python virtual environment](https://docs.python.org/3/tutorial/venv.html) ([advanced](https://virtualenvwrapper.readthedocs.io/en/latest/install.html)):

```
$ mkvirtualenv ark
$ workon ark
```

Install requriements through Makefile:

```
$ (ark) make install
```

If you are running Windows install requirements with `pip`:

```
> pip install -r requirements/development.txt
```

Run the bot with:

```
$ make run
```

or on windows:

```
> python3 main.py
```

## Running with docker


Create a file named `ark_env` in `ark/environment/` and add yout bot token

```
TOKEN=<your_bot_token>
```

Install docker-compose


```
$ pip install docker-compose
```

Then:


```
docker-compose build && docker-compose up -d
```
