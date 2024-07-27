import { SSTConfig } from "sst";
import { API } from "./stacks/api";

export default {
  config(_input) {
    return {
      name: "data-jam",
      region: "us-east-1",
    };
  },
  stacks(app) {
    app.stack(API);
  },
} satisfies SSTConfig;
