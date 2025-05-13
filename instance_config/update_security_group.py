import boto3

# Initialize EC2 client
ec2 = boto3.client("ec2", region_name="us-west-2")  # change region if needed

# Your security group ID
security_group_id = "sg-xxxxxxxx"  # replace with your actual security group ID

# Add SSH (port 22) rule to allow all IPs (0.0.0.0/0)
ec2.authorize_security_group_ingress(
    GroupId=security_group_id,
    IpPermissions=[
        {
            "IpProtocol": "tcp",
            "FromPort": 22,
            "ToPort": 22,
            "IpRanges": [{"CidrIp": "0.0.0.0/0"}],  # or restrict to your IP
        }
    ],
)

print(f"SSH access (port 22) added to security group {security_group_id}")
