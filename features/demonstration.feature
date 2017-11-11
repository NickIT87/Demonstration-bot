Feature: Demonstration bot for QA white book

 Scenario Outline: Demonstartion my features
    Given I am on home page
    Then i learn more and redirect to features page
    Then i work with features cypher <original_text>, <crypt_key>, <crypt_message>
    Then i work with features bot <runquestion>, <answerone>, <answertwo>, <answerthree>
 
 Examples: By category
    | original_text       | crypt_key | crypt_message       | runquestion | answerone | answertwo | answerthree |
    | hasta la vista baby | 98769865  | qizzj rf dpyci gjjf | start       | yes       | no        | okay        |
