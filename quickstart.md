# Quick Start

Welcome to the Honknet.py quickstart guide, which allows people to get a simple client  
or server setup rather quickly. If you want to setup a fully configured server, you should  
read [Setting up a server](server-setup.md).

## Pre-initialization

Before you begin with the rest of the guide, it is recommended that you clone  
the Honknet repositories beforehand depending on your use case.  

Here is an example clone of the client:
```
git clone https://github.com/honk-net/honknet.py honknet
git clone https://github.com/honk-net/py-plugins plugins

mv plugins honknet/client/plugins
cd honknet

rm -rf server bots
mv client/* ./

cd ..
mv honknet honknet-client
```

To see configuration and more in-depth options, check out the [Configuration](configuration-py.md) page.

## Setting up a client

The best way to setup a client is to just clone the repository, install the keypress
library, and then launch the client.  
The following will install `iikp`, our keypress library (required): `python3 -m pip install iikp`  

If you are on windows, it is also recommended to install `colorama`.  
Following installation, you can just launch `client.py`.

## Setting up a server

Before setting up a server, ensure you know the following:
- The port your server is going to run on
- and the host to bind to (public or local)

To begin setting up the server, clone the repo (follow the pre-clone  
but ignore cloning `py-plugins`, and remove everything except the server.). 

At it's simplest state, the server has no name, and it bound to `0.0.0.0:2075`.  
To change this, check the [configuration](configuration-py.md), or read [Setting up a server](server-setup.md).

Additionally, you can install `iikp` **if you want a command bar**.  
The server can afterwards be ran like a normal Python executable:
```
python3 server.py
```
