import pytest


@pytest.mark.e2e
def test_homepage_loads(page, fastapi_server):
    page.goto("http://127.0.0.1:8000")
    assert page.locator("h1").inner_text() == "Hello World"


@pytest.mark.e2e
def test_addition_flow(page, fastapi_server):
    page.goto("http://127.0.0.1:8000")

    page.fill("#a", "8")
    page.fill("#b", "2")
    page.click("text=Add")

    assert page.locator("#result").inner_text() == "Calculation Result: 10"


@pytest.mark.e2e
def test_subtraction_flow(page, fastapi_server):
    page.goto("http://127.0.0.1:8000")

    page.fill("#a", "8")
    page.fill("#b", "3")
    page.click("text=Subtract")

    assert page.locator("#result").inner_text() == "Calculation Result: 5"


@pytest.mark.e2e
def test_multiplication_flow(page, fastapi_server):
    page.goto("http://127.0.0.1:8000")

    page.fill("#a", "6")
    page.fill("#b", "4")
    page.click("text=Multiply")

    assert page.locator("#result").inner_text() == "Calculation Result: 24"


@pytest.mark.e2e
def test_division_flow(page, fastapi_server):
    page.goto("http://127.0.0.1:8000")

    page.fill("#a", "20")
    page.fill("#b", "5")
    page.click("text=Divide")

    assert page.locator("#result").inner_text() == "Calculation Result: 4"


@pytest.mark.e2e
def test_divide_by_zero_shows_error(page, fastapi_server):
    page.goto("http://127.0.0.1:8000")

    page.fill("#a", "10")
    page.fill("#b", "0")
    page.click("text=Divide")

    assert page.locator("#result").inner_text() == "Error: Cannot divide by zero!"