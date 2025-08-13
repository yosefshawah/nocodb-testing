import pytest
from config import (
    get_auth_headers,
    Endpoints,
    make_api_request,
    get_response_data,
)


class TestFetchEmployee:
    @classmethod
    def setup_class(cls):
        # This record_id should be set from add_employee test
        cls.record_id = 3
        cls.headers = get_auth_headers()

        cls.expected_data = {
            "Id": 3,
            "first_name": "Carol",
            "last_name": "Davis",
            "email": "carol@company.com",
            "hire_date": "2024-01-15",
            "salary": 60000,
            # Now matching API's integer ID for relations
            "nc_4p9k___departments_csv_id": 2,
            "nc_4p9k___roles_id": 3,
        }

    def test_fetch_employee_by_id(self):
        # Fetch Carol by ID
        get_url = Endpoints.employees_record(self.record_id)
        get_resp = make_api_request("GET", get_url, headers=self.headers)
        assert get_resp is not None, "No response from fetch"
        assert get_resp.status_code == 200, f"Fetch failed: {get_resp.status_code} {get_resp.text}"

        fetched = get_response_data(get_resp)
        assert isinstance(fetched, dict), f"Unexpected fetch payload: {type(fetched)}"

        # Check each field matches expected
        for key, expected_value in self.expected_data.items():
            actual_value = fetched.get(key)
            assert actual_value == expected_value, (
                f"{key} mismatch:\nExpected: {expected_value}\nGot: {actual_value}"
            )
