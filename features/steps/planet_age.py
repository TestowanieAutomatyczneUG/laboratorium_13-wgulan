from behave import *
from src.planet_age.PlanetAgeCalculator import PlanetAgeCalculator


@given('there is a PlanetAgeCalucator')
def step_impl(context):
    context.planet_age_calculator = PlanetAgeCalculator()


@when('planet is "{planet}" and passed time is equal to "{time:d}" seconds')
def step_impl(context, planet, time):
    context.planet = planet
    context.time = time


@then('the age on this planet is equal to "{age:f}"')
def step_impl(context, age):
    assert context.planet_age_calculator.calculate_age(context.planet, context.time) == age
