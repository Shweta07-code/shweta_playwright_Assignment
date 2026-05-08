from pages.login_page import LoginPage


def test_careerflow_login(page):

    """
    This test validates the login functionality
    of Careerflow.ai.

    Login is a critical user flow because users
    must authenticate successfully to access
    career tools and dashboards.
    """

    login = LoginPage(page)

    # Open Website
    login.load()

    # Click Login
    login.click_login()

    # Enter Credentials
    login.enter_email("shwetapachouri7@gmail.com")

    login.enter_password("Testing@12345")

    # Submit Login
    login.submit_login()

    # Assertion
    
    page.wait_for_load_state("domcontentloaded")

    print(page.url)

    assert "login" in page.url