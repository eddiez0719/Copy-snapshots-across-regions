import boto3, datetime


def lambda_handler(event, context):
    conn = boto3.client('ec2', region_name='ap-southeast-2')
    snapshots = conn.describe_snapshots()

    snapshots_sorted = sorted(
        [(s['SnapshotId'], datetime.datetime.strftime(s['StartTime'], '%Y-%m-%d'), s['VolumeId']) for s in
         snapshots['Snapshots']], key=lambda k: k[1], reverse=True)

    for snapshot in snapshots_sorted:

        print(snapshot)
        if snapshot[2] == 'vol-099cc6ff1ce6bc10e':
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
            break
    for snapshot in snapshots_sorted:
        if snapshot[2] == 'vol-0deb7c69aace940a5':
            print('Copying Snapshot -> ' + snapshot[0])

            destination_client = boto3.client('ec2', region_name='ap-southeast-1')
            copy_response = destination_client.copy_snapshot(
                Description='Snapshot copied from snapshot' + snapshot[0] + " at " + snapshot[1],
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
                            }
                        ]
                    }
                ]

            )

            print(copy_response)
            break
    for snapshot in snapshots_sorted:
        if snapshot[2] == 'vol-06906cce4f523bbc4':
            print('Copying Snapshot -> ' + snapshot[0])

            destination_client = boto3.client('ec2', region_name='ap-southeast-1')
            copy_response = destination_client.copy_snapshot(
                Description='Snapshot copied from snapshot' + snapshot[0] + " at " + snapshot[1],
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
                            }
                        ]
                    }
                ]

            )

            print(copy_response)
            break
    for snapshot in snapshots_sorted:
        if snapshot[2] == 'vol-0b77ba1055cde48ac':
            print('Copying Snapshot -> ' + snapshot[0])

            destination_client = boto3.client('ec2', region_name='ap-southeast-1')
            copy_response = destination_client.copy_snapshot(
                Description='Snapshot copied from snapshot' + snapshot[0] + " at " + snapshot[1],
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
                            }
                        ]
                    }
                ]

            )

            print(copy_response)
            break
    for snapshot in snapshots_sorted:
        if snapshot[2] == 'vol-0febbe3ff641f547d':
            print('Copying Snapshot -> ' + snapshot[0])

            destination_client = boto3.client('ec2', region_name='ap-southeast-1')
            copy_response = destination_client.copy_snapshot(
                Description='Snapshot copied from snapshot' + snapshot[0] + " at " + snapshot[1],
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
                            }
                        ]
                    }
                ]

            )

            print(copy_response)
            break
    for snapshot in snapshots_sorted:
        if snapshot[2] == 'vol-0ba66804738267fd2':
            print('Copying Snapshot -> ' + snapshot[0])

            destination_client = boto3.client('ec2', region_name='ap-southeast-1')
            copy_response = destination_client.copy_snapshot(
                Description='Snapshot copied from snapshot' + snapshot[0] + " at " + snapshot[1],
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
                            }
                        ]
                    }
                ]

            )

            print(copy_response)
            break
    for snapshot in snapshots_sorted:
        if snapshot[2] == 'vol-07306208033024ece':
            print('Copying Snapshot -> ' + snapshot[0])

            destination_client = boto3.client('ec2', region_name='ap-southeast-1')
            copy_response = destination_client.copy_snapshot(
                Description='Snapshot copied from snapshot' + snapshot[0] + " at " + snapshot[1],
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
                            }
                        ]
                    }
                ]

            )

            print(copy_response)
            break
