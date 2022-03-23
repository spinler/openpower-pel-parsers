from pel.peltool.pel_types import TransmissionState

"""
Creator IDs
"""
creatorIDs = {"B": "Hostboot", "C": "HMC", "H": "PHYP", "K": "Sapphire",
              "L": "Partition FW", "M": "I/O Drawer", "O": "BMC",
              "P": "PowerNV", "S": "SLIC",  "T": "OCC"}


"""
The possible values for the subsystem field  in the User Header.
"""
subsystemValues = {
    0x10: ("processor", "Processor"),
    0x11: ("processor_fru", "Processor FRU"),
    0x12: ("processor_chip", "Processor Chip Cache"),
    0x13: ("processor_unit", "Processor Unit (CPU)"),
    0x14: ("processor_bus", "Processor Bus Controller"),

    0x20: ("memory", "Memory "),
    0x21: ("memory_ctlr", "Memory Controller"),
    0x22: ("memory_bus", "Memory Bus Interface"),
    0x23: ("memory_dimm", "Memory DIMM"),
    0x24: ("memory_fru", "Memory Card/FRU"),
    0x25: ("external_cache", "External Cache"),

    0x30: ("io", "I/O"),
    0x31: ("io_hub", "I/O Hub"),
    0x32: ("io_bridge", "I/O Bridge"),
    0x33: ("io_bus", "I/O bus interface"),
    0x34: ("io_processor", "I/O Processor"),
    0x35: ("io_hub_other", "SMA Hub"),
    0x38: ("phb", "PCI Bridge Chip"),

    0x40: ("io_adapter", "I/O Adapter"),
    0x41: ("io_adapter_comm", "I/O Adapter Communication"),
    0x46: ("io_device", "I/O Device"),
    0x47: ("io_device_dasd", "I/O Device Disk"),
    0x4C: ("io_external_general", "I/O External Peripheral"),
    0x4D: ("io_external_workstation",
           "I/O External Peripheral Local Work Station"),
    0x4E: ("io_storage_mezz", "I/O Storage Mezza Expansion"),

    0x50: ("cec_hardware", "CEC Hardware"),
    0x51: ("cec_sp_a", "CEC Hardware - Service Processor A"),
    0x52: ("cec_sp_b", "CEC Hardware - Service Processor B"),
    0x53: ("cec_node_controller", "CEC Hardware - Node Controller"),
    0x55: ("cec_vpd", "CEC Hardware - VPD Interface"),
    0x56: ("cec_i2c", "CEC Hardware - I2C Devices"),
    0x57: ("cec_chip_iface", "CEC Hardware - CEC Chip Interface"),
    0x58: ("cec_clocks", "CEC Hardware - Clock"),
    0x59: ("cec_op_panel", "CEC Hardware - Operator Panel"),
    0x5A: ("cec_tod", "CEC Hardware - Time-Of-Day Hardware"),
    0x5B: ("cec_storage_device", "CEC Hardware - Memory Device"),
    0x5C: ("cec_sp_hyp_iface",
           "CEC Hardware - Hypervisor<->Service Processor Interface"),
    0x5D: ("cec_service_network", "CEC Hardware - Service Network"),
    0x5E: ("cec_sp_hostboot_iface",
           "CEC Hardware - Hostboot-Service Processor Interface"),

    0x60: ("power", "Power/Cooling"),
    0x61: ("power_supply", "Power Supply"),
    0x62: ("power_control_hw", "Power Control Hardware"),
    0x63: ("power_fans", "Fan (AMD)"),
    0x64: ("power_sequencer", "Digital Power Supply"),

    0x70: ("others", "Miscellaneous"),
    0x71: ("other_hmc", "HMC & Hardware"),
    0x72: ("other_test_tool", "Test Tool"),
    0x73: ("other_media", "Removable Media"),
    0x74: ("other_multiple_subsystems", "Multiple Subsystems"),
    0x75: ("other_na", "Not Applicable"),
    0x76: ("other_info_src", "Miscellaneous"),

    0x7A: ("surv_hyp_lost_sp",
           "Hypervisor lost communication with service processor"),
    0x7B: ("surv_sp_lost_hyp",
           "Service processor lost communication with Hypervisor"),
    0x7C: ("surv_sp_lost_hmc", "Service processor lost communication with HMC"),
    0x7D: ("surv_hmc_lost_lpar",
           "HMC lost communication with logical partition"),
    0x7E: ("surv_hmc_lost_bpa", "HMC lost communication with BPA"),
    0x7F: ("surv_hmc_lost_hmc", "HMC lost communication with another HMC"),

    0x80: ("platform_firmware", "Platform Firmware"),
    0x81: ("sp_firmware", "Service Processor Firmware"),
    0x82: ("hyp_firmware", "System Hypervisor Firmware"),
    0x83: ("partition_firmware", "Partition Firmware"),
    0x84: ("slic_firmware", "SLIC Firmware"),
    0x85: ("spcn_firmware", "System Power Control Network Firmware"),
    0x86: ("bulk_power_firmware_side_a", "Bulk Power Firmware Side A"),
    0x87: ("hmc_code_firmware", "HMC Code"),
    0x88: ("bulk_power_firmware_side_b", "Bulk Power Firmware Side B"),
    0x89: ("virtual_sp", "Virtual Service Processor Firmware"),
    0x8A: ("hostboot", "HostBoot"),
    0x8B: ("occ", "OCC"),
    0x8D: ("bmc_firmware", "BMC Firmware"),

    0x90: ("software", "Software"),
    0x91: ("os_software", "Operating System software"),
    0x92: ("xpf_software", "XPF software"),
    0x93: ("app_software", "Application software"),

    0xA0: ("ext_env", "External Environment"),
    0xA1: ("input_power_source", "Input Power Source (ac)"),
    0xA2: ("ambient_temp", "Room Ambient Temperature"),
    0xA3: ("user_error", "User Error"),
    0xA4: ("corrosion", "Corrosion")}


