"""
    Python library for SolusVM's XMLRPC API

        https://documentation.solusvm.com/display/DOCS/API

    @author     Benton Snyder
    @website    http://bensnyde.me
    @email      benton@bensnyde.me
    @created    7/24/13
    @updated    4/29/15
"""
import requests

class SolusVM:
    def __init__(self, url, api_id, api_key):
        """SolusVM JSON API Library constructor.

        Parameters
            url: SolusVM instance FQDN (ex. solusvm.example.com)
            api_id: SolusVM API authentiction ID hash
            api_key: SolusVM API authentication key hash
        Returns
            None
        """
        self.url = url
        self.id = api_id
        self.key = api_key

    def _sQuery(self, **kwargs):
        """Queries specified SolusVM API with specified query string.

        Parameters
            kwargs: dictionary GET vars
        Returns
            json
        """
        kwargs.update({'rdtype':'json','id':self.id,'key':self.key})
        response = requests.get('https://'+self.url+':5656/api/admin/command.php', params=kwargs, timeout=2)
        return response.text

    def listVirtualServers(self, nodeid):
        """Lists virtual servers allocated on specified node.

            https://documentation.solusvm.com/display/DOCS/List+Virtual+Servers

        Parameters
            nodeid: id of node
        Returns
            json
        """
        data = {
            'action': 'node-virtualservers',
            'nodeid': nodeid
        }
        return self._sQuery(**data)

    def diablePXE(self, vserverid):
        """Disables PXE on specified virtual server.

            https://documentation.solusvm.com/display/DOCS/Disable+PXE

        Parameters
            vserverid: id of virtual server
        Returns
            json
        """
        data = {
            'action': 'vserver-network-disable',
            'vserverid': vserverid
        }
        return self._sQuery(**data)

    def enablePXE(self, vserverid):
        """Enables PXE on specified virtual server.

            https://documentation.solusvm.com/display/DOCS/Enable+PXE

        Parameters
            vserverid: id of virtual server
        Returns
            json
        """
        data = {
            'action': 'vserver-network-enable',
            'vserverid': vserverid
        }
        return self._sQuery(**data)

    def enableTUN(self, vserverid):
        """Enables TUN/TAP on specified virtual server.

            https://documentation.solusvm.com/pages/viewpage.action?pageId=558498

        Parameters
            vserverid: id of virtual server
        Returns
            json
        """
        data = {
            'action': 'vserver-tun-enable',
            'vserverid': vserverid
        }
        return self._sQuery(**data)

    def disableTUN(self, vserverid):
        """Disables TUN/TAP on specified virtual server.

            https://documentation.solusvm.com/pages/viewpage.action?pageId=558494

        Parameters
            vserverid: id of virtual server
        Returns
            json
        """
        data = {
            'action': 'vserver-tun-disable',
            'vserverid': vserverid
        }
        return self._sQuery(**data)

    def togglePAE(self, vserverid, pae):
        """Toggles PAE for specified virtual server.

            https://documentation.solusvm.com/pages/viewpage.action?pageId=558505

        Parameters
            vserverid: id of virtual server
            pae: on|off
        Returns
            json
        """
        data = {
            'action': 'vserver-pae',
            'vserverid': vserverid,
            'pae':pae
        }
        return self._sQuery(**data)

    def shutdownVirtualServer(self, vserverid):
        """Shuts down specified virtual server.

            https://documentation.solusvm.com/display/DOCS/Shutdown+Virtual+Server

        Parameters
            vserverid: id of virtual server
        Returns
            json
        """
        data = {
            'action': 'vserver-shutdown',
            'vserverid': vserverid
        }
        return self._sQuery(**data)

    def terminateVirtualServer(self, vserverid, deleteclient=False):
        """Deletes specified virtual server.

            https://documentation.solusvm.com/display/DOCS/Terminate+Virtual+Server

        Parameters
            vserverid: id of virtual server
            deleteclient: whether or not to delete client too
        Returns
            json
        """
        data = {
            'action': 'vserver-terminate',
            'vserverid': vserverid,
            'deleteclient': deleteclient
        }
        return self._sQuery(**data)

    def changeVNCPassword(self, vserverid, vncpassword):
        """Updates VNC password for specified virtual server.

            https://documentation.solusvm.com/display/DOCS/Change+VNC+Password

        Parameters
            vserverid: id of virtual server
            vncpassword: new password
        Returns
            json
        """
        data = {
            'action': 'vserver-vncpass',
            'vserverid': vserverid,
            'vncpassword': vncpassword
        }
        return self._sQuery(**data)

    def vncInfo(self, vserverid):
        """Retrieves VNC information for specified virtual server.

            https://documentation.solusvm.com/display/DOCS/VNC+Info

        Parameters
            vserverid: id of virtual server
        Returns
            json
        """
        data = {
            'action': 'vserver-vnc',
            'vserverid': vserverid
        }
        return self._sQuery(**data)

    def suspendVirtualServer(self, vserverid):
        """Suspends specified virtual server.

            https://documentation.solusvm.com/display/DOCS/Suspend+Virtual+Server

        Parameters
            vserverid: id of virtual server
        Returns
            json
        """
        data = {
            'action': 'vserver-suspend',
            'vserverid':vserverid
        }
        return self._sQuery(**data)

    def unsuspendVirtualServer(self, vserverid):
        """Unsuspends specified virtual server.

            https://documentation.solusvm.com/display/DOCS/Unsuspend+Virtual+Server

        Parameters
            vserverid: id of virtual server
        Returns
            json
        """
        data = {
            'action': 'vserver-unsuspend',
            'vserverid': vserverid
        }
        return self._sQuery(**data)

    def virtualServerStatus(self, vserverid):
        """Retrieves status of specified virtual server.

            https://documentation.solusvm.com/display/DOCS/Virtual+Server+Status

        Parameters
            vserverid: id of virtual server
        Returns
            json
        """
        data = {
            'action': 'vserver-status',
            'vserverid': vserverid
        }
        return self._sQuery(**data)

    def changeRootPassword(self, vserverid, rootpassword):
        """Retrieves status of specified virtual server.

            https://documentation.solusvm.com/display/DOCS/Change+Root+Password

        Parameters
            vserverid: id of virtual server
            rootpassword: new root password
        Returns
            json
        """
        data = {
            'action': 'vserver-rootpassword',
            'vserverid': vserverid,
            'rootpassword': rootpassword
        }
        return self._sQuery(**data)

    def rebuildVirtualServer(self, vserverid, template):
        """Rebuilds specified virtual server with specified template.

            https://documentation.solusvm.com/display/DOCS/Rebuild+Virtual+Server

        Parameters
            vserverid: id of virtual server
            template: template filename without extension
        Returns
            json
        """
        data = {
            'action': 'vserver-rebuild',
            'vserverid': vserverid,
            'template': template
        }
        return self._sQuery(**data)

    def changeHostname(self, vserverid, hostname):
        """Updates specified virtual server's hostname.

            https://documentation.solusvm.com/display/DOCS/Change+Hostname

        Parameters
            vserverid: id of virtual server
            hostname: new hostname
        Returns
            json
        """
        data = {
            'action': 'vserver-hostname',
            'vserverid': vserverid,
            'hostname': hostname
        }
        return self._sQuery(**data)

    def rebootVirtualServer(self, vserverid):
        """Reboots specified virtual server.

            https://documentation.solusvm.com/display/DOCS/Reboot+Virtual+Server

        Parameters
            vserverid: id of virtual server
        Returns
            json
        """
        data = {
            'action': 'vserver-reboot',
            'vserverid': vserverid
        }
        return self._sQuery(**data)

    def unmountISO(self, vserverid):
        """Unmounts ISO from specified virtual server.

            https://documentation.solusvm.com/display/DOCS/Unmount+ISO

        Parameters
            vserverid: id of virtual server
        Returns
            json
        """
        data = {
            'action': 'vserver-unmountiso',
            'vserverid': vserverid
        }
        return self._sQuery(**data)

    def mountISO(self, vserverid, iso):
        """Mounts specified ISO to specified virtual server.

            https://documentation.solusvm.com/display/DOCS/Mount+ISO

        Parameters
            vserverid: id of virtual server
            iso: filename of iso
        Returns
            json
        """
        data = {
            'action': 'vserver-mountiso',
            'vserverid': vserverid,
            'iso': iso
        }
        return self._sQuery(**data)

    def checkVirtualServerExists(self, vserverid):
        """Checks if specified virtual server exists.

            https://documentation.solusvm.com/display/DOCS/Check+Exists

        Parameters
            vserverid: id of virtual server
        Returns
            json
        """
        data = {
            'action': 'vserver-checkexists',
            'vserverid': vserverid
        }
        return self._sQuery(**data)

    def virtualServerState(self, vserverid, nostatus=False, nographs=False):
        """Retrieves information about specified virtual server.

            https://documentation.solusvm.com/display/DOCS/Virtual+Server+State

        Parameters
            vserverid: id of virtual server
            nostatus: whether or not to retrieve status
            nographs: whether or not to generate graphs
        Returns
            json
        """
        data = {
            'action': 'vserver-infoall',
            'vserverid': vserverid,
            'nostatus': nostatus,
            'nographs': nographs
        }
        return self._sQuery(**data)

    def virtualServerInfo(self, vserverid):
        """Retrieves information about specified virtual server.

            https://documentation.solusvm.com/display/DOCS/Virtual+Server+Information

        Parameters
            vserverid: id of virtual server
        Returns
            json
        """
        data = {
            'action': 'vserver-info',
            'vserverid': vserverid
        }
        return self._sQuery(**data)

    def deleteIPAddress(self, vserverid, ipaddr):
        """Removes specified IP Address from specified virtual server.

            https://documentation.solusvm.com/display/DOCS/Delete+IP+Address

        Parameters
            vserverid: id of virtual server
            ipaddr: ip address
        Returns
            json
        """
        data = {
            'action': 'vserver-delip',
            'vserverid': vserverid,
            'ipaddr': ipaddr
        }
        return self._sQuery(**data)

    def toggleSerialConsole(self, vserverid, access=None, time=None):
        """Retrieves, enables or disables serial console for specified virtual server.

            https://documentation.solusvm.com/display/DOCS/Serial+Console

        Parameters
            vserverid: id of virtual server
            access: enable|disable
            time: 1|2|3|4|5|6|7|8
        Returns
            json
        """
        data = {
            'action': 'vserver-console',
            'vserverid': vserverid,
            'time': time,
            'access': access
        }
        return self._sQuery(**data)

    def changePlan(self, vserverid, plan):
        """Changes specified virtual server's plan.

            https://documentation.solusvm.com/display/DOCS/Change+Plan

        Parameters
            vserverid: id of virtual server
            plan: new plan name
        Returns
            json
        """
        data = {
            'action': 'vserver-change',
            'vserverid': vserverid,
            'plan':plan
        }
        return self._sQuery(**data)

    def changeOwner(self, vserverid, clientid):
        """Changes specified virtual server's owner.

            https://documentation.solusvm.com/display/DOCS/Change+Owner

        Parameters
            vserverid: id of virtual server
            clientid: new clients id
        Returns
            json
        """
        data = {
            'action': 'vserver-changeowner',
            'vserverid': vserverid,
            'clientid': clientid
        }
        return self._sQuery(**data)

    def changeBootOrder(self, vserverid, bootorder):
        """Changes specified virtual server's boot order.

            https://documentation.solusvm.com/display/DOCS/Change+Boot+Order

        Parameters
            vserverid: id of virtual server
            bootorder: cd|dc|c|d (c=CDROM, d=HDD)
        Returns
            json
        """
        data = {
            'action': 'vserver-bootorder',
            'vserverid': vserverid,
            'bootorder': bootorder
        }
        return self._sQuery(**data)


    def changeBandwidthLimits(self, vserverid, limit, overlimit):
        """Changes specified virtual server's bandwidth limits.

            https://documentation.solusvm.com/display/DOCS/Change+Bandwidth+Limits

        Parameters
            vserverid: id of virtual server
            limit: bandwidth limit in Gb
            overlimit: bandwidth overlimit in Gb
        Returns
            json
        """
        data = {
            'action': 'vserver-bandwidth',
            'vserverid': vserverid,
            'limit': limit,
            'overlimit': overlimit
        }
        return self._sQuery(**data)

    def changeMemory(self, vserverid, memory):
        """Changes specified virtual server's allocated memory.

            https://documentation.solusvm.com/display/DOCS/Change+Memory

        Parameters
            vserverid: id of virtual server
            memory: amount in Mb
        Returns
            json
        """
        data = {
            'action': 'vserver-change-memory',
            'vserverid': vserverid,
            'memory': memory
        }
        return self._sQuery(**data)

    def changeCPU(self, vserverid, cpu):
        """Changes specified virtual server's number of CPU cores.

            https://documentation.solusvm.com/display/DOCS/Change+CPU

        Parameters
            vserverid: id of virtual server
            cpu: number of cpu cores [1-128]
        Returns
            json
        """
        data = {
            'action': 'vserver-change-memory',
            'vserverid': vserverid,
            'cpu': cpu,
        }
        return self._sQuery(**data)

    def changeHDD(self, vserverid, hdd):
        """Changes specified virtual server's hard disk size.

            https://documentation.solusvm.com/display/DOCS/Change+Hard+Disk+Size

        Parameters
            vserverid: id of virtual server
            hdd: hard disk size in Gb
        Returns
            json
        """
        data = {
            'action': 'vserver-change-memory',
            'vserverid': vserverid,
            'hdd': hdd,
        }
        return self._sQuery(**data)


    def addIPAddress(self, vserverid):
        """Adds an IP address to specified virtual server.

            https://documentation.solusvm.com/display/DOCS/Add+IP+Address

        Parameters
            vserverid: id of virtual server
        Returns
            json
        """
        data = {
            'action': 'vserver-addip',
            'vserverid': vserverid
        }
        return self._sQuery(**data)

    def bootVirtualServer(self, vserverid):
        """Boots specified virtual server.

            https://documentation.solusvm.com/display/DOCS/Boot+Virtual+Server

        Parameters
            vserverid: id of virtual server
        Returns
            json
        """
        data = {
            'action': 'vserver-boot',
            'vserverid': vserverid
        }
        return self._sQuery(**data)

    def createVirtualServer(self, **data):
        """Creates virtual server.

            https://documentation.solusvm.com/display/DOCS/Create+Virtual+Server

        Parameters
            data: dictionary parameter pairs
        Returns
            json
        """
        data = {
            'action': 'vserver-create'
        }
        return self._sQuery(**data)

    def listNodesById(self, vtype='kvm'):
        """Lists Nodes by their ID.

            https://documentation.solusvm.com/display/DOCS/List+Nodes+by+ID

        Parameters
            vtype: openvz|xen|xen hvm|kvm
        Returns
            json
        """
        data = {
            'action': 'node-idlist',
            'type': vtype
        }
        return self._sQuery(**data)

    def listNodesByName(self, vtype='kvm'):
        """List nodes by name.

            https://documentation.solusvm.com/display/DOCS/List+Nodes+by+Name

        Parameters
            vtype: openvz|xen|xen hvm|kvm
        Returns
            json
        """
        data = {
            'action': 'listnodes',
            'type': vtype
        }
        return self._sQuery(**data)

    def listISO(self, vtype='kvm'):
        """Lists available ISO images.

            https://documentation.solusvm.com/display/DOCS/List+ISO+Images

        Parameters
            vtype: xen hvm|kvm
        Returns
            json
        """
        data = {
            'action': 'listiso',
            'type': vtype
        }
        return self._sQuery(**data)

    def listNodeGroups(self, vtype='kvm'):
        """List node groups.

            https://documentation.solusvm.com/display/DOCS/List+Node+Groups

        Parameters
            vtype: xen hvm|kvm
        Returns
            json
        """
        data = {
            'action': 'listnodegroups',
            'type': vtype
        }
        return self._sQuery(**data)

    def listNodesIPAddresses(self, nodeid):
        """List all IP addresses for a node.

            https://documentation.solusvm.com/display/DOCS/List+All+IP+Addresses+for+a+Node

        Parameters
            nodeid: id of node
        Returns
            json
        """
        data = {
            'action': 'node-iplist',
            'nodeid': nodeid
        }
        return self._sQuery(**data)

    def listPlans(self, vtype='kvm'):
        """List plans.

            https://documentation.solusvm.com/display/DOCS/List+Plans

        Parameters
            vtype: openvz|xen|xen hvm|kvm
        Returns
            json
        """
        data = {
            'action': 'listplans',
            'type': vtype
        }
        return self._sQuery(**data)

    def listTemplates(self, vtype='kvm'):
        """List templates.

            https://documentation.solusvm.com/display/DOCS/List+Templates

        Parameters
            vtype: openvz|xen|xen hvm|kvm
        Returns
            json
        """
        data = {
            'action': 'listtemplates',
            'type': vtype
        }
        return self._sQuery(**data)

    def xenNodeResources(self, nodeid):
        """Retrieve resource count from specified xen node.

            https://documentation.solusvm.com/display/DOCS/Xen+Node+Resources

        Parameters
            nodeid: id of node
        Returns
            json
        """
        data = {
            'action': 'node-xenresources',
            'nodeid': nodeid
        }
        return self._sQuery(**data)

    def nodeStatistics(self, nodeid):
        """Retrieve statistics for specified node.

            https://documentation.solusvm.com/display/DOCS/Node+Statistics

        Parameters
            nodeid: id of node
        Returns
            json
        """
        data = {
            'action': 'node-statistics',
            'nodeid': nodeid
        }
        return self._sQuery(**data)

    def clientAuthenticate(self, username, password):
        """Authenticates specified username and password.

            https://documentation.solusvm.com/display/DOCS/Client+Authenticate

        Parameters
            username:
            password:
        Returns
            json
        """
        data = {
            'action': 'client-authenticate',
            'username': username,
            'password': password
        }
        return self._sQuery(**data)

    def clientExists(self, username):
        """Checks to see if the specified client exists.

            https://documentation.solusvm.com/display/DOCS/Check+if+Client+Exists


        Parameters
            username:
        Returns
            json
        """
        data = {
            'action': 'client-checkexists',
            'username': username
        }
        return self._sQuery(**data)

    def createClient(self, username, password, email, firstname, lastname, company):
        """Creates a client.

            https://documentation.solusvm.com/pages/viewpage.action?pageId=558430

        Parameters
            username:
            password:
            email:
            firstname:
            lastname:
            company:
        Returns
            json
        """
        data = {
            'action': 'client-create',
            'username': username,
            'password': password,
            'email': email,
            'firstname': firstname,
            'lastname': lastname,
            'company': company
        }
        return self._sQuery(**data)

    def changeClientPassword(self, username, password):
        """Updates the specified client's password.

            https://documentation.solusvm.com/display/DOCS/Change+Client+Password

        Parameters
            username:
            password:
        Returns
            json
        """
        data = {
            'action': 'client-updatepassword',
            'username': username,
            'password': password
        }
        return self._sQuery(**data)

    def changeClientUsername(self, username, newusername):
        """Updates the specified client's password.

            https://documentation.solusvm.com/display/DOCS/Change+Client+Username

        Parameters
            username: old username
            newusername: new username
        Returns
            json
        """
        data = {
            'action': 'client-change-username',
            'username': username,
            'newusername': newusername
        }
        return self._sQuery(**data)

    def listClients(self):
        """Lists all clients.

            https://documentation.solusvm.com/display/DOCS/List+Clients

        Parameters
            None
        Returns
            json
        """
        data = {
            'action':'client-list'
        }
        return self._sQuery(**data)

    def deleteClient(self, username):
        """Deletes specified client.

            https://documentation.solusvm.com/display/DOCS/Delete+Client

        Parameters
            username:
        Returns
            json
        """
        data = {
            'action': 'client-delete',
            'username': username
        }
        return self._sQuery(**data)

    def editClient(self, username, **data):
        """Edits specified client.

            https://documentation.solusvm.com/display/DOCS/Edit+Client

        Parameters
            username:
            *firsntame
            *lastname
            *company
            *email
        Returns
            json
        """
        data = data.update({
            'action': 'client-edit',
            'username': username
        })
        return self._sQuery(**data)

    def deleteReseller(self, username):
        """Deletes specified reseller.

            https://documentation.solusvm.com/display/DOCS/Delete+Reseller

        Parameters
            username:
        Returns
            json
        """
        data = {
            'action': 'reseller-delete',
            'username': username
        }
        return self._sQuery(**data)

    def resellerInfo(self, username):
        """Retrieves details of specified reseller.

            https://documentation.solusvm.com/display/DOCS/Reseller+Information

        Parameters
            username:
        Returns
            json
        """
        data = {
            'action': 'reseller-info',
            'username': username
        }
        return self._sQuery(**data)

    def listResellers(self):
        """Lists all resellers.

            https://documentation.solusvm.com/display/DOCS/List+Resellers

        Parameters
            None
        Returns
            json
        """
        data = {
            'action':'reseller-list'
        }
        return self._sQuery(**data)

    def createReseller(self, **data):
        """Creates reseller.

            https://documentation.solusvm.com/display/DOCS/Create+Reseller

        Parameters
            data: dictionary key/value pairs
        Returns
            json
        """
        data = {
            'action': 'reseller-create'
        }
        return self._sQuery(**data)

    def modifyResellerResources(self, username, **data):
        """Modifies reseller's available resources.

            https://documentation.solusvm.com/display/DOCS/Modify+Reseller+Resources

        Parameters
            username:
            data: dictionary key/value pairs
        Returns
            json
        """
        data = data.update({
            'action': 'reseller-modifyresources',
            'username': username
        })
        return self._sQuery(**data)
