Feature: Kone TestRail Main Page
    Scenario: Login
    Given a user is on the testrail login page
    When the user types "" in the Email field
    And the user types "" in the Password field
    # And the user unchecks the "Keep me logged in" checkbox
    And the user clicks on the Login button
    And the user is redirected to the testrail home page
    And the user clicks on Test User
    Then the user clicks on Logout
    # Then the user is logged out

    Scenario: Add test suite
    Given a user is on the testrail login page
    When the user types "" in the Email field
    And the user types "" in the Password field
    # And the user unchecks the "Keep me logged in" checkbox
    And the user clicks on the Login button
    # And the user is redirected to the testrail home page
    And the user clicks on the Test Suites link
    And the user clicks on the top right Add Test Suite button
    And the user types "Test Suite" in the name field
    And the user types "Test Suite Description" in the description field
    And the user clicks on the Add Test Suite button
    # Then the test suite is created
    Then close the browser