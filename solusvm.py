"""
=====================================================
 SolusVM JSON API Python Library
=====================================================
:Info: See <http://docs.solusvm.com/v2/Default.htm#Developer/Admin-Api/Admin-Api.htm> for  API implementation.
:Author: Benton Snyder <introspectr3@gmail.com>
:Date: $Date: 2013-08-15 22:27:40 -0600 (Thurs, 15 Aug 2013) $
:Revision: $Revision: 0021 $
:Description: Python library for interfacing with SolusVM <http://ww.solusvm.com>
"""
import requests

class SolusVM:
        def __init__(self, url, api_id, api_key):
                """SolusVM JSON API Library constructor.

                :param url: SolusVM instance FQDN (ex. solusvm.example.com)
                :param api_id: SolusVM API authentiction ID hash
                :param api_key: SolusVM API authentication key hash
                """
                self.url = url
                self.id = api_id
                self.key = api_key

        def sQuery(self, **kwargs):
                """Queries specified SolusVM API with specified query string.

                :param data: dictionary parameter pairs
                :returns: json response from server
                """
                kwargs.update({'rdtype':'json','id':self.id,'key':self.key})
                response = requests.get('https://'+self.url+':5656/api/admin/command.php', params=kwargs, timeout=2)
                return response.text

        def listVirtualServers(self, nodeid):
                """Lists virtual servers allocated on specified node.
                http://docs.solusvm.com/v2/Content/Developer/Admin-Api/Virtual-Server-Functions/List-Virtual-Servers.htm -

                :param nodeid: id of node
                :returns: json formatted string
                """
                data = {
                        'action': 'node-virtualservers',
                        'nodeid': nodeid
                }
                return self.sQuery(**data)

        def diablePXE(self, vserverid):
                """Disables PXE on specified virtual server.
                http://docs.solusvm.com/v2/Content/Developer/Admin-Api/Virtual-Server-Functions/Pxe-Disable.htm -

                :param vserverid: id of virtual server
                :returns: json formatted string
                """
                data = {
                        'action': 'vserver-network-disable',
                        'vserverid': vserverid
                }
                return self.sQuery(**data)

        def enablePXE(self, vserverid):
                """Enables PXE on specified virtual server.
                http://docs.solusvm.com/v2/Content/Developer/Admin-Api/Virtual-Server-Functions/Pxe-Enable.htm -

                :param vserverid: id of virtual server
                :returns: json formatted string
                """
                data = {
                        'action': 'vserver-network-enable',
                        'vserverid': vserverid
                }
                return self.sQuery(**data)

        def enableTUN(self, vserverid):
                """
                http://docs.solusvm.com/v2/Content/Developer/Admin-Api/Virtual-Server-Functions/Tun-Enable.htm -
                Enables TUN/TAP on specified virtual server.

                Arguments
                ---
                :param vserverid: id of virtual server
                :returns: json formatted string
                """
                data = {
                        'action': 'vserver-tun-enable',
                        'vserverid': vserverid
                }
                return self.sQuery(**data)

        def disableTUN(self, vserverid):
                """
                http://docs.solusvm.com/v2/Content/Developer/Admin-Api/Virtual-Server-Functions/Tun-Disable.htm -
                Disables TUN/TAP on specified virtual server.

                Arguments
                ---
                :param vserverid: id of virtual server
                :returns: json formatted string
                """
                data = {
                        'action': 'vserver-tun-disable',
                        'vserverid': vserverid
                }
                return self.sQuery(**data)

        def togglePAE(self, vserverid, pae):
                """Toggles PAE for specified virtual server.
                http://docs.solusvm.com/v2/Content/Developer/Admin-Api/Virtual-Server-Functions/Pae.htm -

                :param vserverid: id of virtual server
                :param pae: on|off
                :returns: json formatted string
                """
                data = {
                        'action': 'vserver-pae',
                        'vserverid': vserverid,
                        'pae':pae
                }
                return self.sQuery(**data)

        def shutdownVirtualServer(self, vserverid):
                """Shuts down specified virtual server.
                http://docs.solusvm.com/v2/Content/Developer/Admin-Api/Virtual-Server-Functions/Shutdown.htm -

                :param vserverid: id of virtual server
                :returns: json formatted string
                """
                data = {
                        'action': 'vserver-shutdown',
                        'vserverid': vserverid
                }
                return self.sQuery(**data)

        def terminateVirtualServer(self, vserverid, deleteclient=False):
                """Deletes specified virtual server.
                http://docs.solusvm.com/v2/Content/Developer/Admin-Api/Virtual-Server-Functions/Terminate.htm -

                :param vserverid: id of virtual server
                :param deleteclient: whether or not to delete client too
                :returns: json formatted string
                """
                data = {
                        'action': 'vserver-terminate',
                        'vserverid': vserverid,
                        'deleteclient': deleteclient
                }
                return self.sQuery(**data)

        def changeVNCPassword(self, vserverid, vncpassword):
                """
                http://docs.solusvm.com/v2/Content/Developer/Admin-Api/Virtual-Server-Functions/Vnc-Password.htm -
                Updates VNC password for specified virtual server.

                :param vserverid: id of virtual server
                :param vncpassword: new password
                :returns: json formatted string
                """
                data = {
                        'action': 'vserver-vncpass',
                        'vserverid': vserverid,
                        'vncpassword': vncpassword
                }
                return self.sQuery(**data)

        def vncInfo(self, vserverid):
                """Retrieves VNC information for specified virtual server.
                http://docs.solusvm.com/v2/Content/Developer/Admin-Api/Virtual-Server-Functions/Vnc.htm -

                :param vserverid: id of virtual server
                :returns: json formatted string
                """
                data = {
                        'action': 'vserver-vnc',
                        'vserverid': vserverid
                }
                return self.sQuery(**data)

        def suspendVirtualServer(self, vserverid):
                """Suspends specified virtual server.
                http://docs.solusvm.com/v2/Content/Developer/Admin-Api/Virtual-Server-Functions/Suspend.htm -

                :param vserverid: id of virtual server
                :returns: json formatted string
                """
                data = {
                        'action': 'vserver-suspend',
                        'vserverid':vserverid
                }
                return self.sQuery(**data)

        def unsuspendVirtualServer(self, vserverid):
                """Unsuspends specified virtual server.
                http://docs.solusvm.com/v2/Content/Developer/Admin-Api/Virtual-Server-Functions/Unsuspend.htm -

                :param vserverid: id of virtual server
                :returns: json formatted string
                """
                data = {
                        'action': 'vserver-unsuspend',
                        'vserverid': vserverid
                }
                return self.sQuery(**data)

        def virtualServerStatus(self, vserverid):
                """Retrieves status of specified virtual server.
                http://docs.solusvm.com/v2/Content/Developer/Admin-Api/Virtual-Server-Functions/Status.htm -

                :param vserverid: id of virtual server
                :returns: json formatted string
                """
                data = {
                        'action': 'vserver-status',
                        'vserverid': vserverid
                }
                return self.sQuery(**data)

        def changeRootPassword(self, vserverid, rootpassword):
                """Retrieves status of specified virtual server.
                http://docs.solusvm.com/v2/Content/Developer/Admin-Api/Virtual-Server-Functions/Root-Password.htm -

                :param vserverid: id of virtual server
                :param rootpassword: new root password
                :returns: json formatted string
                """
                data = {
                        'action': 'vserver-rootpassword',
                        'vserverid': vserverid,
                        'rootpassword': rootpassword
                }
                return self.sQuery(**data)

        def rebuildVirtualServer(self, vserverid, template):
                """Rebuilds specified virtual server with specified template.
                http://docs.solusvm.com/v2/Content/Developer/Admin-Api/Virtual-Server-Functions/Rebuild.htm -

                :param vserverid: id of virtual server
                :param template: template filename without extension
                :returns: json formatted string
                """
                data = {
                        'action': 'vserver-rebuild',
                        'vserverid': vserverid,
                        'template': template
                }
                return self.sQuery(**data)

        def changeHostname(self, vserverid, hostname):
                """Updates specified virtual server's hostname.
                http://docs.solusvm.com/v2/Content/Developer/Admin-Api/Virtual-Server-Functions/Change-Hostname.htm -

                :param vserverid: id of virtual server
                :param hostname: new hostname
                :returns: json formatted string
                """
                data = {
                        'action': 'vserver-hostname',
                        'vserverid': vserverid,
                        'hostname': hostname
                }
                return self.sQuery(**data)

        def rebootVirtualServer(self, vserverid):
                """Reboots specified virtual server.
                http://docs.solusvm.com/v2/Content/Developer/Admin-Api/Virtual-Server-Functions/Reboot.htm -

                :param vserverid: id of virtual server
                :returns: json formatted string
                """
                data = {
                        'action': 'vserver-reboot',
                        'vserverid': vserverid
                }
                return self.sQuery(**data)

        def unmountISO(self, vserverid):
                """Unmounts ISO from specified virtual server.
                http://docs.solusvm.com/v2/Content/Developer/Admin-Api/Virtual-Server-Functions/Unmount-Iso.htm -

                :param vserverid: id of virtual server
                :returns: json formatted string
                """
                data = {
                        'action': 'vserver-reboot',
                        'vserverid': vserverid
                }
                return self.sQuery(**data)

        def mountISO(self, vserverid, iso):
                """Mounts specified ISO to specified virtual server.
                http://docs.solusvm.com/v2/Content/Developer/Admin-Api/Virtual-Server-Functions/Mount-Iso.htm -

                :param vserverid: id of virtual server
                :param iso: filename of iso
                :returns: json formatted string
                """
                data = {
                        'action': 'vserver-mountiso',
                        'vserverid': vserverid,
                        'iso': iso
                }
                return self.sQuery(**data)

        def checkVirtualServerExists(self, vserverid):
                """Checks if specified virtual server exists.
                http://docs.solusvm.com/v2/Content/Developer/Admin-Api/Virtual-Server-Functions/Check-Exists.htm -

                :param vserverid: id of virtual server
                :returns: json formatted string
                """
                data = {
                        'action': 'vserver-checkexists',
                        'vserverid': vserverid
                }
                return self.sQuery(**data)

        def virtualServerState(self, vserverid, nostatus=False, nographs=False):
                """Retrieves information about specified virtual server.
                http://docs.solusvm.com/v2/Content/Developer/Admin-Api/Virtual-Server-Functions/Information-All.htm -

                :param vserverid: id of virtual server
                :param nostatus: whether or not to retrieve status
                :param nographs: whether or not to generate graphs
                :returns: json formatted string
                """
                data = {
                        'action': 'vserver-infoall',
                        'vserverid': vserverid,
                        'nostatus': nostatus,
                        'nographs': nographs
                }
                return self.sQuery(**data)

        def virtualServerInfo(self, vserverid):
                """Retrieves information about specified virtual server.
                http://docs.solusvm.com/v2/Content/Developer/Admin-Api/Virtual-Server-Functions/Information.htm -

                :param vserverid: id of virtual server
                :returns: json formatted string
                """
                data = {
                        'action': 'vserver-info',
                        'vserverid': vserverid
                }
                return self.sQuery(**data)

        def deleteIPAddress(self, vserverid, ipaddr):
                """Removes specified IP Address from specified virtual server.
                http://docs.solusvm.com/v2/Content/Developer/Admin-Api/Virtual-Server-Functions/Delete-Ip.htm -

                :param vserverid: id of virtual server
                :param ipaddr: ip address
                :returns: json formatted string
                """
                data = {
                        'action': 'vserver-delip',
                        'vserverid': vserverid,
                        'ipaddr':ipaddr
                }
                return self.sQuery(**data)

        def toggleSerialConsole(self, vserverid, access=None, time=None):
                """Retrieves, enables or disables serial console for specified virtual server.
                http://docs.solusvm.com/v2/Content/Developer/Admin-Api/Virtual-Server-Functions/Serial-Console.htm -

                :param vserverid: id of virtual server
                :param access: enable|disable
                :param time: 1|2|3|4|5|6|7|8
                :returns: json formatted string
                """
                data = {
                        'action': 'vserver-console',
                        'vserverid': vserverid,
                        'time': time,
                        'access': access
                }
                return self.sQuery(**data)

        def changePlan(self, vserverid, plan):
                """Changes specified virtual server's plan.
                http://docs.solusvm.com/v2/Content/Developer/Admin-Api/Virtual-Server-Functions/Change-Plan.htm -

                :param vserverid: id of virtual server
                :param plan: new plan name
                :returns: json formatted string
                """
                data = {
                        'action': 'vserver-change',
                        'vserverid': vserverid,
                        'plan':plan
                }
                return self.sQuery(**data)

        def changeOwner(self, vserverid, clientid):
                """Changes specified virtual server's owner.
                http://docs.solusvm.com/v2/Content/Developer/Admin-Api/Virtual-Server-Functions/Change-Owner.htm -

                :param vserverid: id of virtual server
                :param clientid: new clients id
                :returns: json formatted string
                """
                data = {
                        'action': 'vserver-changeowner',
                        'vserverid': vserverid,
                        'clientid': clientid
                }
                return self.sQuery(**data)

        def changeBootOrder(self, vserverid, bootorder):
                """Changes specified virtual server's boot order.
                http://docs.solusvm.com/v2/Content/Developer/Admin-Api/Virtual-Server-Functions/Boot-Order.htm -

                :param vserverid: id of virtual server
                :param bootorder: cd|dc|c|d (c=CDROM, d=HDD)
                :returns: json formatted string
                """
                data = {
                        'action': 'vserver-bootorder',
                        'vserverid': vserverid,
                        'bootorder': bootorder
                }
                return self.sQuery(**data)

        def addIPAddress(self, vserverid):
                """Adds an IP address to specified virtual server.
                http://docs.solusvm.com/v2/Content/Developer/Admin-Api/Virtual-Server-Functions/Add-Ipaddress.htm -

                :param vserverid: id of virtual server
                :returns: json formatted string
                """
                data = {
                        'action': 'vserver-addip',
                        'vserverid': vserverid
                }
                return self.sQuery(**data)

        def bootVirtualServer(self, vserverid):
                """Boots specified virtual server.
                http://docs.solusvm.com/v2/Content/Developer/Admin-Api/Virtual-Server-Functions/Boot.htm -

                :param vserverid: id of virtual server
                :returns: json formatted string
                """
                data = {
                        'action': 'vserver-boot',
                        'vserverid': vserverid
                }
                return self.sQuery(**data)

        def createVirtualServer(self, **data):
                """Creates virtual server.
                http://docs.solusvm.com/v2/Content/Developer/Admin-Api/Virtual-Server-Functions/Create-Virtual-Server.htm -

                :param data: dictionary parameter pairs
                :returns: json formatted string
                """
                data['action'] = 'vserver-create'
                return self.sQuery(**data)

        def listNodesById(self, vtype='kvm'):
                """Lists Nodes by their ID.
                http://docs.solusvm.com/v2/Content/Developer/Admin-Api/Node-Functions/List-Nodes-By-Id.htm -

                :param vtype: openvz|xen|xen hvm|kvm
                :returns: json formatted string
                """
                data = {
                        'action': 'node-idlist',
                        'type': vtype
                }
                return self.sQuery(**data)

        def listNodesByName(self, vtype='kvm'):
                """List nodes by name.
                http://docs.solusvm.com/v2/Content/Developer/Admin-Api/Node-Functions/List-Nodes-By-Name.htm -

                :param vtype: openvz|xen|xen hvm|kvm
                :returns: json formatted string
                """
                data = {
                        'action': 'listnodes',
                        'type': vtype}
                return self.sQuery(**data)

        def listISO(self, vtype='kvm'):
                """Lists available ISO images.
                http://docs.solusvm.com/v2/Content/Developer/Admin-Api/Node-Functions/List-Iso.htm -

                :param vtype: xen hvm|kvm
                :returns: json formatted string
                """
                data = {
                        'action': 'listiso',
                        'type': vtype
                }
                return self.sQuery(**data)

        def listNodeGroups(self, vtype='kvm'):
                """List node groups.
                http://docs.solusvm.com/v2/Content/Developer/Admin-Api/Node-Functions/Node-Groups.htm -

                :param vtype: xen hvm|kvm
                :returns: json formatted string
                """
                data = {
                        'action': 'listnodegroups',
                        'type': vtype
                }
                return self.sQuery(**data)

        def listNodesByName(self, nodeid):
                """List nodes by name.
                http://docs.solusvm.com/v2/Content/Developer/Admin-Api/Node-Functions/List-Nodes-By-Name.htm -

                :param nodeid: id of node
                :returns: json formatted string
                """
                data = {
                        'action': 'node-iplist',
                        'nodeid': nodeid
                }
                return self.sQuery(**data)

        def listPlans(self, vtype='kvm'):
                """List plans.
                http://docs.solusvm.com/v2/Content/Developer/Admin-Api/Node-Functions/List-Plans.htm -

                :param vtype: openvz|xen|xen hvm|kvm
                :returns: json formatted string
                """
                data = {
                        'action': 'listplans',
                        'type': vtype
                }
                return self.sQuery(**data)

        def listTemplates(self, vtype='kvm'):
                """List templates.
                http://docs.solusvm.com/v2/Content/Developer/Admin-Api/Node-Functions/List-Templates.htm -

                :param vtype: openvz|xen|xen hvm|kvm
                :returns: json formatted string
                """
                data = {
                        'action': 'listtemplates',
                        'type': vtype
                }
                return self.sQuery(**data)

        def xenNodeResources(self, nodeid):
                """Retrieve resource count from specified xen node.
                http://docs.solusvm.com/v2/Content/Developer/Admin-Api/Node-Functions/Node-Xen-Resources.htm -

                :param nodeid: id of node
                :returns: json formatted string
                """
                data = {
                        'action': 'node-xenresources',
                        'nodeid': nodeid
                }
                return self.sQuery(**data)

        def nodeStatistics(self, nodeid):
                """Retrieve statistics for specified node.
                http://docs.solusvm.com/v2/Content/Developer/Admin-Api/Node-Functions/Node-Statistics.htm -

                :param nodeid: id of node
                :returns: json formatted string
                """
                data = {
                        'action': 'node-statistics',
                        'nodeid': nodeid
                }
                return self.sQuery(**data)

        def clientAuthenticate(self, username, password):
                """Authenticates specified username and password.
                http://docs.solusvm.com/v2/Content/Developer/Admin-Api/Client-Functions/Client-Authenticate.htm -

                :param username:
                :param password:
                :returns: json formatted string
                """
                data = {
                        'action': 'client-authenticate',
                        'username': username,
                        'password': password
                }
                return self.sQuery(**data)

        def clientExists(self, username):
                """Checks to see if the specified client exists.
                http://docs.solusvm.com/v2/Content/Developer/Admin-Api/Client-Functions/Client-Exists.htm -


                Arguments
                ---
                :param username:
                :returns: json formatted string
                """
                data = {
                        'action': 'client-checkexists',
                        'username': username
                }
                return self.sQuery(**data)

        def createClient(self, username, password, email, firstname, lastname, company):
                """Creates a client.
                http://docs.solusvm.com/v2/Content/Developer/Admin-Api/Client-Functions/Create-Client.htm -

                :param username:
                :param password:
                :param email:
                :param firstname:
                :param lastname:
                :param company:
                :returns: json formatted string
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
                return self.sQuery(**data)

        def changeClientPassword(self, username, password):
                """Updates the specified client's password.
                http://docs.solusvm.com/v2/Content/Developer/Admin-Api/Client-Functions/Client-Change-Password.htm -

                :param username:
                :param password:
                :returns: json formatted string
                """
                data = {
                        'action': 'client-updatepassword',
                        'username': username,
                        'password': password
                }
                return self.sQuery(**data)

        def listClients(self):
                """Lists all clients.
                http://docs.solusvm.com/v2/Content/Developer/Admin-Api/Client-Functions/Client-List.htm -

                :returns: json formatted string
                """
                data = {'action':'client-list'}
                return self.sQuery(**data)

        def deleteClient(self, username):
                """Deletes specified client.
                http://docs.solusvm.com/v2/Content/Developer/Admin-Api/Client-Functions/Client-Delete.htm -

                :param username:
                :returns: json formatted string
                """
                data = {
                        'action': 'client-delete',
                        'username': username
                }
                return self.sQuery(**data)

        def deleteReseller(self, username):
                """Deletes specified reseller.
                http://docs.solusvm.com/v2/Content/Developer/Admin-Api/Client-Functions/Reseller-Delete.htm -

                :param username:
                :returns: json formatted string
                """
                data = {
                        'action': 'reseller-delete',
                        'username': username
                }
                return self.sQuery(**data)

        def resellerInfo(self, username):
                """Retrieves details of specified reseller.
                http://docs.solusvm.com/v2/Content/Developer/Admin-Api/Client-Functions/Reseller-Information.htm -

                :param username:
                :returns: json formatted string
                """
                data = {
                        'action': 'reseller-info',
                        'username': username
                }
                return self.sQuery(**data)

        def listResellers(self):
                """Lists all resellers.
                http://docs.solusvm.com/v2/Content/Developer/Admin-Api/Client-Functions/Reseller-List.htm -

                :returns: json formatted string
                """
                data = {'action':'reseller-list'}
                return self.sQuery(**data)

        def createReseller(self, **data):
                """Creates reseller.
                http://docs.solusvm.com/v2/Content/Developer/Admin-Api/Client-Functions/Create-Reseller.htm -

                :param data: dictionary paramater pairs
                :returns: json formatted string
                """
                data['action'] = 'reseller-create'
                return self.sQuery(**data)

        def modifyResellerResources(self, username, **data):
                """Modifies reseller's available resources.
                http://docs.solusvm.com/v2/Content/Developer/Admin-Api/Client-Functions/Reseller-Modify-Resources.htm -

                :param username:
                :param data: dictionary paramater pairs
                :returns: json formatted string
                """
                data = data.update({
                        'action': 'reseller-modifyresources',
                        'username': username
                })
                return self.sQuery(**data)
