Feature: ITESO navigation
  As a user
  I want to search for "<Search>" on DuckDuckGo
  So that I can see the search results page

  Scenario Outline: Search university and verify section
    Given I am on DuckDuckGo
    When I search for "<university_url>" on DuckDuckGo
    And I click the first result
    Then I should be on the "<university_url>" website
    When I search for "<section>" inside the site
    Then I should see the "<tab_id>" tab

    Examples:
      | university_url  | section          | tab_id               |
      | iteso.mx        | programas        | carreras-tab         |
      | iteso.mx        | investigacion    | op1-bl1-tab          |
      | iteso.mx        | admision         | Main-Content         |
      | uvm.mx          | oferta-academica | oferta-educativa     |
      | uvm.mx          | admisiones       | hsform-container     |
      | tec.mx          | en/education     | educational-offering |
      | tec.mx          | en/about-us      | Our Institution      |

      
