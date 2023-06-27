# File: classes.py
#
# Copyright (c) 2022 Liqid, Inc. All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are not permitted without prior consent.
#
# Liqid SDK - Version 3.2.0
# This file was automatically generated - do not modify it directly.
#

from liqidsdk.constants import *


class AsynchronousInfo:
    """
    Reports an identifier of an asynchronous operation
    """

    def __init__(self):
        self.AsynchronousId = None
        self.DeviceId = None

    def __str__(self):
        s = '{'
        s += 'AsynchronousId: ' + str(self.AsynchronousId)
        s += ', ' + 'DeviceId: ' + str(self.DeviceId)
        s += '}'
        return s

    def __repr__(self):
        return self.__str__()

    def from_dictionary(self, source):
        """
        Populates an object from the given dictionary
        :param source: Dictionary containing a representation of a JSON object
        :return: This object after being populated from the source dictionary
        """
        if 'async_id' in source:
            self.AsynchronousId = source['async_id']
        if 'device_id' in source:
            self.DeviceId = source['device_id']
        return self

    def to_dictionary(self):
        """
        Creates a dictionary and populates it from this object in a manner
        consistent with JSON conventions
        :return: dictionary object
        """
        result = dict()
        result['async_id'] = self.AsynchronousId
        result['device_id'] = self.DeviceId
        return result


class AsynchronousStatus:
    """
    Reports the status of an asynchronous operation
    """

    def __init__(self):
        self.ExecutionState = None
        self.DeviceId = None
        self.ExecutionDateTime = None

    def __str__(self):
        s = '{'
        s += 'ExecutionState: ' + str(self.ExecutionState)
        s += ', ' + 'DeviceId: ' + str(self.DeviceId)
        s += ', ' + 'ExecutionDateTime: ' + str(self.ExecutionDateTime)
        s += '}'
        return s

    def __repr__(self):
        return self.__str__()

    def from_dictionary(self, source):
        """
        Populates an object from the given dictionary
        :param source: Dictionary containing a representation of a JSON object
        :return: This object after being populated from the source dictionary
        """
        if 'command_execution_state' in source:
            self.ExecutionState = source['command_execution_state']
        if 'device_id' in source:
            self.DeviceId = source['device_id']
        if 'execution_date' in source:
            self.ExecutionDateTime = source['execution_date']
        return self

    def to_dictionary(self):
        """
        Creates a dictionary and populates it from this object in a manner
        consistent with JSON conventions
        :return: dictionary object
        """
        result = dict()
        result['command_execution_state'] = self.ExecutionState
        result['device_id'] = self.DeviceId
        result['execution_date'] = self.ExecutionDateTime
        return result


class AvailableCoordinates:
    """
    A description of an available REST target including IP addressing information and Liqid Coordinates
    """

    def __init__(self):
        self.IPAddress = None
        self.PortNumber = None
        self.Coordinates = Coordinates()

    def __str__(self):
        s = '{'
        s += 'IPAddress: ' + str(self.IPAddress)
        s += ', ' + 'PortNumber: ' + str(self.PortNumber)
        s += ', ' + 'Coordinates: ' + str(self.Coordinates)
        s += '}'
        return s

    def __repr__(self):
        return self.__str__()

    def from_dictionary(self, source):
        """
        Populates an object from the given dictionary
        :param source: Dictionary containing a representation of a JSON object
        :return: This object after being populated from the source dictionary
        """
        if 'address' in source:
            self.IPAddress = source['address']
        if 'port' in source:
            self.PortNumber = source['port']
        if 'coordinates' in source and source['coordinates'] is not None:
            self.Coordinates = Coordinates().from_dictionary(source['coordinates'])
        return self

    def to_dictionary(self):
        """
        Creates a dictionary and populates it from this object in a manner
        consistent with JSON conventions
        :return: dictionary object
        """
        result = dict()
        result['address'] = self.IPAddress
        result['port'] = self.PortNumber
        result['coordinates'] = self.Coordinates.to_dictionary()
        return result


class BackupResult:
    """
    Backups up the Director configuration
    """

    def __init__(self):
        self.CommandLine = None
        self.StandardOutput = None
        self.StandardError = None
        self.ExitValue = None

    def __str__(self):
        s = '{'
        s += 'CommandLine: ' + str(self.CommandLine)
        s += ', ' + 'StandardOutput: ' + str(self.StandardOutput)
        s += ', ' + 'StandardError: ' + str(self.StandardError)
        s += ', ' + 'ExitValue: ' + str(self.ExitValue)
        s += '}'
        return s

    def __repr__(self):
        return self.__str__()

    def from_dictionary(self, source):
        """
        Populates an object from the given dictionary
        :param source: Dictionary containing a representation of a JSON object
        :return: This object after being populated from the source dictionary
        """
        if 'commandLine' in source:
            self.CommandLine = source['commandLine']
        if 'standardOutput' in source:
            self.StandardOutput = source['standardOutput']
        if 'standardError' in source:
            self.StandardError = source['standardError']
        if 'exitValue' in source:
            self.ExitValue = source['exitValue']
        return self

    def to_dictionary(self):
        """
        Creates a dictionary and populates it from this object in a manner
        consistent with JSON conventions
        :return: dictionary object
        """
        result = dict()
        result['commandLine'] = self.CommandLine
        result['standardOutput'] = self.StandardOutput
        result['standardError'] = self.StandardError
        result['exitValue'] = self.ExitValue
        return result


class Coordinates:
    """
    Describes a unique Liqid coordinate.
    Most of the members of this entity are obsolete.
    """

    def __init__(self):
        self.Rack = 0
        self.Shelf = 0
        self.Node = None

    def __str__(self):
        s = '{'
        s += 'Rack: ' + str(self.Rack)
        s += ', ' + 'Shelf: ' + str(self.Shelf)
        s += ', ' + 'Node: ' + str(self.Node)
        s += '}'
        return s

    def __repr__(self):
        return self.__str__()

    def from_dictionary(self, source):
        """
        Populates an object from the given dictionary
        :param source: Dictionary containing a representation of a JSON object
        :return: This object after being populated from the source dictionary
        """
        if 'rack' in source:
            self.Rack = source['rack']
        if 'shelf' in source:
            self.Shelf = source['shelf']
        if 'node' in source:
            self.Node = source['node']
        return self

    def to_dictionary(self):
        """
        Creates a dictionary and populates it from this object in a manner
        consistent with JSON conventions
        :return: dictionary object
        """
        result = dict()
        result['rack'] = self.Rack
        result['shelf'] = self.Shelf
        result['node'] = self.Node
        return result


class ConnectionHistory:
    """
    Describes one connection to a machine
    """

    def __init__(self):
        self.AttachTime = None
        self.DeviceType = None
        self.DetachTime = None
        self.FabricGlobalId = None
        self.Free = None
        self.Name = None
        self.OwnerGlobalId = None
        self.UserDescription = None

    def __str__(self):
        s = '{'
        s += 'AttachTime: ' + str(self.AttachTime)
        s += ', ' + 'DeviceType: ' + str(self.DeviceType)
        s += ', ' + 'DetachTime: ' + str(self.DetachTime)
        s += ', ' + 'FabricGlobalId: ' + str(self.FabricGlobalId)
        s += ', ' + 'Free: ' + str(self.Free)
        s += ', ' + 'Name: ' + str(self.Name)
        s += ', ' + 'OwnerGlobalId: ' + str(self.OwnerGlobalId)
        s += ', ' + 'UserDescription: ' + str(self.UserDescription)
        s += '}'
        return s

    def __repr__(self):
        return self.__str__()

    def from_dictionary(self, source):
        """
        Populates an object from the given dictionary
        :param source: Dictionary containing a representation of a JSON object
        :return: This object after being populated from the source dictionary
        """
        if 'atime' in source:
            self.AttachTime = source['atime']
        if 'dev_type' in source:
            self.DeviceType = source['dev_type']
        if 'dtime' in source:
            self.DetachTime = source['dtime']
        if 'fabr_gid' in source:
            self.FabricGlobalId = source['fabr_gid']
        if 'free' in source:
            self.Free = source['free']
        if 'name' in source:
            self.Name = source['name']
        if 'owner_gid' in source:
            self.OwnerGlobalId = source['owner_gid']
        if 'udesc' in source:
            self.UserDescription = source['udesc']
        return self

    def to_dictionary(self):
        """
        Creates a dictionary and populates it from this object in a manner
        consistent with JSON conventions
        :return: dictionary object
        """
        result = dict()
        result['atime'] = self.AttachTime
        result['dev_type'] = self.DeviceType
        result['dtime'] = self.DetachTime
        result['fabr_gid'] = self.FabricGlobalId
        result['free'] = self.Free
        result['name'] = self.Name
        result['owner_gid'] = self.OwnerGlobalId
        result['udesc'] = self.UserDescription
        return result


class Credentials:
    """
    Contains credentials necessary for managing some managed entity within the configuration (such as via IPMI)
    """

    def __init__(self):
        self.Principal = None
        self.Password = None

    def __str__(self):
        s = '{'
        s += 'Principal: ' + str(self.Principal)
        s += ', ' + 'Password: ' + str(self.Password)
        s += '}'
        return s

    def __repr__(self):
        return self.__str__()

    def from_dictionary(self, source):
        """
        Populates an object from the given dictionary
        :param source: Dictionary containing a representation of a JSON object
        :return: This object after being populated from the source dictionary
        """
        if 'principal' in source:
            self.Principal = source['principal']
        if 'password' in source:
            self.Password = source['password']
        return self

    def to_dictionary(self):
        """
        Creates a dictionary and populates it from this object in a manner
        consistent with JSON conventions
        :return: dictionary object
        """
        result = dict()
        result['principal'] = self.Principal
        result['password'] = self.Password
        return result


class DeviceCounters:
    """
    Counts of discovered devices by device type
    """

    def __init__(self):
        self.CPUCount = None
        self.FPGACount = None
        self.GPUCount = None
        self.LinkCount = None
        self.PLXCount = None
        self.TargetCount = None

    def __str__(self):
        s = '{'
        s += 'CPUCount: ' + str(self.CPUCount)
        s += ', ' + 'FPGACount: ' + str(self.FPGACount)
        s += ', ' + 'GPUCount: ' + str(self.GPUCount)
        s += ', ' + 'LinkCount: ' + str(self.LinkCount)
        s += ', ' + 'PLXCount: ' + str(self.PLXCount)
        s += ', ' + 'TargetCount: ' + str(self.TargetCount)
        s += '}'
        return s

    def __repr__(self):
        return self.__str__()

    def from_dictionary(self, source):
        """
        Populates an object from the given dictionary
        :param source: Dictionary containing a representation of a JSON object
        :return: This object after being populated from the source dictionary
        """
        if 'comp_cnt' in source:
            self.CPUCount = source['comp_cnt']
        if 'fpga_cnt' in source:
            self.FPGACount = source['fpga_cnt']
        if 'gpu_cnt' in source:
            self.GPUCount = source['gpu_cnt']
        if 'link_cnt' in source:
            self.LinkCount = source['link_cnt']
        if 'plx_cnt' in source:
            self.PLXCount = source['plx_cnt']
        if 'targ_cnt' in source:
            self.TargetCount = source['targ_cnt']
        return self

    def to_dictionary(self):
        """
        Creates a dictionary and populates it from this object in a manner
        consistent with JSON conventions
        :return: dictionary object
        """
        result = dict()
        result['comp_cnt'] = self.CPUCount
        result['fpga_cnt'] = self.FPGACount
        result['gpu_cnt'] = self.GPUCount
        result['link_cnt'] = self.LinkCount
        result['plx_cnt'] = self.PLXCount
        result['targ_cnt'] = self.TargetCount
        return result


class DeviceInfo:
    """
    All information other than status, for a given device
    """

    def __init__(self):
        self.BusGeneration = None
        self.BusWidth = None
        self.DeviceClass = None
        self.ConnectionType = None
        self.DeviceIdentifier = None
        self.DeviceState = None
        self.DeviceType = None
        self.FabricGlobalId = None
        self.FabricType = None
        self.Family = None
        self.Flags = None
        self.FirmwareRevision = None
        self.Index = None
        self.Location = Coordinates()
        self.Model = None
        self.Name = None
        self.Owner = Coordinates()
        self.PartNumber = None
        self.PCIDeviceId = None
        self.PCIVendorId = None
        self.PodId = -1
        self.SerialNumber = None
        self.SledId = None
        self.UserDescription = None
        self.Unique = None
        self.Vendor = None

    def __str__(self):
        s = '{'
        s += 'BusGeneration: ' + str(self.BusGeneration)
        s += ', ' + 'BusWidth: ' + str(self.BusWidth)
        s += ', ' + 'DeviceClass: ' + str(self.DeviceClass)
        s += ', ' + 'ConnectionType: ' + str(self.ConnectionType)
        s += ', ' + 'DeviceIdentifier: ' + str(self.DeviceIdentifier)
        s += ', ' + 'DeviceState: ' + str(self.DeviceState)
        s += ', ' + 'DeviceType: ' + str(self.DeviceType)
        s += ', ' + 'FabricGlobalId: ' + str(self.FabricGlobalId)
        s += ', ' + 'FabricType: ' + str(self.FabricType)
        s += ', ' + 'Family: ' + str(self.Family)
        s += ', ' + 'Flags: ' + str(self.Flags)
        s += ', ' + 'FirmwareRevision: ' + str(self.FirmwareRevision)
        s += ', ' + 'Index: ' + str(self.Index)
        s += ', ' + 'Location: ' + str(self.Location)
        s += ', ' + 'Model: ' + str(self.Model)
        s += ', ' + 'Name: ' + str(self.Name)
        s += ', ' + 'Owner: ' + str(self.Owner)
        s += ', ' + 'PartNumber: ' + str(self.PartNumber)
        s += ', ' + 'PCIDeviceId: ' + str(self.PCIDeviceId)
        s += ', ' + 'PCIVendorId: ' + str(self.PCIVendorId)
        s += ', ' + 'PodId: ' + str(self.PodId)
        s += ', ' + 'SerialNumber: ' + str(self.SerialNumber)
        s += ', ' + 'SledId: ' + str(self.SledId)
        s += ', ' + 'UserDescription: ' + str(self.UserDescription)
        s += ', ' + 'Unique: ' + str(self.Unique)
        s += ', ' + 'Vendor: ' + str(self.Vendor)
        s += '}'
        return s

    def __repr__(self):
        return self.__str__()

    def from_dictionary(self, source):
        """
        Populates an object from the given dictionary
        :param source: Dictionary containing a representation of a JSON object
        :return: This object after being populated from the source dictionary
        """
        if 'busgen' in source:
            self.BusGeneration = source['busgen']
        if 'buswidth' in source:
            self.BusWidth = source['buswidth']
        if 'class' in source:
            self.DeviceClass = source['class']
        if 'conn_type' in source:
            self.ConnectionType = source['conn_type']
        if 'dev_id' in source:
            self.DeviceIdentifier = source['dev_id']
        if 'device_state' in source:
            self.DeviceState = source['device_state']
        if 'device_type' in source:
            self.DeviceType = source['device_type']
        if 'fabr_gid' in source:
            self.FabricGlobalId = source['fabr_gid']
        if 'fabric_type' in source:
            self.FabricType = source['fabric_type']
        if 'family' in source:
            self.Family = source['family']
        if 'flags' in source:
            self.Flags = source['flags']
        if 'fw_rev' in source:
            self.FirmwareRevision = source['fw_rev']
        if 'index' in source:
            self.Index = source['index']
        if 'location' in source and source['location'] is not None:
            self.Location = Coordinates().from_dictionary(source['location'])
        if 'model' in source:
            self.Model = source['model']
        if 'name' in source:
            self.Name = source['name']
        if 'owner' in source and source['owner'] is not None:
            self.Owner = Coordinates().from_dictionary(source['owner'])
        if 'part_num' in source:
            self.PartNumber = source['part_num']
        if 'pci_device' in source:
            self.PCIDeviceId = source['pci_device']
        if 'pci_vendor' in source:
            self.PCIVendorId = source['pci_vendor']
        if 'pod_id' in source:
            self.PodId = source['pod_id']
        if 'serial_num' in source:
            self.SerialNumber = source['serial_num']
        if 'sled_id' in source:
            self.SledId = source['sled_id']
        if 'udesc' in source:
            self.UserDescription = source['udesc']
        if 'unique' in source:
            self.Unique = source['unique']
        if 'vendor' in source:
            self.Vendor = source['vendor']
        return self

    def to_dictionary(self):
        """
        Creates a dictionary and populates it from this object in a manner
        consistent with JSON conventions
        :return: dictionary object
        """
        result = dict()
        result['busgen'] = self.BusGeneration
        result['buswidth'] = self.BusWidth
        result['class'] = self.DeviceClass
        result['conn_type'] = self.ConnectionType
        result['dev_id'] = self.DeviceIdentifier
        result['device_state'] = self.DeviceState
        result['device_type'] = self.DeviceType
        result['fabr_gid'] = self.FabricGlobalId
        result['fabric_type'] = self.FabricType
        result['family'] = self.Family
        result['flags'] = self.Flags
        result['fw_rev'] = self.FirmwareRevision
        result['index'] = self.Index
        result['location'] = self.Location.to_dictionary()
        result['model'] = self.Model
        result['name'] = self.Name
        result['owner'] = self.Owner.to_dictionary()
        result['part_num'] = self.PartNumber
        result['pci_device'] = self.PCIDeviceId
        result['pci_vendor'] = self.PCIVendorId
        result['pod_id'] = self.PodId
        result['serial_num'] = self.SerialNumber
        result['sled_id'] = self.SledId
        result['udesc'] = self.UserDescription
        result['unique'] = self.Unique
        result['vendor'] = self.Vendor
        return result


