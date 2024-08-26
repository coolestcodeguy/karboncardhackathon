import json
from model import probe_model_5l_profit

def getResult(data):
    # Include your logic here
    return probe_model_5l_profit(data=data)

def handler(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        result = getResult(body["data"])
        return {
            "statusCode": 200,
            "body": json.dumps(result),
            "headers": {
                "Content-Type": "application/json"
            }
        }
    return {
        "statusCode": 404,
        "body": "Not Found"
    }
