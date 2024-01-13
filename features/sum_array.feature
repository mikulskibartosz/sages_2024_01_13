Feature: Sum an array of numbers

  Scenario: Sum an empty array
    Given an empty array
    When I sum the array
    Then the result is 0

  Scenario: Sum an array of one number
    Given an array of one number
    When I sum the array
    Then the result is that number

  Scenario: Sum an array of two numbers
    Given an array with numbers 1, 2
    When I sum the array
    Then I get the result 3

  Scenario Outline: Sum an array of any numbers
    Given an array with numbers <numbers>
    When I sum the array
    Then I get the result <result>
    Examples:
      | numbers | result |
      | 1, 2    | 3      |
      | 1, 2, 3 | 6      |
      | 1, 2, 3, 4 | 10  |
      | 1, 2, 3, 4, 5 | 15 |