# /sbin/ip6tables -A INPUT -p icmpv6 -j DROP
# exec > /dev/null 2>&1

# ip netns del h1
# ip netns del h2

# sleep 1

# ip netns add h1
# ip netns add h2

# ip link set dtap0 netns h1
# ip link set dtap1 netns h2

# sysctl -w net.ipv6.conf.all.disable_ipv6=1 --quiet
# ip netns exec h1 sysctl -w net.ipv6.conf.all.disable_ipv6=1 --quiet
# ip netns exec h2 sysctl -w net.ipv6.conf.all.disable_ipv6=1 --quiet

ip netns exec h1 ip link set dev dtap0 up
ip netns exec h2 ip link set dev dtap1 up

ip netns exec h1 ifconfig dtap0 192.168.10.1/24
ip netns exec h2 ifconfig dtap1 192.168.10.2/24

ip netns exec h1 arp -s 192.168.10.2 00:00:00:00:00:02
ip netns exec h2 arp -s 192.168.10.1 00:00:00:00:00:01
