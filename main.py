from capture import PacketCapture
import packet
from visualizer import Visualizer


df = PacketCapture("./data/sample.csv")
vis = Visualizer()
#print(vis.format_result(df.top_talkers(by = "bytes")))
#vis.plot_packet_size_hist(df.get_packet_lengths())


print(df.classify())