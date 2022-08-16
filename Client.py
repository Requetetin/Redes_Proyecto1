import asyncio
from distutils.log import debug
import slixmpp
from slixmpp.stanza import Iq
from slixmpp.xmlstream.xmlstream import XMLStream
import xmpp
import threading
import time

# <stream:stream xmlns="jabber:client" version="1.0" xmlns:stream="http://etherx.jabber.org/streams" to="alumchat.fun" xml:lang="en"
# iq = Iq()
# iq['to'] = 'alumchat.fun'
# iq['type'] = 'set'
# print(iq)

#slixmpp.ClientXMPP()

class Client:
    def __init__(self, user:str , password:str) -> None:
        self.jid = xmpp.JID(user)
        self.password = password
        self.client = xmpp.Client(self.jid.getDomain(), debug=debug)
        self.client.connect()

    def signUp(self, user:str, password:str):
        jid = xmpp.JID(user)
        return xmpp.features.register(self.client, jid.getDomain(), {
        'username': jid.getNode(),
        'password': password,
        })

    def sendPresence(self):
        self.client.sendInitPresence()

        self.client.getRoster()

    def deletUser(self):
        return xmpp.features.unregister(self.client, self.jid.getDomain())

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
class SLIXClient(slixmpp.ClientXMPP):
    def __init__(self, jid: str, password: str, option: int, contact: str = "", message: str = "") -> None:
        slixmpp.ClientXMPP.__init__(self, jid, password)

        self.register_plugin('xep_0004')  # Data Forms
        self.register_plugin('xep_0030')  # Service Discovery
        self.register_plugin('xep_0045')  # Group Chat
        self.register_plugin('xep_0060')  # PubSub
        self.register_plugin('xep_0077')  # In Bound Registration
        self.register_plugin('xep_0092')  # Software version
        self.register_plugin('xep_0199')  # XMPP Ping
        self.register_plugin('xep_0249')  # Direct MUC Invitations
        
        self.option = option

        if option == 6 or option == 7:
            self.contact = contact

        if option == 8:
            self.contact = contact
            self.add_event_handler("message", self.chatting)


        if option == 10:
            self.newStatus = contact

        print('WAITING FOR SERVER START')
        self.add_event_handler("session_start", self.start_this)


    async def start_this(self, event):
        """
        Process the session_start event.

        Typical actions for the session_start event are
        requesting the roster and broadcasting an initial
        presence stanza.

        Arguments:
            event -- An empty dictionary. The session_start
                    event does not provide any additional
                    data.
        """
        print('SERVER STARTED')
        self.send_presence()
        await self.get_roster()

        if self.option == 4:
            print(self, 'BEING DELETED...')
            iq = self.Iq()
            iq['from'] = self.boundjid.user
            iq['type'] = 'set'
            iq.set_query('jabber:iq:register')
            iq['register']['remove'] = True

            await iq.send()
        if self.option == 5:
            users = self.client_roster
            for user in users:
                status = ''
                availability = ''
                for key, item in users.presence(user).items():
                    if item['status']:
                        status = item['status']
                    if item['show']:
                        availability = item['show']
                userList = """
                -----------------
                USER: {0}
                STATUS: {1}
                MESSAGE: {2}
                -----------------
                """
                print(userList.format(user, availability, status))
        
        if self.option == 6:
            self.send_presence_subscription(pto=self.contact)
        if self.option == 7:
            users = self.client_roster
            for user in users:
                if user == self.contact:
                    presence = ''
                    availability = ''
                    for key, item in users.presence(user).items():
                        if item['status']:
                            presence = item['status']
                        if item['show']:
                            availability = item['show']
                    userList = """
                    -----------------
                    USER: {0}
                    STATUS: {1}
                    MESSAGE: {2}
                    -----------------
                    """
                    print(userList.format(user, availability, presence))
        if self.option == 8:
            print("CHATTING WITH:", self.contact)
            print("TYPE 'close' TO GO BACK")
            reply = input("PRESS ANY KEY TO START CHATTING ")
            if reply == 'close':
                self.disconnect()
            msg.reply(reply).send()
        if self.option == 10:
            pres = self.Presence()
            pres['status'] = self.newStatus
            print('UPDATING STATUS TO:', self.newStatus)
            pres.send()
        
        self.disconnect()

    async def chatting(self, msg):
        print("----" + str(msg['from'])+"----\n-"+str(msg['body']))
        reply = input("TYPE YOUR REPLY ")
        if reply == 'close':
            self.disconnect()
        msg.reply(reply).send()


        
    