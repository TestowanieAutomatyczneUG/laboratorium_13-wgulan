from behave import *
from src.roman.RomanConverter import RomanConverter

@given('there is a roman converter')
def step_impl(context):
    context.roman_converter = RomanConverter()

@when('arabic number is 4')
def step_impl(context):
    context.arabic_num = 4
@then('converted roman number is IV')
def step_impl(context):
    assert context.roman_converter.roman(context.arabic_num) == 'IV'


@when('arabic number is 6')
def step_impl(context):
    context.arabic_num = 6
@then('converted roman number is VI')
def step_impl(context):
    assert context.roman_converter.roman(context.arabic_num) == 'VI'


@when('arabic number is 9')
def step_impl(context):
    context.arabic_num = 9
@then('converted roman number is IX')
def step_impl(context):
    assert context.roman_converter.roman(context.arabic_num) == 'IX'


@when('arabic number is XXVII')
def step_impl(context):
    context.arabic_num = 27
@then('converted roman number is XXVII')
def step_impl(context):
    assert context.roman_converter.roman(context.arabic_num) == 'XXVII'


@when('arabic number is 48')
def step_impl(context):
    context.arabic_num = 48
@then('converted roman number is XLVIII')
def step_impl(context):
    assert context.roman_converter.roman(context.arabic_num) == 'XLVIII'


@when('arabic number is 49')
def step_impl(context):
    context.arabic_num = 49
@then('converted roman number is XLIX')
def step_impl(context):
    assert context.roman_converter.roman(context.arabic_num) == 'XLIX'


@when('arabic number is 59')
def step_impl(context):
    context.arabic_num = 59
@then('converted roman number is LIX')
def step_impl(context):
    assert context.roman_converter.roman(context.arabic_num) == 'LIX'


@when('arabic number is 93')
def step_impl(context):
    context.arabic_num = 93
@then('converted roman number is XCIII')
def step_impl(context):
    assert context.roman_converter.roman(context.arabic_num) == 'XCIII'