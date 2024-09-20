/*-----------------Deparser-----------------*/
control MyDeparser(
    packet_out packet,
    inout    headers hdr,
    in    metadata meta,
    in    pna_main_output_metadata_t ostd)
{
    InternetChecksum() checksum;

    apply {
        bit<16> word1 = hdr.ipv4.version ++ hdr.ipv4.ihl ++ hdr.ipv4.diffserv;
        bit<32> word4 = hdr.ipv4.flags ++ hdr.ipv4.fragOffset ++ hdr.ipv4.ttl ++ hdr.ipv4.protocol;

         checksum.add({
            word1,
            hdr.ipv4.totalLen,
            hdr.ipv4.identification,
            word4,
            hdr.ipv4.srcAddr,
            hdr.ipv4.dstAddr
        });

        hdr.ipv4.hdrChecksum = checksum.get();
        
        /*Emit the Ethernet Header below*/
        packet.emit(hdr.ethernet);

        /*Emit the IPv4 Header below*/
        packet.emit(hdr.ipv4);

        /*Emit the TCP Header below*/
        packet.emit(hdr.tcp);
    } 
}