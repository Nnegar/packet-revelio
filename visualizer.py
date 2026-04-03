import matplotlib.pyplot as plt




class Visualizer:  
        

    def plot_packet_size_hist(self, lengths):
        plt.hist(lengths, bins=10)
        plt.xlabel("Packet Size")
        plt.ylabel("Frequency")
        plt.title("Packet Size Distribution")
        plt.show()       
        
        
        
    @staticmethod  
    def format_result(counts):
    
        lines = []
        max_len = max(len(key) for key in counts.keys())
        for item, count in counts.items():
            lines.append(f"{item:<{max_len}} : {count}")
        return "\n".join(lines)