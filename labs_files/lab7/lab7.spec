

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

struct cksum_state_t {
	bit<16> state_0
}

struct dpdk_pseudo_header_t {
	bit<16> pseudo
	bit<32> pseudo_0
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
	bit<8> MainDeparserT_deparser_tmp
	bit<8> MainDeparserT_deparser_tmp_0
	bit<8> MainDeparserT_deparser_tmp_1
	bit<8> MainDeparserT_deparser_tmp_4
	bit<8> MainDeparserT_deparser_tmp_5
	bit<8> MainDeparserT_deparser_tmp_6
	bit<8> MainDeparserT_deparser_tmp_9
	bit<8> MainDeparserT_deparser_tmp_10
	bit<16> MainDeparserT_deparser_tmp_12
	bit<16> MainDeparserT_deparser_tmp_14
	bit<16> MainDeparserT_deparser_tmp_15
	bit<16> MainDeparserT_deparser_tmp_16
	bit<16> MainDeparserT_deparser_tmp_17
	bit<16> MainDeparserT_deparser_tmp_20
	bit<16> MainDeparserT_deparser_tmp_21
	bit<16> MainDeparserT_deparser_tmp_22
	bit<16> MainDeparserT_deparser_tmp_25
	bit<16> MainDeparserT_deparser_tmp_26
	bit<24> MainDeparserT_deparser_tmp_28
	bit<24> MainDeparserT_deparser_tmp_30
	bit<24> MainDeparserT_deparser_tmp_31
	bit<32> MainDeparserT_deparser_tmp_33
	bit<32> MainDeparserT_deparser_tmp_35
	bit<16> MainDeparserT_deparser_word1
	bit<32> MainDeparserT_deparser_word4
}
metadata instanceof metadata

header ethernet instanceof ethernet_t
header ipv4 instanceof ipv4_t
header tcp instanceof tcp_t
header cksum_state instanceof cksum_state_t
header dpdk_pseudo_header instanceof dpdk_pseudo_header_t

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
	LABEL_END :	mov m.MainDeparserT_deparser_tmp h.ipv4.version_ihl
	shr m.MainDeparserT_deparser_tmp 0x4
	mov m.MainDeparserT_deparser_tmp_0 m.MainDeparserT_deparser_tmp
	and m.MainDeparserT_deparser_tmp_0 0xF
	mov m.MainDeparserT_deparser_tmp_1 m.MainDeparserT_deparser_tmp_0
	and m.MainDeparserT_deparser_tmp_1 0xF
	mov m.MainDeparserT_deparser_tmp_4 m.MainDeparserT_deparser_tmp_1
	shl m.MainDeparserT_deparser_tmp_4 0x4
	mov m.MainDeparserT_deparser_tmp_5 h.ipv4.version_ihl
	and m.MainDeparserT_deparser_tmp_5 0xF
	mov m.MainDeparserT_deparser_tmp_6 m.MainDeparserT_deparser_tmp_5
	and m.MainDeparserT_deparser_tmp_6 0xF
	mov m.MainDeparserT_deparser_tmp_9 m.MainDeparserT_deparser_tmp_6
	and m.MainDeparserT_deparser_tmp_9 0xF
	mov m.MainDeparserT_deparser_tmp_10 m.MainDeparserT_deparser_tmp_4
	or m.MainDeparserT_deparser_tmp_10 m.MainDeparserT_deparser_tmp_9
	mov m.MainDeparserT_deparser_tmp_12 m.MainDeparserT_deparser_tmp_10
	shl m.MainDeparserT_deparser_tmp_12 0x8
	mov m.MainDeparserT_deparser_tmp_14 h.ipv4.diffserv
	and m.MainDeparserT_deparser_tmp_14 0xFF
	mov m.MainDeparserT_deparser_word1 m.MainDeparserT_deparser_tmp_12
	or m.MainDeparserT_deparser_word1 m.MainDeparserT_deparser_tmp_14
	mov m.MainDeparserT_deparser_tmp_15 h.ipv4.flags_fragOffset
	shr m.MainDeparserT_deparser_tmp_15 0xD
	mov m.MainDeparserT_deparser_tmp_16 m.MainDeparserT_deparser_tmp_15
	and m.MainDeparserT_deparser_tmp_16 0x7
	mov m.MainDeparserT_deparser_tmp_17 m.MainDeparserT_deparser_tmp_16
	and m.MainDeparserT_deparser_tmp_17 0x7
	mov m.MainDeparserT_deparser_tmp_20 m.MainDeparserT_deparser_tmp_17
	shl m.MainDeparserT_deparser_tmp_20 0xD
	mov m.MainDeparserT_deparser_tmp_21 h.ipv4.flags_fragOffset
	and m.MainDeparserT_deparser_tmp_21 0x1FFF
	mov m.MainDeparserT_deparser_tmp_22 m.MainDeparserT_deparser_tmp_21
	and m.MainDeparserT_deparser_tmp_22 0x1FFF
	mov m.MainDeparserT_deparser_tmp_25 m.MainDeparserT_deparser_tmp_22
	and m.MainDeparserT_deparser_tmp_25 0x1FFF
	mov m.MainDeparserT_deparser_tmp_26 m.MainDeparserT_deparser_tmp_20
	or m.MainDeparserT_deparser_tmp_26 m.MainDeparserT_deparser_tmp_25
	mov m.MainDeparserT_deparser_tmp_28 m.MainDeparserT_deparser_tmp_26
	shl m.MainDeparserT_deparser_tmp_28 0x8
	mov m.MainDeparserT_deparser_tmp_30 h.ipv4.ttl
	and m.MainDeparserT_deparser_tmp_30 0xFF
	mov m.MainDeparserT_deparser_tmp_31 m.MainDeparserT_deparser_tmp_28
	or m.MainDeparserT_deparser_tmp_31 m.MainDeparserT_deparser_tmp_30
	mov m.MainDeparserT_deparser_tmp_33 m.MainDeparserT_deparser_tmp_31
	shl m.MainDeparserT_deparser_tmp_33 0x8
	mov m.MainDeparserT_deparser_tmp_35 h.ipv4.protocol
	and m.MainDeparserT_deparser_tmp_35 0xFF
	mov m.MainDeparserT_deparser_word4 m.MainDeparserT_deparser_tmp_33
	or m.MainDeparserT_deparser_word4 m.MainDeparserT_deparser_tmp_35
	mov h.dpdk_pseudo_header.pseudo m.MainDeparserT_deparser_word1
	mov h.dpdk_pseudo_header.pseudo_0 m.MainDeparserT_deparser_word4
	ckadd h.cksum_state.state_0 h.dpdk_pseudo_header.pseudo
	ckadd h.cksum_state.state_0 h.ipv4.totalLen
	ckadd h.cksum_state.state_0 h.ipv4.identification
	ckadd h.cksum_state.state_0 h.dpdk_pseudo_header.pseudo_0
	ckadd h.cksum_state.state_0 h.ipv4.srcAddr
	ckadd h.cksum_state.state_0 h.ipv4.dstAddr
	mov h.ipv4.hdrChecksum h.cksum_state.state_0
	emit h.ethernet
	emit h.ipv4
	emit h.tcp
	tx m.pna_main_output_metadata_output_port
}


