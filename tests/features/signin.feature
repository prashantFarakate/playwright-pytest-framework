Feature: Verify sign in functionality
    As a BBC website user
    I want to sign in and out of my account
    So that I can access personalized features

    @smoke
    Scenario: User can sign in and sign out successfully
        Given I am on the BBC Home Page
        When I click on sign in button
        And I enter my email
        And I click continue button
        And I enter my password
        And Click sign in button
        Then I should see the BBC Home Page with correct title
        When I click on your account
        And I click on Sign Out
        Then I should see the sign out message

