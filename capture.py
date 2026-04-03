import pandas as pd
from packet import Packet
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
            
    
    def ptl_count(self):
        return Counter(packet.protocol for packet in self.packets)
    
 
    #returns the ips that have max packets or max data based on name argument by
    def top_talkers(self, by = "packets"):
        
        counts={}
        
        for packet in self.packets:
            key = packet.src_ip
            
            if by == "packets":
                value = 1
                
            elif by == "bytes":
                value = packet.length
                
            else:
                raise ValueError("Error in name argument")
            
            
            counts[key] = counts.get(key, 0) + value
        
        return dict(sorted(
            counts.items(),
            key= lambda item: item[1], 
            reverse = True))
        
        
    #right now for ploting histograg   
    def get_packet_lengths(self):
        return [packet.length for packet in self.packets]
        
            
    
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
            
            
        
        
        
