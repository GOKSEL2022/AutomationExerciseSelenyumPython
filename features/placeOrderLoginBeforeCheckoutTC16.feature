Feature: place_order_login_before_checkout
  Scenario:login_before_checkout
Given Navigate to url 'http://automationexercise.com'
When  Verify that home page is visible successfully
And   Click Signup_Login button
And   Fill email password and click Login button
And   Verify Logged in as username at top
