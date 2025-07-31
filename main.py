import ipaddress
import pandas as pd
import netaddr
import matplotlib.pyplot as plot
df = pd.read_excel('ip_data.xlsx')
results = []
for index, row in df.iterrows():
    IP_Address = row['IP Address']
    Subnet_Mask = row['Subnet Mask']
    
    IP_CIDR_Notation = netaddr.IPNetwork(f"{IP_Address}/{Subnet_Mask}")
    Network_address = IP_CIDR_Notation.network
    Broadcast_address = IP_CIDR_Notation.broadcast
    No_usable_hosts = IP_CIDR_Notation.size - 2

    results.append({"IP Address": IP_Address, "Subnet Mask" : Subnet_Mask, "CIDR notation": f"{IP_CIDR_Notation.network}/{IP_CIDR_Notation.prefixlen}", "Network Address":Network_address, "Broadcast Address": Broadcast_address, "Usable hosts number": No_usable_hosts })
    output = pd.DataFrame(results)
    grouped_output = output.groupby('CIDR notation')
    
print(output)
output.to_csv("out_report.csv", index=False)
plot.bar(output["CIDR notation"], output["Usable hosts number"], color="skyblue")
plot.xlabel("Subnet (CIDR Notation)")
plot.ylabel("Usable Hosts")
plot.show()







