import boto3

# Create EC2 client
ec2 = boto3.client("ec2", region_name="us-west-2")

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
                    "Value": "test1"
                }
            ]
        }
    ]
)

# Print instance ID
instance_id = response["Instances"][0]["InstanceId"]
print(f"Launched EC2 Instance ID: {instance_id}")
