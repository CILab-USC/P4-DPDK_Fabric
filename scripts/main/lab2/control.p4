/*-----------------Control-----------------*/
control MainControl(
    inout headers hdr,
    inout metadata meta,
    in pna_main_input_metadata_t istd,
    inout pna_main_output_metadata_t ostd)
{    
    apply {

        if (istd.input_port == (PortId_t) 0){
            send_to_port((PortId_t) 1);
        }
        else if (istd.input_port == (PortId_t) 1){
            send_to_port((PortId_t) 0);
        }
        
    }
}
