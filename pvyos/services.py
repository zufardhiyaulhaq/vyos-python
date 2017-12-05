import router

class services(router.vyos):

    def __init__(self,ipaddr,username,password):
        super().__init__(ipaddr,username,password)

    def ssh(self):

        if (self.session == None):
            return False
        else:
            session = self.session

        session.sendline("set service ssh")

    def telnet(self):

        if (self.session == None):
            return False
        else:
            session = self.session

        session.sendline("set service telnet")

    def dnsforwarder(self,ipdns):
       
        if (self.session == None):
            return False
        else:
            session = self.session
        
        session.sendline("set service dns forwarding name-server %s"&(ipdns))

