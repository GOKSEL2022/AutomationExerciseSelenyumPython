Feature:TC24
  Scenario:TC24
    Given Navigate to url "https://www.automationexercise.com/"
    When Verify that home page is visible successfully
    And  Add products to cart
    And  Click Cart button
    And  Verify that cart page is displayed
    And  Click Proceed To Checkout
    And  Click Register_Login button
    And  Fill all details in Signup and create account
    And  Verify ACCOUNT CREATED and click Continue button