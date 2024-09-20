/*-----------------Headers-----------------*/
typedef bit<48> EthernetAddress;

header ethernet_t {
    EthernetAddress dstAddr;
    EthernetAddress srcAddr;
    bit<16> etherType; }

struct metadata {
    /* empty */ }

struct headers {
    ethernet_t ethernet; }
