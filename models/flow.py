from datetime import datetime



class Flow:
    def __init__(self, packet):
        self.src_ip = packet.src_ip
        self.dst_ip = packet.dst_ip
        self.protocol = packet.protocol
        self.src_port = packet.src_port
        self.dst_port = packet.dst_port
        self.packet_count = 1
        self.total_bytes = packet.length
        self.start_time = packet.time_stamp
        self.end_time = packet.time_stamp
        self.duration = 0
        
        
    def __str__(self):
        return (
            f"\n--- Flow ---\n"
            f"Source IP: {self.src_ip}\n"
            f"Destination IP: {self.dst_ip}\n"
            f"Protocol: {self.protocol}\n"
            f"Source Port: {self.src_port}\n"
            f"Destination Port: {self.dst_port}\n"
            f"Packet Count: {self.packet_count}\n"
            f"Total Bytes: {self.total_bytes}\n"
            f"Duration: {self.duration}\n"
        )
    
    
    def __repr__(self):
        return self.__str__()
        
        
        
    def add_packet(self, packet):
        self.packet_count += 1
        self.total_bytes += packet.length
        if packet.time_stamp > self.end_time:
            self.end_time = packet.time_stamp
        elif packet.time_stamp < self.start_time:
            self.start_time = packet.time_stamp
        self.duration = self.end_time - self.start_time
        
    @staticmethod
    def build_flows(capture):
        flows = {}
        for packet in capture:
            key = (packet.src_ip,packet.dst_ip,packet.protocol,packet.src_port, packet.dst_port)
            if key in flows:
                flows[key].add_packet(packet)
            else:
                flows[key] = Flow(packet)
        
        return list(flows.values())
                
            