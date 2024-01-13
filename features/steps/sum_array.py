from behave import *

def sum_array(array):
    return sum(array)

ONE_NUMBER_ARRAY_VALUE = 1

@given(u'an empty array')
def step_impl(context):
    context.addends = []


@when(u'I sum the array')
def step_impl(context):
    context.result = sum_array(context.addends)


@then(u'the result is 0')
def step_impl(context):
    assert context.result == 0


@given(u'an array of one number')
def step_impl(context):
    context.addends = [ONE_NUMBER_ARRAY_VALUE]


@then(u'the result is that number')
def step_impl(context):
    assert context.result == ONE_NUMBER_ARRAY_VALUE, \
        "Expected {0}, but got {1}".format(ONE_NUMBER_ARRAY_VALUE, context.result)


@given(u'an array with numbers {numbers}')
def step_impl(context, numbers):
    context.addends = [int(number) for number in numbers.split(',')]


@then(u'I get the result {result}')
def step_impl(context, result):
    assert context.result == int(result), \
        "Expected {0}, but got {1}".format(result, context.result)
