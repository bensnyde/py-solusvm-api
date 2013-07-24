import requests

class SolusVM:
        def __init__(self, url, api_id, api_key):
                self.url = url
                self.id = api_id
                self.key = api_key

        def sQuery(self, args):
                """
                Queries specified SolusVM API with specified query string.

                Arguments
                ---
                args:dict - name:value get paramter pairs.

                Returns JSON response from server
                """
                args.update({'rdtype':'json','id':self.id,'key':self.key})
                r = requests.get('https://'+self.url+':5656/api/admin/command.php', params=args, timeout=2)
                return r.text

        def listVirtualServers(self, nodeid):
                """
                Lists virtual servers allocated on specified node.

                Arguments
                ---
                nodeid:str              [id of node]

                Returns JSON
                ---
                status:str              [success|error]
                statusmsg:str
                virtualservers
                -vserverid:str
                -ctid:str
                -clientid:str
                -ipaddress:str
                -hostname:str
                -template:str
                -hdd:str
                -memory:str
                -swap-burst:str
                -type:str
                -mac:str
                """
                args = {'action':'node-virtualservers', 'nodeid':nodeid}
                return self.sQuery(args)

        def diablePXE(self, vserverid):
                """
                Disables PXE on specified virtual server.

                Arguments
                ---
                vserverid:str           [id of virtual server]

                Returns JSON
                ---
                status:str              [success|error]
                statusmsg:str
                """
                args = {'action':'vserver-network-disable', 'vserverid':vserverid}
                return self.sQuery(args)

        def enablePXE(self, vserverid):
                """
                Enables PXE on specified virtual server.

                Arguments
                ---
                vserverid:str           [id of virtual server]

                Returns JSON
                ---
                status:str              [success|error]
                statusmsg:str
                """
                args = {'action':'vserver-network-enable', 'vserverid':vserverid}
                return self.sQuery(args)

        def enableTUN(self, vserverid):
                """
                Enables TUN/TAP on specified virtual server.

                Arguments
                ---
                vserverid:str           [id of virtual server]

                Returns JSON
                ---
                status:str              [success|error]
                statusmsg:str
                """
                args = {'action':'vserver-tun-enable', 'vserverid':vserverid}
                return self.sQuery(args)

        def disableTUN(self, vserverid):
                """
                Disables TUN/TAP on specified virtual server.

                Arguments
                ---
                vserverid:str           [id of virtual server]

                Returns JSON
                ---
                status:str              [success|error]
                statusmsg:str
                """
                args = {'action':'vserver-tun-disable', 'vserverid':vserverid}
                return self.sQuery(args)

        def togglePAE(self, vserverid, pae):
                """
                Toggles PAE for specified virtual server.

                Arguments
                ---
                vserverid:str           [id of virtual server]
                pae:str                         [on|off]

                Returns JSON
                ---
                status:str              [success|error]
                statusmsg:str
                """
                args = {'action':'vserver-pae', 'vserverid':vserverid, 'pae':pae}
                return self.sQuery(args)

        def shutdownVirtualServer(self, vserverid):
                """
                Shuts down specified virtual server.

                Arguments
                ---
                vserverid:str           [id of virtual server]

                Returns JSON
                ---
                status:str              [success|error]
                statusmsg:str
                """
                args = {'action':'vserver-shutdown', 'vserverid':vserverid}
                return self.sQuery(args)

        def terminateVirtualServer(self, vserverid, deleteclient=False):
                """
                Deletes specified virtual server.

                Arguments
                ---
                vserverid:str           [id of virtual server]
                deleteclient:bool       [whether or not to delete client too]

                Returns JSON
                ---
                status:str              [success|error]
                statusmsg:str
                """
                args = {'action':'vserver-terminate', 'vserverid':vserverid, 'deleteclient':deleteclient}
                return self.sQuery(args)

        def changeVNCPassword(self, vserverid, vncpassword):
                """
                Updates VNC password for specified virtual server.

                Arguments
                ---
                vserverid:str           [id of virtual server]
                vncpassword:str         [new password]

                Returns JSON
                ---
                status:str              [success|error]
                statusmsg:str
                vncpassword:str
                """
                args = {'action':'vserver-vncpass', 'vserverid':vserverid, 'vncpassword':vncpassword}
                return self.sQuery(args)

        def vncInfo(self, vserverid):
                """
                Retrieves VNC information for specified virtual server.

                Arguments
                ---
                vserverid:str           [id of virtual server]

                Returns JSON
                ---
                status:str              [success|error]
                statusmsg:str
                type:str
                vncip:str
                vncport:str
                vncpassword:str
                """
                args = {'action':'vserver-vnc', 'vserverid':vserverid}
                return self.sQuery(args)

        def suspendVirtualServer(self, vserverid):
                """
                Suspends specified virtual server.

                Arguments
                ---
                vserverid:str           [id of virtual server]

                Returns JSON
                ---
                status:str              [success|error]
                statusmsg:str
                """
                args = {'action':'vserver-suspend', 'vserverid':vserverid}
                return self.sQuery(args)

        def unsuspendVirtualServer(self, vserverid):
                """
                Unsuspends specified virtual server.

                Arguments
                ---
                vserverid:str           [id of virtual server]

                Returns JSON
                ---
                status:str              [success|error]
                statusmsg:str
                """
                args = {'action':'vserver-unsuspend', 'vserverid':vserverid}
                return self.sQuery(args)

        def virtualServerStatus(self, vserverid):
                """
                Retrieves status of specified virtual server.

                Arguments
                ---
                vserverid:str           [id of virtual server]

                Returns JSON
                ---
                status:str              [success|error]
                statusmsg:str           [disabled|online|offline]
                """
                args = {'action':'vserver-status', 'vserverid':vserverid}
                return self.sQuery(args)

        def changeRootPassword(self, vserverid, rootpassword):
                """
                Retrieves status of specified virtual server.

                Arguments
                ---
                vserverid:str           [id of virtual server]
                rootpassword:str        [new root password]

                Returns JSON
                ---
                status:str              [success|error]
                statusmsg:str
                rootpassword:str
                """
                args = {'action':'vserver-rootpassword', 'vserverid':vserverid,'rootpassword':rootpassword}
                return self.sQuery(args)

        def rebuildVirtualServer(self, vserverid, template):
                """
                Rebuilds specified virtual server with specified template.

                Arguments
                ---
                vserverid:str           [id of virtual server]
                template:str            [template filename without extension]

                Returns JSON
                ---
                status:str              [success|error]
                statusmsg:str
                """
                args = {'action':'vserver-rebuild', 'vserverid':vserverid,'template':template}
                return self.sQuery(args)

        def changeHostname(self, vserverid, hostname):
                """
                Updates specified virtual server's hostname.

                Arguments
                ---
                vserverid:str           [id of virtual server]
                hostname:str            [new hostname]

                Returns JSON
                ---
                status:str              [success|error]
                statusmsg:str
                hostname:str
                """
                args = {'action':'vserver-hostname', 'vserverid':vserverid,'hostname':hostname}
                return self.sQuery(args)

        def rebootVirtualServer(self, vserverid):
                """
                Reboots specified virtual server.

                Arguments
                ---
                vserverid:str           [id of virtual server]

                Returns JSON
                ---
                status:str              [success|error]
                statusmsg:str
                """
                args = {'action':'vserver-reboot', 'vserverid':vserverid}
                return self.sQuery(args)

        def unmountISO(self, vserverid):
                """
                Unmounts ISO from specified virtual server.

                Arguments
                ---
                vserverid:str           [id of virtual server]

                Returns JSON
                ---
                status:str              [success|error]
                statusmsg:str
                """
                args = {'action':'vserver-reboot', 'vserverid':vserverid}
                return self.sQuery(args)

        def mountISO(self, vserverid, iso):
                """
                Mounts specified ISO to specified virtual server.

                Arguments
                ---
                vserverid:str           [id of virtual server]
                iso:str                         [filename of iso]

                Returns JSON
                ---
                status:str              [success|error]
                statusmsg:str
                """
                args = {'action':'vserver-mountiso', 'vserverid':vserverid, 'iso':iso}
                return self.sQuery(args)

        def checkVirtualServerExists(self, vserverid):
                """
                Checks if specified virtual server exists.

                Arguments
                ---
                vserverid:str           [id of virtual server]

                Returns JSON
                ---
                status:str              [success|error]
                statusmsg:str
                """
                args = {'action':'vserver-checkexists', 'vserverid':vserverid}
                return self.sQuery(args)

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
                status:str              [success|error]
                statusmsg:str
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
                args = {'action':'vserver-infoall', 'vserverid':vserverid, 'nostatus':nostatus, 'nographs':nographs}
                return self.sQuery(args)

        def virtualServerInfo(self, vserverid):
                """
                Retrieves information about specified virtual server.

                Arguments
                ---
                vserverid:str           [id of virtual server]

                Returns JSON
                ---
                status:str              [success|error]
                statusmsg:str
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
                args = {'action':'vserver-info', 'vserverid':vserverid}
                return self.sQuery(args)

        def deleteIPAddress(self, vserverid, ipaddr):
                """
                Removes specified IP Address from specified virtual server.

                Arguments
                ---
                vserverid:str           [id of virtual server]
                ipaddr:str                      [ip address]

                Returns JSON
                ---
                status:str              [success|error]
                statusmsg:str
                """
                args = {'action':'vserver-delip', 'vserverid':vserverid, 'ipaddr':ipaddr}
                return self.sQuery(args)

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
                status:str              [success|error]
                statusmsg:str
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
                args = {'action':'vserver-console', 'vserverid':vserverid, 'time':time, 'access':access}
                return self.sQuery(args)

        def changePlan(self, vserverid, plan):
                """
                Changes specified virtual server's plan.

                Arguments
                ---
                vserverid:str           [id of virtual server]
                plan:str                        [new plan name]

                Returns JSON
                ---
                status:str              [success|error]
                statusmsg:str
                """
                args = {'action':'vserver-change', 'vserverid':vserverid, 'plan':plan}
                return self.sQuery(args)

        def changeOwner(self, vserverid, clientid):
                """
                Changes specified virtual server's owner.

                Arguments
                ---
                vserverid:str           [id of virtual server]
                clientid:str            [new clients id]

                Returns JSON
                ---
                status:str              [success|error]
                statusmsg:str
                """
                args = {'action':'vserver-changeowner', 'vserverid':vserverid, 'clientid':clientid}
                return self.sQuery(args)

        def changeBootOrder(self, vserverid, bootorder):
                """
                Changes specified virtual server's boot order.

                Arguments
                ---
                vserverid:str           [id of virtual server]
                bootorder:str           [cd|dc|c|d]

                Returns JSON
                ---
                status:str              [success|error]
                statusmsg:str
                """
                args = {'action':'vserver-bootorder', 'vserverid':vserverid, 'bootorder':bootorder}
                return self.sQuery(args)

        def addIPAddress(self, vserverid):
                """
                Adds an IP address to specified virtual server.

                Arguments
                ---
                vserverid:str           [id of virtual server]

                Returns JSON
                ---
                status:str              [success|error]
                statusmsg:str
                ipaddress:str
                """
                args = {'action':'vserver-addip', 'vserverid':vserverid}
                return self.sQuery(args)

        def bootVirtualServer(self, vserverid):
                """
                Boots specified virtual server.

                Arguments
                ---
                vserverid:str           [id of virtual server]

                Returns JSON
                ---
                status:str              [success|error]
                statusmsg:str
                """
                args = {'action':'vserver-boot', 'vserverid':vserverid}
                return self.sQuery(args)

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
                status:str              [success|error]
                statusmsg:str
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
                args = {
                        'action':'vserver-create', 'type':vtype, 'node':node, 'nodegroup':nodegroup, 'hostname':hostname, 'password':password,
                        'username':username, 'plan':plan, 'template':template, 'ips':ips, 'hvmt':hvmt, 'custommemory':custommemory,
                        'customdiskspace':customdiskspace, 'custombandwidth':custombandwidth, 'customcpu':customcpu, 'customextraip':customextraip,
                        'issuelicense':issuelicense, 'internalip':internalip
                }
                return self.sQuery(args)

        def listNodesById(self, vtype='kvm'):
                """
                Lists Nodes by their ID.

                Arguments
                ---
                vtype:str               [openvz|xen|xen hvm|kvm]

                Returns JSON
                ---
                status:str              [success|error]
                statusmsg:str
                nodes:str                       [nodeid,nodeid,nodeid]
                """
                args = {'action':'node-idlist', 'type':vtype}
                return self.sQuery(args)

        def listNodesByName(self, vtype='kvm'):
                """
                List nodes by name.

                Arguments
                ---
                vtype:str               [openvz|xen|xen hvm|kvm]

                Returns JSON
                ---
                status:str              [success|error]
                statusmsg:str
                nodes:str                       [node1,node2,node3]
                """
                args = {'action':'listnodes', 'type':vtype}
                return self.sQuery(args)

        def listISO(self, vtype='kvm'):
                """
                Lists available ISO images.

                Arguments
                ---
                vtype:str               [xen hvm|kvm]

                Returns JSON
                ---
                status:str              [success|error]
                statusmsg:str
                iso:str                         [iso1,iso2,iso3]
                """
                args = {'action':'listiso', 'type':vtype}
                return self.sQuery(args)

        def listNodeGroups(self, vtype='kvm'):
                """
                List node groups.

                Arguments
                ---
                vtype:str               [xen hvm|kvm]

                Returns JSON
                ---
                status:str              [success|error]
                statusmsg:str
                nodegroups:str          [0|--none--,1|nodegroup1,2|nodegroup2,3|nodegroup3]
                """
                args = {'action':'listnodegroups', 'type':vtype}
                return self.sQuery(args)

        def listNodesByName(self, nodeid):
                """
                List nodes by name.

                Arguments
                ---
                nodeid:int              [id of node]

                Returns JSON
                ---
                status:str              [success|error]
                statusmsg:str
                ipcount:str
                ips:str                         [ip1,ip2,ip3]
                """
                args = {'action':'node-iplist', 'nodeid':nodeid}
                return self.sQuery(args)

        def listPlans(self, vtype='kvm'):
                """
                List plans.

                Arguments
                ---
                vtype:str               [openvz|xen|xen hvm|kvm]

                Returns JSON
                ---
                status:str              [success|error]
                statusmsg:str
                plans:str                       [plan1,plan2,plan3]
                """
                args = {'action':'listplans','type':vtype}
                return self.sQuery(args)

        def listTemplates(self, vtype='kvm'):
                """
                List templates.

                Arguments
                ---
                vtype:str               [openvz|xen|xen hvm|kvm]

                Returns JSON
                ---
                status:str              [success|error]
                statusmsg:str
                templates:str           [template1,template2,template3]
                templateshvm:str        [template1,template2,template3]
                templatekvm:str         [template1,template2,template3]
                """
                args = {'action':'listtemplates','type':vtype}
                return self.sQuery(args)

        def xenNodeResources(self, nodeid):
                """
                Retrieve resource count from specified xen node.

                Arguments
                ---
                nodeid:str              [id of node]

                Returns JSON
                ---
                status:str              [success|error]
                statusmsg:str
                freememory:str
                freehdd:str
                """
                args = {'action':'node-xenresources','nodeid':nodeid}
                return self.sQuery(args)

        def nodeStatistics(self, nodeid):
                """
                Retrieve statistics for specified node.

                Arguments
                ---
                nodeid:str              [node id or name]

                Returns JSON
                ---
                status:str              [success|error]
                statusmsg:str
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
                args = {'action':'node-statistics','nodeid':nodeid}
                return self.sQuery(args)

        def clientAuthenticate(self, username, password):
                """
                Authenticates specified username and password.

                Arguments
                ---
                username:str
                password:str

                Returns JSON
                ---
                status:str              [success|error]
                statusmsg:str           [validated|invalid username or password]
                """
                args = {'action':'client-authenticate','username':username,'password':password}
                return self.sQuery(args)

        def clientExists(self, username):
                """
                Checks to see if the specified client exists.

                Arguments
                ---
                username:str

                Returns JSON
                ---
                status:str              [success|error]
                statusmsg:str           [Client exists|*error message*]
                """
                args = {'action':'client-checkexists','username':username}
                return self.sQuery(args)

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
                status:str              [success|error]
                statusmsg:str
                username:str
                password:str
                email:str
                firstname:str
                lastname:str
                company:str
                """
                args = {'action':'client-create','username':username,'password':password,'email':email,'firstname':firstname,'lastname':lastname,'company':company}
                return self.sQuery(args)

        def changeClientPassword(self, username, password):
                """
                Updates the specified client's password.

                Arguments
                ---
                username:str
                password:str

                Returns JSON
                ---
                status:str              [success|error]
                statusmsg:str
                username:str
                password:str
                """
                args = {'action':'client-updatepassword','username':username,'password':password}
                return self.sQuery(args)

        def listClients(self):
                """
                Lists all clients.

                Returns JSON
                ---
                status:str              [success|error]
                statusmsg:str
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
                args = {'action':'client-list'}
                return self.sQuery(args)

        def deleteClient(self, username):
                """
                Deletes specified client.

                Arguments
                ---
                username:str

                Returns JSON
                ---
                status:str              [success|error]
                statusmsg:str
                """
                args = {'action':'client-delete','username':username}
                return self.sQuery(args)

        def deleteReseller(self, username):
                """
                Deletes specified reseller.

                Arguments
                ---
                username:str

                Returns JSON
                ---
                status:str              [success|error]
                statusmsg:str
                """
                args = {'action':'reseller-delete','username':username}
                return self.sQuery(args)

        def resellerInfo(self, username):
                """
                Retrieves details of specified reseller.

                Arguments
                ---
                username:str

                Returns JSON
                ---
                status:str              [success|error]
                statusmsg:str
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
                args = {'action':'reseller-info','username':username}
                return self.sQuery(args)

        def listResellers(self):
                """
                Lists all resellers.

                Returns JSON
                ---
                status:str              [success|error]
                statusmsg:str
                usernames                       [username1,username2,username3]
                """
                args = {'action':'reseller-list'}
                return self.sQuery(args)

        def createReseller(self, username, password, email, firstname, lastname, company, args=None):
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
                status:str              [success|error]
                statusmsg:str
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
                args = args.update({'action':'reseller-create','username':username,'password':password,'email':email,'firstname':firstname,'lastname':lastname,'company':company})
                return self.sQuery(args)

        def modifyResellerResources(self, username, args=None):
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
                status:str              [success|error]
                statusmsg:str
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
                args = args.update({'action':'reseller-modifyresources','username':username})
                return self.sQuery(args)
