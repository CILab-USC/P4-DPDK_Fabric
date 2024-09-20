
struct ethernet_t {
	bit<48> dstAddr
	bit<48> srcAddr
	bit<16> etherType
}

struct ipv4_t {
	bit<8> version_ihl
	bit<8> diffserv
	bit<16> totalLen
	bit<16> identification
	bit<16> flags_fragOffset
	bit<8> ttl
	bit<8> protocol
	bit<16> hdrChecksum
	bit<32> srcAddr
	bit<32> dstAddr
}

struct tcp_t {
	bit<16> srcPort
	bit<16> dstPort
	bit<32> seqNo
	bit<32> ackNo
	bit<16> dataOffset_res_ecn_ctrl
	bit<16> window
	bit<16> checksum
	bit<16> urgentPtr
}

struct forward_exact_arg_t {
	bit<48> dstAddr
	bit<32> port_id
}

struct forward_lpm_arg_t {
	bit<48> dstAddr
	bit<32> port_id
}

struct metadata {
	bit<32> pna_main_input_metadata_input_port
	bit<32> pna_main_output_metadata_output_port
}
metadata instanceof metadata

header ethernet instanceof ethernet_t
header ipv4 instanceof ipv4_t
header tcp instanceof tcp_t

regarray direction size 0x100 initval 0
action NoAction args none {
	return
}

action forward_exact args instanceof forward_exact_arg_t {
	mov m.pna_main_output_metadata_output_port t.port_id
	mov h.ethernet.srcAddr h.ethernet.dstAddr
	mov h.ethernet.dstAddr t.dstAddr
	add h.ipv4.ttl 0xFF
	return
}

action forward_lpm args instanceof forward_lpm_arg_t {
	mov m.pna_main_output_metadata_output_port t.port_id
	mov h.ethernet.srcAddr h.ethernet.dstAddr
	mov h.ethernet.dstAddr t.dstAddr
	add h.ipv4.ttl 0xFF
	return
}

action drop args none {
	drop
	return
}

table forwarding_exact {
	key {
		h.ipv4.dstAddr exact
	}
	actions {
		forward_exact
		NoAction
	}
	default_action NoAction args none 
	size 0x400
}


table forwarding_lpm {
	key {
		h.ipv4.dstAddr lpm
	}
	actions {
		forward_lpm
		drop
	}
	default_action drop args none 
	size 0x400
}


apply {
	rx m.pna_main_input_metadata_input_port
	extract h.ethernet
	jmpeq MYPARSER_PARSE_IPV4 h.ethernet.etherType 0x800
	jmp MYPARSER_ACCEPT
	MYPARSER_PARSE_IPV4 :	extract h.ipv4
	jmpeq MYPARSER_PARSE_TCP h.ipv4.protocol 0x6
	jmp MYPARSER_ACCEPT
	MYPARSER_PARSE_TCP :	extract h.tcp
	MYPARSER_ACCEPT :	jmpnv LABEL_END h.ipv4
	table forwarding_exact
	jmpnh LABEL_FALSE_0
	jmp LABEL_END
	LABEL_FALSE_0 :	table forwarding_lpm
	LABEL_END :	emit h.ethernet
	emit h.ipv4
	emit h.tcp
	tx m.pna_main_output_metadata_output_port
}


