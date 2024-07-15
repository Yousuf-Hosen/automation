from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    #expected indented block of code
    
    #1 Launch the browerser
    browser=playwright.chromium.launch(headless=False,slow_mo=5000)
    #2 create a new page
    page=browser.new_page()
    #3 visit the playwright website
    page.goto("https://playwright.dev/python")
    
    #4 locate a link element with "Docs" text
    #locator
    docs_button=page.get_by_role('link',name="Docs")
    
    
    docs_button.click()
    
    # get the url
    print("Docs: ",page.url)
    
    browser.close()
    
    
    