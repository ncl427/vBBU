from bjsonrpc import connect
import pickle
from models.Mdd import Mdd

# global-variables
nssfConnect = False
nssfIp = "117.17.102.129"
nssfPort = 10123

def attachNSSF(ueIp, serviceType):

   if(nssfConnect):
      return attachReal(ueIp, serviceType)
   else:
      return attachFake(ueIp, serviceType)

def attachReal(ueIp, serviceType):
   print "\n--------------------------\n...connecting to vBBU-NSSF"
   c = connect(nssfIp)
   print "connected vBBU-NSSF.\n...attaching vBBU-NSSF"
   response =  c.call.networkAttach(ueIp, serviceType)
   printNSSFresponse(response)

   return response

def attachFake(ueIp, serviceType):
   print "\n--------------------------\n...connecting to vBBU-NSSF"
   print "connected vBBU-NSSF.\n...attaching vBBU-NSSF"
   response1 = Mdd()
   response = pickle.dumps(response1)
   vwNssfAttResponse(response)

   return response

def vwNssfAttResponse(Mdd):
   obj = pickle.loads(Mdd)
   print "attaching vBBU-NSSF response: "
   print "\tMdd-nesId: ", obj.nesId
   print "\tMdd-tempId: ", obj.tempId
   print "attached vBBU-NSSf."

