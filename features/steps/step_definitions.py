from src.number_category import categorize_number
from behave import given, when, then

# TODO: Írd meg a step definition-öket a feature fájlban lévő scenáriók alapján

@given('the number is {number}')
def step_given_a_number(context, number):
    context.number = float(number)

@when('I check the number')
def step_when_categorize_number(context):
    context.result = categorize_number(context.number)

@then('I should be told the number is "{expected}"')
def step_then_result_positive(context, expected):
    assert context.result == expected