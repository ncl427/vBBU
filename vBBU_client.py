from bjsonrpc import connect
import pickle
from models.Mdd import Mdd

def attachNSSF(ueIp, serviceType):
   nssfIp = "117.17.102.21"
   nssfPort = 10123

   print "\n--------------------------"
   print "...connecting to vBBU-NSSF"
   #c = connect(nssfIp)
   print "connected vBBU-NSSF."

   print "...attaching vBBU-NSSF: ", ueIp, " - ", serviceType
   #response =  c.call.networkAttach(ueIp, serviceType)
   #response = "attached vBBU-NSSF"
   response = Mdd()
   print "attaching vBBU-NSSF response: ", response.nesId
   return response.nesId
