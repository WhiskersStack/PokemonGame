import time
import boto3

region = 'us-west-2'
key_name = 'MyKeyPair'
security_group_name = 'MySSHGroup'
instance_name = 'AutoLaunchedEC2'

ec2 = boto3.resource('ec2', region_name=region)
client = boto3.client('ec2', region_name=region)

# 1. Create Key Pair
try:
    key_pair = client.create_key_pair(KeyName=key_name)
    with open(f'{key_name}.pem', 'w') as file:
        file.write(key_pair['KeyMaterial'])
    print(f'✅ Key pair saved to {key_name}.pem')
except client.exceptions.ClientError as e:
    if 'InvalidKeyPair.Duplicate' in str(e):
        print(f'ℹ️ Key pair "{key_name}" already exists. Skipping.')
    else:
        raise

# 2. Create Security Group
try:
    sg_response = client.create_security_group(
        GroupName=security_group_name,
        Description='Allow SSH',
    )
    sg_id = sg_response['GroupId']
    client.authorize_security_group_ingress(
        GroupId=sg_id,
        IpProtocol='tcp',
        FromPort=22,
        ToPort=22,
        CidrIp='0.0.0.0/0'
    )
    print(
        f'✅ Security group "{security_group_name}" created and port 22 opened.')
except client.exceptions.ClientError as e:
    if 'InvalidGroup.Duplicate' in str(e):
        sgs = client.describe_security_groups(GroupNames=[security_group_name])
        sg_id = sgs['SecurityGroups'][0]['GroupId']
        print(
            f'ℹ️ Security group "{security_group_name}" already exists. Using it.')
    else:
        raise

# 3. Get Latest Ubuntu 22.04 AMI
images = client.describe_images(
    Owners=['099720109477'],
    Filters=[
        {'Name': 'name', 'Values': [
            'ubuntu/images/hvm-ssd/ubuntu-22.04-amd64-server-*']},
        {'Name': 'state', 'Values': ['available']}
    ]
)['Images']
latest_ami = sorted(images, key=lambda x: x['CreationDate'], reverse=True)[0]
ami_id = latest_ami['ImageId']
print(f'✅ Using latest Ubuntu AMI: {ami_id}')

# 4. Launch EC2 Instance
instance = ec2.create_instances(
    ImageId=ami_id,
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=1,
    KeyName=key_name,
    SecurityGroupIds=[sg_id],
    TagSpecifications=[{
        'ResourceType': 'instance',
        'Tags': [{'Key': 'Name', 'Value': instance_name}]
    }]
)[0]

print(f'🚀 Launching EC2 instance... ID: {instance.id}')
instance.wait_until_running()
instance.reload()

print(f'✅ Instance is running at IP: {instance.public_ip_address}')
print(
    f'👉 Connect with:\nssh -i {key_name}.pem ubuntu@{instance.public_ip_address}')
