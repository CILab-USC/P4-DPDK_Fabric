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

    action forward_miss () {
        forward_action_keys forward_params;
        forward_params.port_id = (PortId_t) 1;
        add_entry(action_name = "forward", action_params = forward_params, 
                    expire_time_profile_id = EXPIRE_TIME_PROFILE_ID);
    }

    table forwarding {
        key = { 
            hdr.ipv4.dstAddr: exact; 
        }
        actions = { 
            forward;
            forward_miss;
        }
        add_on_miss = true;
        default_action = forward_miss;
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

///home/admin/sde/p4-dpdk-target/examples/pna/add_on_miss/add_on_miss.p4

// /*-----------------Control-----------------*/
// control MainControl(
//     inout headers hdr,
//     inout metadata meta,
//     in pna_main_input_metadata_t istd,
//     inout pna_main_output_metadata_t ostd) {    

//     action forward (PortId_t port_id) {
//         send_to_port(port_id);
//     }

//     action drop () {
//         drop_packet();
//     }

//     table forwarding {
//         key = { 
//             hdr.ipv4.dstAddr: exact; 
//         }
//         actions = { 
//             forward;
//             drop; 
//         }
//         size = 1024;
//     }

//     apply {
//         if(hdr.ipv4.isValid()) {
//             forwarding.apply();
//         }else{
//             drop();
//         }
//     }   
// }
