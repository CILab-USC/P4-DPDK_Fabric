<header class="hkb-article__header">
				<h1 class="hkb-article__title" itemprop="headline">Virtual Labs on P4-DPDK</h1>
			</header>
   
<body class="ht_kb-template-default single single-ht_kb postid-5016 single-format-standard wp-embed-responsive ht-kb" itemscope="" itemtype="https://schema.org/WebPage" data-spy="scroll" data-offset="30" data-target="#navtoc" data-new-gr-c-s-check-loaded="14.1196.0" data-gr-ext-installed="">
	
<p>Network packet processing faces significant performance challenges due to kernel overheads. These issues have become more pronounced with the rapid growth of network traffic, leading to performance limitations in packet processing. To address these challenges, the Data Plane Development Kit (DPDK) was developed. DPDK bypasses the kernel and operates directly in user space, offering significant improvements in performance and latency for packet processing tasks. However, DPDK's steep learning curve presents a barrier to entry for developers and network administrators. In recent years, P4 has emerged as a language specifically designed for expressing packet processing data paths. Building on this development, P4-DPDK has been introduced as a new technology that bridges P4 and DPDK. It allows developers to create P4 code which is then translated into a DPDK pipeline, combining the expressiveness of P4 with the performance benefits of DPDK. </p>

<p>The Cyberinfrastructure Lab (CILab) at the University of South Carolina (USC) has developed step-by-step hands-on lab experiments on DPDK using the P4 language. 
Topics include fundamentals of P4-DPDK, P4 building blocks in the PNA architecture, parser implementation in the data plane, populating match-action tables, and others. 
The learner will acquire expertise to create, test, and deploy P4-DPDK applications on custom topologies in FABRIC.</p>

<p>The <a href="https://github.com/CILab-USC/P4-DPDK_Fabric/tree/main">lab library</a> consists of the following experiments:</p>

<ul class="wp-block-list">
<li><a href="https://github.com/CILab-USC/P4-DPDK_Fabric/blob/main/lab1_creating_a_slice_with_a_P4DPDK_pipeline.ipynb">Lab 1</a> – 
  Creating a Slice with a P4-DPDK Pipeline: This lab provides an introduction to DPDK, a software-based packet processing acceleration tool. 
  It demonstrates how to build a topology using namespaces and provides an explanation of scripts needed to build a P4-DPDK pipeline.</li>

<li><a href="https://github.com/CILab-USC/P4-DPDK_Fabric/blob/main/lab2_P4_programmable_building_blocks_with_the_PNA_architecture.ipynb">Lab 2</a> – 
  P4 Program Building Blocks with the PNA Architecture: This lab provides guidance to the process of building the P4 coding blocks compatible with 
  the PNA architecture that will be compiled into a DPDK pipeline.</li>

<li><a href="https://github.com/CILab-USC/P4-DPDK_Fabric/blob/main/lab3_PNA_parser_implementation.ipynb">Lab 3</a> – 
  PNA Parser Implementation: This lab starts by describing how to define custom headers in a P4 program and then explains how to implement a simple parser that parses the defined headers.</li>

<li><a href="https://github.com/CILab-USC/P4-DPDK_Fabric/blob/main/lab4_introduction_to_match_action_tables_1.ipynb">Lab 4</a> – 
  Introduction to Match-action Tables (Part 1): This lab describes match-action tables explaining the exact matching that can be performed on keys and also highlights the importance of the add_on_miss feature.</li>

<li><a href="https://github.com/CILab-USC/P4-DPDK_Fabric/blob/main/lab5_introduction_to_match_action_tables_2.ipynb">Lab 5</a> – 
  Introduction to Match-action Tables (Part 2): This lab describes match-action tables with the different types of matching that can be performed on keys and how to define them in a P4 program.</li>

<li><a href="https://github.com/CILab-USC/P4-DPDK_Fabric/blob/main/lab6_populating_and_managing_match_action_tables_at_runtime.ipynb">Lab 6</a> – 
  Populating and Managing Match-action Tables at Runtime: This describes how to populate and manage match-action tables at runtime.</li>

<li><a href="https://github.com/CILab-USC/P4-DPDK_Fabric/blob/main/lab7_checksum_recalculation_and_packet_deparsing.ipynb">Lab 7</a> – 
  Checksum Recalculation and Packet Deparsing: This lab describes how to recompute the checksum of a header. 
  Recomputing the checksum is necessary if the packet header was modified by the P4 program.</li>

<li><a href="https://github.com/CILab-USC/P4-DPDK_Fabric/blob/main/lab8_creating_a_slice_with_a_P4DPDK_pipeline_with_real_hardware.ipynb">Lab 8</a> – 
  Creating a Slice with a P4-DPDK Pipeline Running on Real Hardware: This lab provides an introduction to DPDK and demonstrates how to build a topology using real hardware NICs.</li>

<li><a href="https://github.com/CILab-USC/P4-DPDK_Fabric/blob/main/lab9_P4DPDK_pipeline_multicore_processing.ipynb">Lab 9</a> – 
  P4-DPDK Pipeline Multicore Processing: This lab shows how to parallelize packet processing by running multiple P4-DPDK pipeline each on a different CPU core to enhance performance.</li>

</ul>

<p><strong>Acknowledgements</strong></p>



<p><em>The P4-DPDK documentation and notebooks are provided by The Cyberinfrastructure Lab at the University of South Carolina (<a href="https://research.cec.sc.edu/cyberinfra">https://research.cec.sc.edu/cyberinfra</a>). This work is in part funded by NSF grants #2417823 and #2118311.</em></p>



<figure class="wp-block-image size-full is-resized"><img decoding="async" src="https://learn.fabric-testbed.net/wp-content/uploads/2023/08/usc-logo.png" alt="" class="wp-image-5021" style="width:311px;height:81px" width="311" height="81" srcset="https://learn.fabric-testbed.net/wp-content/uploads/2023/08/usc-logo.png 486w, https://learn.fabric-testbed.net/wp-content/uploads/2023/08/usc-logo-300x78.png 300w, https://learn.fabric-testbed.net/wp-content/uploads/2023/08/usc-logo-50x13.png 50w, https://learn.fabric-testbed.net/wp-content/uploads/2023/08/usc-logo-60x16.png 60w, https://learn.fabric-testbed.net/wp-content/uploads/2023/08/usc-logo-100x26.png 100w" sizes="(max-width: 311px) 100vw, 311px"></figure>

			
