import requests
import uuid

API_TOKEN = "FI4iRIPQGzk3CiS4gBEyIlyVQ_cn_PCouLzIxKlb"
BASE_URL = "http://localhost:8080"
TABLE_ID = "mpx6j6dtu5sr10u"  # Replace with your actual table ID

headers = {
    "xc-token": API_TOKEN,
    "Content-Type": "application/json"
}

def test_insert_and_get_record():
    unique_id = str(uuid.uuid4())[:8]

    payload = {
        "id1": unique_id,
        "first_name": "Test",
        "last_name": "User",
        "email": f"test{unique_id}@example.com",
        "department": "QA",
        "hire_date": "2025-08-05"
    }

    # Create record
    response = requests.post(
        f"{BASE_URL}/api/v2/tables/{TABLE_ID}/records",
        headers=headers,
        json=payload
    )

    assert response.status_code == 200, f"Insert failed: {response.text}"
    inserted_id = response.json()["Id"]

    # Get record by ID
    get_response = requests.get(
        f"{BASE_URL}/api/v2/tables/{TABLE_ID}/records/{inserted_id}",
        headers=headers,
    )

    assert get_response.status_code == 200, f"Get record failed: {get_response.text}"
    record_data = get_response.json()
    print("record data:", record_data)

    assert record_data["first_name"] == "Test"
    assert record_data["last_name"] == "User"
    assert record_data["email"] == f"test{unique_id}@example.com"
    assert record_data["department"] == "QA"
