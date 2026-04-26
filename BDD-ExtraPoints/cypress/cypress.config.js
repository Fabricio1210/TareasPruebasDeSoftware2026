const { defineConfig } = require("cypress");
const createBundler = require("@bahmutov/cypress-esbuild-preprocessor");
const {
  addCucumberPreprocessorPlugin,
} = require("@badeball/cypress-cucumber-preprocessor");
const {
  createEsbuildPlugin,
} = require("@badeball/cypress-cucumber-preprocessor/esbuild");

module.exports = defineConfig({
  e2e: {
    specPattern: "cypress/e2e/**/*.feature",
    defaultCommandTimeout: 10000,
    chromeWebSecurity: false,

    async setupNodeEvents(on, config) {
      await addCucumberPreprocessorPlugin(on, config);

      on(
        "file:preprocessor",
        createBundler({
          plugins: [createEsbuildPlugin(config)],
        })
      );
      on("before:browser:launch", (browser, launchOptions) => {
        if (browser.name === "chrome" || browser.name === "electron") {
          launchOptions.args.push("--disable-blink-features=AutomationControlled");
          launchOptions.args.push("--disable-infobars");
          launchOptions.args.push("--no-sandbox");
        }
        return launchOptions;
      });

      return config;
    },
  },
});