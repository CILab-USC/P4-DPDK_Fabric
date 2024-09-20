#include "headers.p4"

/*-----------------Parser-----------------*/
parser MyParser(
    packet_in packet,
    out headers hdr,
    inout metadata meta,
    in pna_main_parser_input_metadata_t istd)
{
    state start {
        transition parse_ethernet;
    }

    state parse_ethernet{
        packet.extract(hdr.ethernet);
        transition accept;
        }
}
