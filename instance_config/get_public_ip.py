import boto3
import time


def get_public_ip(ec2, instance_id):
    # Wait a bit for the instance to be assigned a public IP
    print("\nWaiting for instance to be assigned a public IP...\n")
    time.sleep(10)

    # Describe instance to get full info
    desc = ec2.describe_instances(InstanceIds=[instance_id])
    public_ip = desc["Reservations"][0]["Instances"][0]["PublicIpAddress"]

    print("Public IP:", public_ip)


if __name__ == "__main__":
    get_public_ip(boto3.client("ec2", region_name="us-west-2"), "i-0a1b2c3d4e5f6g7h8")