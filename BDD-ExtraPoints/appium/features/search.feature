Feature: Google Search
  As a user
  I want to search on Google
  So that I can see relevant results

  Scenario Outline: Searching for "<Search>" on Google
    Given I am on the Google homepage
    When I search for "<Search>"
    Then the results page title should contain "<Search>"

  Examples:
    | Search        |
    | Hello, world! |
    | Iteso         |
    | Amazon        |