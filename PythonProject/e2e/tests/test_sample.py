def test_open_page(page):
    page.goto("https://saucedemo.com/")
    assert "Example Domain" in page.title()
