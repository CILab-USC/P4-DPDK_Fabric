# /home/admin/p4c/build/p4c-dpdk --arch pna main.p4 -o lab2.spec

export RTE_INSTALL_DIR=/home/ubuntu/dpdk
export LAB_DIR=/home/ubuntu

echo 1024 > /sys/kernel/mm/hugepages/hugepages-2048kB/nr_hugepages

$RTE_INSTALL_DIR/examples/pipeline/build/pipeline -c 0x3 --vdev=net_tap0,mac="00:00:00:00:00:01" --vdev=net_tap1,mac="00:00:00:00:00:02" --  -s $LAB_DIR/lab2.cli

