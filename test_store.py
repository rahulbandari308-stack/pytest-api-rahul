from jsonschema import validate
import pytest
import schemas
import api_helpers
from hamcrest import assert_that, contains_string, is_

'''
TODO: Finish this test by...
1) Creating a function to test the PATCH request /store/order/{order_id}
2) *Optional* Consider using @pytest.fixture to create unique test data for each run
2) *Optional* Consider creating an 'Order' model in schemas.py and validating it in the test
3) Validate the response codes and values
4) Validate the response message "Order and pet status updated successfully"
'''

@pytest.fixture
def order_payload():
    return {
        "status":"delivered"
    }

def test_patch_order_by_id(order_payload):
    endpoint = '/store/order/1'

    response = api_helpers.patch_api_data(endpoint, order_payload)

    assert response.status_code == 200

    data = response.json()
    assert data["status"] == "delivered"