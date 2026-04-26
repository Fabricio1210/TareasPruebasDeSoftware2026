const { Given, When, Then, Before, After } = require("@cucumber/cucumber");
const { chromium, expect } = require("@playwright/test");

let browser;
let page;

Before(async () => {
    browser = await chromium.launch({
        headless: false,
        args: ["--disable-blink-features=AutomationControlled"],
    });
    page = await browser.newPage();
});

After(async () => {
    await browser.close();
});

Given("I am on the DuckDuckGo homepage", async () => {
    await page.goto("https://duckduckgo.com/");
});

When("I search for {string}", async (query) => {
    await page.locator("#searchbox_input").fill(query);
    await page.keyboard.press("Enter");
    await page.waitForSelector("ol.react-results--main", { timeout: 15000 });
});

Then("the results page title should start with {string}", async (query) => {
    const title = await page.title();
    if (!title.toLowerCase().startsWith(query.toLowerCase())) {
        throw new Error(`Expected title to start with "${query}" but got "${title}"`);
    }
});