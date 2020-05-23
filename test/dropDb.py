'''
Drops all tables in the database, resetting it for testing purposes.
Don't run this in production.....
'''

import boto3

# Get the service resource.
db = boto3.client('dynamodb', endpoint_url='http://localhost:8000')

confirmation = input('Running this script will drop the entire database!\n\
    Are you sure you wish to proceed? (y/n) : ')

if(confirmation == 'y'):
    for tableName in db.list_tables()['TableNames']:
        print('Deleting %s' % (tableName))
        db.delete_table(TableName=tableName)