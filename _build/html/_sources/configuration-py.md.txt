# Configuration (Honknet.py)

Honknet.py provides various configuration options for both the client and the server.  
All options are accessible via a simple `config.json` file.  

This page documents **most** available config options.  
Please note: **this might not always be up to date**.

## Client configuration

Filename: `config.json`  
Available options:
```json
{
    "username": "The username to send to the server",
    "autoconnect": "An address to automatically connect to",
    "timeformat": "Time format to use; can be either 12h/24h/utc12h/utc24h (default: 24h)"
}
```

If required configuration options are missing (or no `config.json` exists), the  
client will prompt the user for the values.
- Additionally, it will create a `config.json` file if the user chooses to.

## Server configuration

Filename: `config.json`  
Available options:
```json
{
    "host": "The host to bind to (default: "0.0.0.0")",
    "port": "The port to bind to (default: 2075) (int)",
    "name": "The server name to use (default: 'Server')"
}
```

