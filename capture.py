import pandas as pd
from packet import Packet
from collections import Counter


class PacketCapture:
    def __init__(self, path):
        self.packets = []
        df = pd.read_csv(path)
        for _, raw in df.iterrows():
            data = raw.to_dict()
            packet = Packet(data)
            self.packets.append(packet)
            
            
    
    
    def ptl_count(self):
        return Counter(packet.protocol for packet in self.packets)
        
        
                
                
        
    
            
    
    def __str__(self):
        lines = []
        for packet in self.packets:
            lines.append( f"""Id: {packet.packet_id} 
    timestamp: {packet.time_stamp} 
    source IP: {packet.src_ip}
    destination IP: {packet.dst_ip}
    protocol: {packet.protocol}
    source port: {packet.src_port}
    destination port: {packet.dst_port}
    length: {packet.length}""" )
        return "\n".join(lines)
            
            
        
        
        
