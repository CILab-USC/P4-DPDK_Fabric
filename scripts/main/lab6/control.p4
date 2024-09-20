/*-----------------Control-----------------*/
control MainControl(
    inout headers hdr,
    inout metadata meta,
    in pna_main_input_metadata_t istd,
    inout pna_main_output_metadata_t ostd){    

    action forward_exact (EthernetAddress dstAddr, PortId_t port_id) {
        send_to_port(port_id);
        hdr.ethernet.srcAddr = hdr.ethernet.dstAddr;
        hdr.ethernet.dstAddr = dstAddr;
        hdr.ipv4.ttl = hdr.ipv4.ttl -1;
    }

    action forward_lpm (EthernetAddress dstAddr, PortId_t port_id) {
        send_to_port(port_id);
        hdr.ethernet.srcAddr = hdr.ethernet.dstAddr;
        hdr.ethernet.dstAddr = dstAddr;
        hdr.ipv4.ttl = hdr.ipv4.ttl -1;
    }

    action drop () {
        drop_packet();
    }

    table forwarding_exact {
        key = { 
            hdr.ipv4.dstAddr: exact;
        }
        actions = { 
            forward_exact;
        }
        size = 1024;
    }

    table forwarding_lpm {
        key = { 
            hdr.ipv4.dstAddr: lpm;
        }
        actions = { 
            forward_lpm;
            drop; 
        }
        size = 1024;
        default_action = drop;
    }

    apply {

        if(hdr.ipv4.isValid()) {
            if(forwarding_exact.apply().miss) {
                forwarding_lpm.apply();
            }
        }
        
    }
}
