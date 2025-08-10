import pytest
from config import (
    get_auth_headers, 
    SampleData, 
    Endpoints, 
    make_api_request, 
    is_success_response, 
    get_response_data
)

class TestAddEmployee:
    """Test class for adding employee records"""
    
    @classmethod
    def setup_class(cls):
        """Setup authentication headers for all tests in this class"""
        cls.headers = get_auth_headers()
        print(f"Using API token: {cls.headers['xc-token'][:20]}...")
    
    def test_add_employee(self):
        """Test adding a new employee record"""
        url = Endpoints.employees_records()
        payload = SampleData.valid_employee()
        
        print(f"Adding employee: {payload['first_name']} {payload['last_name']}")
        print(f"Email: {payload['email']}")
        print(f"Salary: ${payload['salary']}")
        
        response = make_api_request('POST', url, data=payload, headers=self.headers)
        
        if response:
            print(f"Response status: {response.status_code}")
            print(f"Response: {response.text}")
            
            # Assert successful creation
            assert is_success_response(response), f"Failed to add employee. Status: {response.status_code}, Response: {response.text}"
            
            # Verify response contains the created record ID
            response_data = get_response_data(response)
            assert response_data is not None, "Response should contain data"
            assert "id" in response_data or "Id" in response_data, "Response should contain record ID"
            
            # Get the created ID
            employee_id = response_data.get("Id") or response_data.get("id")
            print(f"✅ Employee added successfully with ID: {employee_id}")
            
            # Verify ID is a number
            assert isinstance(employee_id, int), f"Employee ID should be an integer, got {type(employee_id)}"
            
        else:
            assert False, "Request failed - could not add employee"
