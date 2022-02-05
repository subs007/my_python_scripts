ips = [] # a list of IP addresses.
ips2 = {} # a dictionary of IP addresses to frequency counts.
with open('log_file.log') as f:
    print(type(f))
    lines = f.readlines() # we got a list
    #print(type(read))
    for line in lines:
        print(line.split()[0])
        words = line.split()
        print(words)
        ips.append(words[0])
print(ips)
print(type(ips))

for ipaddr in ips: # take each IP address in the ips list.
    if ipaddr not in ips2:
        ips2[ipaddr] = 1 # dict[key]
    else:
        ips2[ipaddr] += 1

print(ips2)


max_key = max(ips2, key=ips2.get)

print(max_key)

all_values = ips2.values()
max_value = max(all_values)
print(max_value)