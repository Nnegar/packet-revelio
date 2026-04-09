import pandas as pd
from models.packet import Packet
from collections import Counter


class PacketCapture:
    def __init__(self, packets):
        self.packets = list(packets)

            
    def __iter__(self):
        return iter(self.packets)
    
    def __len__(self):
        return len(self.packets)

    def __getitem__(self, index):
        return self.packets[index]
            
    

        
        
    #right now for ploting histograg   
    def get_packet_lengths(self):
        return [packet.length for packet in self.packets]
    
    
    def to_dataframe(self):
        rows = [packet.to_dict() for packet in self.packets]
        return pd.DataFrame(rows)
        
        
            
    
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
            
            
        
        
        