class DeviceStatus:
    """
    Status of a manageable device
    """

    def __init__(self):
        self.ConnectionType = None
        self.DeviceId = None
        self.DeviceState = None
        self.DeviceType = None
        self.PCIDeviceId = None
        self.GlobalId = None
        self.FabricId = None
        self.FabricType = None
        self.Flags = None
        self.Flags2 = None
        self.Index = None
        self.PCILaneCount = None
        self.Location = Coordinates()
        self.Name = None
        self.Owner = Coordinates()
        self.PodId = -1
        self.PortGlobalId = None
        self.SledId = None
        self.SwitchGlobalId = None
        self.DeviceStatusType = None
        self.PCIVendorId = None

    def __str__(self):
        s = '{'
        s += 'ConnectionType: ' + str(self.ConnectionType)
        s += ', ' + 'DeviceId: ' + str(self.DeviceId)
        s += ', ' + 'DeviceState: ' + str(self.DeviceState)
        s += ', ' + 'DeviceType: ' + str(self.DeviceType)
        s += ', ' + 'PCIDeviceId: ' + str(self.PCIDeviceId)
        s += ', ' + 'GlobalId: ' + str(self.GlobalId)
        s += ', ' + 'FabricId: ' + str(self.FabricId)
        s += ', ' + 'FabricType: ' + str(self.FabricType)
        s += ', ' + 'Flags: ' + str(self.Flags)
        s += ', ' + 'Flags2: ' + str(self.Flags2)
        s += ', ' + 'Index: ' + str(self.Index)
        s += ', ' + 'PCILaneCount: ' + str(self.PCILaneCount)
        s += ', ' + 'Location: ' + str(self.Location)
        s += ', ' + 'Name: ' + str(self.Name)
        s += ', ' + 'Owner: ' + str(self.Owner)
        s += ', ' + 'PodId: ' + str(self.PodId)
        s += ', ' + 'PortGlobalId: ' + str(self.PortGlobalId)
        s += ', ' + 'SledId: ' + str(self.SledId)
        s += ', ' + 'SwitchGlobalId: ' + str(self.SwitchGlobalId)
        s += ', ' + 'DeviceStatusType: ' + str(self.DeviceStatusType)
        s += ', ' + 'PCIVendorId: ' + str(self.PCIVendorId)
        s += '}'
        return s

    def __repr__(self):
        return self.__str__()

    def from_dictionary(self, source):
        """
        Populates an object from the given dictionary
        :param source: Dictionary containing a representation of a JSON object
        :return: This object after being populated from the source dictionary
        """
        if 'conn_type' in source:
            self.ConnectionType = source['conn_type']
        if 'dev_id' in source:
            self.DeviceId = source['dev_id']
        if 'device_state' in source:
            self.DeviceState = source['device_state']
        if 'device_type' in source:
            self.DeviceType = source['device_type']
        if 'did' in source:
            self.PCIDeviceId = source['did']
        if 'fabr_gid' in source:
            self.GlobalId = source['fabr_gid']
        if 'fabr_id' in source:
            self.FabricId = source['fabr_id']
        if 'fabric_type' in source:
            self.FabricType = source['fabric_type']
        if 'flags' in source:
            self.Flags = source['flags']
        if 'flags2' in source:
            self.Flags2 = source['flags2']
        if 'index' in source:
            self.Index = source['index']
        if 'lanes' in source:
            self.PCILaneCount = source['lanes']
        if 'location' in source and source['location'] is not None:
            self.Location = Coordinates().from_dictionary(source['location'])
        if 'name' in source:
            self.Name = source['name']
        if 'owner' in source and source['owner'] is not None:
            self.Owner = Coordinates().from_dictionary(source['owner'])
        if 'pod_id' in source:
            self.PodId = source['pod_id']
        if 'port_gid' in source:
            self.PortGlobalId = source['port_gid']
        if 'sled_id' in source:
            self.SledId = source['sled_id']
        if 'swit_gid' in source:
            self.SwitchGlobalId = source['swit_gid']
        if 'type' in source:
            self.DeviceStatusType = source['type']
        if 'vid' in source:
            self.PCIVendorId = source['vid']
        return self

    def to_dictionary(self):
        """
        Creates a dictionary and populates it from this object in a manner
        consistent with JSON conventions
        :return: dictionary object
        """
        result = dict()
        result['conn_type'] = self.ConnectionType
        result['dev_id'] = self.DeviceId
        result['device_state'] = self.DeviceState
        result['device_type'] = self.DeviceType
        result['did'] = self.PCIDeviceId
        result['fabr_gid'] = self.GlobalId
        result['fabr_id'] = self.FabricId
        result['fabric_type'] = self.FabricType
        result['flags'] = self.Flags
        result['flags2'] = self.Flags2
        result['index'] = self.Index
        result['lanes'] = self.PCILaneCount
        result['location'] = self.Location.to_dictionary()
        result['name'] = self.Name
        result['owner'] = self.Owner.to_dictionary()
        result['pod_id'] = self.PodId
        result['port_gid'] = self.PortGlobalId
        result['sled_id'] = self.SledId
        result['swit_gid'] = self.SwitchGlobalId
        result['type'] = self.DeviceStatusType
        result['vid'] = self.PCIVendorId
        return result


class DeviceTypeAndAttributes:
    """
    Describes the various attributes for a particular device type
    """

    def __init__(self):
        self.DeviceType = None
        self.Attributes = None

    def __str__(self):
        s = '{'
        s += 'DeviceType: ' + str(self.DeviceType)
        s += ', ' + 'Attributes: ' + str(self.Attributes)
        s += '}'
        return s

    def __repr__(self):
        return self.__str__()

    def from_dictionary(self, source):
        """
        Populates an object from the given dictionary
        :param source: Dictionary containing a representation of a JSON object
        :return: This object after being populated from the source dictionary
        """
        if 'deviceType' in source:
            self.DeviceType = source['deviceType']
        if 'attributes' in source:
            self.Attributes = source['attributes']
        return self

    def to_dictionary(self):
        """
        Creates a dictionary and populates it from this object in a manner
        consistent with JSON conventions
        :return: dictionary object
        """
        result = dict()
        result['deviceType'] = self.DeviceType
        result['attributes'] = self.Attributes
        return result


class DeviceUserDescription:
    """
    Wraps a user-provided description for a particular device
    """

    def __init__(self):
        self.UserDescription = None

    def __str__(self):
        s = '{'
        s += 'UserDescription: ' + str(self.UserDescription)
        s += '}'
        return s

    def __repr__(self):
        return self.__str__()

    def from_dictionary(self, source):
        """
        Populates an object from the given dictionary
        :param source: Dictionary containing a representation of a JSON object
        :return: This object after being populated from the source dictionary
        """
        if 'udesc' in source:
            self.UserDescription = source['udesc']
        return self

    def to_dictionary(self):
        """
        Creates a dictionary and populates it from this object in a manner
        consistent with JSON conventions
        :return: dictionary object
        """
        result = dict()
        result['udesc'] = self.UserDescription
        return result


class DigestInfo:
    """
    Describes information related to a newly-created digest message
    """

    def __init__(self):
        self.DigestId = None
        self.DigestKey = None
        self.DigestLabel = None

    def __str__(self):
        s = '{'
        s += 'DigestId: ' + str(self.DigestId)
        s += ', ' + 'DigestKey: ' + str(self.DigestKey)
        s += ', ' + 'DigestLabel: ' + str(self.DigestLabel)
        s += '}'
        return s

    def __repr__(self):
        return self.__str__()

    def from_dictionary(self, source):
        """
        Populates an object from the given dictionary
        :param source: Dictionary containing a representation of a JSON object
        :return: This object after being populated from the source dictionary
        """
        if 'digest_id' in source:
            self.DigestId = source['digest_id']
        if 'digest_key' in source:
            self.DigestKey = source['digest_key']
        if 'digest_label' in source:
            self.DigestLabel = source['digest_label']
        return self

    def to_dictionary(self):
        """
        Creates a dictionary and populates it from this object in a manner
        consistent with JSON conventions
        :return: dictionary object
        """
        result = dict()
        result['digest_id'] = self.DigestId
        result['digest_key'] = self.DigestKey
        result['digest_label'] = self.DigestLabel
        return result


class DiscoveryToken:
    """
    Describes a single discovery token
    """

    def __init__(self):
        self.Token = None
        self.Index = None

    def __str__(self):
        s = '{'
        s += 'Token: ' + str(self.Token)
        s += ', ' + 'Index: ' + str(self.Index)
        s += '}'
        return s

    def __repr__(self):
        return self.__str__()

    def from_dictionary(self, source):
        """
        Populates an object from the given dictionary
        :param source: Dictionary containing a representation of a JSON object
        :return: This object after being populated from the source dictionary
        """
        if 'discovery_token' in source:
            self.Token = source['discovery_token']
        if 'index' in source:
            self.Index = source['index']
        return self

    def to_dictionary(self):
        """
        Creates a dictionary and populates it from this object in a manner
        consistent with JSON conventions
        :return: dictionary object
        """
        result = dict()
        result['discovery_token'] = self.Token
        result['index'] = self.Index
        return result


class FabricItem:
    """
    Describes a Liqid entity, the aggregate of which comprises the fabric.
    """

    def __init__(self):
        self.Name = None
        self.Id = None
        self.ParentId = None
        self.DeviceType = None
        self.HardwareComponent = HardwareComponent()

    def __str__(self):
        s = '{'
        s += 'Name: ' + str(self.Name)
        s += ', ' + 'Id: ' + str(self.Id)
        s += ', ' + 'ParentId: ' + str(self.ParentId)
        s += ', ' + 'DeviceType: ' + str(self.DeviceType)
        s += ', ' + 'HardwareComponent: ' + str(self.HardwareComponent)
        s += '}'
        return s

    def __repr__(self):
        return self.__str__()

    def from_dictionary(self, source):
        """
        Populates an object from the given dictionary
        :param source: Dictionary containing a representation of a JSON object
        :return: This object after being populated from the source dictionary
        """
        if 'name' in source:
            self.Name = source['name']
        if 'id' in source:
            self.Id = source['id']
        if 'parentId' in source:
            self.ParentId = source['parentId']
        if 'deviceType' in source:
            self.DeviceType = source['deviceType']
        if 'hardwareComponent' in source and source['hardwareComponent'] is not None:
            self.HardwareComponent = HardwareComponent().from_dictionary(source['hardwareComponent'])
        return self

    def to_dictionary(self):
        """
        Creates a dictionary and populates it from this object in a manner
        consistent with JSON conventions
        :return: dictionary object
        """
        result = dict()
        result['name'] = self.Name
        result['id'] = self.Id
        result['parentId'] = self.ParentId
        result['deviceType'] = self.DeviceType
        result['hardwareComponent'] = self.HardwareComponent.to_dictionary()
        return result


class FabricToggleComposite:
    """
    Describes the result of a fabric change operation
    """

    def __init__(self):
        self.Coordinates = Coordinates()
        self.ControlFlag = NameValuePair()
        self.Options = None

    def __str__(self):
        s = '{'
        s += 'Coordinates: ' + str(self.Coordinates)
        s += ', ' + 'ControlFlag: ' + str(self.ControlFlag)
        s += ', ' + 'Options: ' + str(self.Options)
        s += '}'
        return s

    def __repr__(self):
        return self.__str__()

    def from_dictionary(self, source):
        """
        Populates an object from the given dictionary
        :param source: Dictionary containing a representation of a JSON object
        :return: This object after being populated from the source dictionary
        """
        if 'coordinates' in source and source['coordinates'] is not None:
            self.Coordinates = Coordinates().from_dictionary(source['coordinates'])
        if 'flag' in source and source['flag'] is not None:
            self.ControlFlag = NameValuePair().from_dictionary(source['flag'])
        if 'options' in source:
            self.Options = source['options']
        return self

    def to_dictionary(self):
        """
        Creates a dictionary and populates it from this object in a manner
        consistent with JSON conventions
        :return: dictionary object
        """
        result = dict()
        result['coordinates'] = self.Coordinates.to_dictionary()
        result['flag'] = self.ControlFlag.to_dictionary()
        result['options'] = self.Options
        return result


class Group:
    """
    Describes a configured group which contains a free device pool and some number of configured machines.
    This struct does not contain information regarding the related entities; that information must be obtained via other functions/methods.
    """

    def __init__(self):
        self.FabricId = None
        self.GroupId = None
        self.GroupName = None
        self.PodId = -1

    def __str__(self):
        s = '{'
        s += 'FabricId: ' + str(self.FabricId)
        s += ', ' + 'GroupId: ' + str(self.GroupId)
        s += ', ' + 'GroupName: ' + str(self.GroupName)
        s += ', ' + 'PodId: ' + str(self.PodId)
        s += '}'
        return s

    def __repr__(self):
        return self.__str__()

    def from_dictionary(self, source):
        """
        Populates an object from the given dictionary
        :param source: Dictionary containing a representation of a JSON object
        :return: This object after being populated from the source dictionary
        """
        if 'fabr_id' in source:
            self.FabricId = source['fabr_id']
        if 'grp_id' in source:
            self.GroupId = source['grp_id']
        if 'group_name' in source:
            self.GroupName = source['group_name']
        if 'pod_id' in source:
            self.PodId = source['pod_id']
        return self

    def to_dictionary(self):
        """
        Creates a dictionary and populates it from this object in a manner
        consistent with JSON conventions
        :return: dictionary object
        """
        result = dict()
        result['fabr_id'] = self.FabricId
        result['grp_id'] = self.GroupId
        result['group_name'] = self.GroupName
        result['pod_id'] = self.PodId
        return result


class GroupComputeDeviceRelator:
    """
    Describes a relation between a group and a compute device
    """

    def __init__(self):
        self.DeviceStatus = ComputeDeviceStatus()
        self.Group = Group()

    def __str__(self):
        s = '{'
        s += 'DeviceStatus: ' + str(self.DeviceStatus)
        s += ', ' + 'Group: ' + str(self.Group)
        s += '}'
        return s

    def __repr__(self):
        return self.__str__()

    def from_dictionary(self, source):
        """
        Populates an object from the given dictionary
        :param source: Dictionary containing a representation of a JSON object
        :return: This object after being populated from the source dictionary
        """
        if 'deviceStatus' in source and source['deviceStatus'] is not None:
            self.DeviceStatus = ComputeDeviceStatus().from_dictionary(source['deviceStatus'])
        if 'group' in source and source['group'] is not None:
            self.Group = Group().from_dictionary(source['group'])
        return self

    def to_dictionary(self):
        """
        Creates a dictionary and populates it from this object in a manner
        consistent with JSON conventions
        :return: dictionary object
        """
        result = dict()
        result['deviceStatus'] = self.DeviceStatus.to_dictionary()
        result['group'] = self.Group.to_dictionary()
        return result


