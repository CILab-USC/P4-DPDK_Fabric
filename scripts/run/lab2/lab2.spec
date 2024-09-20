
struct ethernet_t {
	bit<48> dstAddr
	bit<48> srcAddr
	bit<16> etherType
}

struct metadata {
	bit<32> pna_main_input_metadata_input_port
	bit<32> pna_main_output_metadata_output_port
}
metadata instanceof metadata

header ethernet instanceof ethernet_t

regarray direction size 0x100 initval 0
apply {
	rx m.pna_main_input_metadata_input_port
	extract h.ethernet
	jmpneq LABEL_FALSE m.pna_main_input_metadata_input_port 0x0
	mov m.pna_main_output_metadata_output_port 0x1
	jmp LABEL_END
	LABEL_FALSE :	jmpneq LABEL_END m.pna_main_input_metadata_input_port 0x1
	mov m.pna_main_output_metadata_output_port 0x0
	LABEL_END :	emit h.ethernet
	tx m.pna_main_output_metadata_output_port
}


