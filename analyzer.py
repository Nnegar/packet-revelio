from collections import Counter


class PacketAnalyzer:
    @staticmethod
    def protocol_count(packets):
        return Counter(packet.protocol for packet in packets)
    
 
    #returns the ips that have max packets or max data based on name argument by
    @staticmethod
    def top_talkers(packets, by = "packets",limit=10):
        
        counts={}
        
        for packet in packets:
            key = packet.src_ip
            
            if by == "packets":
                value = 1
                
            elif by == "bytes":
                value = packet.length
                
            else:
                raise ValueError("Error in name argument")
            
            
            counts[key] = counts.get(key, 0) + value
        sorted_counts = (sorted(counts.items(),key= lambda item: item[1], reverse = True))
        
        return sorted_counts[:limit]
    
    
    @staticmethod
    def longest_flow(flows):
        if not flows:
            return None
        
        return max(flows, key = lambda f: f.duration)
    
    
    @staticmethod
    def top_flows(flows, number=3):
        if not flows:
            return []
        sorted_flows = sorted(flows, key=lambda f:f.duration, reverse = True)
        return sorted_flows[:number]