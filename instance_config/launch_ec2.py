import boto3
import os
import json
from botocore.exceptions import ClientError

def launch_ec2_instance(ec2):
    # Launch EC2 instance
    response = ec2.run_instances(
        # Amazon Linux 2 AMI (check region-specific AMIs)
        ImageId="ami-075686beab831bb7f",
        InstanceType="t2.micro",
        KeyName="MyKeyPair",
        MinCount=1,
        MaxCount=1,
        TagSpecifications=[
            {
                "ResourceType": "instance",
                "Tags": [
                    {
                        "Key": "Name",
                        "Value": "pokemon3",
                    }
                ]
            }
        ]
    )

    # Print instance security group ID
    instance_id = response["Instances"][0]["InstanceId"]
    print(f"Instance ID: {instance_id}")
    print(f"Security Group ID: {response['Instances'][0]['SecurityGroups'][0]['GroupId']}")
    security_group_id = response["Instances"][0]["SecurityGroups"][0]["GroupId"]


    return instance_id

if __name__ == "__main__":
    launch_ec2_instance(boto3.client("ec2", region_name="us-west-2"))
