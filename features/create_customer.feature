Feature: Customer creation

  Scenario: Create a new customer
    Given I have valid customer data
    When I create a customer through the API
    Then I should see a success message