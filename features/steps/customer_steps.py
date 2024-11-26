from behave import given, when, then
from rest_framework.test import APIClient

client = APIClient()

@given('I have valid customer data')
def step_impl(context):
    context.customer_data = {
        "firstname": "Daniel",
        "lastname": "Mohajer",
        "date_of_birth": "1996-06-06",
        "phone_number": "+989024278589",
        "email": "daniel.mohajer.mohacel@gmail.com",
        "bank_account_number": "123456789012"
    }

@when('I create a customer through the API')
def step_impl(context):
    context.response = client.post('/api/customers/', context.customer_data)

@then('I should see a success message')
def step_impl(context):
    assert context.response.status_code == 201
