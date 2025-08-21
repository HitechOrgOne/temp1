def test_uat_example(page, base_url):
    page.goto(base_url)
    assert "Example" in page.title()
