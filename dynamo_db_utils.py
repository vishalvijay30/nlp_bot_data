import boto3

dynamodb = boto3.resource('dynamodb')

def create_table(table_name):
    dynamodb.create_table(
        TableName=table_name,
        KeySchema=[
            {
                'AttributeName': 'question',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'answer',
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'question',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'answer',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1
        }
    )

def populate_table(data, table):
    with table.batch_writer() as batch:
        # data is a dictionary of question:answer pairs
        for question in data:
            batch.put_item(
                Item = {
                    'question': question,
                    'answer': data[question]
                }
            )
            print("Added question: " + question + " with answer: ", data[question])