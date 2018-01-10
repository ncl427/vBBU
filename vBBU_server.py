from vBBU_client import attachNSSF
from bjsonrpc.handlers import BaseHandler
from bjsonrpc import createserver
import time

# class for server handlers
class ServerHandler(BaseHandler):

   def attachvBBU(self, ueAttachedObj):
      return attachNSSF(ueAttachedObj)

# creating the server to listen 
print "\n"
print "...initializing vBBU"
time.sleep(1)
print "vBBU initialized\n"
s = createserver(host="192.168.186.61", port=10123, handler_factory=ServerHandler)
s.serve() #.setmaxtimeout("write", 10)
