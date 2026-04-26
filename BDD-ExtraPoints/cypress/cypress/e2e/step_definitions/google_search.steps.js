import { Given, When, Then } from "@badeball/cypress-cucumber-preprocessor";

Given("I am on the DuckDuckGo homepage", () => {
    cy.visit("https://duckduckgo.com/");
});

When("I search for {string}", (query) => {
    cy.get('#searchbox_input')
    .should("be.visible")
    .clear()
    .type(query)
    .type("{enter}");
    cy.get('ol.react-results--main', { timeout: 15000 }).should("exist");
});

Then("the results page title should start with {string}", (query) => {
    cy.title().should("match", new RegExp(`^${query}`, "i"));
});