from vBBU_client import attachNSSF
from bjsonrpc.handlers import BaseHandler
from bjsonrpc import createserver

# class for server handlers
class ServerHandler(BaseHandler):

   def attachvBBU(self, ueIp, serviceType):
      return attachNSSF(ueIp, serviceType)

# creating the server to listen 
s = createserver(host="192.168.186.61", port=10123, handler_factory=ServerHandler)
s.serve()