class GroupDetails:
    """
    Contains statistical information which is accumulated for the group.
    Does not contain relations with devices; that information resides in the various device relators.
    """

    def __init__(self):
        self.GroupId = None
        self.GroupName = None
        self.CpuFrequency = None
        self.CpuCount = None
        self.CpuLanes = None
        self.CpuCoreCount = None
        self.TotalDRAM = None
        self.NetworkAdapterCount = None
        self.TotalThroughput = None
        self.StorageDriveCount = None
        self.TotalCapacity = None
        self.GPUCores = None
        self.TotalMachines = None

    def __str__(self):
        s = '{'
        s += 'GroupId: ' + str(self.GroupId)
        s += ', ' + 'GroupName: ' + str(self.GroupName)
        s += ', ' + 'CpuFrequency: ' + str(self.CpuFrequency)
        s += ', ' + 'CpuCount: ' + str(self.CpuCount)
        s += ', ' + 'CpuLanes: ' + str(self.CpuLanes)
        s += ', ' + 'CpuCoreCount: ' + str(self.CpuCoreCount)
        s += ', ' + 'TotalDRAM: ' + str(self.TotalDRAM)
        s += ', ' + 'NetworkAdapterCount: ' + str(self.NetworkAdapterCount)
        s += ', ' + 'TotalThroughput: ' + str(self.TotalThroughput)
        s += ', ' + 'StorageDriveCount: ' + str(self.StorageDriveCount)
        s += ', ' + 'TotalCapacity: ' + str(self.TotalCapacity)
        s += ', ' + 'GPUCores: ' + str(self.GPUCores)
        s += ', ' + 'TotalMachines: ' + str(self.TotalMachines)
        s += '}'
        return s

    def __repr__(self):
        return self.__str__()

    def from_dictionary(self, source):
        """
        Populates an object from the given dictionary
        :param source: Dictionary containing a representation of a JSON object
        :return: This object after being populated from the source dictionary
        """
        if 'grp_id' in source:
            self.GroupId = source['grp_id']
        if 'group_name' in source:
            self.GroupName = source['group_name']
        if 'cpu-frequency' in source:
            self.CpuFrequency = source['cpu-frequency']
        if 'cpu-count' in source:
            self.CpuCount = source['cpu-count']
        if 'cpu-lanes' in source:
            self.CpuLanes = source['cpu-lanes']
        if 'cpu-core-count' in source:
            self.CpuCoreCount = source['cpu-core-count']
        if 'total-dram' in source:
            self.TotalDRAM = source['total-dram']
        if 'network-adapter-count' in source:
            self.NetworkAdapterCount = source['network-adapter-count']
        if 'total-throughput' in source:
            self.TotalThroughput = source['total-throughput']
        if 'storage-drive-count' in source:
            self.StorageDriveCount = source['storage-drive-count']
        if 'total-capacity' in source:
            self.TotalCapacity = source['total-capacity']
        if 'gpu-cores' in source:
            self.GPUCores = source['gpu-cores']
        if 'total-machines' in source:
            self.TotalMachines = source['total-machines']
        return self

    def to_dictionary(self):
        """
        Creates a dictionary and populates it from this object in a manner
        consistent with JSON conventions
        :return: dictionary object
        """
        result = dict()
        result['grp_id'] = self.GroupId
        result['group_name'] = self.GroupName
        result['cpu-frequency'] = self.CpuFrequency
        result['cpu-count'] = self.CpuCount
        result['cpu-lanes'] = self.CpuLanes
        result['cpu-core-count'] = self.CpuCoreCount
        result['total-dram'] = self.TotalDRAM
        result['network-adapter-count'] = self.NetworkAdapterCount
        result['total-throughput'] = self.TotalThroughput
        result['storage-drive-count'] = self.StorageDriveCount
        result['total-capacity'] = self.TotalCapacity
        result['gpu-cores'] = self.GPUCores
        result['total-machines'] = self.TotalMachines
        return result


class GroupFPGADeviceRelator:
    """
    Describes a relation between a group and an FPGA device
    """

    def __init__(self):
        self.DeviceStatus = FPGADeviceStatus()
        self.Group = Group()

    def __str__(self):
        s = '{'
        s += 'DeviceStatus: ' + str(self.DeviceStatus)
        s += ', ' + 'Group: ' + str(self.Group)
        s += '}'
        return s

    def __repr__(self):
        return self.__str__()

    def from_dictionary(self, source):
        """
        Populates an object from the given dictionary
        :param source: Dictionary containing a representation of a JSON object
        :return: This object after being populated from the source dictionary
        """
        if 'deviceStatus' in source and source['deviceStatus'] is not None:
            self.DeviceStatus = FPGADeviceStatus().from_dictionary(source['deviceStatus'])
        if 'group' in source and source['group'] is not None:
            self.Group = Group().from_dictionary(source['group'])
        return self

    def to_dictionary(self):
        """
        Creates a dictionary and populates it from this object in a manner
        consistent with JSON conventions
        :return: dictionary object
        """
        result = dict()
        result['deviceStatus'] = self.DeviceStatus.to_dictionary()
        result['group'] = self.Group.to_dictionary()
        return result


class GroupGPUDeviceRelator:
    """
    Describes a relation between a group and an GPU device
    """

    def __init__(self):
        self.DeviceStatus = GPUDeviceStatus()
        self.Group = Group()

    def __str__(self):
        s = '{'
        s += 'DeviceStatus: ' + str(self.DeviceStatus)
        s += ', ' + 'Group: ' + str(self.Group)
        s += '}'
        return s

    def __repr__(self):
        return self.__str__()

    def from_dictionary(self, source):
        """
        Populates an object from the given dictionary
        :param source: Dictionary containing a representation of a JSON object
        :return: This object after being populated from the source dictionary
        """
        if 'deviceStatus' in source and source['deviceStatus'] is not None:
            self.DeviceStatus = GPUDeviceStatus().from_dictionary(source['deviceStatus'])
        if 'group' in source and source['group'] is not None:
            self.Group = Group().from_dictionary(source['group'])
        return self

    def to_dictionary(self):
        """
        Creates a dictionary and populates it from this object in a manner
        consistent with JSON conventions
        :return: dictionary object
        """
        result = dict()
        result['deviceStatus'] = self.DeviceStatus.to_dictionary()
        result['group'] = self.Group.to_dictionary()
        return result


class GroupPool:
    """
    Describes a group pool
    """

    def __init__(self):
        self.Coordinates = Coordinates()
        self.FabricId = None
        self.GroupId = None

    def __str__(self):
        s = '{'
        s += 'Coordinates: ' + str(self.Coordinates)
        s += ', ' + 'FabricId: ' + str(self.FabricId)
        s += ', ' + 'GroupId: ' + str(self.GroupId)
        s += '}'
        return s

    def __repr__(self):
        return self.__str__()

    def from_dictionary(self, source):
        """
        Populates an object from the given dictionary
        :param source: Dictionary containing a representation of a JSON object
        :return: This object after being populated from the source dictionary
        """
        if 'coordinates' in source and source['coordinates'] is not None:
            self.Coordinates = Coordinates().from_dictionary(source['coordinates'])
        if 'fabr_id' in source:
            self.FabricId = source['fabr_id']
        if 'grp_id' in source:
            self.GroupId = source['grp_id']
        return self

    def to_dictionary(self):
        """
        Creates a dictionary and populates it from this object in a manner
        consistent with JSON conventions
        :return: dictionary object
        """
        result = dict()
        result['coordinates'] = self.Coordinates.to_dictionary()
        result['fabr_id'] = self.FabricId
        result['grp_id'] = self.GroupId
        return result


class GroupMemoryDeviceRelator:
    """
    Describes a relation between a group and a memory device
    """

    def __init__(self):
        self.DeviceStatus = MemoryDeviceStatus()
        self.Group = Group()

    def __str__(self):
        s = '{'
        s += 'DeviceStatus: ' + str(self.DeviceStatus)
        s += ', ' + 'Group: ' + str(self.Group)
        s += '}'
        return s

    def __repr__(self):
        return self.__str__()

    def from_dictionary(self, source):
        """
        Populates an object from the given dictionary
        :param source: Dictionary containing a representation of a JSON object
        :return: This object after being populated from the source dictionary
        """
        if 'deviceStatus' in source and source['deviceStatus'] is not None:
            self.DeviceStatus = MemoryDeviceStatus().from_dictionary(source['deviceStatus'])
        if 'group' in source and source['group'] is not None:
            self.Group = Group().from_dictionary(source['group'])
        return self

    def to_dictionary(self):
        """
        Creates a dictionary and populates it from this object in a manner
        consistent with JSON conventions
        :return: dictionary object
        """
        result = dict()
        result['deviceStatus'] = self.DeviceStatus.to_dictionary()
        result['group'] = self.Group.to_dictionary()
        return result


class GroupNetworkDeviceRelator:
    """
    Describes a relation between a group and a network device
    """

    def __init__(self):
        self.DeviceStatus = NetworkDeviceStatus()
        self.Group = Group()

    def __str__(self):
        s = '{'
        s += 'DeviceStatus: ' + str(self.DeviceStatus)
        s += ', ' + 'Group: ' + str(self.Group)
        s += '}'
        return s

    def __repr__(self):
        return self.__str__()

    def from_dictionary(self, source):
        """
        Populates an object from the given dictionary
        :param source: Dictionary containing a representation of a JSON object
        :return: This object after being populated from the source dictionary
        """
        if 'deviceStatus' in source and source['deviceStatus'] is not None:
            self.DeviceStatus = NetworkDeviceStatus().from_dictionary(source['deviceStatus'])
        if 'group' in source and source['group'] is not None:
            self.Group = Group().from_dictionary(source['group'])
        return self

    def to_dictionary(self):
        """
        Creates a dictionary and populates it from this object in a manner
        consistent with JSON conventions
        :return: dictionary object
        """
        result = dict()
        result['deviceStatus'] = self.DeviceStatus.to_dictionary()
        result['group'] = self.Group.to_dictionary()
        return result


class GroupStorageDeviceRelator:
    """
    Describes a relation between a group and a storage device
    """

    def __init__(self):
        self.DeviceStatus = StorageDeviceStatus()
        self.Group = Group()

    def __str__(self):
        s = '{'
        s += 'DeviceStatus: ' + str(self.DeviceStatus)
        s += ', ' + 'Group: ' + str(self.Group)
        s += '}'
        return s

    def __repr__(self):
        return self.__str__()

    def from_dictionary(self, source):
        """
        Populates an object from the given dictionary
        :param source: Dictionary containing a representation of a JSON object
        :return: This object after being populated from the source dictionary
        """
        if 'deviceStatus' in source and source['deviceStatus'] is not None:
            self.DeviceStatus = StorageDeviceStatus().from_dictionary(source['deviceStatus'])
        if 'group' in source and source['group'] is not None:
            self.Group = Group().from_dictionary(source['group'])
        return self

    def to_dictionary(self):
        """
        Creates a dictionary and populates it from this object in a manner
        consistent with JSON conventions
        :return: dictionary object
        """
        result = dict()
        result['deviceStatus'] = self.DeviceStatus.to_dictionary()
        result['group'] = self.Group.to_dictionary()
        return result


class HardwareComponent:
    """
    Describes the hardware details of a component
    """

    def __init__(self):
        self.Type = None
        self.Name = None
        self.Flags = None
        self.State = None
        self.FabricId = None
        self.FabricGlobalId = None
        self.SwitchGlobalId = None
        self.PCIVendorId = None
        self.PCIDeviceId = None
        self.Revision = None
        self.PortCount = None
        self.Ports = []
        self.PCILaneCount = None
        self.ReceiverErrorCount = None
        self.BadTLPCount = None
        self.BadDLLPCount = None
        self.ErrorCount = None
        self.IngressBytes = None
        self.EgressBytes = None
        self.Location = Coordinates()
        self.Owner = Coordinates()

    def __str__(self):
        s = '{'
        s += 'Type: ' + str(self.Type)
        s += ', ' + 'Name: ' + str(self.Name)
        s += ', ' + 'Flags: ' + str(self.Flags)
        s += ', ' + 'State: ' + str(self.State)
        s += ', ' + 'FabricId: ' + str(self.FabricId)
        s += ', ' + 'FabricGlobalId: ' + str(self.FabricGlobalId)
        s += ', ' + 'SwitchGlobalId: ' + str(self.SwitchGlobalId)
        s += ', ' + 'PCIVendorId: ' + str(self.PCIVendorId)
        s += ', ' + 'PCIDeviceId: ' + str(self.PCIDeviceId)
        s += ', ' + 'Revision: ' + str(self.Revision)
        s += ', ' + 'PortCount: ' + str(self.PortCount)
        s += ', ' + 'Ports: ' + str(self.Ports)
        s += ', ' + 'PCILaneCount: ' + str(self.PCILaneCount)
        s += ', ' + 'ReceiverErrorCount: ' + str(self.ReceiverErrorCount)
        s += ', ' + 'BadTLPCount: ' + str(self.BadTLPCount)
        s += ', ' + 'BadDLLPCount: ' + str(self.BadDLLPCount)
        s += ', ' + 'ErrorCount: ' + str(self.ErrorCount)
        s += ', ' + 'IngressBytes: ' + str(self.IngressBytes)
        s += ', ' + 'EgressBytes: ' + str(self.EgressBytes)
        s += ', ' + 'Location: ' + str(self.Location)
        s += ', ' + 'Owner: ' + str(self.Owner)
        s += '}'
        return s

    def __repr__(self):
        return self.__str__()

    def from_dictionary(self, source):
        """
        Populates an object from the given dictionary
        :param source: Dictionary containing a representation of a JSON object
        :return: This object after being populated from the source dictionary
        """
        if 'type' in source:
            self.Type = source['type']
        if 'name' in source:
            self.Name = source['name']
        if 'flags' in source:
            self.Flags = source['flags']
        if 'state' in source:
            self.State = source['state']
        if 'fabr_id' in source:
            self.FabricId = source['fabr_id']
        if 'fabr_gid' in source:
            self.FabricGlobalId = source['fabr_gid']
        if 'swit_gid' in source:
            self.SwitchGlobalId = source['swit_gid']
        if 'vid' in source:
            self.PCIVendorId = source['vid']
        if 'did' in source:
            self.PCIDeviceId = source['did']
        if 'rev' in source:
            self.Revision = source['rev']
        if 'port_cnt' in source:
            self.PortCount = source['port_cnt']
        self.Ports = []
        if 'ports' in source and source['ports'] is not None:
            for item in source['ports']:
                self.Ports.append(Port().from_dictionary(item))
        if 'lanes' in source:
            self.PCILaneCount = source['lanes']
        if 'rcv_errs' in source:
            self.ReceiverErrorCount = source['rcv_errs']
        if 'bad_tlp' in source:
            self.BadTLPCount = source['bad_tlp']
        if 'bad_dllp' in source:
            self.BadDLLPCount = source['bad_dllp']
        if 'errs' in source:
            self.ErrorCount = source['errs']
        if 'ibytes' in source:
            self.IngressBytes = source['ibytes']
        if 'ebytes' in source:
            self.EgressBytes = source['ebytes']
        if 'location' in source and source['location'] is not None:
            self.Location = Coordinates().from_dictionary(source['location'])
        if 'owner' in source and source['owner'] is not None:
            self.Owner = Coordinates().from_dictionary(source['owner'])
        return self

    def to_dictionary(self):
        """
        Creates a dictionary and populates it from this object in a manner
        consistent with JSON conventions
        :return: dictionary object
        """
        result = dict()
        result['type'] = self.Type
        result['name'] = self.Name
        result['flags'] = self.Flags
        result['state'] = self.State
        result['fabr_id'] = self.FabricId
        result['fabr_gid'] = self.FabricGlobalId
        result['swit_gid'] = self.SwitchGlobalId
        result['vid'] = self.PCIVendorId
        result['did'] = self.PCIDeviceId
        result['rev'] = self.Revision
        result['port_cnt'] = self.PortCount
        container = []
        for item in self.Ports:
            container.append(item.to_dictionary())
        result['ports'] = container
        result['lanes'] = self.PCILaneCount
        result['rcv_errs'] = self.ReceiverErrorCount
        result['bad_tlp'] = self.BadTLPCount
        result['bad_dllp'] = self.BadDLLPCount
        result['errs'] = self.ErrorCount
        result['ibytes'] = self.IngressBytes
        result['ebytes'] = self.EgressBytes
        result['location'] = self.Location.to_dictionary()
        result['owner'] = self.Owner.to_dictionary()
        return result


