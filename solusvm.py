import requests

class SolusVM:
        def __init__(self, url, api_id, api_key):
                self.url = url
                self.id = api_id
                self.key = api_key

        def sQuery(self, **kwargs):
                """
                Queries specified SolusVM API with specified query string.

                Arguments
                ---
                data:dict - name:value get paramter pairs.

                Returns JSON response from server
                """
                kwargs.update({'rdtype':'json','id':self.id,'key':self.key})
                response = requests.get('https://'+self.url+':5656/api/admin/command.php', params=kwargs, timeout=2)
                return response.text

        def listVirtualServers(self, nodeid):
                """
                Lists virtual servers allocated on specified node.

                Arguments
                ---
                nodeid:str              [id of node]

                Returns JSON
                ---
                <status>success|error</status>
                <statusmsg>MSG</statusmsg>
        			<virtualservers>
				 <virtualserver>                              
				  <vserverid>[vserverid]</vserverid>
				  <ctid-xid>[ctid or xen id]</ctid-xid>
				  <clientid>[clientid]</clientid>
				  <ipaddress>[main ipaddress]</ipaddress>
				  <hostname>[hostname]</hostname>
				  <template>[template]</template>
				  <hdd>[diskspace]</hdd>
				  <memory>[memory]</memory>
				  <swap-burst>[swp or burst memory]</swap-burst>
				  <type>[openvz/xen/xenhvm]</type>
				  <mac>[mac address]</mac>
				 </virtualserver>
				</virtualservers>
                """
                data = {
                	'action': 'node-virtualservers', 
                	'nodeid': nodeid
                }
                return self.sQuery(**data)

        def diablePXE(self, vserverid):
                """
                Disables PXE on specified virtual server.

                Arguments
                ---
                vserverid:str           [id of virtual server]

                Returns JSON
                ---
                <status>success|error</status>
                <statusmsg>MSG</statusmsg>
                """
                data = {
                	'action': 'vserver-network-disable', 
                	'vserverid': vserverid
                }
                return self.sQuery(**data)

        def enablePXE(self, vserverid):
                """
                Enables PXE on specified virtual server.

                Arguments
                ---
                vserverid:str           [id of virtual server]

                Returns JSON
                ---
                <status>success|error</status>
                <statusmsg>MSG</statusmsg>
                """
                data = {
                	'action': 'vserver-network-enable', 
                	'vserverid': vserverid
                }
                return self.sQuery(**data)

        def enableTUN(self, vserverid):
                """
                Enables TUN/TAP on specified virtual server.

                Arguments
                ---
                vserverid:str           [id of virtual server]

                Returns JSON
                ---
                <status>success|error</status>
                <statusmsg>MSG</statusmsg>
                """
                data = {
                	'action': 'vserver-tun-enable', 
                	'vserverid': vserverid
                }
                return self.sQuery(**data)

        def disableTUN(self, vserverid):
                """
                Disables TUN/TAP on specified virtual server.

                Arguments
                ---
                vserverid:str           [id of virtual server]

                Returns JSON
                ---
                <status>success|error</status>
                <statusmsg>MSG</statusmsg>
                """
                data = {
                	'action': 'vserver-tun-disable', 
                	'vserverid': vserverid
                }
                return self.sQuery(**data)

        def togglePAE(self, vserverid, pae):
                """
                Toggles PAE for specified virtual server.

                Arguments
                ---
                vserverid:str           [id of virtual server]
                pae:str                         [on|off]

                Returns JSON
                ---
                <status>success|error</status>
                <statusmsg>MSG</statusmsg>
                """
                data = {
                	'action': 'vserver-pae', 
                	'vserverid': vserverid, 
                	'pae':pae
                }
                return self.sQuery(**data)

        def shutdownVirtualServer(self, vserverid):
                """
                Shuts down specified virtual server.

                Arguments
                ---
                vserverid:str           [id of virtual server]

                Returns JSON
                ---
                <status>success|error</status>
                <statusmsg>MSG</statusmsg>
                """
                data = {
                	'action': 'vserver-shutdown', 
                	'vserverid': vserverid
                }
                return self.sQuery(**data)

        def terminateVirtualServer(self, vserverid, deleteclient=False):
                """
                Deletes specified virtual server.

                Arguments
                ---
                vserverid:str           [id of virtual server]
                deleteclient:bool       [whether or not to delete client too]

                Returns JSON
                ---
                <status>success|error</status>
                <statusmsg>MSG</statusmsg>
                """
                data = {
                	'action': 'vserver-terminate', 
                	'vserverid': vserverid, 
                	'deleteclient': deleteclient
                }
                return self.sQuery(**data)

        def changeVNCPassword(self, vserverid, vncpassword):
                """
                Updates VNC password for specified virtual server.

                Arguments
                ---
                vserverid:str           [id of virtual server]
                vncpassword:str         [new password]

                Returns JSON
                ---
                <status>success|error</status>
                <statusmsg>MSG</statusmsg>
                <vncpassword />
                """
                data = {
                	'action': 'vserver-vncpass', 
                	'vserverid': vserverid, 
                	'vncpassword': vncpassword
                }
                return self.sQuery(**data)

        def vncInfo(self, vserverid):
                """
                Retrieves VNC information for specified virtual server.

                Arguments
                ---
                vserverid:str           [id of virtual server]

                Returns JSON
                ---
                <status>success|error</status>
                <statusmsg>MSG</statusmsg>
                type:str
                vncip:str
                vncport:str
                vncpassword:str
                """
                data = {
                	'action': 'vserver-vnc', 
                	'vserverid': vserverid
                }
                return self.sQuery(**data)

        def suspendVirtualServer(self, vserverid):
                """
                Suspends specified virtual server.

                Arguments
                ---
                vserverid:str           [id of virtual server]

                Returns JSON
                ---
                <status>success|error</status>
                <statusmsg>MSG</statusmsg>
                """
                data = {
                	'action': 'vserver-suspend', 
                	'vserverid':vserverid
                }
                return self.sQuery(**data)

        def unsuspendVirtualServer(self, vserverid):
                """
                Unsuspends specified virtual server.

                Arguments
                ---
                vserverid:str           [id of virtual server]

                Returns JSON
                ---
                <status>success|error</status>
                <statusmsg>MSG</statusmsg>
                """
                data = {
                	'action': 'vserver-unsuspend', 
                	'vserverid': vserverid
                }
                return self.sQuery(**data)

        def virtualServerStatus(self, vserverid):
                """
                Retrieves status of specified virtual server.

                Arguments
                ---
                vserverid:str           [id of virtual server]

                Returns JSON
                ---
                <status>success|error</status>
                <statusmsg>MSG</statusmsg>
                """
                data = {
                	'action': 'vserver-status', 
                	'vserverid': vserverid
                }
                return self.sQuery(**data)

        def changeRootPassword(self, vserverid, rootpassword):
                """
                Retrieves status of specified virtual server.

                Arguments
                ---
                vserverid:str           [id of virtual server]
                rootpassword:str        [new root password]

                Returns JSON
                ---
                <status>success|error</status>
                <statusmsg>MSG</statusmsg>
                rootpassword:str
                """
                data = {
                	'action': 'vserver-rootpassword', 
                	'vserverid': vserverid,
                	'rootpassword': rootpassword
                }
                return self.sQuery(**data)

        def rebuildVirtualServer(self, vserverid, template):
                """
                Rebuilds specified virtual server with specified template.

                Arguments
                ---
                vserverid:str           [id of virtual server]
                template:str            [template filename without extension]

                Returns JSON
                ---
                <status>success|error</status>
                <statusmsg>MSG</statusmsg>
                """
                data = {
                	'action': 'vserver-rebuild', 
                	'vserverid': vserverid,
                	'template': template
                }
                return self.sQuery(**data)

        def changeHostname(self, vserverid, hostname):
                """
                Updates specified virtual server's hostname.

                Arguments
                ---
                vserverid:str           [id of virtual server]
                hostname:str            [new hostname]

                Returns JSON
                ---
                <status>success|error</status>
                <statusmsg>MSG</statusmsg>
                hostname:str
                """
                data = {
                	'action': 'vserver-hostname', 
                	'vserverid': vserverid,
                	'hostname': hostname
                }
                return self.sQuery(**data)

        def rebootVirtualServer(self, vserverid):
                """
                Reboots specified virtual server.

                Arguments
                ---
                vserverid:str           [id of virtual server]

                Returns JSON
                ---
                <status>success|error</status>
                <statusmsg>MSG</statusmsg>
                """
                data = {
                	'action': 'vserver-reboot', 
                	'vserverid': vserverid
                }
                return self.sQuery(**data)

        def unmountISO(self, vserverid):
                """
                Unmounts ISO from specified virtual server.

                Arguments
                ---
                vserverid:str           [id of virtual server]

                Returns JSON
                ---
                <status>success|error</status>
                <statusmsg>MSG</statusmsg>
                """
                data = {
                	'action': 'vserver-reboot', 
                	'vserverid': vserverid
                }
                return self.sQuery(**data)

        def mountISO(self, vserverid, iso):
                """
                Mounts specified ISO to specified virtual server.

                Arguments
                ---
                vserverid:str           [id of virtual server]
                iso:str                         [filename of iso]

                Returns JSON
                ---
                <status>success|error</status>
                <statusmsg>MSG</statusmsg>
                """
                data = {
                	'action': 'vserver-mountiso', 
                	'vserverid': vserverid, 
                	'iso': iso
                }
                return self.sQuery(**data)

        def checkVirtualServerExists(self, vserverid):
                """
                Checks if specified virtual server exists.

                Arguments
                ---
                vserverid:str           [id of virtual server]

                Returns JSON
                ---
                <status>success|error</status>
                <statusmsg>MSG</statusmsg>
                """
                data = {
                	'action': 'vserver-checkexists', 
                	'vserverid': vserverid
                }
                return self.sQuery(**data)

        def virtualServerState(self, vserverid, nostatus=False, nographs=False):
                """
                Retrieves information about specified virtual server.

                Arguments
                ---
                vserverid:str           [id of virtual server]
                nostatus:bool           [whether or not to retrieve status]
                nographs:bool           [whether or not to generate graphs]

                Returns JSON
                ---
                <status>success|error</status>
                <statusmsg>MSG</statusmsg>
                state:str                       [online|offline|disabled]
                ipaddresses:csv         [ip1,ip2,ip3]
                mainipaddress:str       [main ip address]
                type:str                        [openvz|xen|xenhvm|kvm]
                trafficgraph:str        [path to graph]
                loadgraph:str           [path to graph]
                memorygraph:str         [path to graph]
                node:str                        [name of node]
                hdd:csv                         [total, used, free, percent used]
                bandwidth:csv           [total, used, free, percent used]
                memory:csv                      [total, used, free, percent used]
                internalips:str         [internal ip address]
                """
                data = {
                	'action': 'vserver-infoall', 
                	'vserverid': vserverid, 
                	'nostatus': nostatus, 
                	'nographs': nographs
                }
                return self.sQuery(**data)

        def virtualServerInfo(self, vserverid):
                """
                Retrieves information about specified virtual server.

                Arguments
                ---
                vserverid:str           [id of virtual server]

                Returns JSON
                ---
                <status>success|error</status>
                <statusmsg>MSG</statusmsg>
                vserverid:str
                ctid-xid:str
                clientid:str
                ipaddress:str
                hostname:str
                template:str
                hdd:str                         [diskspace]
                memory:str
                swap-burst:str
                type:str
                mac:str
                """
                data = {
                	'action': 'vserver-info', 
                	'vserverid': vserverid
                }
                return self.sQuery(**data)

        def deleteIPAddress(self, vserverid, ipaddr):
                """
                Removes specified IP Address from specified virtual server.

                Arguments
                ---
                vserverid:str           [id of virtual server]
                ipaddr:str                      [ip address]

                Returns JSON
                ---
                <status>success|error</status>
                <statusmsg>MSG</statusmsg>
                """
                data = {
                	'action': 'vserver-delip', 
                	'vserverid': vserverid, 
                	'ipaddr':ipaddr
                }
                return self.sQuery(**data)

        def toggleSerialConsole(self, vserverid, access=None, time=None):
                """
                Retrieves, enables or disables serial console for specified virtual server.

                Arguments
                ---
                vserverid:str           [id of virtual server]
                *access:str             [enable|disable]
                *time:str                       [1|2|3|4|5|6|7|8]

                Returns JSON
                ---
                <status>success|error</status>
                <statusmsg>MSG</statusmsg>
                created:str
                type:str
                consoleip:str
                consoleport:str
                consolepassword:str
                consoleusername:str
                cancelled:str
                sessionactive:str
                sessionexpire:int
                """
                data = {
                	'action': 'vserver-console', 
                	'vserverid': vserverid, 
                	'time': time, 
                	'access': access
                }
                return self.sQuery(**data)

        def changePlan(self, vserverid, plan):
                """
                Changes specified virtual server's plan.

                Arguments
                ---
                vserverid:str           [id of virtual server]
                plan:str                        [new plan name]

                Returns JSON
                ---
                <status>success|error</status>
                <statusmsg>MSG</statusmsg>
                """
                data = {
                	'action': 'vserver-change', 
                	'vserverid': vserverid, 
                	'plan':plan
                }
                return self.sQuery(**data)

        def changeOwner(self, vserverid, clientid):
                """
                Changes specified virtual server's owner.

                Arguments
                ---
                vserverid:str           [id of virtual server]
                clientid:str            [new clients id]

                Returns JSON
                ---
                <status>success|error</status>
                <statusmsg>MSG</statusmsg>
                """
                data = {
                	'action': 'vserver-changeowner', 
                	'vserverid': vserverid, 
                	'clientid': clientid
                }
                return self.sQuery(**data)

        def changeBootOrder(self, vserverid, bootorder):
                """
                Changes specified virtual server's boot order.

                Arguments
                ---
                vserverid:str           [id of virtual server]
                bootorder:str           [cd|dc|c|d]

                Returns JSON
                ---
                <status>success|error</status>
                <statusmsg>MSG</statusmsg>
                """
                data = {
                	'action': 'vserver-bootorder', 
                	'vserverid': vserverid, 
                	'bootorder': bootorder
                }
                return self.sQuery(**data)

        def addIPAddress(self, vserverid):
                """
                Adds an IP address to specified virtual server.

                Arguments
                ---
                vserverid:str           [id of virtual server]

                Returns JSON
                  ---
                <status>success|error</status>
                <statusmsg>MSG</statusmsg>
                ipaddress:str
                """
                data = {
                	'action': 'vserver-addip', 
                	'vserverid': vserverid
                }
                return self.sQuery(**data)

        def bootVirtualServer(self, vserverid):
                """
                Boots specified virtual server.

                Arguments
                ---
                vserverid:str           [id of virtual server]

                Returns JSON
                ---
                <status>success|error</status>
                <statusmsg>MSG</statusmsg>
                """
                data = {
                	'action': 'vserver-boot', 
                	'vserverid': vserverid
                }
                return self.sQuery(**data)

        def createVirtualServer(self, vtype, node, nodegroup, hostname, password, username, plan, template, ips,
                        hvmt=None, custommemory=None, customdiskspace=None, custombandwidth=None, customcpu=None,
                        customextraip=0,issuelicense=None,internalip=None):
                """
                Boots specified virtual server.

                Arguments
                ---
                vtype                   [openvz|xen|xen hvm|kvm]
                node                     [name of node]
                nodegroup                [name of nodegroup]
                hostname                 [hostname of virtual server]
                password                 [root password]
                username                 [client username]
                plan                     [plan name]
                template                 [template or iso name]
                ips                     [amount of ips]
                hvmt                    [0|1] default is 0. This allows to to define templates & isos for Xen HVM
                custommemory            [overide plan memory with this amount]
                customdiskspace         [overide plan diskspace with this amount]
                custombandwidth         [overide plan bandwidth with this amount]
                customcpu               [overide plan cpu cores with this amount]
                customextraip           [add this amount of extra ips]
                issuelicense            [1|2] 1 = cPanel monthly 2= cPanel yearly
                internalip              [0|1] default is 0

                Returns JSON
                ---
                <status>success|error</status>
                <statusmsg>MSG</statusmsg>
                mainipaddress:str
                extraipaddress:csv
                rootpassword:str
                vserverid:str
                consoleuser:str
                consolepassword:str
                hostname:str
                virtid:str
                nodeid:str
                """
                data = {
                        'action': 'vserver-create', 
                        'type': vtype, 
                        'node': node, 
                        'nodegroup': nodegroup, 
                        'hostname': hostname, 
                        'password': password,
                        'username': username, 
                        'plan': plan, 
                        'template': template, 
                        'ips': ips, 
                        'hvmt': hvmt, 
                        'custommemory': custommemory,
                        'customdiskspace': customdiskspace, 
                        'custombandwidth': custombandwidth, 
                        'customcpu': customcpu, 
                        'customextraip': customextraip,
                        'issuelicense': issuelicense, 
                        'internalip': internalip
                }
                return self.sQuery(**data)

        def listNodesById(self, vtype='kvm'):
                """
                Lists Nodes by their ID.

                Arguments
                ---
                vtype:str               [openvz|xen|xen hvm|kvm]

                Returns JSON
                ---
                <status>success|error</status>
                <statusmsg>MSG</statusmsg>
                nodes:str                       [nodeid,nodeid,nodeid]
                """
                data = {
                	'action': 'node-idlist', 
                	'type': vtype
                }
                return self.sQuery(**data)

        def listNodesByName(self, vtype='kvm'):
                """
                List nodes by name.

                Arguments
                ---
                vtype:str               [openvz|xen|xen hvm|kvm]

                Returns JSON
                ---
                <status>success|error</status>
                <statusmsg>MSG</statusmsg>
                nodes:str                       [node1,node2,node3]
                """
                data = {
                	'action': 'listnodes', 
                	'type': vtype}
                return self.sQuery(**data)

        def listISO(self, vtype='kvm'):
                """
                Lists available ISO images.

                Arguments
                ---
                vtype:str               [xen hvm|kvm]

                Returns JSON
                ---
                <status>success|error</status>
                <statusmsg>MSG</statusmsg>
                iso:str                         [iso1,iso2,iso3]
                """
                data = {
                	'action': 'listiso', 
                	'type': vtype
                }
                return self.sQuery(**data)

        def listNodeGroups(self, vtype='kvm'):
                """
                List node groups.

                Arguments
                ---
                vtype:str               [xen hvm|kvm]

                Returns JSON
                ---
                <status>success|error</status>
                <statusmsg>MSG</statusmsg>
                nodegroups:str          [0|--none--,1|nodegroup1,2|nodegroup2,3|nodegroup3]
                """
                data = {
                	'action': 'listnodegroups', 
                	'type': vtype
                }
                return self.sQuery(**data)

        def listNodesByName(self, nodeid):
                """
                List nodes by name.

                Arguments
                ---
                nodeid:int              [id of node]

                Returns JSON
                ---
                <status>success|error</status>
                <statusmsg>MSG</statusmsg>
                ipcount:str
                ips:str                         [ip1,ip2,ip3]
                """
                data = {
                	'action': 'node-iplist', 
                	'nodeid': nodeid
                }
                return self.sQuery(**data)

        def listPlans(self, vtype='kvm'):
                """
                List plans.

                Arguments
                ---
                vtype:str               [openvz|xen|xen hvm|kvm]

                Returns JSON
                ---
                <status>success|error</status>
                <statusmsg>MSG</statusmsg>
                plans:str                       [plan1,plan2,plan3]
                """
                data = {
                	'action': 'listplans',
                	'type': vtype
                }
                return self.sQuery(**data)

        def listTemplates(self, vtype='kvm'):
                """
                List templates.

                Arguments
                ---
                vtype:str               [openvz|xen|xen hvm|kvm]

                Returns JSON
                ---
                <status>success|error</status>
                <statusmsg>MSG</statusmsg>
                templates:str           [template1,template2,template3]
                templateshvm:str        [template1,template2,template3]
                templatekvm:str         [template1,template2,template3]
                """
                data = {
                	'action': 'listtemplates',
                	'type': vtype
                }
                return self.sQuery(**data)

        def xenNodeResources(self, nodeid):
                """
                Retrieve resource count from specified xen node.

                Arguments
                ---
                nodeid:str              [id of node]

                Returns JSON
                ---
                <status>success|error</status>
                <statusmsg>MSG</statusmsg>
                freememory:str
                freehdd:str
                """
                data = {
                	'action': 'node-xenresources',
                	'nodeid': nodeid
                }
                return self.sQuery(**data)

        def nodeStatistics(self, nodeid):
                """
                Retrieve statistics for specified node.

                Arguments
                ---
                nodeid:str              [node id or name]

                Returns JSON
                ---
                <status>success|error</status>
                <statusmsg>MSG</statusmsg>
                id:str
                name:str
                ip:str
                memorylimit:int
                disklimit:int
                hostname:str
                country:str
                city:str
                sshport:str
                arch:str
                freememory:str
                allocatedmemory:int
                allocatedbandwidth:int
                freedisk:str
                virtualservers:int
                freeips:int
                """
                data = {
                	'action': 'node-statistics',
                	'nodeid': nodeid
                }
                return self.sQuery(**data)

        def clientAuthenticate(self, username, password):
                """
                Authenticates specified username and password.

                Arguments
                ---
                username:str
                password:str

                Returns JSON
                ---
                <status>success|error</status>
                <statusmsg>MSG</statusmsg>           [validated|invalid username or password]
                """
                data = {
                	'action': 'client-authenticate',
                	'username': username,
                	'password': password
                }
                return self.sQuery(**data)

        def clientExists(self, username):
                """
                Checks to see if the specified client exists.

                Arguments
                ---
                username:str

                Returns JSON
                ---
                <status>success|error</status>
                <statusmsg>MSG</statusmsg>           [Client exists|*error message*]
                """
                data = {
                	'action': 'client-checkexists',
                	'username': username
                }
                return self.sQuery(**data)

        def createClient(self, username, password, email, firstname, lastname, company):
                """
                Creates a client.

                Arguments
                ---
                username:str
                password:str
                email:str
                firstname:str
                lastname:str
                company:str

                Returns JSON
                ---
                <status>success|error</status>
                <statusmsg>MSG</statusmsg>
                username:str
                password:str
                email:str
                firstname:str
                lastname:str
                company:str
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
                """
                Updates the specified client's password.

                Arguments
                ---
                username:str
                password:str

                Returns JSON
                ---
                <status>success|error</status>
                <statusmsg>MSG</statusmsg>
                username:str
                password:str
                """
                data = {
                	'action': 'client-updatepassword',
                	'username': username,
                	'password': password
                }
                return self.sQuery(**data)

        def listClients(self):
                """
                Lists all clients.

                Returns JSON
                ---
                <status>success|error</status>
                <statusmsg>MSG</statusmsg>
                clients
                -id:str
                -username:str
                -email:str
                -firstname:str
                -lastname:str
                -company:str
                -level:str
                -status:str
                -created:str
                -lastlogin:str
                """
                data = {'action':'client-list'}
                return self.sQuery(**data)

        def deleteClient(self, username):
                """
                Deletes specified client.

                Arguments
                ---
                username:str

                Returns JSON
                ---
                <status>success|error</status>
                <statusmsg>MSG</statusmsg>
                """
                data = {
                	'action': 'client-delete',
                	'username': username
                }
                return self.sQuery(**data)

        def deleteReseller(self, username):
                """
                Deletes specified reseller.

                Arguments
                ---
                username:str

                Returns JSON
                ---
                <status>success|error</status>
                <statusmsg>MSG</statusmsg>
                """
                data = {
                	'action': 'reseller-delete',
                	'username': username
                }
                return self.sQuery(**data)

        def resellerInfo(self, username):
                """
                Retrieves details of specified reseller.

                Arguments
                ---
                username:str

                Returns JSON
                ---
                <status>success|error</status>
                <statusmsg>MSG</statusmsg>
                username:str
                email:str
                firstname:str
                lastname:str
                company:str
                usernamprefix:str
                maxvps:str
                maxdisk:str
                maxmem:str
                maxusers:str
                maxipv4:str
                maxipv6
                maxburst:str
                maxbw:str
                nodegroupids:str
                mediagroupids:str
                xenpv:str
                xenhvm:str
                kvm:str
                openvz:str
                """
                data = {
                	'action': 'reseller-info',
                	'username': username
                }
                return self.sQuery(**data)

        def listResellers(self):
                """
                Lists all resellers.

                Returns JSON
                ---
                <status>success|error</status>
                <statusmsg>MSG</statusmsg>
                usernames                       [username1,username2,username3]
                """
                data = {'action':'reseller-list'}
                return self.sQuery(**data)

        def createReseller(self, username, password, email, firstname, lastname, company, **data):
                """
                Creates reseller.

                Arguments
                ---
                username:str
                password:str
                email:str
                firstname:str
                lastname:str
                company:str
                *usernameprefix:str
                *maxvps:str
                *maxusers:str
                *maxmem:str
                *maxburst:str
                *maxdisk:str
                *maxbw:str
                *maxipv4:str
                *maxipv6:str
                *nodegroup:csv
                *mediagroups:csv
                *openvz:bool
                *xenpv:bool
                *xenhvm:bool
                *kvm:bool

                Returns JSON
                ---
                <status>success|error</status>
                <statusmsg>MSG</statusmsg>
                username:str
                email:str
                firstname:str
                lastname:str
                company:str
                *usernamprefix:str
                *maxvps:str
                *maxdisk:str
                *maxmem:str
                *maxusers:str
                *maxipv4:str
                *maxipv6
                *maxburst:str
                *maxbw:str
                *nodegroupids:str
                *mediagroupids:str
                *xenpv:str
                *xenhvm:str
                *kvm:str
                *openvz:str
                """
                data = data.update({
                	'action': 'reseller-create',
                	'username': username,
                	'password': password,
                	'email': email,
                	'firstname': firstname,
                	'lastname': lastname,
                	'company': company
                })
                return self.sQuery(**data)

        def modifyResellerResources(self, username, **data):
                """
                Creates reseller.

                Arguments
                ---
                username:str
                *maxvps:str
                *maxusers:str
                *maxmem:str
                *maxburst:str
                *maxdisk:str
                *maxbw:str
                *maxipv4:str
                *maxipv6:str
                *nodegroup:csv
                *mediagroups:csv
                *openvz:bool
                *xenpv:bool
                *xenhvm:bool
                *kvm:bool

                Returns JSON
                ---
                <status>success|error</status>
                <statusmsg>MSG</statusmsg>
                username:str
                *maxvps:str
                *maxdisk:str
                *maxmem:str
                *maxusers:str
                *maxipv4:str
                *maxipv6
                *maxburst:str
                *maxbw:str
                *nodegroupids:str
                *mediagroupids:str
                *xenpv:str
                *xenhvm:str
                *kvm:str
                *openvz:str
                """
                data = data.update({
                	'action': 'reseller-modifyresources',
                	'username': username
                })
                return self.sQuery(**data)
