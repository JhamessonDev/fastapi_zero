import pytest
from fastapi.testclient import TestClient

from fastapi_zero.app import app


@pytest.fixture
def client():
    """
    Em teste tem 3 etapas (AAA)
    - A: Arrange - Arranjar
    - A: Act     - Agir (executa a coisa, o SUT - suit under test)
    - A: Assert  - Afirma (garante que A é A)
    """
    return TestClient(app)