class Machine:
    """
    Describes a configured machine
    """

    def __init__(self):
        self.Index = None
        self.MachineId = None
        self.GroupId = None
        self.FabricId = None
        self.FabricGlobalId = None
        self.PortGlobalId = None
        self.SwitchGlobalId = None
        self.ComputeName = None
        self.MachineName = None
        self.P2PEnabled = P2PTypeOff
        self.CreatedTimestamp = None
        self.ConnectionHistory = []

    def __str__(self):
        s = '{'
        s += 'Index: ' + str(self.Index)
        s += ', ' + 'MachineId: ' + str(self.MachineId)
        s += ', ' + 'GroupId: ' + str(self.GroupId)
        s += ', ' + 'FabricId: ' + str(self.FabricId)
        s += ', ' + 'FabricGlobalId: ' + str(self.FabricGlobalId)
        s += ', ' + 'PortGlobalId: ' + str(self.PortGlobalId)
        s += ', ' + 'SwitchGlobalId: ' + str(self.SwitchGlobalId)
        s += ', ' + 'ComputeName: ' + str(self.ComputeName)
        s += ', ' + 'MachineName: ' + str(self.MachineName)
        s += ', ' + 'P2PEnabled: ' + str(self.P2PEnabled)
        s += ', ' + 'CreatedTimestamp: ' + str(self.CreatedTimestamp)
        s += ', ' + 'ConnectionHistory: ' + str(self.ConnectionHistory)
        s += '}'
        return s

    def __repr__(self):
        return self.__str__()

    def from_dictionary(self, source):
        """
        Populates an object from the given dictionary
        :param source: Dictionary containing a representation of a JSON object
        :return: This object after being populated from the source dictionary
        """
        if 'index' in source:
            self.Index = source['index']
        if 'mach_id' in source:
            self.MachineId = source['mach_id']
        if 'grp_id' in source:
            self.GroupId = source['grp_id']
        if 'fabr_id' in source:
            self.FabricId = source['fabr_id']
        if 'fabr_gid' in source:
            self.FabricGlobalId = source['fabr_gid']
        if 'port_gid' in source:
            self.PortGlobalId = source['port_gid']
        if 'swit_gid' in source:
            self.SwitchGlobalId = source['swit_gid']
        if 'comp_name' in source:
            self.ComputeName = source['comp_name']
        if 'mach_name' in source:
            self.MachineName = source['mach_name']
        if 'p2p' in source:
            self.P2PEnabled = source['p2p']
        if 'mtime' in source:
            self.CreatedTimestamp = source['mtime']
        self.ConnectionHistory = []
        if 'connection_history' in source and source['connection_history'] is not None:
            for item in source['connection_history']:
                self.ConnectionHistory.append(ConnectionHistory().from_dictionary(item))
        return self

    def to_dictionary(self):
        """
        Creates a dictionary and populates it from this object in a manner
        consistent with JSON conventions
        :return: dictionary object
        """
        result = dict()
        result['index'] = self.Index
        result['mach_id'] = self.MachineId
        result['grp_id'] = self.GroupId
        result['fabr_id'] = self.FabricId
        result['fabr_gid'] = self.FabricGlobalId
        result['port_gid'] = self.PortGlobalId
        result['swit_gid'] = self.SwitchGlobalId
        result['comp_name'] = self.ComputeName
        result['mach_name'] = self.MachineName
        result['p2p'] = self.P2PEnabled
        result['mtime'] = self.CreatedTimestamp
        container = []
        for item in self.ConnectionHistory:
            container.append(item.to_dictionary())
        result['connection_history'] = container
        return result


class MachineComputeDeviceRelator:
    """
    Describes a relation between a machine and a compute device
    """

    def __init__(self):
        self.GroupDeviceRelator = GroupComputeDeviceRelator()
        self.Machine = Machine()

    def __str__(self):
        s = '{'
        s += 'GroupDeviceRelator: ' + str(self.GroupDeviceRelator)
        s += ', ' + 'Machine: ' + str(self.Machine)
        s += '}'
        return s

    def __repr__(self):
        return self.__str__()

    def from_dictionary(self, source):
        """
        Populates an object from the given dictionary
        :param source: Dictionary containing a representation of a JSON object
        :return: This object after being populated from the source dictionary
        """
        if 'groupDeviceRelator' in source and source['groupDeviceRelator'] is not None:
            self.GroupDeviceRelator = GroupComputeDeviceRelator().from_dictionary(source['groupDeviceRelator'])
        if 'machine' in source and source['machine'] is not None:
            self.Machine = Machine().from_dictionary(source['machine'])
        return self

    def to_dictionary(self):
        """
        Creates a dictionary and populates it from this object in a manner
        consistent with JSON conventions
        :return: dictionary object
        """
        result = dict()
        result['groupDeviceRelator'] = self.GroupDeviceRelator.to_dictionary()
        result['machine'] = self.Machine.to_dictionary()
        return result


class MachineDetails:
    """
    Additional details for a particular machine
    """

    def __init__(self):
        self.CPUSocketsField = None
        self.MachineId = None
        self.MachineName = None
        self.CPUThreadCount = None
        self.CPUFrequency = None
        self.CPUCoreCount = None
        self.CPUSockets = None
        self.DynamicRAM = None
        self.FabricConnect = None
        self.NetworkAdapterCount = None
        self.TotalThroughput = None
        self.StorageDriveCount = None
        self.TotalCapacity = None
        self.GPUCount = None
        self.GPUCoreCount = None
        self.OperatingSystem = None
        self.BootImage = None
        self.BootDevice = None
        self.IPAddress = None
        self.IPMIAddress = None
        self.FPGACount = None
        self.FPGASpeed = None
        self.FPGADRAMSize = None
        self.CreatedAt = None
        self.LastModifiedAt = None

    def __str__(self):
        s = '{'
        s += 'CPUSocketsField: ' + str(self.CPUSocketsField)
        s += ', ' + 'MachineId: ' + str(self.MachineId)
        s += ', ' + 'MachineName: ' + str(self.MachineName)
        s += ', ' + 'CPUThreadCount: ' + str(self.CPUThreadCount)
        s += ', ' + 'CPUFrequency: ' + str(self.CPUFrequency)
        s += ', ' + 'CPUCoreCount: ' + str(self.CPUCoreCount)
        s += ', ' + 'CPUSockets: ' + str(self.CPUSockets)
        s += ', ' + 'DynamicRAM: ' + str(self.DynamicRAM)
        s += ', ' + 'FabricConnect: ' + str(self.FabricConnect)
        s += ', ' + 'NetworkAdapterCount: ' + str(self.NetworkAdapterCount)
        s += ', ' + 'TotalThroughput: ' + str(self.TotalThroughput)
        s += ', ' + 'StorageDriveCount: ' + str(self.StorageDriveCount)
        s += ', ' + 'TotalCapacity: ' + str(self.TotalCapacity)
        s += ', ' + 'GPUCount: ' + str(self.GPUCount)
        s += ', ' + 'GPUCoreCount: ' + str(self.GPUCoreCount)
        s += ', ' + 'OperatingSystem: ' + str(self.OperatingSystem)
        s += ', ' + 'BootImage: ' + str(self.BootImage)
        s += ', ' + 'BootDevice: ' + str(self.BootDevice)
        s += ', ' + 'IPAddress: ' + str(self.IPAddress)
        s += ', ' + 'IPMIAddress: ' + str(self.IPMIAddress)
        s += ', ' + 'FPGACount: ' + str(self.FPGACount)
        s += ', ' + 'FPGASpeed: ' + str(self.FPGASpeed)
        s += ', ' + 'FPGADRAMSize: ' + str(self.FPGADRAMSize)
        s += ', ' + 'CreatedAt: ' + str(self.CreatedAt)
        s += ', ' + 'LastModifiedAt: ' + str(self.LastModifiedAt)
        s += '}'
        return s

    def __repr__(self):
        return self.__str__()

    def from_dictionary(self, source):
        """
        Populates an object from the given dictionary
        :param source: Dictionary containing a representation of a JSON object
        :return: This object after being populated from the source dictionary
        """
        if 'cpuSocketsField' in source:
            self.CPUSocketsField = source['cpuSocketsField']
        if 'mach_id' in source:
            self.MachineId = source['mach_id']
        if 'mach_name' in source:
            self.MachineName = source['mach_name']
        if 'cpu-threads' in source:
            self.CPUThreadCount = source['cpu-threads']
        if 'cpu-frequency' in source:
            self.CPUFrequency = source['cpu-frequency']
        if 'cpu-cores' in source:
            self.CPUCoreCount = source['cpu-cores']
        if 'cpu-sockets' in source:
            self.CPUSockets = source['cpu-sockets']
        if 'dram-memory' in source:
            self.DynamicRAM = source['dram-memory']
        if 'fabric-connect' in source:
            self.FabricConnect = source['fabric-connect']
        if 'network-adapter-count' in source:
            self.NetworkAdapterCount = source['network-adapter-count']
        if 'total-throughput' in source:
            self.TotalThroughput = source['total-throughput']
        if 'storage-drive-count' in source:
            self.StorageDriveCount = source['storage-drive-count']
        if 'total-capacity' in source:
            self.TotalCapacity = source['total-capacity']
        if 'gpu-count' in source:
            self.GPUCount = source['gpu-count']
        if 'gpu-cores' in source:
            self.GPUCoreCount = source['gpu-cores']
        if 'os_name' in source:
            self.OperatingSystem = source['os_name']
        if 'boot_image' in source:
            self.BootImage = source['boot_image']
        if 'boot_device' in source:
            self.BootDevice = source['boot_device']
        if 'ip_address' in source:
            self.IPAddress = source['ip_address']
        if 'ipmi_address' in source:
            self.IPMIAddress = source['ipmi_address']
        if 'fpga-count' in source:
            self.FPGACount = source['fpga-count']
        if 'fpga-speed' in source:
            self.FPGASpeed = source['fpga-speed']
        if 'fpga-dram-size' in source:
            self.FPGADRAMSize = source['fpga-dram-size']
        if 'created' in source:
            self.CreatedAt = source['created']
        if 'modified' in source:
            self.LastModifiedAt = source['modified']
        return self

    def to_dictionary(self):
        """
        Creates a dictionary and populates it from this object in a manner
        consistent with JSON conventions
        :return: dictionary object
        """
        result = dict()
        result['cpuSocketsField'] = self.CPUSocketsField
        result['mach_id'] = self.MachineId
        result['mach_name'] = self.MachineName
        result['cpu-threads'] = self.CPUThreadCount
        result['cpu-frequency'] = self.CPUFrequency
        result['cpu-cores'] = self.CPUCoreCount
        result['cpu-sockets'] = self.CPUSockets
        result['dram-memory'] = self.DynamicRAM
        result['fabric-connect'] = self.FabricConnect
        result['network-adapter-count'] = self.NetworkAdapterCount
        result['total-throughput'] = self.TotalThroughput
        result['storage-drive-count'] = self.StorageDriveCount
        result['total-capacity'] = self.TotalCapacity
        result['gpu-count'] = self.GPUCount
        result['gpu-cores'] = self.GPUCoreCount
        result['os_name'] = self.OperatingSystem
        result['boot_image'] = self.BootImage
        result['boot_device'] = self.BootDevice
        result['ip_address'] = self.IPAddress
        result['ipmi_address'] = self.IPMIAddress
        result['fpga-count'] = self.FPGACount
        result['fpga-speed'] = self.FPGASpeed
        result['fpga-dram-size'] = self.FPGADRAMSize
        result['created'] = self.CreatedAt
        result['modified'] = self.LastModifiedAt
        return result


class MachineFPGADeviceRelator:
    """
    Describes a relation between a machine and a FPGA device
    """

    def __init__(self):
        self.GroupDeviceRelator = GroupFPGADeviceRelator()
        self.Machine = Machine()

    def __str__(self):
        s = '{'
        s += 'GroupDeviceRelator: ' + str(self.GroupDeviceRelator)
        s += ', ' + 'Machine: ' + str(self.Machine)
        s += '}'
        return s

    def __repr__(self):
        return self.__str__()

    def from_dictionary(self, source):
        """
        Populates an object from the given dictionary
        :param source: Dictionary containing a representation of a JSON object
        :return: This object after being populated from the source dictionary
        """
        if 'groupDeviceRelator' in source and source['groupDeviceRelator'] is not None:
            self.GroupDeviceRelator = GroupFPGADeviceRelator().from_dictionary(source['groupDeviceRelator'])
        if 'machine' in source and source['machine'] is not None:
            self.Machine = Machine().from_dictionary(source['machine'])
        return self

    def to_dictionary(self):
        """
        Creates a dictionary and populates it from this object in a manner
        consistent with JSON conventions
        :return: dictionary object
        """
        result = dict()
        result['groupDeviceRelator'] = self.GroupDeviceRelator.to_dictionary()
        result['machine'] = self.Machine.to_dictionary()
        return result


class MachineGPUDeviceRelator:
    """
    Describes a relation between a machine and a GPU device
    """

    def __init__(self):
        self.GroupDeviceRelator = GroupGPUDeviceRelator()
        self.Machine = Machine()

    def __str__(self):
        s = '{'
        s += 'GroupDeviceRelator: ' + str(self.GroupDeviceRelator)
        s += ', ' + 'Machine: ' + str(self.Machine)
        s += '}'
        return s

    def __repr__(self):
        return self.__str__()

    def from_dictionary(self, source):
        """
        Populates an object from the given dictionary
        :param source: Dictionary containing a representation of a JSON object
        :return: This object after being populated from the source dictionary
        """
        if 'groupDeviceRelator' in source and source['groupDeviceRelator'] is not None:
            self.GroupDeviceRelator = GroupGPUDeviceRelator().from_dictionary(source['groupDeviceRelator'])
        if 'machine' in source and source['machine'] is not None:
            self.Machine = Machine().from_dictionary(source['machine'])
        return self

    def to_dictionary(self):
        """
        Creates a dictionary and populates it from this object in a manner
        consistent with JSON conventions
        :return: dictionary object
        """
        result = dict()
        result['groupDeviceRelator'] = self.GroupDeviceRelator.to_dictionary()
        result['machine'] = self.Machine.to_dictionary()
        return result


class MachineMemoryDeviceRelator:
    """
    Describes a relation between a machine and a memory device
    """

    def __init__(self):
        self.GroupDeviceRelator = GroupMemoryDeviceRelator()
        self.Machine = Machine()

    def __str__(self):
        s = '{'
        s += 'GroupDeviceRelator: ' + str(self.GroupDeviceRelator)
        s += ', ' + 'Machine: ' + str(self.Machine)
        s += '}'
        return s

    def __repr__(self):
        return self.__str__()

    def from_dictionary(self, source):
        """
        Populates an object from the given dictionary
        :param source: Dictionary containing a representation of a JSON object
        :return: This object after being populated from the source dictionary
        """
        if 'groupDeviceRelator' in source and source['groupDeviceRelator'] is not None:
            self.GroupDeviceRelator = GroupMemoryDeviceRelator().from_dictionary(source['groupDeviceRelator'])
        if 'machine' in source and source['machine'] is not None:
            self.Machine = Machine().from_dictionary(source['machine'])
        return self

    def to_dictionary(self):
        """
        Creates a dictionary and populates it from this object in a manner
        consistent with JSON conventions
        :return: dictionary object
        """
        result = dict()
        result['groupDeviceRelator'] = self.GroupDeviceRelator.to_dictionary()
        result['machine'] = self.Machine.to_dictionary()
        return result


class MachineNetworkDeviceRelator:
    """
    Describes a relation between a machine and a network device
    """

    def __init__(self):
        self.GroupDeviceRelator = GroupNetworkDeviceRelator()
        self.Machine = Machine()

    def __str__(self):
        s = '{'
        s += 'GroupDeviceRelator: ' + str(self.GroupDeviceRelator)
        s += ', ' + 'Machine: ' + str(self.Machine)
        s += '}'
        return s

    def __repr__(self):
        return self.__str__()

    def from_dictionary(self, source):
        """
        Populates an object from the given dictionary
        :param source: Dictionary containing a representation of a JSON object
        :return: This object after being populated from the source dictionary
        """
        if 'groupDeviceRelator' in source and source['groupDeviceRelator'] is not None:
            self.GroupDeviceRelator = GroupNetworkDeviceRelator().from_dictionary(source['groupDeviceRelator'])
        if 'machine' in source and source['machine'] is not None:
            self.Machine = Machine().from_dictionary(source['machine'])
        return self

    def to_dictionary(self):
        """
        Creates a dictionary and populates it from this object in a manner
        consistent with JSON conventions
        :return: dictionary object
        """
        result = dict()
        result['groupDeviceRelator'] = self.GroupDeviceRelator.to_dictionary()
        result['machine'] = self.Machine.to_dictionary()
        return result


class MachineStorageDeviceRelator:
    """
    Describes a relation between a machine and a storage device
    """

    def __init__(self):
        self.GroupDeviceRelator = GroupStorageDeviceRelator()
        self.Machine = Machine()

    def __str__(self):
        s = '{'
        s += 'GroupDeviceRelator: ' + str(self.GroupDeviceRelator)
        s += ', ' + 'Machine: ' + str(self.Machine)
        s += '}'
        return s

    def __repr__(self):
        return self.__str__()

    def from_dictionary(self, source):
        """
        Populates an object from the given dictionary
        :param source: Dictionary containing a representation of a JSON object
        :return: This object after being populated from the source dictionary
        """
        if 'groupDeviceRelator' in source and source['groupDeviceRelator'] is not None:
            self.GroupDeviceRelator = GroupStorageDeviceRelator().from_dictionary(source['groupDeviceRelator'])
        if 'machine' in source and source['machine'] is not None:
            self.Machine = Machine().from_dictionary(source['machine'])
        return self

    def to_dictionary(self):
        """
        Creates a dictionary and populates it from this object in a manner
        consistent with JSON conventions
        :return: dictionary object
        """
        result = dict()
        result['groupDeviceRelator'] = self.GroupDeviceRelator.to_dictionary()
        result['machine'] = self.Machine.to_dictionary()
        return result


