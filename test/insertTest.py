import boto3

db = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')
sessions = db.Table('sessions')



sessions.update_item (
    Key = {
        'id' : '123456789'
    },
    UpdateExpression = 'SET command = :val1',
    ExpressionAttributeValues = {
        ':val1' : 'register'
    } 
)
response = sessions.get_item(
    Key = {
        'id' : '123456789'
    }
)
print(response['Item'])