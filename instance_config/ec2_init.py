import boto3
from launch_ec2 import launch_ec2_instance
from update_security_group import update_security_group
from create_key_pair import create_key_pair



ec2 = boto3.client("ec2", region_name="us-west-2")


def main():
    # Create a key pair
    create_key_pair(ec2)

    # Update security group to allow SSH access
    update_security_group(ec2)

    # Launch an EC2 instance
    launch_ec2_instance(ec2)
    print("EC2 instance launched successfully.")


if __name__ == "__main__":
    main()
