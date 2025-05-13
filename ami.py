import boto3

ec2 = boto3.client('ec2', region_name='us-west-2')

response = ec2.describe_images(
    Owners=['099720109477'],  # Canonical (Ubuntu)
    Filters=[
        {'Name': 'name', 'Values': [
            'ubuntu/images/hvm-ssd/ubuntu-*-amd64-server-*']},
        {'Name': 'state', 'Values': ['available']}
    ]
)

images = sorted(response['Images'],
                key=lambda x: x['CreationDate'], reverse=True)

for image in images[:5]:  # top 5 recent AMIs
    print(f"{image['ImageId']}  -  {image['Name']}")
