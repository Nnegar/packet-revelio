from capture import PacketCapture
import packet
from visualizer import Visualizer
from readers import CsvPacketReader
from analyzer import PacketAnalyzer

packets = CsvPacketReader.read("./data/sample.csv")
capture = PacketCapture(packets)
top10=PacketAnalyzer.top_talkers(capture)
print(dict(top10))
print(Visualizer.format_result(dict(top10)))
print(Visualizer.format_result(PacketAnalyzer.protocol_count(capture)))
print(capture.to_dataframe())
vis = Visualizer()
#print(vis.format_result(df.top_talkers(by = "bytes")))
#vis.plot_packet_size_hist(df.get_packet_lengths())


print(capture[0])