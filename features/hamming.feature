Feature: Hamming distance -
  Calculates count of different genes on same postions in two genotypes

  Scenario: Two empty strands
    Given there is a Hamming distance calculator
    When we calculate hamming distance between two empty strands
    Then the result is 0

  Scenario: Two identical single letter strands
    Given there is a Hamming distance calculator
    When we calculate hamming distance between strand A and A
    Then the result is 0

  Scenario: Two different single letter strands
    Given there is a Hamming distance calculator
    When we calculate hamming distance between strand G and T
    Then the result is 1

  Scenario: Two different long strands
    Given there is a Hamming distance calculator
    When we calculate hamming distance between strand GGACGGATTCTG and AGGACGGATTCT
    Then the result is 9

  Scenario: Two identical long strands
    Given there is a Hamming distance calculator
    When we calculate hamming distance between strand GGACTGAAATCTG and GGACTGAAATCTG
    Then the result is 0