"""
The possible values for the Event Scope field in the User Header.
"""
eventScopeValues = {
    0x01: ("single_partition", "Single Partition"),
    0x02: ("multiple_partitions", "Multiple Partitions"),
    0x03: ("entire_platform", "Entire Platform"),
    0x04: ("possibly_multiple_platforms", "Multiple Platforms")}


"""
The possible values for the Event Type field in the User Header.
"""
eventTypeValues = {
    0x00: ("na", "Not Applicable"),
    0x01: ("misc_information_only", "Miscellaneous, Informational Only"),
    0x02: ("tracing_event", "Tracing Event"),
    0x08: ("dump_notification", "Dump Notification"),
    0x30: ("env_normal", "Customer environmental problem back to normal")}


"""
The possible values for the severity field in the User Header.
"""
severityValues = {
    0x00: ("non_error", "Informational Event"),

    0x10: ("recovered", "Recovered Error"),
    0x20: ("predictive", "Predictive Error"),
    0x21: ("predictive_degraded_perf",
           "Predictive Error, Degraded Performance"),
    0x22: ("predictive_reboot", "Predictive Error, Correctable"),
    0x23: ("predictive_reboot_degraded",
           "Predictive Error, Correctable, Degraded"),
    0x24: ("predictive_redundancy_loss", "Predictive Error, Redundancy Lost"),

    0x40: ("unrecoverable", "Unrecoverable Error"),
    0x41: ("unrecoverable_degraded_perf",
           "Unrecoverable Error, Degraded Performance"),
    0x44: ("unrecoverable_redundancy_loss",
           "Unrecoverable Error, Loss of Redundancy"),
    0x45: ("unrecoverable_redundancy_loss_perf",
           "Unrecoverable, Loss of Redundancy + Performance"),
    0x48: ("unrecoverable_loss_of_function",
           "Unrecoverable Error, Loss of Function"),

    0x50: ("critical", "Critical Error, Scope of Failure unknown"),
    0x51: ("critical_system_term", "Critical Error, System Termination"),
    0x52: ("critical_imminent_failure",
           "Critical Error, System Failure likely or imminent"),
    0x53: ("critical_partition_term",
           "Critical Error, Partition(s) Termination"),
    0x54: ("critical_partition_imminent_failure",
           "Critical Error, Partition(s) Failure likely or imminent"),

    0x60: ("diagnostic_error", "Error detected during diagnostic test"),
    0x61: ("diagnostic_error_incorrect_results",
           "Diagostic error, resource w/incorrect results"),

    0x71: ("symptom_recovered", "Symptom Recovered"),
    0x72: ("symptom_predictive", "Symptom Predictive"),
    0x74: ("symptom_unrecoverable", "Symptom Unrecoverable"),
    0x75: ("symptom_critical", "Symptom Critical"),
    0x76: ("symptom_diag_err", "Symptom Diag Err")}


"""
The possible values for the Action Flags field in the User Header.
"""
actionFlagsValues = {
    0x8000: ("service_action", "Service Action Required"),
    0x4000: ("hidden", "Event not customer viewable"),
    0x2000: ("report", "Report Externally"),
    0x1000: ("dont_report", "Do Not Report To Hypervisor"),
    0x0800: ("call_home", "HMC Call Home"),
    0x0400: ("isolation_incomplete",
             "Isolation Incomplete, further analysis required"),
    0x0100: ("termination", "Service Processor Call Home Required")}

"""
Map for transmission states
"""
transmissionStates = {
    TransmissionState.newPEL.value: "Not Sent",
    TransmissionState.badPEL.value: "Rejected",
    TransmissionState.sent.value: "Sent",
    TransmissionState.acked.value: "Acked"}

"""
Map for Callout Failing Component Types
"""
failingComponentType = {
    0x10: "Normal Hardware FRU",
    0x20: "Code FRU",
    0x30: "Configuration error, configuration procedure required",
    0x40: "Maintenance Procedure Required",
    0x90: "External FRU",
    0xA0: "External Code FRU",
    0xB0: "Tool FRU",
    0xC0: "Symbolic FRU",
    0xE0: "Symbolic FRU with trusted location code"}

"""
The possible values for the Callout Priority field in the SRC.
"""
calloutPriorityValues = {
    0x48: ("high", "Mandatory, replace all with this type as a unit"),
    0x4D: ("medium", "Medium Priority"),
    0x41: ("medium_group_a", "Medium Priority A, replace these as a group"),
    0x42: ("medium_group_b", "Medium Priority B, replace these as a group"),
    0x43: ("medium_group_c", "Medium Priority C, replace these as a group"),
    0x4C: ("low", "Lowest priority replacement")}

"""
Map for Procedure Descriptions
"""
procedureDesc = {"TODO": "TODO"}
