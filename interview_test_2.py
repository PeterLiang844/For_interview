from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 設定 Appium capabilities (根據你的設備修改)
capabilities = {
    "platformName": "Android",
    "deviceName": "你的設備名稱",
    "browserName": "Chrome",
    "chromedriverExecutable": "/path/to/chromedriver",  # 請改成你的 chromedriver 路徑
    "noReset": True
}

# 連線到 Appium Server
driver = webdriver.Remote("http://localhost:4723/wd/hub", capabilities)

try:
    # 1. 開啟國泰世華銀行官網並截圖
    driver.get("https://www.cathaybk.com.tw/cathaybk/")
    time.sleep(5)  # 等待載入
    driver.save_screenshot("step1_homepage.png")
    print("已截圖: step1_homepage.png")

    # 2. 進入信用卡列表頁面
    menu_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.hamburger-menu"))
    )
    menu_button.click()
    time.sleep(2)

    # 點選 個人金融 > 產品介紹 > 信用卡列表
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), '個人金融')]"))
    ).click()
    time.sleep(1)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), '產品介紹')]"))
    ).click()
    time.sleep(1)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), '信用卡列表')]"))
    ).click()
    time.sleep(5)  # 等待頁面載入

    # 計算信用卡數量
    credit_cards = driver.find_elements(By.CSS_SELECTOR, ".credit-card-item")  # 請確認正確的 CSS 選擇器
    credit_card_count = len(credit_cards)
    print(f"信用卡數量: {credit_card_count}")

    # 截圖信用卡列表
    driver.save_screenshot("step2_credit_card_list.png")
    print("已截圖: step2_credit_card_list.png")

    # 3. 進入卡片介紹，計算停發信用卡數量
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), '卡片介紹')]"))
    ).click()
    time.sleep(5)

    # 找出停發的信用卡數量
    discontinued_cards = driver.find_elements(By.XPATH, "//div[contains(text(), '停發')]")
    discontinued_count = len(discontinued_cards)
    print(f"停發信用卡數量: {discontinued_count}")

    # 截圖停發信用卡列表
    driver.save_screenshot("step3_discontinued_cards.png")
    print("已截圖: step3_discontinued_cards.png")

finally:
    driver.quit()
