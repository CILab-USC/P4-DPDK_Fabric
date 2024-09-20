/*-----------------Deparser-----------------*/
control MyDeparser(
    packet_out packet,
    inout    headers hdr,
    in    metadata meta,
    in    pna_main_output_metadata_t ostd)
{


    apply {
        
        /*Emit the Ethernet Header below*/

        /*Emit the IPv4 Header below*/

        /*Emit the TCP Header below*/


    } 
}