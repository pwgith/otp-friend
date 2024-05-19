Feature:  
  
Background:
  * def otp_post_url = karate.readAsString('url_otp_post.txt')
  * def otp_get_url = karate.readAsString('url_otp_get.txt')
  * def otp_okta_post_url = karate.readAsString('url_otp_okta_post.txt')
  
Scenario: Basic operations - post and get
  Given url otp_okta_post_url
    And request  
    """
      {
        "eventId": "uS5871kJThSsU8qlA1LTcg",
        "eventTime": "2022-01-28T21:43:40.000Z",
        "eventType": "com.okta.telephony.provider",
        "eventTypeVersion": "1.0",
        "contentType": "application/json",
        "cloudEventVersion": "0.1",
        "source": "https://${yourOktaDomain}/api/v1/inlineHooks/calz6lVQA77AwFeEe0g3",
        "requestType": "com.okta.user.telephony.pre-enrollment",
        "data": {
          "context": {
            "request": {
              "id": "reqRgSk8IBBRhuo0YdlEDTmUw",
              "method": "POST",
              "url": {
                "value": "/api/internal/v1/inlineHooks/com.okta.telephony.provider/generatePreview"
              },
              "ipAddress": "127.0.0.1"
            }
          },
          "userProfile": {
            "firstName": "test",
            "lastName": "user",
            "login": "test.user@okta.com",
            "userId": "00uyxxSknGtK8022w0g3"
          },
          "messageProfile": {
            "msgTemplate": "(HOOK)Your code is 11111",
            "phoneNumber": "9876543210",
            "otpExpires": "2022-01-28T21:48:34.321Z",
            "deliveryChannel": "SMS",
            "otpCode": "11111",
            "locale": "EN-US"
          }
        }
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

