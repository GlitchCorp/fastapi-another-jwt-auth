import pytest
from fastapi_another_jwt_auth import AuthJWT

@pytest.fixture(scope="module")
def Authorize():
    return AuthJWT()