class ManagedEntity:
    """
    Describes information regarding a particular vendor and model of a manageable device
    """

    def __init__(self):
        self.Description = None
        self.PCIVendorId = None
        self.PCIDeviceId = None
        self.Model = None
        self.NumberOfCores = None
        self.NumberOfThreads = None
        self.Speed = None
        self.Capacity = None
        self.SRIOVEnabled = None
        self.ManagedEntityType = None
        self.Unique = None
        self.CoreMHZ = None
        self.DRAMSize = None
        self.DRAMType = None
        self.Manufacturer = None
        self.DeviceType = None
        self.DiscoveryToken = None
        self.CompanionDevice = None
        self.EntryDescription = ManagedEntityState()

    def __str__(self):
        s = '{'
        s += 'Description: ' + str(self.Description)
        s += ', ' + 'PCIVendorId: ' + str(self.PCIVendorId)
        s += ', ' + 'PCIDeviceId: ' + str(self.PCIDeviceId)
        s += ', ' + 'Model: ' + str(self.Model)
        s += ', ' + 'NumberOfCores: ' + str(self.NumberOfCores)
        s += ', ' + 'NumberOfThreads: ' + str(self.NumberOfThreads)
        s += ', ' + 'Speed: ' + str(self.Speed)
        s += ', ' + 'Capacity: ' + str(self.Capacity)
        s += ', ' + 'SRIOVEnabled: ' + str(self.SRIOVEnabled)
        s += ', ' + 'ManagedEntityType: ' + str(self.ManagedEntityType)
        s += ', ' + 'Unique: ' + str(self.Unique)
        s += ', ' + 'CoreMHZ: ' + str(self.CoreMHZ)
        s += ', ' + 'DRAMSize: ' + str(self.DRAMSize)
        s += ', ' + 'DRAMType: ' + str(self.DRAMType)
        s += ', ' + 'Manufacturer: ' + str(self.Manufacturer)
        s += ', ' + 'DeviceType: ' + str(self.DeviceType)
        s += ', ' + 'DiscoveryToken: ' + str(self.DiscoveryToken)
        s += ', ' + 'CompanionDevice: ' + str(self.CompanionDevice)
        s += ', ' + 'EntryDescription: ' + str(self.EntryDescription)
        s += '}'
        return s

    def __repr__(self):
        return self.__str__()

    def from_dictionary(self, source):
        """
        Populates an object from the given dictionary
        :param source: Dictionary containing a representation of a JSON object
        :return: This object after being populated from the source dictionary
        """
        if 'description' in source:
            self.Description = source['description']
        if 'vid' in source:
            self.PCIVendorId = source['vid']
        if 'did' in source:
            self.PCIDeviceId = source['did']
        if 'model' in source:
            self.Model = source['model']
        if 'cores' in source:
            self.NumberOfCores = source['cores']
        if 'threads' in source:
            self.NumberOfThreads = source['threads']
        if 'speed' in source:
            self.Speed = source['speed']
        if 'capacity' in source:
            self.Capacity = source['capacity']
        if 'sriov' in source:
            self.SRIOVEnabled = source['sriov']
        if 'type' in source:
            self.ManagedEntityType = source['type']
        if 'unique' in source:
            self.Unique = source['unique']
        if 'core_mhz' in source:
            self.CoreMHZ = source['core_mhz']
        if 'dram_size' in source:
            self.DRAMSize = source['dram_size']
        if 'dram_type' in source:
            self.DRAMType = source['dram_type']
        if 'device_manufacturer' in source:
            self.Manufacturer = source['device_manufacturer']
        if 'device_type' in source:
            self.DeviceType = source['device_type']
        if 'discovery_token' in source:
            self.DiscoveryToken = source['discovery_token']
        if 'companion_device' in source:
            self.CompanionDevice = source['companion_device']
        if 'entry_description' in source and source['entry_description'] is not None:
            self.EntryDescription = ManagedEntityState().from_dictionary(source['entry_description'])
        return self

    def to_dictionary(self):
        """
        Creates a dictionary and populates it from this object in a manner
        consistent with JSON conventions
        :return: dictionary object
        """
        result = dict()
        result['description'] = self.Description
        result['vid'] = self.PCIVendorId
        result['did'] = self.PCIDeviceId
        result['model'] = self.Model
        result['cores'] = self.NumberOfCores
        result['threads'] = self.NumberOfThreads
        result['speed'] = self.Speed
        result['capacity'] = self.Capacity
        result['sriov'] = self.SRIOVEnabled
        result['type'] = self.ManagedEntityType
        result['unique'] = self.Unique
        result['core_mhz'] = self.CoreMHZ
        result['dram_size'] = self.DRAMSize
        result['dram_type'] = self.DRAMType
        result['device_manufacturer'] = self.Manufacturer
        result['device_type'] = self.DeviceType
        result['discovery_token'] = self.DiscoveryToken
        result['companion_device'] = self.CompanionDevice
        result['entry_description'] = self.EntryDescription.to_dictionary()
        return result


class ManagedEntityState:
    """
    Describes the state of a managed entity entry
    """

    def __init__(self):
        self.Active = None
        self.Required = None

    def __str__(self):
        s = '{'
        s += 'Active: ' + str(self.Active)
        s += ', ' + 'Required: ' + str(self.Required)
        s += '}'
        return s

    def __repr__(self):
        return self.__str__()

    def from_dictionary(self, source):
        """
        Populates an object from the given dictionary
        :param source: Dictionary containing a representation of a JSON object
        :return: This object after being populated from the source dictionary
        """
        if 'active' in source:
            self.Active = source['active']
        if 'required' in source:
            self.Required = source['required']
        return self

    def to_dictionary(self):
        """
        Creates a dictionary and populates it from this object in a manner
        consistent with JSON conventions
        :return: dictionary object
        """
        result = dict()
        result['active'] = self.Active
        result['required'] = self.Required
        return result


class NameValuePair:
    """
    A simple tuple tying a value key or name to a value
    """

    def __init__(self):
        self.Name = None
        self.ValueString = None

    def __str__(self):
        s = '{'
        s += 'Name: ' + str(self.Name)
        s += ', ' + 'ValueString: ' + str(self.ValueString)
        s += '}'
        return s

    def __repr__(self):
        return self.__str__()

    def from_dictionary(self, source):
        """
        Populates an object from the given dictionary
        :param source: Dictionary containing a representation of a JSON object
        :return: This object after being populated from the source dictionary
        """
        if 'name' in source:
            self.Name = source['name']
        if 'valueString' in source:
            self.ValueString = source['valueString']
        return self

    def to_dictionary(self):
        """
        Creates a dictionary and populates it from this object in a manner
        consistent with JSON conventions
        :return: dictionary object
        """
        result = dict()
        result['name'] = self.Name
        result['valueString'] = self.ValueString
        return result


class NetworkManagedCPU:
    """
    Describes the access information required to manage a CPU device (e.g., via IPMI)
    """

    def __init__(self):
        self.Credentials = Credentials()
        self.IPAddress = None
        self.PortNumber = None
        self.ManagerType = None
        self.CPUName = None

    def __str__(self):
        s = '{'
        s += 'Credentials: ' + str(self.Credentials)
        s += ', ' + 'IPAddress: ' + str(self.IPAddress)
        s += ', ' + 'PortNumber: ' + str(self.PortNumber)
        s += ', ' + 'ManagerType: ' + str(self.ManagerType)
        s += ', ' + 'CPUName: ' + str(self.CPUName)
        s += '}'
        return s

    def __repr__(self):
        return self.__str__()

    def from_dictionary(self, source):
        """
        Populates an object from the given dictionary
        :param source: Dictionary containing a representation of a JSON object
        :return: This object after being populated from the source dictionary
        """
        if 'credentials' in source and source['credentials'] is not None:
            self.Credentials = Credentials().from_dictionary(source['credentials'])
        if 'ip_address' in source:
            self.IPAddress = source['ip_address']
        if 'port' in source:
            self.PortNumber = source['port']
        if 'type' in source:
            self.ManagerType = source['type']
        if 'cpu_name' in source:
            self.CPUName = source['cpu_name']
        return self

    def to_dictionary(self):
        """
        Creates a dictionary and populates it from this object in a manner
        consistent with JSON conventions
        :return: dictionary object
        """
        result = dict()
        result['credentials'] = self.Credentials.to_dictionary()
        result['ip_address'] = self.IPAddress
        result['port'] = self.PortNumber
        result['type'] = self.ManagerType
        result['cpu_name'] = self.CPUName
        return result


class NetworkManagedEnclosure:
    """
    Describes the access information required to manage an enclosure
    """

    def __init__(self):
        self.Credentials = Credentials()
        self.IPAddress = None
        self.PortNumber = None
        self.ManagerType = None
        self.EnclosureName = None

    def __str__(self):
        s = '{'
        s += 'Credentials: ' + str(self.Credentials)
        s += ', ' + 'IPAddress: ' + str(self.IPAddress)
        s += ', ' + 'PortNumber: ' + str(self.PortNumber)
        s += ', ' + 'ManagerType: ' + str(self.ManagerType)
        s += ', ' + 'EnclosureName: ' + str(self.EnclosureName)
        s += '}'
        return s

    def __repr__(self):
        return self.__str__()

    def from_dictionary(self, source):
        """
        Populates an object from the given dictionary
        :param source: Dictionary containing a representation of a JSON object
        :return: This object after being populated from the source dictionary
        """
        if 'credentials' in source and source['credentials'] is not None:
            self.Credentials = Credentials().from_dictionary(source['credentials'])
        if 'ip_address' in source:
            self.IPAddress = source['ip_address']
        if 'port' in source:
            self.PortNumber = source['port']
        if 'type' in source:
            self.ManagerType = source['type']
        if 'enclosure_name' in source:
            self.EnclosureName = source['enclosure_name']
        return self

    def to_dictionary(self):
        """
        Creates a dictionary and populates it from this object in a manner
        consistent with JSON conventions
        :return: dictionary object
        """
        result = dict()
        result['credentials'] = self.Credentials.to_dictionary()
        result['ip_address'] = self.IPAddress
        result['port'] = self.PortNumber
        result['type'] = self.ManagerType
        result['enclosure_name'] = self.EnclosureName
        return result


class NodeStatus:
    """
    Status information regarding one particular node.
    A node should be thought of as a unique host or CPU.
    The use of the word 'node' does not imply any association with a clustered system.
    """

    def __init__(self):
        self.ConfigVersion = None
        self.ConfigIdentifier = None
        self.Comps = None
        self.CurrentTime = None
        self.FabricId = None
        self.Flags = None
        self.LinkCount = None
        self.Location = Coordinates()
        self.OperatingSystem = None
        self.RunState = None
        self.SoftwareVersion = None
        self.TargetCount = None
        self.UpTime = None

    def __str__(self):
        s = '{'
        s += 'ConfigVersion: ' + str(self.ConfigVersion)
        s += ', ' + 'ConfigIdentifier: ' + str(self.ConfigIdentifier)
        s += ', ' + 'Comps: ' + str(self.Comps)
        s += ', ' + 'CurrentTime: ' + str(self.CurrentTime)
        s += ', ' + 'FabricId: ' + str(self.FabricId)
        s += ', ' + 'Flags: ' + str(self.Flags)
        s += ', ' + 'LinkCount: ' + str(self.LinkCount)
        s += ', ' + 'Location: ' + str(self.Location)
        s += ', ' + 'OperatingSystem: ' + str(self.OperatingSystem)
        s += ', ' + 'RunState: ' + str(self.RunState)
        s += ', ' + 'SoftwareVersion: ' + str(self.SoftwareVersion)
        s += ', ' + 'TargetCount: ' + str(self.TargetCount)
        s += ', ' + 'UpTime: ' + str(self.UpTime)
        s += '}'
        return s

    def __repr__(self):
        return self.__str__()

    def from_dictionary(self, source):
        """
        Populates an object from the given dictionary
        :param source: Dictionary containing a representation of a JSON object
        :return: This object after being populated from the source dictionary
        """
        if 'cfg_vers' in source:
            self.ConfigVersion = source['cfg_vers']
        if 'cid' in source:
            self.ConfigIdentifier = source['cid']
        if 'comps' in source:
            self.Comps = source['comps']
        if 'currtime' in source:
            self.CurrentTime = source['currtime']
        if 'fabr_id' in source:
            self.FabricId = source['fabr_id']
        if 'flags' in source:
            self.Flags = source['flags']
        if 'links' in source:
            self.LinkCount = source['links']
        if 'location' in source and source['location'] is not None:
            self.Location = Coordinates().from_dictionary(source['location'])
        if 'os_type' in source:
            self.OperatingSystem = source['os_type']
        if 'run' in source:
            self.RunState = source['run']
        if 'sw_vers' in source:
            self.SoftwareVersion = source['sw_vers']
        if 'targs' in source:
            self.TargetCount = source['targs']
        if 'uptime' in source:
            self.UpTime = source['uptime']
        return self

    def to_dictionary(self):
        """
        Creates a dictionary and populates it from this object in a manner
        consistent with JSON conventions
        :return: dictionary object
        """
        result = dict()
        result['cfg_vers'] = self.ConfigVersion
        result['cid'] = self.ConfigIdentifier
        result['comps'] = self.Comps
        result['currtime'] = self.CurrentTime
        result['fabr_id'] = self.FabricId
        result['flags'] = self.Flags
        result['links'] = self.LinkCount
        result['location'] = self.Location.to_dictionary()
        result['os_type'] = self.OperatingSystem
        result['run'] = self.RunState
        result['sw_vers'] = self.SoftwareVersion
        result['targs'] = self.TargetCount
        result['uptime'] = self.UpTime
        return result


class Port:
    """
    Describes a switch port
    """

    def __init__(self):
        self.Type = None
        self.Index = None
        self.Flags = None
        self.State = None
        self.FabricGlobalId = None
        self.PCILaneCount = None
        self.ReceiverErrorCount = None
        self.BadTLPCount = None
        self.BadDLLPCount = None
        self.ErrorCount = None
        self.IngressBytes = None
        self.EgressBytes = None
        self.Switches = []
        self.CPU = PortCPU()
        self.DeviceState = None

    def __str__(self):
        s = '{'
        s += 'Type: ' + str(self.Type)
        s += ', ' + 'Index: ' + str(self.Index)
        s += ', ' + 'Flags: ' + str(self.Flags)
        s += ', ' + 'State: ' + str(self.State)
        s += ', ' + 'FabricGlobalId: ' + str(self.FabricGlobalId)
        s += ', ' + 'PCILaneCount: ' + str(self.PCILaneCount)
        s += ', ' + 'ReceiverErrorCount: ' + str(self.ReceiverErrorCount)
        s += ', ' + 'BadTLPCount: ' + str(self.BadTLPCount)
        s += ', ' + 'BadDLLPCount: ' + str(self.BadDLLPCount)
        s += ', ' + 'ErrorCount: ' + str(self.ErrorCount)
        s += ', ' + 'IngressBytes: ' + str(self.IngressBytes)
        s += ', ' + 'EgressBytes: ' + str(self.EgressBytes)
        s += ', ' + 'Switches: ' + str(self.Switches)
        s += ', ' + 'CPU: ' + str(self.CPU)
        s += ', ' + 'DeviceState: ' + str(self.DeviceState)
        s += '}'
        return s

    def __repr__(self):
        return self.__str__()

    def from_dictionary(self, source):
        """
        Populates an object from the given dictionary
        :param source: Dictionary containing a representation of a JSON object
        :return: This object after being populated from the source dictionary
        """
        if 'type' in source:
            self.Type = source['type']
        if 'index' in source:
            self.Index = source['index']
        if 'flags' in source:
            self.Flags = source['flags']
        if 'state' in source:
            self.State = source['state']
        if 'fabr_gid' in source:
            self.FabricGlobalId = source['fabr_gid']
        if 'lanes' in source:
            self.PCILaneCount = source['lanes']
        if 'rcv_errs' in source:
            self.ReceiverErrorCount = source['rcv_errs']
        if 'bad_tlp' in source:
            self.BadTLPCount = source['bad_tlp']
        if 'bad_dllp' in source:
            self.BadDLLPCount = source['bad_dllp']
        if 'errs' in source:
            self.ErrorCount = source['errs']
        if 'ibytes' in source:
            self.IngressBytes = source['ibytes']
        if 'ebytes' in source:
            self.EgressBytes = source['ebytes']
        self.Switches = []
        if 'switches' in source and source['switches'] is not None:
            for item in source['switches']:
                self.Switches.append(Switch().from_dictionary(item))
        if 'cpu' in source and source['cpu'] is not None:
            self.CPU = PortCPU().from_dictionary(source['cpu'])
        if 'device_state' in source:
            self.DeviceState = source['device_state']
        return self

    def to_dictionary(self):
        """
        Creates a dictionary and populates it from this object in a manner
        consistent with JSON conventions
        :return: dictionary object
        """
        result = dict()
        result['type'] = self.Type
        result['index'] = self.Index
        result['flags'] = self.Flags
        result['state'] = self.State
        result['fabr_gid'] = self.FabricGlobalId
        result['lanes'] = self.PCILaneCount
        result['rcv_errs'] = self.ReceiverErrorCount
        result['bad_tlp'] = self.BadTLPCount
        result['bad_dllp'] = self.BadDLLPCount
        result['errs'] = self.ErrorCount
        result['ibytes'] = self.IngressBytes
        result['ebytes'] = self.EgressBytes
        container = []
        for item in self.Switches:
            container.append(item.to_dictionary())
        result['switches'] = container
        result['cpu'] = self.CPU.to_dictionary()
        result['device_state'] = self.DeviceState
        return result


