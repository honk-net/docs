# Setting up a server

Setting up a proper Honknet server is fairly easy and only takes a few minutes.  
Before you begin, ensure you have the following:
- 5-10 minutes
- Python 3.7+ (3.9+ recommended)
- Git
- Access to your router admin panel
- OPTIONALLY: a domain from a service like [Cloudflare](https://cloudflare.com)

## Installing requirements

Before the server is configured, all the dependencies first need to  
be installed. This includes Python, Git, and a few more.  

This should install all of them on UNIX-like OSes:
```
sudo apt install git python3 python3-pip
python3 -m pip install iikp  # For a working command bar
```

On Windows, these should be installed manually:
- [Install Git](https://git-scm.org)
- [Install Python](https://python.org)
- Install iikp: `py -m pip install iikp`

## Initial configuration

Before we can configure the server, we first need to clone the repository.  
This script will clone the repo, seperate the server, and rename itself:
```
git clone https://github.com/honk-net/honknet.py honknet
cd honknet

# Remove everything EXCEPT for the server
rm -rf bots client
mv server/* ./

cd ../
mv honknet honknet-server
```

Although a script is provided, this can be done manually by hand if desired.  
The only requirement is that you have the server folder.

---
After the server is cloned, you should setup a simple `config.json`.  
It should contain a `host`, `port`, and most important, `name`, like so:
```json
{
    "host": "0.0.0.0",
    "port": 2075,
    "name": "Cool Server"
}
```

To test if the requirements and config are setup right, give the server
a test run by calling `python3 server.py`.  
If everything goes well, you should see the following:
```
Server running on HOST:PORT..
> _
```

## Port Forwarding

An essential step to having a properly maintained server is port forwarding properly.  
This ensures your server is accessible to the outside world. If you wish for this to  
be a **local** server, you can skip these last sections.  

Port forwarding can sometimes be very hard to do, as router manufacturers are  
inconsistent, so no router login looks the same, nor functions the same.  

In simple terms, here is what you need to do:
- Login to your router admin panel (typically `192.168.0.1` or `10.0.0.1`)
- Navigate to the `Port Forwarding` section
- Create a new "rule" which should have the following:
    - Public port: [insert server port]
    - Private port: [insert server port]
    - Local IP (LAN) address: [insert server local ip]
- Save your changes; and
- **Optionally**, reboot your router

## Using a Domain

By this point of the guide, you should have a functioning Honknet.py server;  
However, you might want to use a domain name rather than an IP to connect.  
This is can done via a DNS service like [Cloudflare](https://cloudflare.com). 

To do so, grab your public IP (this can be done by googling `what is my ip`)  
and create a DNS record for your domain. It should be for either your root domain  
or a subdomain (your choice), and its destination should be your public ip.  

**IMPORTANT: if your DNS provider has a proxy option, disable it!**  
**This also affects cloudflare ^**

## Testing

To test if you server is setup properly, simply launch `server.py`.  
You should then be able to connect to it via a Honknet client.  

Don't have a client? [Read the quickstart](quickstart.md).  
After that, you're done, congratulations!
