from os import environ
from urllib import request
from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.event_handler import APIGatewayHttpResolver
from aws_lambda_powertools.utilities.typing.lambda_context import LambdaContext
from aws_lambda_powertools.logging import correlation_paths
from xmlToJson import xmlStringToJson

tracer = Tracer()
logger = Logger()
app = APIGatewayHttpResolver()

baseUrl = environ.get('CARTA_URL', 'https://localhost:3000');

@app.get("/routes/<route_id>/buses")
@tracer.capture_method
def get_buses_by_route_id(route_id: str):
    url = f"{baseUrl}/bustime/map/getBusesForRoute.jsp?route={route_id}"
    response = request.urlopen(url).read().decode('utf-8')
    parsed_data = xmlStringToJson(response)

    # write to dynamodb.

    # return response
    return {"route_id": route_id, "response": parsed_data}

@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_HTTP)
@tracer.capture_lambda_handler
def handler(event:dict, context:LambdaContext)->dict:
    logger.info(event)
    return app.resolve(event, context)