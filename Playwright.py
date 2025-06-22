from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Set to True to hide the browser window
        page = browser.new_page()
        page.goto("https://pictory.ai/")
        print(page.title())
        browser.close()

if __name__ == "__main__":
    main()
