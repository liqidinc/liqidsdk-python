# File: constants.py
#
# Copyright (c) 2022 Liqid, Inc. All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are not permitted without prior consent.
#
# Liqid SDK - Version 3.2.0
# This file was automatically generated - do not modify it directly.
#

"""
BackupDestination enumeration constants
Indicates the backup destination
"""
BackupDestinationLocal = 0
BackupDestinationRemote = 1

"""
ConfigurationFileSection enumeration constants
Describes a type of configuration file section
"""
ConfigurationFileSectionEnclosure = "enclosure"
ConfigurationFileSectionCPU = "cpu"

"""
ConfigurationFileType enumeration constants
Describes a type of configuration file
"""
ConfigurationFileTypeSlurm = "slurm"
ConfigurationFileTypeKubernetes = "kubernetes"
ConfigurationFileTypeRedfish = "redfish"
ConfigurationFileTypeVAPI = "vapi"
ConfigurationFileTypeIPMI = "ipmi"

"""
DeviceType enumeration constants
Represents a particular device type as a short string.
Note that redundant but differing values are not represented here.
This includes iba, fch, ramd, scm, vic, enc, nof, gof, pcpu, ncpu, gcpu
"""
DeviceTypeEnclosure = "encl"
DeviceTypeEthernet = "eth"
DeviceTypeLink = "link"
DeviceTypeMemory = "mem"
DeviceTypeNetwork = "nic"
DeviceTypeInfiniband1 = "infi"
DeviceTypeInfiniband2 = "iba"
DeviceTypeSSD = "ssd"
DeviceTypeTarget = "targ"
DeviceTypePLX = "plx"
DeviceTypeCompute = "compute"
DeviceTypeCPU = "cpu"
DeviceTypeGPU = "gpu"
DeviceTypeGCPU = "gcpu"
DeviceTypeFiberChannel1 = "fibr"
DeviceTypeFiberChannel2 = "fch"
DeviceTypeFPGA = "fpga"

"""
FabricToggleCompositeOption enumeration constants
TODO
"""
FabricToggleCompositeOptionAdd = "add"

"""
FabricType enumeration constants
Describes a particular fabric topology type
"""
FabricTypeGen3 = "gen3"
FabricTypeGen4 = "gen4"
FabricTypeNVOverFabric = "nvof"
FabricTypeGPUOverFabric = "gpuof"
FabricTypeGenZ = "genz"
FabricTypeNVMEOverFabric = "nvmeof"
FabricTypeIPBased = "ip_based"

"""
ImageType enumeration constants
Describes a type of software image file
"""
ImageTypeBoot = "boot"
ImageTypeFPGA = "fpga"
ImageTypeVNIC = "vnic"
ImageTypeUpgrade = "upgrade"
ImageTypeApplication = "application"

"""
LogType enumeration constants
Describes a log file type
"""
LogTypeSystem = "system"
LogTypeLiqid = "liqid"
LogTypeCombined = "combined"

"""
ManageableType enumeration constants
Describes a type of manageable entity
"""
ManageableTypeDevice = "ManageableDevice"
ManageableTypeCpuIpmiNetwork = "ManageableCpuIpmiNetworkConfig"
ManageableTypeEnclosureIpmiNetwork = "ManageableDeviceIpmiNetworkConfig"

"""
NorthboundApplicationType enumeration constants
Describes a northbound application type
"""
NorthboundApplicationTypeSlurm = "slurm"
NorthboundApplicationTypeKubernetes = "kubernetes"
NorthboundApplicationTypeRedfish = "redfish"
NorthboundApplicationTypeVAPI = "vapi"
NorthboundApplicationTypeIPMI = "ipmi"

"""
OperatingSystemType enumeration constants
Describes an operating system
"""
OperatingSystemTypeLinux = "linux"
OperatingSystemTypeFreeBSD = "FreeBSD"
OperatingSystemTypeWindows = "windows"
OperatingSystemTypeLiqidOS = "liqidos"
OperatingSystemTypeMaxOSX = "Apple Inc. Mac(TM) OSX operating system"
OperatingSystemTypeUnknown = "unknown"

"""
P2PType enumeration constants
Indicates whether P2P is enabled
"""
P2PTypeOff = "off"
P2PTypeOn = "on"

"""
RunType enumeration constants
Describes the various run states for liqid
"""
RunTypeUp = "up"
RunTypeOn = "on"
RunTypeOff = "off"
RunTypeUnknown = "unknown"

"""
ToggleFlag enumeration constants
TODO
"""
ToggleFlagPermanent = "perm"
ToggleFlagDisappear = "disappear"
ToggleFlagActive = "active"
ToggleFlagHidden = "hidden"

"""
ToggleState enumeration constants
Describes a binary state of enablement/disablement
"""
ToggleStateEnabled = "enabled"
ToggleStateDisabled = "disabled"

"""
TokenType enumeration constants
A subset of DeviceType values used exclusively with tokens
"""
TokenTypeTarget = "targ"
TokenTypeLink = "link"
TokenTypeGPU = "gpu"
TokenTypeFPGA = "fpga"
