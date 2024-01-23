Feature: place_order_login_before_checkout
  Scenario:login_before_checkout
Given Navigate to url 'http://automationexercise.com'
When  Verify that home page is visible successfully
And   Click Signup_Login button
And   Fill email password and click Login button
And   Verify Logged in as username at top
And   Add products to cart
And   Click Cart button
And   Verify that cart page is displayed
And   Click Proceed To Checkout
And   Verify Address Details and Review Your Order


