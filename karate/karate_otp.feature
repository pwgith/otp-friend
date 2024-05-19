Feature:  
  
Background:
  * def otp_post_url = karate.readAsString('url_otp_post.txt')
  * def otp_get_url = karate.readAsString('url_otp_get.txt')
  * def otp_okta_post_url = karate.readAsString('url_otp_okta_post.txt')
  
Scenario: Basic operations - post and get
  Given url otp_post_url
    And request  
    """
    {
      "otp_key": "key1",
      "otp_data": "data1" 
    }
    """
    When method POST
    Then status 200

  Given url otp_get_url
    And path "key1"
    When method GET
    Then status 200  
    And match response == 
    """
    {
      "otp_key": "key1", 
      "otp_data": "data1" 
    }
    """


Scenario: update - post and get
  Given url otp_post_url
    And request  
    """
    {
      "otp_key": "key1",
      "otp_data": "data1" 
    }
    """
    When method POST
    Then status 200

  Given url otp_post_url
    And request  
    """
    {
      "otp_key": "key1",
      "otp_data": "data2" 
    }
    """
    When method POST
    Then status 200

  Given url otp_get_url
    And path "key1"
    When method GET
    Then status 200  
    And match response == 
    """
    {
      "otp_key": "key1", 
      "otp_data": "data2" 
    }
    """
