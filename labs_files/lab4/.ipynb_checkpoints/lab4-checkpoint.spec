
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

struct forward_arg_t {
	bit<32> port_id
}

struct metadata {
	bit<32> pna_main_input_metadata_input_port
	bit<32> pna_main_output_metadata_output_port
	bit<32> MainControlT_tmp
	bit<8> timeout_id
}
metadata instanceof metadata

header ethernet instanceof ethernet_t
header ipv4 instanceof ipv4_t
header tcp instanceof tcp_t

regarray direction size 0x100 initval 0
action forward args instanceof forward_arg_t {
	mov m.pna_main_output_metadata_output_port t.port_id
	return
}

action forward_miss args none {
	mov m.MainControlT_tmp 0x1
	mov m.timeout_id 0x1
	learn forward m.MainControlT_tmp m.timeout_id
	return
}

learner forwarding {
	key {
		h.ipv4.dstAddr
	}
	actions {
		forward
		forward_miss
	}
	default_action forward_miss args none 
	size 0x400
	timeout {
		10
		30
		60
		120
		300
		43200
		120
		120

		}
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
	MYPARSER_ACCEPT :	jmpnv LABEL_FALSE h.ipv4
	table forwarding
	jmp LABEL_END
	LABEL_FALSE :	drop
	LABEL_END :	emit h.ethernet
	emit h.ipv4
	emit h.tcp
	tx m.pna_main_output_metadata_output_port
}


