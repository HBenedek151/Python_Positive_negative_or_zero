Feature: Is Pozitive, Negeative or Zero?
  
  Scenario: 
    Given the number is 3
    When I check the number
    Then I should be told the number is "Pozitive"

  Scenario: 
    Given the number is -5
    When I check the number
    Then I should be told the number is "Negative"

  Scenario: 
    Given the number is 0
    When I check the number
    Then I should be told the number is "Zero"

