# API Test Plan (NocoDB Testing)

## What we test (API scope)

- Employees API on the NocoDB-generated endpoints (table: `m3jxshm3jce0b2v`).
  - Create employee: `POST /api/v2/tables/{tableId}/records`
  - Get employees (paginated): `GET /api/v2/tables/{tableId}/records`
  - Get employee by Id: `GET /api/v2/tables/{tableId}/records/{id}`
  - Delete employee: `DELETE /api/v2/tables/{tableId}/records` with body `{ "Id": <id> }`

## How we test (strategy)

- Unit-style API tests using `pytest` and `requests`.
- Authentication via `xc-token` header if `API_TOKEN` is provided.
- Deterministic database state:
  - A snapshot DB lives at `nocodb/noco.db.bak`.
  - A pytest `autouse` fixture in `tests/conftest.py` stops the NocoDB container, restores `nocodb/noco.db` from the snapshot, and restarts the service after each test.
  - This guarantees isolation and repeatability.
- Schema/contract checks:
  - Verify creation returns an Id.
  - Verify GET list and paging shape (`list` + `PageInfo`) where applicable.
  - Verify record fields on GET-by-id.
  - Verify DELETE removes the record (404 or not-found on subsequent GET).

### Architectural notes (to justify decisions)

- NocoDB auto-generates REST APIs on top of a SQLite DB (here `nocodb/noco.db`).
- Running behind Docker Compose service `noco` (see `docker-compose.yml`).
- Snapshot-restore pattern keeps tests independent without requiring bespoke seed scripts.

## Success criteria

- Server health: base URL responds with 200/302.
- Create: `POST` returns 200/201 and a numeric `Id`.
- Read (list): `GET` returns 200 with valid JSON (list/dict shape as configured).
- Read (by id): `GET` returns 200 and contains expected fields for the created record.
- Delete: `DELETE` returns 200/204 (or 404 if record absent) and the record is not retrievable afterward.
- No cross-test interference thanks to snapshot restore.

## Environment

- Default base URL: `http://localhost:8080/` (override with `NOCODB_URL`).
- Auth token (optional): `API_TOKEN` (sent as `xc-token`).
- Employees table id: `EMPLOYEES_TABLE_ID` (default `m3jxshm3jce0b2v`).
- Docker Compose service name: `noco`.

Example env setup:

```
export NOCODB_URL=http://localhost:8080/
export API_TOKEN=your_api_token_here   # optional
export EMPLOYEES_TABLE_ID=m3jxshm3jce0b2v
```

## Test data

- Create employee payload (minimal):

```
{
  "first_name": "Alice",
  "last_name": "Tester",
  "email": "alice@example.com",
  "hire_date": "2024-01-15",
  "salary": 55000
}
```

- Deletion sample: `{"Id": <created_id>}`.
- For list endpoint: `?limit=25&shuffle=0&offset=0`.

## Reporting results

- Local runs: `pytest tests/ -v` for verbose output.
- CI-compatible: add `-q --maxfail=1` or `--junitxml=report.xml` if needed.
- Failures print HTTP status codes and response bodies for quick diagnosis.

---

Note: UI test plan will be added later (Selenium-based tests are defined separately and can reuse environment variables and DB snapshoting strategy).
