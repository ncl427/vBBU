from bjsonrpc import connect

def attachNSSF(ueIp, serviceType):
   nssfIp = "117.17.102.21"
   nssfPort = 10123

   print "\n--------------------------"
   print "...connecting to vBBU-NSSF"
   #c = connect(nssfIp)
   print "connected vBBU-NSSF."

   print "...attaching vBBU-NSSF: ", ueIp, " - ", serviceType
   #response =  c.call.networkAttach(ueIp, serviceType)
   response = "attached vBBU-NSSF"
   print "attaching vBBU-NSSF response: ", response
   return response
