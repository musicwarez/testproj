#!/usr/bin/python2.7
import struct
import sys
from datetime import datetime
import time

protocol = {
    "54": {"name": "Time", 'len': 6, 'bin': "<BBI"},
    "45": {"name": "Order Executed", 'len': 26, 'bin': "<BBIQIQ"},
    "43": {"name": "Order Executed With Price/Sized", 'len': 39, 'bin': "<BBIQIIQBQ"},
    "50": {"name": "Trade", 'len': 33,'bin': "<BBIIIBBQQB"},
    "51": {"name": "Auction Trade", 'len': 33,'bin': "<BBIIIBBQQB"},
    "78": {"name": "Off-Book Trade", 'len': 70, 'bin': "<BBIIIBBQQ4sQQ4sQ5sB"},
    "42": {"name": "Trade Break", 'len': 19, 'bin': "<BBIQBI"},
    "49": {"name": "Auction Info", 'len': 30, 'bin': ""},
    "77": {"name": "Statistics", 'len': 23, 'bin': ""},
    "01": {"name": "Login Request", 'len': 18, 'bin': ""},
    "02": {"name": "Login Response", 'len': 3, 'bin': ""},
    "05": {"name": "Logout Request", 'len': 2, 'bin': ""},
    "03": {"name": "Replay Request", 'len': 9, 'bin': ""},
    "04": {"name": "Replay Response", 'len': 10, 'bin': ""},
    "81": {"name": "Snapshot Request", 'len': 16, 'bin': ""},
    "82": {"name": "Snapshot Response", 'len': 11, 'bin': ""},
    "83": {"name": "Snapshot Complete", 'len': 17, 'bin': ""},
    "41": {"name": "Add Order", 'len': 34, 'bin': ""},
    "48": {"name": "Add Order", 'len': 28, 'bin': ""},
    "53": {"name": "System Event", 'len': 7, 'bin': ""},
    "46": {"name": "Add Attributed Order", 'len': 45, 'bin': ""},
    "44": {"name": "Order Deleted", 'len': 19, 'bin': ""},
    "55": {"name": "Order Modified", 'len': 27, 'bin': ""},
    "79": {"name": "Order Book Clear", 'len': 13, 'bin': ""},
    "52": {"name": "Symbol Directory", 'len': 65, 'bin': "" },
}
# Here Messages type witch we should check
need = ("45", "50", "51", "78")
look = ['10444957', '7528158', '10439722', '10444976', '10444975', '10438800', '10444958',
 '9957331', '10445098', '10445299', '7440239', '10445151', '10444925', '10445295',
 '10445294', '10445297', '10445149', '8163507', '10438909', '10445100', '10445103',
 '10445102', '10445866', '9267735', '10445162', '10445161', '10439914', '10438799',
 '10439823', '10441119', '10438910', '8652045', '10439424', '10444965', '10444966',
 '10439718', '10444960', '10444961', '10439915', '10439416', '10439822', '10446537',
 '3452601', '10444915', '10444980', '1278043', '10444078', '10444079', '3462787',
 '9356961', '9356735']

look1 = ['2778', '2735', '2769', '2737', '2781', '2731', '2733', '2763', '2772', '2760', '2766',
         '2729', '2775', '2741', '2752', '2744', '2750', '2746', '2739', '2748']

