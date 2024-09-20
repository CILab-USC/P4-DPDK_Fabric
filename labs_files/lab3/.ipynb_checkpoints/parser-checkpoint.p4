#include "headers.p4"

parser MyParser(packet_in packet,
                out headers hdr,
                inout metadata meta,
                in pna_main_parser_input_metadata_t istd)
{

    /*Add the start state below*/

    /*Add the parse_ethernet state below*/

    /*Add the parse_ipv4 state below*/

    /*Add the parse_tcp state below*/

}
