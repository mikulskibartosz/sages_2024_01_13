Feature: Check user permissions

  Scenario:
    Given a logged in user
    And the user has access permission
    But the user is not an admin
    When user tries to access a page
    Then user should be able to access the page
    And user action should be logged