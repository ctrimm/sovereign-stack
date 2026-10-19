/// <reference path="./.sst/platform/config.d.ts" />

export default $config({
  app(input) {
    return {
      name: "sovereign-stack",
      removal: input?.stage === "production" ? "retain" : "remove",
      protect: ["production"].includes(input?.stage),
      home: "aws",
    };
  },
  async run() {
    new sst.aws.Astro("Web", {
      // Uncomment and set once the domain is chosen and DNS is ready.
      // domain: "sovereignstack.co",
    });
  },
});
