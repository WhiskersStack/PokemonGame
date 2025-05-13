import boto3

ec2 = boto3.client("ec2", region_name="us-west-2")

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
                        "Value": "test1"
                    }
                ]
            }
        ]
    )

    # Print instance ID
    instance_id = response["Instances"][0]["InstanceId"]
    print(f"Launched EC2 Instance ID: {instance_id}")

if __name__ == "__main__":
    launch_ec2_instance(ec2)