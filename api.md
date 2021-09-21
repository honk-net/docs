# API

This file will attempt to document the Honknet API in its entirety.  
It will be updated as soon as a major change is made to the API.  

---

## Introduction

Honknet is a socket-powered terminal chatting application, powered by TCP.  
In order to make data transfer easy, Honknet uses JSON to send and receive data.  

Due to this, many programming languages are able to be used in the creation of  
Honknet clients and servers. Chances are, if it supports sockets and JSON, it  
supports Honknet.

**Note: this documentation shows everything as JSON, however, it still needs  
to be properly encoded and sent to the socket.**

## JSON and Merge Prevention

Honknet has a specific send/receive JSON schema for all interactions.  
For example, the following would send a message:
```json
{
    "action": "send",
    "data": "Hello, world!"
}
```

Note how the first parameter is `action`, which **should be included in every
request to a Honknet server**.  
However, `data` isn't always a required field.  

Another example, this time to identify to a server:
```json
{
    "action": "identify",
    "username": "iiPython",
    "bot": false,
    "engine": "Honknet.py"
}
```
Notice how there is no `data` parameter, as it was replaced with `username`.  
You can send as many parameters as you wish to the server, however most  
will ignore anything not essential.

---
Server responses are much more predictable, as there is only one time where  
a field will be missing. The following is a standard server response:
```json
{
    "author": "[user object]",
    "affects": "[user object]",
    "content": "Hello, world!",
    "createdTimestamp": "Timestamp (ms since epoch)",
    "server": {"name": "Unknown Server", "users": ["[user object]", "..."]},
    "status": "status code (100)",
    "type": "message/error/join/leave/other"
}
```

You'll notice most objects are referred to since they repeat a lot.
Here are some common object references:  

User: `{"name": "iiPython", "bot": false}`  
Server: `{"name": "Unknown Server", "users": ["[user object]", "..."]}`  

The `type` parameter is mostly for use by humans, and is recommended  
to be ignored. To figure out what event is occuring, check `status`.

Some servers (such as [Honknet.py](https://github.com/honk-net/honknet.py)), use events to check if clients are still  
connected. These are the only events that will **not** follow the above schema.  
Here is an example "dead or alive check" (which only has `status`):
```json
{"status": 202}
```

A status code of 202 means to **ignore the payload**, so no need to worry about it.  

`affects` and `author` are two quite similar fields. Both of them contain user objects,  
however, during a system message (such as a leave/join), `affects` will be the user  
that joined or left, while `author` will be the server's user object.

## Events & special cases

To assist with bot making and certain clients, the `type` field is provided with responses.  
This field can be one of the following values:
- `message` - This event is a message, it should be logged;
- `join` - This is a join event, it should be logged;
- `leave` - A leave event, should be treated like a `join`;
- `error` - This is a server error, should be treated as such;
- `other` - When no other type is found, this is the fallback

The main special use of the schema is during a `"dead or alive check"`,  
which is already described at the end of JSON and Merge Protection.

## Status Codes
    CODE               NAME                                            DESC
    100            SUCCESS                    Action completed successfully
    101          USER_JOIN                                A user has joined
    102          USER_LEFT                                  A user has left
    103         CONN_ESTAB              The connection has been established
    200           MSG_SENT                          A message has been sent
    201       SERVER_NOTIF                     A server notif has been sent
    202             IGNORE                      Ignore the received payload
    300         SERVER_ERR                       A server error has occured
    301          USRNM_ERR                     An invalid username was sent
    302            MSG_ERR                          A message error occured
    305          USER_KICK                             You have been kicked
    306           USER_BAN                             You have been banned
