Feature: My first feature file using radish
    In order to test my awesome software
    I need an awesome BDD tool like radish
    to test my software.
    
    Scenario: Test get_roots function
        Given I have biquadrate equation with coefficients 1 and 0 and -16
        When I find the roots of it
        Then I expect the result to be "-2, 2"
