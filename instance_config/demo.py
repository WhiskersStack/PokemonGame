{
    "ReservationId": "r-0a129898dc5fa77d5",
    "OwnerId": "356627517575",
    "Groups": [],
    "Instances": [
        {
            "Architecture": "x86_64",
            "BlockDeviceMappings": [],
            "ClientToken": "dc3f21fb-b82f-4d3d-bb9b-38fa1541edc5",
            "EbsOptimized": False,
            "EnaSupport": True,
            "Hypervisor": "xen",
            "NetworkInterfaces": [
                {
                    "Attachment": {
                        "AttachTime": datetime.datetime(
                            2025, 5, 13, 18, 59, 24, tzinfo=tzutc()
                        ),
                        "AttachmentId": "eni-attach-05feb4bded51e07f2",
                        "DeleteOnTermination": True,
                        "DeviceIndex": 0,
                        "Status": "attaching",
                        "NetworkCardIndex": 0,
                    },
                    "Description": "",
                    "Groups": [
                        {"GroupId": "sg-047644bececda0cd3", "GroupName": "default"}
                    ],
                    "Ipv6Addresses": [],
                    "MacAddress": "02:3c:87:a7:b9:e9",
                    "NetworkInterfaceId": "eni-06305b39ba4512d83",
                    "OwnerId": "356627517575",
                    "PrivateDnsName": "ip-172-31-26-216.us-west-2.compute.internal",
                    "PrivateIpAddress": "172.31.26.216",
                    "PrivateIpAddresses": [
                        {
                            "Primary": True,
                            "PrivateDnsName": "ip-172-31-26-216.us-west-2.compute.internal",
                            "PrivateIpAddress": "172.31.26.216",
                        }
                    ],
                    "SourceDestCheck": True,
                    "Status": "in-use",
                    "SubnetId": "subnet-0eda065d0083045ae",
                    "VpcId": "vpc-0223f5e601c8e9292",
                    "InterfaceType": "interface",
                    "Operator": {"Managed": False},
                }
            ],
            "RootDeviceName": "/dev/sda1",
            "RootDeviceType": "ebs",
            "SecurityGroups": [
                {"GroupId": "sg-047644bececda0cd3", "GroupName": "default"}
            ],
            "SourceDestCheck": True,
            "StateReason": {"Code": "pending", "Message": "pending"},
            "Tags": [{"Key": "Name", "Value": "test5"}],
            "VirtualizationType": "hvm",
            "CpuOptions": {"CoreCount": 1, "ThreadsPerCore": 1},
            "CapacityReservationSpecification": {
                "CapacityReservationPreference": "open"
            },
            "MetadataOptions": {
                "State": "pending",
                "HttpTokens": "required",
                "HttpPutResponseHopLimit": 2,
                "HttpEndpoint": "enabled",
                "HttpProtocolIpv6": "disabled",
                "InstanceMetadataTags": "disabled",
            },
            "EnclaveOptions": {"Enabled": False},
            "BootMode": "uefi-preferred",
            "PrivateDnsNameOptions": {
                "HostnameType": "ip-name",
                "EnableResourceNameDnsARecord": False,
                "EnableResourceNameDnsAAAARecord": False,
            },
            "MaintenanceOptions": {"AutoRecovery": "default"},
            "CurrentInstanceBootMode": "legacy-bios",
            "Operator": {"Managed": False},
            "InstanceId": "i-0c359a71808c95222",
            "ImageId": "ami-075686beab831bb7f",
            "State": {"Code": 0, "Name": "pending"},
            "PrivateDnsName": "ip-172-31-26-216.us-west-2.compute.internal",
            "PublicDnsName": "",
            "StateTransitionReason": "",
            "KeyName": "MyKeyPair",
            "AmiLaunchIndex": 0,
            "ProductCodes": [],
            "InstanceType": "t2.micro",
            "LaunchTime": datetime.datetime(2025, 5, 13, 18, 59, 24, tzinfo=tzutc()),
            "Placement": {
                "GroupName": "",
                "Tenancy": "default",
                "AvailabilityZone": "us-west-2b",
            },
            "Monitoring": {"State": "disabled"},
            "SubnetId": "subnet-0eda065d0083045ae",
            "VpcId": "vpc-0223f5e601c8e9292",
            "PrivateIpAddress": "172.31.26.216",
        }
    ],
    "ResponseMetadata": {
        "RequestId": "7909a63f-9348-41b3-94ae-7846327686d6",
        "HTTPStatusCode": 200,
        "HTTPHeaders": {
            "x-amzn-requestid": "7909a63f-9348-41b3-94ae-7846327686d6",
            "cache-control": "no-cache, no-store",
            "strict-transport-security": "max-age=31536000; includeSubDomains",
            "vary": "accept-encoding",
            "content-type": "text/xml;charset=UTF-8",
            "content-length": "3869",
            "date": "Tue, 13 May 2025 18:59:24 GMT",
            "server": "AmazonEC2",
        },
        "RetryAttempts": 0,
    },
}
