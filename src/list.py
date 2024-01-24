import json
import decimalencoder
import todoList

def list(event, context):
    try:
        token = event['authorizationToken']
        
        if token == 'allow':
            print('authorized')
            # Obtener la lista de elementos solo si la autorización es exitosa
            result = todoList.get_items()

            # Crear la respuesta
            response = {
                "statusCode": 200,
                "body": json.dumps(result, cls=decimalencoder.DecimalEncoder)
            }

            
            return response

        elif token == 'deny':
            print('unauthorized')
            # Solo generar la política de autorización en caso de denegación
            response = generatePolicy('user', 'Deny', event['methodArn'])
            return response

        elif token == 'unauthorized':
            print('unauthorized')
            raise Exception('Unauthorized')  # Retornar una respuesta 401 No Autorizado

    except Exception as e:
        print(f'Error: {str(e)}')

    # Retornar una respuesta 500 si hay un error no manejado
    return {
        "statusCode": 500,
        "body": json.dumps({"error": "Internal Server Error"})
    }

def generatePolicy(principalId, effect, resource):
    authResponse = {
        "principalId": principalId,
        "policyDocument": {
            "Version": "2012-10-17",
            "Statement": [{
                "Action": "execute-api:Invoke",
                "Effect": effect,
                "Resource": resource
            }]
        },
        "context": {
            "stringKey": "stringval",
            "numberKey": 123,
            "booleanKey": True
        }
    }
    return authResponse
