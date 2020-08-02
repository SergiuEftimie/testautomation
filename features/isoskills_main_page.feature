Feature: IsoSkills Main Page
    Scenario: Contact Form
    Given a user is on the main page
    When the user types "John" in the "Your Name (required)" contact field
    And the user types "john.doe@test.com" in the "Your Email (required)" contact field
    And the user types "Test Subject - Automated Test" in the "Subject" contact field
    And the user types "This is a test message" in the "Your Message" text area
    And the user clicks on the send button
    Then the "Thank you for your message. It has been sent." text is displayed

    Scenario: AI Training for IT Specialists News Article
    Given a user is on the main page
    When the user clicks on the "News and Articles" link
    And the user clicks on the "Read more" button for the "AI Training for IT Specialists" article
    Then the "AI Training for IT Specialists" article is opened

    Scenario: Agile Transformation Done Right News Article
    Given a user is on the main page
    When the user clicks on the "News and Articles" link
    And the user clicks on the "Read more" button for the "Agile Transformation Done Right" article
    Then the "Agile Transformation Done Right" article is opened

    Scenario: Looking forward to in 2019! News Article
    Given a user is on the main page
    When the user clicks on the "News and Articles" link
    And the user clicks on the "Read more" button for the "Looking forward to in 2019!" article
    Then the "Looking forward to in 2019!" article is opened

    Scenario: Search field
    Given a user is on the main page
    When the user searches for "Agile" using the search field
    Then the "Agile Transformation Done Right" appears in the results list

    Scenario: Facebook Social Media
    Given a user is on the main page
    When the user clicks on the "Facebook" social button
    Then the user is redirected to the "https://www.facebook.com/isoskills" page

    Scenario: LinkedIn Social Media
    Given a user is on the main page
    When the user clicks on the "LinkedIn" social button
    Then the user is redirected to the "https://www.linkedin.com/company/isoskills" page
    Then close the browser