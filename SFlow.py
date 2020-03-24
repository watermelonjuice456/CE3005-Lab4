import pandas as pd


SFlowData = pd.read_csv('SFlow_Data_1.csv.csv', header=None)
#SFlowData = pd.read_csv('test_SFlow_data.csv .csv', header=None)
SFlowData = SFlowData.drop(SFlowData.columns[20], axis=1)
print(SFlowData.head())

SFlowData.columns = ["Type", "sflow_agent_address", "inputPort", "outputPort", "src_MAC", "dst_MAC", "ethernet_type", "in_vlan", "out_vlan", "src_IP", "dst_IP", "IP_protocol", "ip_tos",  "ip_ttl", "udp_src_port_tcp_src_port_icmp_type", "udp_dst_port_tcp_dst_port_icmp_code", "tcp_flag", "packet_size", "IP_size", "sampling_rate"]
print(SFlowData)

#count top talkers and listeners
talkers = SFlowData['src_IP'].value_counts()
print("-------talkers-------")
print(talkers)
listeners = SFlowData['dst_IP'].value_counts()
print("-------listeners-------")
print(listeners)


#determine amount of TCP and UDP protocol
row = len(SFlowData.index) -1
TCP = len(SFlowData[SFlowData["IP_protocol"] == 6])
UDP = len(SFlowData[SFlowData["IP_protocol"] == 17])
print("Amount of TCP: ", TCP)
print("Amount of UDP: ", UDP)

#using the destination IP port number determine the most frequently used application protocol
portNumber = SFlowData['udp_dst_port_tcp_dst_port_icmp_code'].value_counts()
print("-------portNumber-------")
print(portNumber)

#traffic indensity
totalTraffic = SFlowData['IP_size'].sum()
totalTraffic = totalTraffic/1048576
print("-------traffic intensity-------")
print(totalTraffic, "MB")

#top 5 communication pair
pairs = SFlowData.groupby(["src_IP", "dst_IP"]).size().reset_index(name="frequency")
pairs = pairs.sort_values("frequency")
print(pairs)