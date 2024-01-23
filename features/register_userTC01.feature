Feature: register_created
  Scenario:register
    Given Navigate to url "https://www.automationexercise.com/"
    When  Verify that home page is visible successfully
    And   Click on Signup_Login button
    And   Verify New User Signup is visible
    And   Enter name and email address
    And   Click Signup button
    And   Verify that ENTER ACCOUNT INFORMATION is visible
    And   Fill details Title Name Email Password Date of birth
    And   Select checkbox Sign up for our newsletter
    And   Select checkbox Receive special offers from our partners
    And   Fill details First name Last name Company Address Address2 Country State City Zipcode Mobile Number
    And   Verify that ACCOUNT CREATED is visible
    And   Click Continue button
    And   Verify that Logged in as username is visible
    #And   Click Delete Account button
    #And   Verify that ACCOUNT DELETED is visible and click Continue button