from behave import *
from src.hamming.Hamming import Hamming


@given('there is a Hamming distance calculator')
def step_impl(context):
    context.hamming = Hamming()


@when('we calculate hamming distance between two empty strands')
def step_impl(context):
    context.first_strand = ""
    context.second_strand = ""


@then('the result is 0')
def step_impl(context):
    assert context.hamming.distance(context.first_strand, context.second_strand) == 0


@when('we calculate hamming distance between strand A and A')
def step_impl(context):
    context.first_strand = "A"
    context.second_strand = "A"


@when('we calculate hamming distance between strand G and T')
def step_impl(context):
    context.first_strand = "G"
    context.second_strand = "T"


@then('the result is 1')
def step_impl(context):
    assert context.hamming.distance(context.first_strand, context.second_strand) == 1


@when('we calculate hamming distance between strand GGACGGATTCTG and AGGACGGATTCT')
def step_impl(context):
    context.first_strand = "GGACGGATTCTG"
    context.second_strand = "AGGACGGATTCT"


@then('the result is 9')
def step_impl(context):
    assert context.hamming.distance(context.first_strand, context.second_strand) == 9


@when('we calculate hamming distance between strand GGACTGAAATCTG and GGACTGAAATCTG')
def step_impl(context):
    context.first_strand = "GGACTGAAATCTG"
    context.second_strand = "GGACTGAAATCTG"
