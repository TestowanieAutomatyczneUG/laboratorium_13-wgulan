@roman_setup
Feature: Convert arabic number to roman number

  Scenario: Converting number 4
    Given there is a roman converter
    When arabic number is 4
    Then converted roman number is IV

    Scenario: Converting number 6
  Given there is a roman converter
  When arabic number is 6
  Then converted roman number is VI

    Scenario: Converting number 9
  Given there is a roman converter
  When arabic number is 9
  Then converted roman number is IX

    Scenario: Converting number 27
  Given there is a roman converter
  When arabic number is XXVII
  Then converted roman number is XXVII

    Scenario: Converting number 48
  Given there is a roman converter
  When arabic number is 48
  Then converted roman number is XLVIII

    Scenario: Converting number 49
  Given there is a roman converter
  When arabic number is 49
  Then converted roman number is XLIX

    Scenario: Converting number 59
  Given there is a roman converter
  When arabic number is 59
  Then converted roman number is LIX

    Scenario: Converting number 93
  Given there is a roman converter
  When arabic number is 93
  Then converted roman number is XCIII