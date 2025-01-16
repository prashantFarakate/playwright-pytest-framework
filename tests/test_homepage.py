import pytest
from pages.home_page import HomePage

@pytest.mark.regression
def test_bbc_homepage_navigation(page, config):
    """
    Verifies BBC Home Page loads and essential elements are present.
    """
    home_page = HomePage(page)
    home_page.navigate_to_home_page(config.get_url())

    # Check page title
    expected_title = "BBC Home - Breaking News, World News, US News, Sports, Business, Innovation, Climate, Culture, Travel, Video & Audio"
    assert page.title() == expected_title

    # Verify links and search button
    expected_items = [
        'Home', 'News', 'Sport', 'Business', 'Innovation',
        'Culture', 'Arts', 'Travel', 'Earth', 'Video', 'Live'
    ]
    home_page.assert_links_visible(expected_items)
    assert home_page.is_search_visible()
