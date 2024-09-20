/*-----------------Control-----------------*/
control MainControl(
    inout headers hdr,
    inout metadata meta,
    in pna_main_input_metadata_t istd,
    inout pna_main_output_metadata_t ostd) {    

    action forward (PortId_t port_id) {
        send_to_port(port_id);
    }

    action drop () {
        drop_packet();
    }

    table forwarding {
        key = { 
            hdr.ipv4.dstAddr: exact; 
        }
        actions = { 
            forward;
            drop; 
        }
         size = 1024;
     }

    apply {
        if(hdr.ipv4.isValid()) {
            forwarding.apply();
        }else{
            drop();
        }
    }   
}
