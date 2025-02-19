from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        self.page.goto(url)

    def click(self, selector: str):
        self.page.click(selector)

    def enter_text(self, selector: str, text: str):
        self.page.fill(selector, text)

    def get_text(self, selector: str):
        return self.page.inner_text(selector)
