import pytest

from generate_schedule_c import generate_schedule_c1
from generate_schedule_c import generate_schedule_c2
from generate_schedule_c import generate_schedule_c3

from app import app


@pytest.fixture
def multipliers_1():
    return generate_schedule_c1.MULTIPLIERS_1


@pytest.fixture
def multipliers_2():
    return generate_schedule_c2.MULTIPLIERS_2


@pytest.fixture
def multipliers_3():
    return generate_schedule_c3.MULTIPLIERS_3


@pytest.fixture
def transactions_1():
    generate_schedule_c1.TRANSACTIONS_1


@pytest.fixture
def transactions_2():
    return generate_schedule_c2.TRANSACTIONS_2


@pytest.fixture
def transactions_3():
    return generate_schedule_c3.TRANSACTIONS_3


@pytest.fixture
def jobs_3():
    return generate_schedule_c3.JOBS_3


@pytest.fixture
def client():
    """Return test client."""
    return app.test_client()
