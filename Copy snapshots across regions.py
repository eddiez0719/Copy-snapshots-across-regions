import boto3, datetime


def lambda_handler(event, context):
    conn = boto3.client('ec2', region_name='ap-southeast-2')
    snapshots = conn.describe_snapshots()

    snapshots_sorted = sorted(
        [(s['SnapshotId'], datetime.datetime.strftime(s['StartTime'], '%Y-%m-%d'), s['VolumeId']) for s in
         snapshots['Snapshots']], key=lambda k: k[1], reverse=True)

    for snapshot in snapshots_sorted:

        print(snapshot)
        if snapshot[2] == 'vol-xyz001':
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
        if snapshot[2] == 'vol-xyz002':
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
        if snapshot[2] == 'xyz003':
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
        if snapshot[2] == 'xyz004':
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
        if snapshot[2] == 'xyz005':
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
        if snapshot[2] == 'xyz0016':
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
        if snapshot[2] == 'xyz0017':
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
