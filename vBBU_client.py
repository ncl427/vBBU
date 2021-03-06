from bjsonrpc import connect
import pickle
from models.Mdd import Mdd
from models.ueAttachObj import ueAttachObj
import time

# global-variables
nssfConnect = not False
nssfIp = "117.17.102.129"
nssfPort = 10123

def attachNSSF(ueAttachedObj):

   if(nssfConnect):
      return attachReal(ueAttachedObj)
   else:
      return attachFake(ueAttachedObj)

def attachReal(ueAttachedObj):
   print "\n--------------------------\n...connecting to vBBU-NSSF"
   c = connect(nssfIp)
   time.sleep(1)
   print "connected vBBU-NSSF."
   time.sleep(1)
   print "...attaching vBBU-NSSF"
   time.sleep(1)

   ueAttachedObjUnpickled = pickle.loads(ueAttachedObj)
   #print "ueAttachObj:"
   #print "\t", ueAttachedObjUnpickled.ip
   #print "\t", ueAttachedObjUnpickled.serviceType

   #response =  c.call.networkAttach(ueIp, serviceType, ueAttachedObjUnpickled)
   response =  c.call.networkAttach(ueAttachedObj)
   printNSSFresponse(response)

   return response

def attachFake(ueAttachedObj):
   print "\n--------------------------\n...connecting to vBBU-NSSF"
   print "connected vBBU-NSSF.\n...attaching vBBU-NSSF"

   ueAttachedObjUnpickled = pickle.loads(ueAttachedObj)
   print "ueAttachObj: "
   print "\t", ueAttachedObjUnpickled.ip
   print "\t", ueAttachedObjUnpickled.serviceType

   response1 = Mdd()
   response1.nesId = 526
   response1.tempId = 7
   response = pickle.dumps(response1)
   printNSSFresponse(response)

   return response

def printNSSFresponse(Mdd):
   obj = pickle.loads(Mdd)
   time.sleep(1)
   print "attached vBBU-NSSf."
   time.sleep(0.5)
   print "attaching vBBU-NSSF response: "
   print "\tMdd-nesId: ", obj.nesId
   print "\tMdd-tempId: ", obj.tempId

