#data structure fo packets
#attributes for now: src_ip, dst_ip, src_port, dst_port, protocol


class Packet:
    def __init__(self, data):
        self.packet_id = int(data["packet_id"])
        self.time_stamp = data["timestamp"]
        self.src_ip = data["source ip"]
        self.dst_ip = data["destination ip"]
        self.protocol = data["protocol"]
        self.src_port = int(data["source port"])
        self.dst_port = int(data["destination port"])
        self.length = int(data["length"])
        