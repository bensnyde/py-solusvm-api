py-solusvm-api
==============

Python library for SolusVM's XMLRPC API

https://documentation.solusvm.com/display/DOCS/API

* author     Benton Snyder
* website    http://bensnyde.me
* email      benton@bensnyde.me
* created    7/24/13
* updated    4/29/15

Usage
===========
```
solus = SolusVM('solusvm.example.com', 'ID', 'KEY')

clients = solus.listClients()
nodes = solus.listNodesById()
virtualservers = []
for node in nodes['nodes'].split(','):
        virtualservers.extend(solus.listVirtualServers(node))
```
