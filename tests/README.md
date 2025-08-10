# NocoDB API Tests

This directory contains comprehensive tests for the NocoDB API, organized with a shared configuration system for maintainability and reusability.

## 📁 File Structure

```
tests/
├── config.py                    # Shared configuration and utilities
├── test_server_health.py        # Server health and availability tests
├── test_add_employee.py         # Employee record management tests
└── README.md                    # This file
```

## 🔧 Configuration System (`config.py`)

The `config.py` file contains all shared configuration and utilities:

### **Base Configuration**

- `BASE_URL`: NocoDB server URL
- `API_TOKEN`: Authentication token
- `EMPLOYEES_TABLE_ID`: Descriptive table ID for employees

### **Helper Functions**

- `get_auth_headers()`: Returns authentication headers
- `make_api_request()`: Makes HTTP requests with error handling
- `is_success_response()`: Checks if response indicates success
- `is_error_response()`: Checks if response indicates error
- `get_response_data()`: Safely extracts JSON data from response

### **Sample Data (`SampleData` class)**

- `valid_employee()`: Valid employee record
- `employee_with_string_salary()`: Employee with string salary
- `invalid_employee()`: Invalid data for validation testing
- `partial_employee()`: Incomplete data for required field testing
- `salary_test_cases()`: Different salary format test cases

### **API Endpoints (`Endpoints` class)**

- `employees_records()`: Employees table records endpoint
- `employees_record(record_id)`: Specific employee record endpoint
- `table_columns()`: Table schema endpoint

## 🧪 Test Files

### **`test_server_health.py`**

Tests server availability and basic connectivity:

- `test_server_up()`: Basic server response
- `test_server_accessible()`: Network accessibility

### **`test_add_employee.py`**

Comprehensive employee record management tests:

- `test_authentication_status()`: Verify API authentication
- `test_create_record_success()`: Successful record creation
- `test_create_record_with_string_salary()`: String salary handling
- `test_create_record_invalid_data()`: Invalid data validation
- `test_create_record_missing_required_fields()`: Required field validation
- `test_create_record_matching_expected_response()`: Response structure validation
- `test_salary_field_behavior()`: Multiple salary format testing

## 🚀 Usage

### **Run All Tests**

```bash
pytest tests/ -v
```

### **Run Specific Test Files**

```bash
# Server health tests only
pytest tests/test_server_health.py -v

# Employee tests only
pytest tests/test_add_employee.py -v
```

### **Run Specific Test Classes**

```bash
# Only server health tests
pytest tests/test_server_health.py::TestServerHealth -v

# Only employee API tests
pytest tests/test_add_employee.py::TestRecordsAPI -v
```

### **Run Specific Test Methods**

```bash
# Single test method
pytest tests/test_add_employee.py::TestRecordsAPI::test_create_record_success -v
```

## 🔄 Adding New Tests

### **1. Create New Test File**

```python
import pytest
from config import (
    get_auth_headers,
    SampleData,
    Endpoints,
    make_api_request,
    is_success_response,
    is_error_response,
    get_response_data
)

class TestNewFeature:
    """Test class for new feature"""

    @classmethod
    def setup_class(cls):
        cls.headers = get_auth_headers()

    def test_new_functionality(self):
        # Your test logic here
        pass
```

### **2. Add New Sample Data**

In `config.py`, add to the `SampleData` class:

```python
@staticmethod
def new_test_data():
    """Get test data for new feature"""
    return {
        "field1": "value1",
        "field2": "value2"
    }
```

### **3. Add New Endpoints**

In `config.py`, add to the `Endpoints` class:

```python
@staticmethod
def new_feature_endpoint():
    """Get the new feature endpoint"""
    return f"{BASE_URL}api/v2/tables/{NEW_TABLE_ID}/records"
```

## 🎯 Benefits of This Structure

- **DRY Principle**: No code duplication across test files
- **Maintainability**: Single source of truth for configuration
- **Consistency**: All tests use the same patterns and utilities
- **Scalability**: Easy to add new test files and features
- **Readability**: Clear separation of concerns
- **Reusability**: Shared utilities can be used across all tests

## 🔐 Security Notes

- API tokens are stored in the configuration file
- Consider using environment variables for production
- Never commit sensitive tokens to version control
