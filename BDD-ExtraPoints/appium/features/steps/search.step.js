const { Given, When, Then } = require('@wdio/cucumber-framework');
const assert = require('assert');

Given('I am on the Google homepage', async function () {
    await browser.url('https://www.google.com');
});

When('I search for {string}', async function (query) {
    const searchBox = await $('textarea[name="q"]');
    await searchBox.waitForExist({ timeout: 10000 });
    await searchBox.setValue(query);

    await browser.keys('Enter');
    const results = await $('#rso');
    await results.waitForExist({ timeout: 10000 });
});

Then('the results page title should contain {string}', async function (query) {
    const title = await browser.getTitle();
    assert.ok(
        title.toLowerCase().includes(query.toLowerCase()),
        `Expected title "${title}" to contain "${query}"`
    );
});