class filehandle(object):
    def __init__(self, filename):
        self.data = None
        self.iter = 0
        self.end_read = 0
        self.data_str = None
        #receive time seconds
        self.rtmc = 0
        self.filename = filename
        self.year = None
        self.sequence = 0

    def find_nex_pay(self, payload_str):
        toHex = lambda x: "".join([hex(ord(c))[2:].zfill(2) for c in x])
        label = False
        while payload_str:
            m_type = toHex(payload_str[1:2])
            le = protocol[m_type]['len']
            bin = protocol[m_type]['bin']
            real_len = len(payload_str)
            #if self.sequence == 2748:
            #    print m_type
            #    exit()

            #first positioh has message type payload_str[0:1]
            if m_type in need:
                label = True
                #try:
                tmp = struct.unpack(bin, payload_str[0:le])
                #except struct.error as e:
                #    print >>sys.stderr, "Error. unpack payload"
                # + message type [1]
                self.data_str = self.data_str + ":" +str(m_type)
                ################################
                #if str(self.sequence) in look1:
                #    print tmp
                #    #exit()
                ################################
                if m_type == "54":
                    #Time!!! convert from sec to msec
                    self.rtmc = tmp[2] * 1000000
                # Here tmp[2] in Nanosecond
                ttt = self.rtmc + tmp[2] / 1000 + self.year * 1000000
                exch_time = str(ttt)
                if m_type == "45":
                    #0x45 Order Executed (Trade ID position 5) 1447413802 + nanosec / 1000000000
                    self.data_str = self.data_str + ":" + str(tmp[5]) + ":" + exch_time + ":" + str(tmp[3])
                if m_type == "43":
                    #0x43 Order Executed With Price/ Size (Trade ID  position 6)
                    self.data_str = self.data_str + ":" + str(tmp[6]) + ":" + exch_time + ":" + str(tmp[3])
                if m_type == "50":
                    #0x50 Trade (Trade ID  position 8)
                    self.data_str = self.data_str + ":" + str(tmp[8]) + ":" + exch_time
                if m_type == "51":
                    #0x51 Auction Trade (Trade ID  position 8)
                    self.data_str = self.data_str + ":" + str(tmp[8]) + ":" + exch_time
                if m_type == "78":
                    ###############################
                    #if str(self.sequence) in look:
                    #    print tmp
                        #exit()
                    #if str(tmp[14]) in ("XOFF "):
                    #    print tmp
                    ###############################
                    if str(tmp[14]) not in ("XLON "):
                        #print tmp
                        #print "OKZ"
                        #exit()
                #if m_type == "78":
                    #0x51 Auction Trade (Trade ID [8] Trade type [9] )
                        self.data_str = self.data_str + ":" + str(tmp[8]) + ":" + exch_time + ":" +str(tmp[9]) + ":"\
                                                                                                       +str(tmp[14])
                    else:
                        #print str(tmp[14])
                        label = False
                #delete used message
                payload_str = payload_str[le:real_len]
                if len(payload_str) == le or len(payload_str) == 0:
                    payload_str = False
            else:
                payload_str = payload_str[le:real_len]
                if real_len == le or real_len == 0:
                    payload_str = False
        if label:
            print(self.data_str)
            pass

    def data_type(self, payload, mc):
        #needs only
        #0x54 Time,
        #0x45 Order Executed
        #0x43 Order Executed With Price/ Size,
        #0x50 Trade,
        #0x51 Auction Trade.
        self.find_nex_pay(payload)

    def read_log(self):
        #Read RAW data from file
        self.data = open(self.filename, "rb")
        #Read RAW data from stdin
        #self.data = sys.stdin
        while True:
            char = self.data.read(1)
            if not char:
                print("Data END. Bye!")
                break
            self.process(char)
            self.iter += 1
        self.data.close()

    def process(self, char):
        if char == "_":
            #begin need accamulate firs 20 bytes BL. Header
            #length, receive time seconds, receive time microseconds, write time seconds, write time microseconds
            #here we need receive time seconds. This is first element in data string
            head_bl = self.data.read(20)
            try:
                var0 = struct.unpack("!IIIII", head_bl)
            except struct.error as e:
                print >>sys.stderr, "Error. unpack Header \t"
            #firs 8 bytes Unit Header
            head_u = self.data.read(8)
            try:
                var1 = struct.unpack("HBBI", head_u)
            except struct.error as e:
                print >>sys.stderr, "Error. unpack Unit Header \t"
            self.end_read = self.iter + 20
            #Length var1[0]
            #Message Count var1[1]))
            #Market Data Group var1[2]
            #Sequence Number var1[3]
            self.sequence = var1[3]
            #if var1[3] == 10444078:
            #    print var0
            #    print var1
            rtmc = str(var0[1] * 1000000 +  var0[2])
            y = datetime.date(datetime.fromtimestamp(var0[3]))
            y = y.timetuple()
            self.year = int(time.mktime(y))
            self.data_str = str(var0[1]) + ":" + rtmc + ":" + str(var1[3])
            if (var1[0] == 8):
                pass
            else:
                #Find netx position for firs payload
                if var1[1] >= 1:
                    if var1[1] > 1:
                        pass
                    n = var1[0] - 8
                    payload = self.data.read(n)
                    #if var1[3] == 10444078:
                    #    print payload
                    self.data_type(payload, var1[1])


if __name__ == "__main__":
    req_version = (2,7)
    cur_version = sys.version_info[0:2]
    if cur_version != req_version:
        sys.exit("This script requires Python 2.7!")

    filez = filehandle("/work/testproj/testproj/new/lse_araw.log")
    filez.read_log()