class PortCPU:
    """
    Describes a CPU switch port
    """

    def __init__(self):
        self.Name = None
        self.GlobalId = None
        self.VendorId = None
        self.DeviceId = None
        self.BusWidth = None
        self.Direction = None
        self.Type = None

    def __str__(self):
        s = '{'
        s += 'Name: ' + str(self.Name)
        s += ', ' + 'GlobalId: ' + str(self.GlobalId)
        s += ', ' + 'VendorId: ' + str(self.VendorId)
        s += ', ' + 'DeviceId: ' + str(self.DeviceId)
        s += ', ' + 'BusWidth: ' + str(self.BusWidth)
        s += ', ' + 'Direction: ' + str(self.Direction)
        s += ', ' + 'Type: ' + str(self.Type)
        s += '}'
        return s

    def __repr__(self):
        return self.__str__()

    def from_dictionary(self, source):
        """
        Populates an object from the given dictionary
        :param source: Dictionary containing a representation of a JSON object
        :return: This object after being populated from the source dictionary
        """
        if 'name' in source:
            self.Name = source['name']
        if 'gid' in source:
            self.GlobalId = source['gid']
        if 'vendorid' in source:
            self.VendorId = source['vendorid']
        if 'deviceid' in source:
            self.DeviceId = source['deviceid']
        if 'buswidth' in source:
            self.BusWidth = source['buswidth']
        if 'direction' in source:
            self.Direction = source['direction']
        if 'type' in source:
            self.Type = source['type']
        return self

    def to_dictionary(self):
        """
        Creates a dictionary and populates it from this object in a manner
        consistent with JSON conventions
        :return: dictionary object
        """
        result = dict()
        result['name'] = self.Name
        result['gid'] = self.GlobalId
        result['vendorid'] = self.VendorId
        result['deviceid'] = self.DeviceId
        result['buswidth'] = self.BusWidth
        result['direction'] = self.Direction
        result['type'] = self.Type
        return result


class PreDevice:
    """
    Describes a device before it is added to a group
    """

    def __init__(self):
        self.DeviceType = None
        self.FabricGlobalId = None
        self.FabricId = None
        self.Flags = None
        self.GroupName = None
        self.GroupId = None
        self.Index = None
        self.PCILaneCount = None
        self.MachineId = None
        self.MachineName = None
        self.DeviceName = None
        self.OwnerId = None
        self.PodId = -1
        self.PortGlobalId = None
        self.SwitchGlobalId = None

    def __str__(self):
        s = '{'
        s += 'DeviceType: ' + str(self.DeviceType)
        s += ', ' + 'FabricGlobalId: ' + str(self.FabricGlobalId)
        s += ', ' + 'FabricId: ' + str(self.FabricId)
        s += ', ' + 'Flags: ' + str(self.Flags)
        s += ', ' + 'GroupName: ' + str(self.GroupName)
        s += ', ' + 'GroupId: ' + str(self.GroupId)
        s += ', ' + 'Index: ' + str(self.Index)
        s += ', ' + 'PCILaneCount: ' + str(self.PCILaneCount)
        s += ', ' + 'MachineId: ' + str(self.MachineId)
        s += ', ' + 'MachineName: ' + str(self.MachineName)
        s += ', ' + 'DeviceName: ' + str(self.DeviceName)
        s += ', ' + 'OwnerId: ' + str(self.OwnerId)
        s += ', ' + 'PodId: ' + str(self.PodId)
        s += ', ' + 'PortGlobalId: ' + str(self.PortGlobalId)
        s += ', ' + 'SwitchGlobalId: ' + str(self.SwitchGlobalId)
        s += '}'
        return s

    def __repr__(self):
        return self.__str__()

    def from_dictionary(self, source):
        """
        Populates an object from the given dictionary
        :param source: Dictionary containing a representation of a JSON object
        :return: This object after being populated from the source dictionary
        """
        if 'dev_type' in source:
            self.DeviceType = source['dev_type']
        if 'fabr_gid' in source:
            self.FabricGlobalId = source['fabr_gid']
        if 'fabr_id' in source:
            self.FabricId = source['fabr_id']
        if 'flags' in source:
            self.Flags = source['flags']
        if 'gname' in source:
            self.GroupName = source['gname']
        if 'grp_id' in source:
            self.GroupId = source['grp_id']
        if 'index' in source:
            self.Index = source['index']
        if 'lanes' in source:
            self.PCILaneCount = source['lanes']
        if 'mach_id' in source:
            self.MachineId = source['mach_id']
        if 'mname' in source:
            self.MachineName = source['mname']
        if 'name' in source:
            self.DeviceName = source['name']
        if 'owner_id' in source:
            self.OwnerId = source['owner_id']
        if 'pod_id' in source:
            self.PodId = source['pod_id']
        if 'port_gid' in source:
            self.PortGlobalId = source['port_gid']
        if 'swit_gid' in source:
            self.SwitchGlobalId = source['swit_gid']
        return self

    def to_dictionary(self):
        """
        Creates a dictionary and populates it from this object in a manner
        consistent with JSON conventions
        :return: dictionary object
        """
        result = dict()
        result['dev_type'] = self.DeviceType
        result['fabr_gid'] = self.FabricGlobalId
        result['fabr_id'] = self.FabricId
        result['flags'] = self.Flags
        result['gname'] = self.GroupName
        result['grp_id'] = self.GroupId
        result['index'] = self.Index
        result['lanes'] = self.PCILaneCount
        result['mach_id'] = self.MachineId
        result['mname'] = self.MachineName
        result['name'] = self.DeviceName
        result['owner_id'] = self.OwnerId
        result['pod_id'] = self.PodId
        result['port_gid'] = self.PortGlobalId
        result['swit_gid'] = self.SwitchGlobalId
        return result


class SSHStatus:
    """
    Describes the current state of SSH
    """

    def __init__(self):
        self.Active = None
        self.Enabled = None

    def __str__(self):
        s = '{'
        s += 'Active: ' + str(self.Active)
        s += ', ' + 'Enabled: ' + str(self.Enabled)
        s += '}'
        return s

    def __repr__(self):
        return self.__str__()

    def from_dictionary(self, source):
        """
        Populates an object from the given dictionary
        :param source: Dictionary containing a representation of a JSON object
        :return: This object after being populated from the source dictionary
        """
        if 'is-active' in source:
            self.Active = source['is-active']
        if 'is-enabled' in source:
            self.Enabled = source['is-enabled']
        return self

    def to_dictionary(self):
        """
        Creates a dictionary and populates it from this object in a manner
        consistent with JSON conventions
        :return: dictionary object
        """
        result = dict()
        result['is-active'] = self.Active
        result['is-enabled'] = self.Enabled
        return result


class Switch:
    """
    Details related to the PCI switch
    """

    def __init__(self):
        self.Name = None
        self.GlobalId = None
        self.VendorId = None
        self.DeviceId = None
        self.BusWidth = None
        self.Direction = None
        self.Type = None
        self.SwitchDevice = SwitchDevice()

    def __str__(self):
        s = '{'
        s += 'Name: ' + str(self.Name)
        s += ', ' + 'GlobalId: ' + str(self.GlobalId)
        s += ', ' + 'VendorId: ' + str(self.VendorId)
        s += ', ' + 'DeviceId: ' + str(self.DeviceId)
        s += ', ' + 'BusWidth: ' + str(self.BusWidth)
        s += ', ' + 'Direction: ' + str(self.Direction)
        s += ', ' + 'Type: ' + str(self.Type)
        s += ', ' + 'SwitchDevice: ' + str(self.SwitchDevice)
        s += '}'
        return s

    def __repr__(self):
        return self.__str__()

    def from_dictionary(self, source):
        """
        Populates an object from the given dictionary
        :param source: Dictionary containing a representation of a JSON object
        :return: This object after being populated from the source dictionary
        """
        if 'name' in source:
            self.Name = source['name']
        if 'gid' in source:
            self.GlobalId = source['gid']
        if 'vendorid' in source:
            self.VendorId = source['vendorid']
        if 'deviceid' in source:
            self.DeviceId = source['deviceid']
        if 'buswidth' in source:
            self.BusWidth = source['buswidth']
        if 'direction' in source:
            self.Direction = source['direction']
        if 'type' in source:
            self.Type = source['type']
        if 'device' in source and source['device'] is not None:
            self.SwitchDevice = SwitchDevice().from_dictionary(source['device'])
        return self

    def to_dictionary(self):
        """
        Creates a dictionary and populates it from this object in a manner
        consistent with JSON conventions
        :return: dictionary object
        """
        result = dict()
        result['name'] = self.Name
        result['gid'] = self.GlobalId
        result['vendorid'] = self.VendorId
        result['deviceid'] = self.DeviceId
        result['buswidth'] = self.BusWidth
        result['direction'] = self.Direction
        result['type'] = self.Type
        result['device'] = self.SwitchDevice.to_dictionary()
        return result


class SwitchDevice:
    """
    Additional details specific to the switch
    """

    def __init__(self):
        self.Name = None
        self.GroupId = None
        self.VendorId = None
        self.DeviceId = None
        self.BusWidth = None
        self.Direction = None
        self.Type = None

    def __str__(self):
        s = '{'
        s += 'Name: ' + str(self.Name)
        s += ', ' + 'GroupId: ' + str(self.GroupId)
        s += ', ' + 'VendorId: ' + str(self.VendorId)
        s += ', ' + 'DeviceId: ' + str(self.DeviceId)
        s += ', ' + 'BusWidth: ' + str(self.BusWidth)
        s += ', ' + 'Direction: ' + str(self.Direction)
        s += ', ' + 'Type: ' + str(self.Type)
        s += '}'
        return s

    def __repr__(self):
        return self.__str__()

    def from_dictionary(self, source):
        """
        Populates an object from the given dictionary
        :param source: Dictionary containing a representation of a JSON object
        :return: This object after being populated from the source dictionary
        """
        if 'name' in source:
            self.Name = source['name']
        if 'gid' in source:
            self.GroupId = source['gid']
        if 'vendorid' in source:
            self.VendorId = source['vendorid']
        if 'deviceid' in source:
            self.DeviceId = source['deviceid']
        if 'buswidth' in source:
            self.BusWidth = source['buswidth']
        if 'direction' in source:
            self.Direction = source['direction']
        if 'type' in source:
            self.Type = source['type']
        return self

    def to_dictionary(self):
        """
        Creates a dictionary and populates it from this object in a manner
        consistent with JSON conventions
        :return: dictionary object
        """
        result = dict()
        result['name'] = self.Name
        result['gid'] = self.GroupId
        result['vendorid'] = self.VendorId
        result['deviceid'] = self.DeviceId
        result['buswidth'] = self.BusWidth
        result['direction'] = self.Direction
        result['type'] = self.Type
        return result


class Timestamp:
    """
    Contains a timestamp value
    """

    def __init__(self):
        self.OldTimestamp = None
        self.Timestamp = None

    def __str__(self):
        s = '{'
        s += 'OldTimestamp: ' + str(self.OldTimestamp)
        s += ', ' + 'Timestamp: ' + str(self.Timestamp)
        s += '}'
        return s

    def __repr__(self):
        return self.__str__()

    def from_dictionary(self, source):
        """
        Populates an object from the given dictionary
        :param source: Dictionary containing a representation of a JSON object
        :return: This object after being populated from the source dictionary
        """
        if 'epoch' in source:
            self.OldTimestamp = source['epoch']
        if 'timestamp' in source:
            self.Timestamp = source['timestamp']
        return self

    def to_dictionary(self):
        """
        Creates a dictionary and populates it from this object in a manner
        consistent with JSON conventions
        :return: dictionary object
        """
        result = dict()
        result['epoch'] = self.OldTimestamp
        result['timestamp'] = self.Timestamp
        return result


class VersionInfo:
    """
    Describes the versions of the various software components which comprise the Director
    """

    def __init__(self):
        self.Branch = None
        self.ChangeSet = None
        self.ShortChangeSet = None
        self.Component = None
        self.Date = None
        self.ShortDate = None
        self.Version = None

    def __str__(self):
        s = '{'
        s += 'Branch: ' + str(self.Branch)
        s += ', ' + 'ChangeSet: ' + str(self.ChangeSet)
        s += ', ' + 'ShortChangeSet: ' + str(self.ShortChangeSet)
        s += ', ' + 'Component: ' + str(self.Component)
        s += ', ' + 'Date: ' + str(self.Date)
        s += ', ' + 'ShortDate: ' + str(self.ShortDate)
        s += ', ' + 'Version: ' + str(self.Version)
        s += '}'
        return s

    def __repr__(self):
        return self.__str__()

    def from_dictionary(self, source):
        """
        Populates an object from the given dictionary
        :param source: Dictionary containing a representation of a JSON object
        :return: This object after being populated from the source dictionary
        """
        if 'branch' in source:
            self.Branch = source['branch']
        if 'changeset' in source:
            self.ChangeSet = source['changeset']
        if 'changeset_short' in source:
            self.ShortChangeSet = source['changeset_short']
        if 'component' in source:
            self.Component = source['component']
        if 'date' in source:
            self.Date = source['date']
        if 'date_short' in source:
            self.ShortDate = source['date_short']
        if 'version' in source:
            self.Version = source['version']
        return self

    def to_dictionary(self):
        """
        Creates a dictionary and populates it from this object in a manner
        consistent with JSON conventions
        :return: dictionary object
        """
        result = dict()
        result['branch'] = self.Branch
        result['changeset'] = self.ChangeSet
        result['changeset_short'] = self.ShortChangeSet
        result['component'] = self.Component
        result['date'] = self.Date
        result['date_short'] = self.ShortDate
        result['version'] = self.Version
        return result


class ComputeDeviceInfo(DeviceInfo):
    """
    Contains non-status information regarding a compute device
    """

    def __init__(self):
        super().__init__()
        self.CoreCount = None
        self.CoreMHz = None
        self.DRAMSize = None
        self.DRAMType = None
        self.InstructionSet = None
        self.Socket = None
        self.NumberOfThreads = None

    def __str__(self):
        s = '{'
        s += 'CoreCount: ' + str(self.CoreCount)
        s += ', ' + 'CoreMHz: ' + str(self.CoreMHz)
        s += ', ' + 'DRAMSize: ' + str(self.DRAMSize)
        s += ', ' + 'DRAMType: ' + str(self.DRAMType)
        s += ', ' + 'InstructionSet: ' + str(self.InstructionSet)
        s += ', ' + 'Socket: ' + str(self.Socket)
        s += ', ' + 'NumberOfThreads: ' + str(self.NumberOfThreads)
        s += ', ' + 'BusGeneration: ' + str(self.BusGeneration)
        s += ', ' + 'BusWidth: ' + str(self.BusWidth)
        s += ', ' + 'DeviceClass: ' + str(self.DeviceClass)
        s += ', ' + 'ConnectionType: ' + str(self.ConnectionType)
        s += ', ' + 'DeviceIdentifier: ' + str(self.DeviceIdentifier)
        s += ', ' + 'DeviceState: ' + str(self.DeviceState)
        s += ', ' + 'DeviceType: ' + str(self.DeviceType)
        s += ', ' + 'FabricGlobalId: ' + str(self.FabricGlobalId)
        s += ', ' + 'FabricType: ' + str(self.FabricType)
        s += ', ' + 'Family: ' + str(self.Family)
        s += ', ' + 'Flags: ' + str(self.Flags)
        s += ', ' + 'FirmwareRevision: ' + str(self.FirmwareRevision)
        s += ', ' + 'Index: ' + str(self.Index)
        s += ', ' + 'Location: ' + str(self.Location)
        s += ', ' + 'Model: ' + str(self.Model)
        s += ', ' + 'Name: ' + str(self.Name)
        s += ', ' + 'Owner: ' + str(self.Owner)
        s += ', ' + 'PartNumber: ' + str(self.PartNumber)
        s += ', ' + 'PCIDeviceId: ' + str(self.PCIDeviceId)
        s += ', ' + 'PCIVendorId: ' + str(self.PCIVendorId)
        s += ', ' + 'PodId: ' + str(self.PodId)
        s += ', ' + 'SerialNumber: ' + str(self.SerialNumber)
        s += ', ' + 'SledId: ' + str(self.SledId)
        s += ', ' + 'UserDescription: ' + str(self.UserDescription)
        s += ', ' + 'Unique: ' + str(self.Unique)
        s += ', ' + 'Vendor: ' + str(self.Vendor)
        s += '}'
        return s

    def __repr__(self):
        return self.__str__()

    def from_dictionary(self, source):
        """
        Populates an object from the given dictionary
        :param source: Dictionary containing a representation of a JSON object
        :return: This object after being populated from the source dictionary
        """
        super().from_dictionary(source)
        if 'core_cnt' in source:
            self.CoreCount = source['core_cnt']
        if 'core_mhz' in source:
            self.CoreMHz = source['core_mhz']
        if 'dram_size' in source:
            self.DRAMSize = source['dram_size']
        if 'dram_type' in source:
            self.DRAMType = source['dram_type']
        if 'inst_set' in source:
            self.InstructionSet = source['inst_set']
        if 'socket' in source:
            self.Socket = source['socket']
        if 'thrd_cnt' in source:
            self.NumberOfThreads = source['thrd_cnt']
        return self

    def to_dictionary(self):
        """
        Creates a dictionary and populates it from this object in a manner
        consistent with JSON conventions
        :return: dictionary object
        """
        result = super().to_dictionary()
        result['core_cnt'] = self.CoreCount
        result['core_mhz'] = self.CoreMHz
        result['dram_size'] = self.DRAMSize
        result['dram_type'] = self.DRAMType
        result['inst_set'] = self.InstructionSet
        result['socket'] = self.Socket
        result['thrd_cnt'] = self.NumberOfThreads
        return result


