import boto3

# Get the service resource.
db = boto3.resource('dynamodb')

# Create a table to store command sessions
db.create_table(
    TableName = 'sessions',
    KeySchema = [
        {
            'AttributeName' : 'id',
            'KeyType' : 'HASH'
        }
    ],
    AttributeDefinitions = [
        {
            'AttributeName' : 'id',
            'AttributeType' : 'N'
        }
    ],
    ProvisionedThroughput = { 
        'ReadCapacityUnits' : 1,
        'WriteCapacityUnits' : 1
    }
)

#Create a table to store member info
db.create_table(
    TableName = 'members',
    KeySchema = [
        {
            'AttributeName' : 'id',
            'KeyType' : 'HASH'
        }
    ],
    AttributeDefinitions = [
        {
            'AttributeName' : 'id',
            'AttributeType' : 'N'
        }
    ],
    ProvisionedThroughput = { 
        'ReadCapacityUnits' : 1,
        'WriteCapacityUnits' : 1
    }
)
