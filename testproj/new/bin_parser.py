import struct

protocol = {
    "54": {"name": "Time", 'len': 6, 'bin': "<BBI"},
    "45": {"name": "Order Executed", 'len': 26, 'bin': "<BBIQIQ"},
    "43": {"name": "Order Executed With Price/Sized", 'len': 39, 'bin': "<BBIQIIQBQ"},
    "50":  {"name": "Trade", 'len': 33,'bin': "<BBIIIBBQQB"},
    "51":  {"name": "Auction Trade", 'len': 33,'bin': "<BBIIIBBQQB"},
    "78":  {"name": "Off-Book Trade", 'len': 70, 'bin': ""},
    "42":  {"name": "Trade Break", 'len': 19, 'bin': ""},
    "49":  {"name": "Auction Info", 'len': 30, 'bin': ""},
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
need = ("54", "45", "43", "50", "51")

class filehandle(object):
    def __init__(self, filename):
        self.data = None
        self.filename = filename
        self.iter = 0
        self.end_read = 0
        self.bufer = []
        self.data_str = None

    def find_nex_pay(self, payload_str):
        toHex = lambda x:"".join([hex(ord(c))[2:].zfill(2) for c in x])
        label = False
        while payload_str:
            m_type = toHex(payload_str[0:1])
            le = protocol[m_type]['len']
            bin = protocol[m_type]['bin']
            real_len = len(payload_str)
            #first positioh has message type payload_str[0:1]
            if m_type in need:
                label = True
                tmp = struct.unpack(bin, payload_str[0:le])
                # + message type [1]
                self.data_str = self.data_str + ":" +str(m_type)
                if m_type == "45":
                    #0x45 Order Executed (Trade ID position 5)
                    self.data_str = self.data_str + ":" + str(tmp[5]) + ":" + str(tmp[3])
                if m_type == "43":
                    #0x43 Order Executed With Price/ Size (Trade ID  position 6)
                    self.data_str = self.data_str + ":" + str(tmp[6]) + ":" + str(tmp[3])
                if m_type == "50":
                    #0x50 Trade (Trade ID  position 8)
                    self.data_str = self.data_str + ":" + str(tmp[8])
                if m_type == "51":
                    #0x51 Auction Trade (Trade ID  position 8)
                    self.data_str = self.data_str + ":" + str(tmp[8])
                #delete used message
                payload_str = payload_str[le:real_len]
                if len(payload_str) == le or len(payload_str) == 0:
                    payload_str = False
            else:
                payload_str = payload_str[le:real_len]
                if real_len == le or real_len == 0:
                    payload_str = False
        if label:
            print self.data_str

    def data_type(self, payload, mc):
        #needs only
        #0x54 Time,
        #0x45 Order Executed
        #0x43 Order Executed With Price/ Size,
        #0x50 Trade,
        #0x51 Auction Trade.
        self.find_nex_pay(payload)

    def read_log(self):
        self.data = open(self.filename, "rb")
        while True:
            char = self.data.read(1)
            if not char:
                print "Error"
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
            var0 = struct.unpack("!IIIII", head_bl)
            #firs 8+1 bytes Unit Header
            head_u = self.data.read(9)
            var1 = struct.unpack("HBBIB", head_u)
            self.end_read = self.iter + 20
            #Length var1[0]
            #Message Count var1[1]))
            #Market Data Group var1[2]
            #Sequence Number var1[3]
            self.data_str = str(var0[1]) + ":" + str(var1[3])
            if (var1[0] == 8):
                pass
            else:
                #Find netx position for firs payload
                if var1[1] >= 1:
                    if var1[1] > 1:
                        pass
                    n = var1[0] - 8
                    payload = self.data.read(n)
                    self.data_type(payload, var1[1])


if __name__ == "__main__":
    filez = filehandle("/work/testproj/testproj/new/lse_araw.log")
    filez.read_log()