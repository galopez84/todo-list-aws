import json
import decimalencoder
import todoList


def list(event, context):
    token = event['authorizationToken']
    if token == 'allow':
        print('authorized')
        response = generatePolicy('user', 'Allow', event['methodArn'])
    elif token == 'deny':
        print('unauthorized')
        response = generatePolicy('user', 'Deny', event['methodArn'])
    elif token == 'unauthorized':
        print('unauthorized')
        raise Exception('Unauthorized') # Return a 401 Unauthorized response
        return 'unauthorized'
    try:
        # fetch all todos from the database
        result = todoList.get_items()
    # create a response
        response = {
        "statusCode": 200,
        "body": json.dumps(result, cls=decimalencoder.DecimalEncoder)
        }
        return response
    except:
        print('unauthorized')
        return 'unauthorized' # Return a 500 response
    
    
