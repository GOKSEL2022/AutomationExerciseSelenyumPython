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
    And  Verify Logged in as username at top
    And  Click Cart button
    And  Click Proceed To Checkout button
    And  Verify Address Details and Review Your Order
    And  Enter description in comment text area and click Place Order
    And  Click Pay and Confirm Order button
    And  Verify success message Your order has been placed successfully
    And  Click Download Invoice button and verify invoice is downloaded successfully