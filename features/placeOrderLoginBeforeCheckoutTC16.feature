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
And   Enter description in comment text area and click Place Order
And   Enter payment details Name on Card Card Number CVC Expiration date
And   Click Pay and Confirm Order button
And   Verify success message Your order has been placed successfully
#And   Click Delete Account button
#And   Verify ACCOUNT DELETED and click Continue button



