from capture import PacketCapture
import packet
from visualizer import Visualizer
from readers import CsvPacketReader



packets = CsvPacketReader.read("./data/sample.csv")
capture = PacketCapture(packets)
vis = Visualizer()
#print(vis.format_result(df.top_talkers(by = "bytes")))
#vis.plot_packet_size_hist(df.get_packet_lengths())


print(capture[0])