class ComputeDeviceStatus(DeviceStatus):
    """
    Compute Device Status Information
    """

    def __init__(self):
        super().__init__()
        self.HConn = None
        self.Unique = None

    def __str__(self):
        s = '{'
        s += 'HConn: ' + str(self.HConn)
        s += ', ' + 'Unique: ' + str(self.Unique)
        s += ', ' + 'ConnectionType: ' + str(self.ConnectionType)
        s += ', ' + 'DeviceId: ' + str(self.DeviceId)
        s += ', ' + 'DeviceState: ' + str(self.DeviceState)
        s += ', ' + 'DeviceType: ' + str(self.DeviceType)
        s += ', ' + 'PCIDeviceId: ' + str(self.PCIDeviceId)
        s += ', ' + 'GlobalId: ' + str(self.GlobalId)
        s += ', ' + 'FabricId: ' + str(self.FabricId)
        s += ', ' + 'FabricType: ' + str(self.FabricType)
        s += ', ' + 'Flags: ' + str(self.Flags)
        s += ', ' + 'Flags2: ' + str(self.Flags2)
        s += ', ' + 'Index: ' + str(self.Index)
        s += ', ' + 'PCILaneCount: ' + str(self.PCILaneCount)
        s += ', ' + 'Location: ' + str(self.Location)
        s += ', ' + 'Name: ' + str(self.Name)
        s += ', ' + 'Owner: ' + str(self.Owner)
        s += ', ' + 'PodId: ' + str(self.PodId)
        s += ', ' + 'PortGlobalId: ' + str(self.PortGlobalId)
        s += ', ' + 'SledId: ' + str(self.SledId)
        s += ', ' + 'SwitchGlobalId: ' + str(self.SwitchGlobalId)
        s += ', ' + 'DeviceStatusType: ' + str(self.DeviceStatusType)
        s += ', ' + 'PCIVendorId: ' + str(self.PCIVendorId)
        s += '}'
        return s

    def __repr__(self):
        return self.__str__()

    def from_dictionary(self, source):
        """
        Populates an object from the given dictionary
        :param source: Dictionary containing a representation of a JSON object
        :return: This object after being populated from the source dictionary
        """
        super().from_dictionary(source)
        if 'hconn' in source:
            self.HConn = source['hconn']
        if 'unique' in source:
            self.Unique = source['unique']
        return self

    def to_dictionary(self):
        """
        Creates a dictionary and populates it from this object in a manner
        consistent with JSON conventions
        :return: dictionary object
        """
        result = super().to_dictionary()
        result['hconn'] = self.HConn
        result['unique'] = self.Unique
        return result


class FPGADeviceInfo(DeviceInfo):
    """
    Contains non-status information regarding an FPGA device
    """

    def __init__(self):
        super().__init__()
        self.CoreCount = None
        self.CoreMHz = None
        self.DRAMSize = None
        self.DRAMType = None
        self.FPGASpeed = None
        self.NumberOfThreads = None

    def __str__(self):
        s = '{'
        s += 'CoreCount: ' + str(self.CoreCount)
        s += ', ' + 'CoreMHz: ' + str(self.CoreMHz)
        s += ', ' + 'DRAMSize: ' + str(self.DRAMSize)
        s += ', ' + 'DRAMType: ' + str(self.DRAMType)
        s += ', ' + 'FPGASpeed: ' + str(self.FPGASpeed)
        s += ', ' + 'NumberOfThreads: ' + str(self.NumberOfThreads)
        s += ', ' + 'BusGeneration: ' + str(self.BusGeneration)
        s += ', ' + 'BusWidth: ' + str(self.BusWidth)
        s += ', ' + 'DeviceClass: ' + str(self.DeviceClass)
        s += ', ' + 'ConnectionType: ' + str(self.ConnectionType)
        s += ', ' + 'DeviceIdentifier: ' + str(self.DeviceIdentifier)
        s += ', ' + 'DeviceState: ' + str(self.DeviceState)
        s += ', ' + 'DeviceType: ' + str(self.DeviceType)
        s += ', ' + 'FabricGlobalId: ' + str(self.FabricGlobalId)
        s += ', ' + 'FabricType: ' + str(self.FabricType)
        s += ', ' + 'Family: ' + str(self.Family)
        s += ', ' + 'Flags: ' + str(self.Flags)
        s += ', ' + 'FirmwareRevision: ' + str(self.FirmwareRevision)
        s += ', ' + 'Index: ' + str(self.Index)
        s += ', ' + 'Location: ' + str(self.Location)
        s += ', ' + 'Model: ' + str(self.Model)
        s += ', ' + 'Name: ' + str(self.Name)
        s += ', ' + 'Owner: ' + str(self.Owner)
        s += ', ' + 'PartNumber: ' + str(self.PartNumber)
        s += ', ' + 'PCIDeviceId: ' + str(self.PCIDeviceId)
        s += ', ' + 'PCIVendorId: ' + str(self.PCIVendorId)
        s += ', ' + 'PodId: ' + str(self.PodId)
        s += ', ' + 'SerialNumber: ' + str(self.SerialNumber)
        s += ', ' + 'SledId: ' + str(self.SledId)
        s += ', ' + 'UserDescription: ' + str(self.UserDescription)
        s += ', ' + 'Unique: ' + str(self.Unique)
        s += ', ' + 'Vendor: ' + str(self.Vendor)
        s += '}'
        return s

    def __repr__(self):
        return self.__str__()

    def from_dictionary(self, source):
        """
        Populates an object from the given dictionary
        :param source: Dictionary containing a representation of a JSON object
        :return: This object after being populated from the source dictionary
        """
        super().from_dictionary(source)
        if 'core_cnt' in source:
            self.CoreCount = source['core_cnt']
        if 'core_mhz' in source:
            self.CoreMHz = source['core_mhz']
        if 'dram_size' in source:
            self.DRAMSize = source['dram_size']
        if 'dram_type' in source:
            self.DRAMType = source['dram_type']
        if 'fpga_speed' in source:
            self.FPGASpeed = source['fpga_speed']
        if 'thrd_cnt' in source:
            self.NumberOfThreads = source['thrd_cnt']
        return self

    def to_dictionary(self):
        """
        Creates a dictionary and populates it from this object in a manner
        consistent with JSON conventions
        :return: dictionary object
        """
        result = super().to_dictionary()
        result['core_cnt'] = self.CoreCount
        result['core_mhz'] = self.CoreMHz
        result['dram_size'] = self.DRAMSize
        result['dram_type'] = self.DRAMType
        result['fpga_speed'] = self.FPGASpeed
        result['thrd_cnt'] = self.NumberOfThreads
        return result


class FPGADeviceStatus(DeviceStatus):
    """
    FPGA Device Status Information
    """

    def __init__(self):
        super().__init__()
        self.Unique = None

    def __str__(self):
        s = '{'
        s += 'Unique: ' + str(self.Unique)
        s += ', ' + 'ConnectionType: ' + str(self.ConnectionType)
        s += ', ' + 'DeviceId: ' + str(self.DeviceId)
        s += ', ' + 'DeviceState: ' + str(self.DeviceState)
        s += ', ' + 'DeviceType: ' + str(self.DeviceType)
        s += ', ' + 'PCIDeviceId: ' + str(self.PCIDeviceId)
        s += ', ' + 'GlobalId: ' + str(self.GlobalId)
        s += ', ' + 'FabricId: ' + str(self.FabricId)
        s += ', ' + 'FabricType: ' + str(self.FabricType)
        s += ', ' + 'Flags: ' + str(self.Flags)
        s += ', ' + 'Flags2: ' + str(self.Flags2)
        s += ', ' + 'Index: ' + str(self.Index)
        s += ', ' + 'PCILaneCount: ' + str(self.PCILaneCount)
        s += ', ' + 'Location: ' + str(self.Location)
        s += ', ' + 'Name: ' + str(self.Name)
        s += ', ' + 'Owner: ' + str(self.Owner)
        s += ', ' + 'PodId: ' + str(self.PodId)
        s += ', ' + 'PortGlobalId: ' + str(self.PortGlobalId)
        s += ', ' + 'SledId: ' + str(self.SledId)
        s += ', ' + 'SwitchGlobalId: ' + str(self.SwitchGlobalId)
        s += ', ' + 'DeviceStatusType: ' + str(self.DeviceStatusType)
        s += ', ' + 'PCIVendorId: ' + str(self.PCIVendorId)
        s += '}'
        return s

    def __repr__(self):
        return self.__str__()

    def from_dictionary(self, source):
        """
        Populates an object from the given dictionary
        :param source: Dictionary containing a representation of a JSON object
        :return: This object after being populated from the source dictionary
        """
        super().from_dictionary(source)
        if 'unique' in source:
            self.Unique = source['unique']
        return self

    def to_dictionary(self):
        """
        Creates a dictionary and populates it from this object in a manner
        consistent with JSON conventions
        :return: dictionary object
        """
        result = super().to_dictionary()
        result['unique'] = self.Unique
        return result


class GPUDeviceInfo(DeviceInfo):
    """
    Contains non-status information regarding a GPU device
    """

    def __init__(self):
        super().__init__()
        self.CacheSize = None
        self.CoreCount = None
        self.CoreSpeed = None
        self.DRAMSize = None
        self.DRAMType = None

    def __str__(self):
        s = '{'
        s += 'CacheSize: ' + str(self.CacheSize)
        s += ', ' + 'CoreCount: ' + str(self.CoreCount)
        s += ', ' + 'CoreSpeed: ' + str(self.CoreSpeed)
        s += ', ' + 'DRAMSize: ' + str(self.DRAMSize)
        s += ', ' + 'DRAMType: ' + str(self.DRAMType)
        s += ', ' + 'BusGeneration: ' + str(self.BusGeneration)
        s += ', ' + 'BusWidth: ' + str(self.BusWidth)
        s += ', ' + 'DeviceClass: ' + str(self.DeviceClass)
        s += ', ' + 'ConnectionType: ' + str(self.ConnectionType)
        s += ', ' + 'DeviceIdentifier: ' + str(self.DeviceIdentifier)
        s += ', ' + 'DeviceState: ' + str(self.DeviceState)
        s += ', ' + 'DeviceType: ' + str(self.DeviceType)
        s += ', ' + 'FabricGlobalId: ' + str(self.FabricGlobalId)
        s += ', ' + 'FabricType: ' + str(self.FabricType)
        s += ', ' + 'Family: ' + str(self.Family)
        s += ', ' + 'Flags: ' + str(self.Flags)
        s += ', ' + 'FirmwareRevision: ' + str(self.FirmwareRevision)
        s += ', ' + 'Index: ' + str(self.Index)
        s += ', ' + 'Location: ' + str(self.Location)
        s += ', ' + 'Model: ' + str(self.Model)
        s += ', ' + 'Name: ' + str(self.Name)
        s += ', ' + 'Owner: ' + str(self.Owner)
        s += ', ' + 'PartNumber: ' + str(self.PartNumber)
        s += ', ' + 'PCIDeviceId: ' + str(self.PCIDeviceId)
        s += ', ' + 'PCIVendorId: ' + str(self.PCIVendorId)
        s += ', ' + 'PodId: ' + str(self.PodId)
        s += ', ' + 'SerialNumber: ' + str(self.SerialNumber)
        s += ', ' + 'SledId: ' + str(self.SledId)
        s += ', ' + 'UserDescription: ' + str(self.UserDescription)
        s += ', ' + 'Unique: ' + str(self.Unique)
        s += ', ' + 'Vendor: ' + str(self.Vendor)
        s += '}'
        return s

    def __repr__(self):
        return self.__str__()

    def from_dictionary(self, source):
        """
        Populates an object from the given dictionary
        :param source: Dictionary containing a representation of a JSON object
        :return: This object after being populated from the source dictionary
        """
        super().from_dictionary(source)
        if 'cache_size' in source:
            self.CacheSize = source['cache_size']
        if 'core_cnt' in source:
            self.CoreCount = source['core_cnt']
        if 'core_speed' in source:
            self.CoreSpeed = source['core_speed']
        if 'dram_size' in source:
            self.DRAMSize = source['dram_size']
        if 'dram_type' in source:
            self.DRAMType = source['dram_type']
        return self

    def to_dictionary(self):
        """
        Creates a dictionary and populates it from this object in a manner
        consistent with JSON conventions
        :return: dictionary object
        """
        result = super().to_dictionary()
        result['cache_size'] = self.CacheSize
        result['core_cnt'] = self.CoreCount
        result['core_speed'] = self.CoreSpeed
        result['dram_size'] = self.DRAMSize
        result['dram_type'] = self.DRAMType
        return result


class GPUDeviceStatus(DeviceStatus):
    """
    GPU Device Status Information
    """

    def __init__(self):
        super().__init__()
        self.Unique = None

    def __str__(self):
        s = '{'
        s += 'Unique: ' + str(self.Unique)
        s += ', ' + 'ConnectionType: ' + str(self.ConnectionType)
        s += ', ' + 'DeviceId: ' + str(self.DeviceId)
        s += ', ' + 'DeviceState: ' + str(self.DeviceState)
        s += ', ' + 'DeviceType: ' + str(self.DeviceType)
        s += ', ' + 'PCIDeviceId: ' + str(self.PCIDeviceId)
        s += ', ' + 'GlobalId: ' + str(self.GlobalId)
        s += ', ' + 'FabricId: ' + str(self.FabricId)
        s += ', ' + 'FabricType: ' + str(self.FabricType)
        s += ', ' + 'Flags: ' + str(self.Flags)
        s += ', ' + 'Flags2: ' + str(self.Flags2)
        s += ', ' + 'Index: ' + str(self.Index)
        s += ', ' + 'PCILaneCount: ' + str(self.PCILaneCount)
        s += ', ' + 'Location: ' + str(self.Location)
        s += ', ' + 'Name: ' + str(self.Name)
        s += ', ' + 'Owner: ' + str(self.Owner)
        s += ', ' + 'PodId: ' + str(self.PodId)
        s += ', ' + 'PortGlobalId: ' + str(self.PortGlobalId)
        s += ', ' + 'SledId: ' + str(self.SledId)
        s += ', ' + 'SwitchGlobalId: ' + str(self.SwitchGlobalId)
        s += ', ' + 'DeviceStatusType: ' + str(self.DeviceStatusType)
        s += ', ' + 'PCIVendorId: ' + str(self.PCIVendorId)
        s += '}'
        return s

    def __repr__(self):
        return self.__str__()

    def from_dictionary(self, source):
        """
        Populates an object from the given dictionary
        :param source: Dictionary containing a representation of a JSON object
        :return: This object after being populated from the source dictionary
        """
        super().from_dictionary(source)
        if 'unique' in source:
            self.Unique = source['unique']
        return self

    def to_dictionary(self):
        """
        Creates a dictionary and populates it from this object in a manner
        consistent with JSON conventions
        :return: dictionary object
        """
        result = super().to_dictionary()
        result['unique'] = self.Unique
        return result


