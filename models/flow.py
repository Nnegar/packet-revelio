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
        self.start_time = packet.timestamp
        self.end_time = packet.timestamp
        self.forward_count = 1
        self.forward_bytes = packet.length
        self.backward_count = 0
        self.backward_bytes = 0
        
        
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
        self.start_time = min(self.start_time, packet.timestamp)
        self.end_time = max(self.end_time, packet.timestamp)
        
        #check backward or forward packets
        if packet.src_ip == self.src_ip and packet.src_port == self.src_port:
            self.forward_count += 1
            self.forward_bytes += packet.length
        elif packet.src_ip == self.dst_ip and packet.src_port == self.dst_port:
            self.backward_count += 1
            self.backward_bytes += packet.length
            

        
    @staticmethod
    def build_flows(capture):
        flows = {}
        for packet in capture:
            
            #to put both forward and backward packets in the same flow
            endpoint1 = (packet.src_ip, packet.src_port)
            endpoint2 = (packet.dst_ip, packet.dst_port)
            endpoints = tuple(sorted([endpoint1, endpoint2]))
            key = (endpoints, packet.protocol)
            if key in flows:
                flows[key].add_packet(packet)
            else:
                flows[key] = Flow(packet)
        
        return list(flows.values())

    @property
    def average_packet_size(self):
        return self.total_bytes/self.packet_count
    
    @property
    def duration(self):
        delta = self.end_time - self.start_time
        return delta.total_seconds()
    
    @property
    def packets_per_second(self):
        if not self.duration == 0:
            return self.packet_count/self.duration
        return None
    
    @property
    def bytes_per_second(self):
        if not self.duration == 0:
            return self.total_bytes/self.duration
        return None