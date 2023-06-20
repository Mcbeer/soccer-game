# It is assumed that DynamoDB contains a pk of match#<matchId>
from mypy_boto3_dynamodb import DynamoDBClient

from handler import TEAMS_TABLE


def getMatch(matchId):
    # Get the match from DynamoDB
    results = DynamoDBClient.query(
        TableName=TEAMS_TABLE,
        KeyConditionExpression='pk = :pk',
        ExpressionAttributeValues={
            ':pk': {
                'S': 'match'
            },
            ':sk': {
                'S': matchId
            },
        }
    )

    # If no match is found, return a 404
    if len(results['Items']) == 0:
        return {
            'statusCode': 404,
            'body': 'Match not found'
        }

    # Return the match
    return results['Items'][0]["match"]["M"]

# Creates highlights for every event in the match, like "pikachu scored against darth vader"
# I've only implemented the "scored against" and "tackled" event, but you can add more
def createHighlights(match):
    highlights = []
    for event in match["events"]["L"]:
        if event["M"]["action"]["S"] == "scored against":    
          highlights.append(
              event["M"]["player"]["M"]["name"]["S"] + " " +
              event["M"]["action"]["S"] + " " +
              event["M"]["opponent"]["M"]["name"]["S"]
          )
        if event["M"]["action"]["S"] == "tackled":    
          highlights.append(
              event["M"]["player"]["M"]["name"]["S"] + " " +
              event["M"]["action"]["S"] + " " +
              event["M"]["opponent"]["M"]["name"]["S"]
          )
    return highlights
    