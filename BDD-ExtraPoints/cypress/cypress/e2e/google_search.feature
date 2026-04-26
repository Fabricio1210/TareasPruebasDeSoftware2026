Feature: DuckDuckGo Search
  As a user
  I want to search for "<Search>" on DuckDuckGo
  So that I can see the search results page

  Scenario Outline: Searching for "<Search>" on DuckDuckGo
    Given I am on the DuckDuckGo homepage
    When I search for "<Search>"
    Then the results page title should start with "<Search>"

    Examples:
      | Search        |
      | Hello, world! |
      | Iteso         |
      | Amazon        |