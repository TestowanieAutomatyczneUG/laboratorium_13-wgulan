@planet_age
Feature: Age on planets
  Calculates age on different planets based on time passed in seconds

  Scenario: Earth, 1000000000 seconds
    Given there is a PlanetAgeCalucator
    When planet is "Earth" and passed time is equal to "1000000000" seconds
    Then the age on this planet is equal to "31.69"

  Scenario: Mercury, 2000000000 seconds
    Given there is a PlanetAgeCalucator
    When planet is "Mercury" and passed time is equal to "2000000000" seconds
    Then the age on this planet is equal to "263.14"

  Scenario: Venus, 6000000000 seconds
    Given there is a PlanetAgeCalucator
    When planet is "Venus" and passed time is equal to "6000000000" seconds
    Then the age on this planet is equal to "309.05"

  Scenario: Mars, 4000000000 seconds
    Given there is a PlanetAgeCalucator
    When planet is "Mars" and passed time is equal to "4000000000" seconds
    Then the age on this planet is equal to "67.39"

  Scenario: Jupiter, 8000000000 seconds
    Given there is a PlanetAgeCalucator
    When planet is "Jupiter" and passed time is equal to "8000000000" seconds
    Then the age on this planet is equal to "21.37"

  Scenario: Saturn, 3000000000 seconds
    Given there is a PlanetAgeCalucator
    When planet is "Saturn" and passed time is equal to "3000000000" seconds
    Then the age on this planet is equal to "3.23"

  Scenario: Uranus, 7000000000 seconds
    Given there is a PlanetAgeCalucator
    When planet is "Uranus" and passed time is equal to "7000000000" seconds
    Then the age on this planet is equal to "2.64"

  Scenario: Neptune, 5000000000 seconds
    Given there is a PlanetAgeCalucator
    When planet is "Neptune" and passed time is equal to "5000000000" seconds
    Then the age on this planet is equal to "0.96"


