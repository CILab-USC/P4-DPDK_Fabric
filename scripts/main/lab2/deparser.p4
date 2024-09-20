/*-----------------Deparser-----------------*/
control MyDeparser(
    packet_out packet,
    inout    headers hdr,
    in    metadata meta,
    in    pna_main_output_metadata_t ostd)
{
    apply {
        
        packet.emit(hdr.ethernet);
    
    }
}
