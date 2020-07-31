import boto3, datetime


def lambda_handler(event, context):
    region_source = 'ap-southeast-2'
    client_source = boto3.client('ec2', region_name=region_source)

    li = ['vol-099cc6ff1ce6bc10e', 'vol-0deb7c69aace940a5', 'vol-06906cce4f523bbc4',
          'vol-0b77ba1055cde48ac', 'vol-0febbe3ff641f547d', 'vol-0ba66804738267fd2', 'vol-07306208033024ece']

    copylist = []

    def get_snapshots(item):
        response = client_source.describe_snapshots(
            Filters=[{'Name': 'tag:OpsAutomator:OpsAutomator-Snapshot-SourceVolume',
                      'Values': item}
                     ]
        )
        return response["Snapshots"]

    for i in li:
        snapshot = sorted(
            [(s['SnapshotId'], datetime.datetime.strftime(s['StartTime'], '%Y-%m-%d'), s['VolumeId']) for s in
             get_snapshots([i])], key=lambda k: k[1], reverse=True)[0]
        copylist.append(snapshot)

    for snapshot in copylist:
        print('Copying Snapshot -> ' + snapshot[0])

        destination_client = boto3.client('ec2', region_name='ap-southeast-1')
        copy_response = destination_client.copy_snapshot(
            Description='Snapshot copied from volume' + snapshot[0] + " at " + snapshot[1],
            DestinationRegion='ap-southeast-1',
            SourceRegion='ap-southeast-2',
            SourceSnapshotId=snapshot[0],
            TagSpecifications=[
                {
                    'ResourceType': 'snapshot',
                    'Tags': [
                        {
                            'Key': 'Name',
                            'Value': snapshot[2]
                        },
                    ]
                },
            ],

        )

        print(copy_response)
