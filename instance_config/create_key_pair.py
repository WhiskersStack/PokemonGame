import os
import boto3

# Initialize EC2 client
ec2 = boto3.client("ec2", region_name="us-west-2")  # Use your desired region

# Create key pair
key_pair_name = "MyKeyPair"
response = ec2.create_key_pair(KeyName=key_pair_name)

# Save private key to a .pem file
with open(f"{key_pair_name}.pem", "w") as file:
    file.write(response["KeyMaterial"])

# Set permissions (optional, but needed for SSH)
os.chmod(f"{key_pair_name}.pem", 0o400)

print(f"Key pair '{key_pair_name}' created and saved as '{key_pair_name}.pem'")