class MemoryDeviceInfo(DeviceInfo):
    """
    Contains non-status information regarding a memory device
    """

    def __init__(self):
        super().__init__()
        self.Capacity = None

    def __str__(self):
        s = '{'
        s += 'Capacity: ' + str(self.Capacity)
        s += ', ' + 'BusGeneration: ' + str(self.BusGeneration)
        s += ', ' + 'BusWidth: ' + str(self.BusWidth)
        s += ', ' + 'DeviceClass: ' + str(self.DeviceClass)
        s += ', ' + 'ConnectionType: ' + str(self.ConnectionType)
        s += ', ' + 'DeviceIdentifier: ' + str(self.DeviceIdentifier)
        s += ', ' + 'DeviceState: ' + str(self.DeviceState)
        s += ', ' + 'DeviceType: ' + str(self.DeviceType)
        s += ', ' + 'FabricGlobalId: ' + str(self.FabricGlobalId)
        s += ', ' + 'FabricType: ' + str(self.FabricType)
        s += ', ' + 'Family: ' + str(self.Family)
        s += ', ' + 'Flags: ' + str(self.Flags)
        s += ', ' + 'FirmwareRevision: ' + str(self.FirmwareRevision)
        s += ', ' + 'Index: ' + str(self.Index)
        s += ', ' + 'Location: ' + str(self.Location)
        s += ', ' + 'Model: ' + str(self.Model)
        s += ', ' + 'Name: ' + str(self.Name)
        s += ', ' + 'Owner: ' + str(self.Owner)
        s += ', ' + 'PartNumber: ' + str(self.PartNumber)
        s += ', ' + 'PCIDeviceId: ' + str(self.PCIDeviceId)
        s += ', ' + 'PCIVendorId: ' + str(self.PCIVendorId)
        s += ', ' + 'PodId: ' + str(self.PodId)
        s += ', ' + 'SerialNumber: ' + str(self.SerialNumber)
        s += ', ' + 'SledId: ' + str(self.SledId)
        s += ', ' + 'UserDescription: ' + str(self.UserDescription)
        s += ', ' + 'Unique: ' + str(self.Unique)
        s += ', ' + 'Vendor: ' + str(self.Vendor)
        s += '}'
        return s

    def __repr__(self):
        return self.__str__()

    def from_dictionary(self, source):
        """
        Populates an object from the given dictionary
        :param source: Dictionary containing a representation of a JSON object
        :return: This object after being populated from the source dictionary
        """
        super().from_dictionary(source)
        if 'capacity' in source:
            self.Capacity = source['capacity']
        return self

    def to_dictionary(self):
        """
        Creates a dictionary and populates it from this object in a manner
        consistent with JSON conventions
        :return: dictionary object
        """
        result = super().to_dictionary()
        result['capacity'] = self.Capacity
        return result


class MemoryDeviceStatus(DeviceStatus):
    """
    Memory Device Status Information
    """

    def __init__(self):
        super().__init__()
        self.CapacityMB = None
        self.Unique = None

    def __str__(self):
        s = '{'
        s += 'CapacityMB: ' + str(self.CapacityMB)
        s += ', ' + 'Unique: ' + str(self.Unique)
        s += ', ' + 'ConnectionType: ' + str(self.ConnectionType)
        s += ', ' + 'DeviceId: ' + str(self.DeviceId)
        s += ', ' + 'DeviceState: ' + str(self.DeviceState)
        s += ', ' + 'DeviceType: ' + str(self.DeviceType)
        s += ', ' + 'PCIDeviceId: ' + str(self.PCIDeviceId)
        s += ', ' + 'GlobalId: ' + str(self.GlobalId)
        s += ', ' + 'FabricId: ' + str(self.FabricId)
        s += ', ' + 'FabricType: ' + str(self.FabricType)
        s += ', ' + 'Flags: ' + str(self.Flags)
        s += ', ' + 'Flags2: ' + str(self.Flags2)
        s += ', ' + 'Index: ' + str(self.Index)
        s += ', ' + 'PCILaneCount: ' + str(self.PCILaneCount)
        s += ', ' + 'Location: ' + str(self.Location)
        s += ', ' + 'Name: ' + str(self.Name)
        s += ', ' + 'Owner: ' + str(self.Owner)
        s += ', ' + 'PodId: ' + str(self.PodId)
        s += ', ' + 'PortGlobalId: ' + str(self.PortGlobalId)
        s += ', ' + 'SledId: ' + str(self.SledId)
        s += ', ' + 'SwitchGlobalId: ' + str(self.SwitchGlobalId)
        s += ', ' + 'DeviceStatusType: ' + str(self.DeviceStatusType)
        s += ', ' + 'PCIVendorId: ' + str(self.PCIVendorId)
        s += '}'
        return s

    def __repr__(self):
        return self.__str__()

    def from_dictionary(self, source):
        """
        Populates an object from the given dictionary
        :param source: Dictionary containing a representation of a JSON object
        :return: This object after being populated from the source dictionary
        """
        super().from_dictionary(source)
        if 'capacity(MB)' in source:
            self.CapacityMB = source['capacity(MB)']
        if 'unique' in source:
            self.Unique = source['unique']
        return self

    def to_dictionary(self):
        """
        Creates a dictionary and populates it from this object in a manner
        consistent with JSON conventions
        :return: dictionary object
        """
        result = super().to_dictionary()
        result['capacity(MB)'] = self.CapacityMB
        result['unique'] = self.Unique
        return result


class NetworkDeviceInfo(DeviceInfo):
    """
    Contains non-status information regarding a network device
    """

    def __init__(self):
        super().__init__()
        self.LinkSpeed = None
        self.DRAMSize = None
        self.DRAMType = None

    def __str__(self):
        s = '{'
        s += 'LinkSpeed: ' + str(self.LinkSpeed)
        s += ', ' + 'DRAMSize: ' + str(self.DRAMSize)
        s += ', ' + 'DRAMType: ' + str(self.DRAMType)
        s += ', ' + 'BusGeneration: ' + str(self.BusGeneration)
        s += ', ' + 'BusWidth: ' + str(self.BusWidth)
        s += ', ' + 'DeviceClass: ' + str(self.DeviceClass)
        s += ', ' + 'ConnectionType: ' + str(self.ConnectionType)
        s += ', ' + 'DeviceIdentifier: ' + str(self.DeviceIdentifier)
        s += ', ' + 'DeviceState: ' + str(self.DeviceState)
        s += ', ' + 'DeviceType: ' + str(self.DeviceType)
        s += ', ' + 'FabricGlobalId: ' + str(self.FabricGlobalId)
        s += ', ' + 'FabricType: ' + str(self.FabricType)
        s += ', ' + 'Family: ' + str(self.Family)
        s += ', ' + 'Flags: ' + str(self.Flags)
        s += ', ' + 'FirmwareRevision: ' + str(self.FirmwareRevision)
        s += ', ' + 'Index: ' + str(self.Index)
        s += ', ' + 'Location: ' + str(self.Location)
        s += ', ' + 'Model: ' + str(self.Model)
        s += ', ' + 'Name: ' + str(self.Name)
        s += ', ' + 'Owner: ' + str(self.Owner)
        s += ', ' + 'PartNumber: ' + str(self.PartNumber)
        s += ', ' + 'PCIDeviceId: ' + str(self.PCIDeviceId)
        s += ', ' + 'PCIVendorId: ' + str(self.PCIVendorId)
        s += ', ' + 'PodId: ' + str(self.PodId)
        s += ', ' + 'SerialNumber: ' + str(self.SerialNumber)
        s += ', ' + 'SledId: ' + str(self.SledId)
        s += ', ' + 'UserDescription: ' + str(self.UserDescription)
        s += ', ' + 'Unique: ' + str(self.Unique)
        s += ', ' + 'Vendor: ' + str(self.Vendor)
        s += '}'
        return s

    def __repr__(self):
        return self.__str__()

    def from_dictionary(self, source):
        """
        Populates an object from the given dictionary
        :param source: Dictionary containing a representation of a JSON object
        :return: This object after being populated from the source dictionary
        """
        super().from_dictionary(source)
        if 'link_speed' in source:
            self.LinkSpeed = source['link_speed']
        if 'dram_sz' in source:
            self.DRAMSize = source['dram_sz']
        if 'dram_type' in source:
            self.DRAMType = source['dram_type']
        return self

    def to_dictionary(self):
        """
        Creates a dictionary and populates it from this object in a manner
        consistent with JSON conventions
        :return: dictionary object
        """
        result = super().to_dictionary()
        result['link_speed'] = self.LinkSpeed
        result['dram_sz'] = self.DRAMSize
        result['dram_type'] = self.DRAMType
        return result


class NetworkDeviceStatus(DeviceStatus):
    """
    Network Device Status Information
    """

    def __init__(self):
        super().__init__()
        self.Unique = None

    def __str__(self):
        s = '{'
        s += 'Unique: ' + str(self.Unique)
        s += ', ' + 'ConnectionType: ' + str(self.ConnectionType)
        s += ', ' + 'DeviceId: ' + str(self.DeviceId)
        s += ', ' + 'DeviceState: ' + str(self.DeviceState)
        s += ', ' + 'DeviceType: ' + str(self.DeviceType)
        s += ', ' + 'PCIDeviceId: ' + str(self.PCIDeviceId)
        s += ', ' + 'GlobalId: ' + str(self.GlobalId)
        s += ', ' + 'FabricId: ' + str(self.FabricId)
        s += ', ' + 'FabricType: ' + str(self.FabricType)
        s += ', ' + 'Flags: ' + str(self.Flags)
        s += ', ' + 'Flags2: ' + str(self.Flags2)
        s += ', ' + 'Index: ' + str(self.Index)
        s += ', ' + 'PCILaneCount: ' + str(self.PCILaneCount)
        s += ', ' + 'Location: ' + str(self.Location)
        s += ', ' + 'Name: ' + str(self.Name)
        s += ', ' + 'Owner: ' + str(self.Owner)
        s += ', ' + 'PodId: ' + str(self.PodId)
        s += ', ' + 'PortGlobalId: ' + str(self.PortGlobalId)
        s += ', ' + 'SledId: ' + str(self.SledId)
        s += ', ' + 'SwitchGlobalId: ' + str(self.SwitchGlobalId)
        s += ', ' + 'DeviceStatusType: ' + str(self.DeviceStatusType)
        s += ', ' + 'PCIVendorId: ' + str(self.PCIVendorId)
        s += '}'
        return s

    def __repr__(self):
        return self.__str__()

    def from_dictionary(self, source):
        """
        Populates an object from the given dictionary
        :param source: Dictionary containing a representation of a JSON object
        :return: This object after being populated from the source dictionary
        """
        super().from_dictionary(source)
        if 'unique' in source:
            self.Unique = source['unique']
        return self

    def to_dictionary(self):
        """
        Creates a dictionary and populates it from this object in a manner
        consistent with JSON conventions
        :return: dictionary object
        """
        result = super().to_dictionary()
        result['unique'] = self.Unique
        return result


class StorageDeviceInfo(DeviceInfo):
    """
    Contains non-status information regarding a storage device
    """

    def __init__(self):
        super().__init__()
        self.Capacity = None

    def __str__(self):
        s = '{'
        s += 'Capacity: ' + str(self.Capacity)
        s += ', ' + 'BusGeneration: ' + str(self.BusGeneration)
        s += ', ' + 'BusWidth: ' + str(self.BusWidth)
        s += ', ' + 'DeviceClass: ' + str(self.DeviceClass)
        s += ', ' + 'ConnectionType: ' + str(self.ConnectionType)
        s += ', ' + 'DeviceIdentifier: ' + str(self.DeviceIdentifier)
        s += ', ' + 'DeviceState: ' + str(self.DeviceState)
        s += ', ' + 'DeviceType: ' + str(self.DeviceType)
        s += ', ' + 'FabricGlobalId: ' + str(self.FabricGlobalId)
        s += ', ' + 'FabricType: ' + str(self.FabricType)
        s += ', ' + 'Family: ' + str(self.Family)
        s += ', ' + 'Flags: ' + str(self.Flags)
        s += ', ' + 'FirmwareRevision: ' + str(self.FirmwareRevision)
        s += ', ' + 'Index: ' + str(self.Index)
        s += ', ' + 'Location: ' + str(self.Location)
        s += ', ' + 'Model: ' + str(self.Model)
        s += ', ' + 'Name: ' + str(self.Name)
        s += ', ' + 'Owner: ' + str(self.Owner)
        s += ', ' + 'PartNumber: ' + str(self.PartNumber)
        s += ', ' + 'PCIDeviceId: ' + str(self.PCIDeviceId)
        s += ', ' + 'PCIVendorId: ' + str(self.PCIVendorId)
        s += ', ' + 'PodId: ' + str(self.PodId)
        s += ', ' + 'SerialNumber: ' + str(self.SerialNumber)
        s += ', ' + 'SledId: ' + str(self.SledId)
        s += ', ' + 'UserDescription: ' + str(self.UserDescription)
        s += ', ' + 'Unique: ' + str(self.Unique)
        s += ', ' + 'Vendor: ' + str(self.Vendor)
        s += '}'
        return s

    def __repr__(self):
        return self.__str__()

    def from_dictionary(self, source):
        """
        Populates an object from the given dictionary
        :param source: Dictionary containing a representation of a JSON object
        :return: This object after being populated from the source dictionary
        """
        super().from_dictionary(source)
        if 'capacity' in source:
            self.Capacity = source['capacity']
        return self

    def to_dictionary(self):
        """
        Creates a dictionary and populates it from this object in a manner
        consistent with JSON conventions
        :return: dictionary object
        """
        result = super().to_dictionary()
        result['capacity'] = self.Capacity
        return result


class StorageDeviceStatus(DeviceStatus):
    """
    Storage Device Status Information
    """

    def __init__(self):
        super().__init__()
        self.CapacityMB = None

    def __str__(self):
        s = '{'
        s += 'CapacityMB: ' + str(self.CapacityMB)
        s += ', ' + 'ConnectionType: ' + str(self.ConnectionType)
        s += ', ' + 'DeviceId: ' + str(self.DeviceId)
        s += ', ' + 'DeviceState: ' + str(self.DeviceState)
        s += ', ' + 'DeviceType: ' + str(self.DeviceType)
        s += ', ' + 'PCIDeviceId: ' + str(self.PCIDeviceId)
        s += ', ' + 'GlobalId: ' + str(self.GlobalId)
        s += ', ' + 'FabricId: ' + str(self.FabricId)
        s += ', ' + 'FabricType: ' + str(self.FabricType)
        s += ', ' + 'Flags: ' + str(self.Flags)
        s += ', ' + 'Flags2: ' + str(self.Flags2)
        s += ', ' + 'Index: ' + str(self.Index)
        s += ', ' + 'PCILaneCount: ' + str(self.PCILaneCount)
        s += ', ' + 'Location: ' + str(self.Location)
        s += ', ' + 'Name: ' + str(self.Name)
        s += ', ' + 'Owner: ' + str(self.Owner)
        s += ', ' + 'PodId: ' + str(self.PodId)
        s += ', ' + 'PortGlobalId: ' + str(self.PortGlobalId)
        s += ', ' + 'SledId: ' + str(self.SledId)
        s += ', ' + 'SwitchGlobalId: ' + str(self.SwitchGlobalId)
        s += ', ' + 'DeviceStatusType: ' + str(self.DeviceStatusType)
        s += ', ' + 'PCIVendorId: ' + str(self.PCIVendorId)
        s += '}'
        return s

    def __repr__(self):
        return self.__str__()

    def from_dictionary(self, source):
        """
        Populates an object from the given dictionary
        :param source: Dictionary containing a representation of a JSON object
        :return: This object after being populated from the source dictionary
        """
        super().from_dictionary(source)
        if 'capacity(MB)' in source:
            self.CapacityMB = source['capacity(MB)']
        return self

    def to_dictionary(self):
        """
        Creates a dictionary and populates it from this object in a manner
        consistent with JSON conventions
        :return: dictionary object
        """
        result = super().to_dictionary()
        result['capacity(MB)'] = self.CapacityMB
        return result


class FabricTopology:
    """
    An array of FabricItem entities
    """

    def __init__(self):
        self.content = []

    def __str__(self):
        return '{' + str(self.content) + '}'

    def from_dictionary(self, source):
        """
        Populates this object from the given dictionary
        :param source: Dictionary containing a representation of a JSON object
        :return: This object after being populated from the source dictionary
        """
        content = list()
        for item in source:
            if item is not None:
                content.append(FabricItem().from_dictionary(item))
        return self

    def to_dictionary(self):
        """
        Creates a dictionary and populates it from this object in a manner
        consistent with JSON conventions
        :return: dictionary object
        """
        result = []
        for entity in self.content:
            list.append(result, entity.to_dictionary())
        return result
