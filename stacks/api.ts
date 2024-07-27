import { StackContext, Api, Table } from "sst/constructs";

export function API({ stack }: StackContext) {
  const table = new Table(stack, "CartaTable", {
    fields: {
      id: "string",
      sk: "string",
    },
    primaryIndex: { partitionKey: "id", sortKey: "sk" },
    timeToLiveAttribute: "expiration",
  });

  const api = new Api(stack, "Api", {
    routes: {
      $default: {
        function: {
          handler: "packages/api/main.handler",
          runtime: "python3.9",
          timeout: 20,
          memorySize: 1024,
          architecture: "arm_64",
          environment: {
            TABLE_NAME: table.tableName,
            CARTA_URL: "http://bustracker.gocarta.org",
          },
        },
      },
    },
  });

  stack.addOutputs({
    TableName: table.tableName,
    TableArn: table.tableArn,
    ApiEndpoint: api.url,
  });
}
