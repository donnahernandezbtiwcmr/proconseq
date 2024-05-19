from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def call_until(times, element_id, driver, wait_time, agree_btn):
    """
    Calls the element with the given ID until it is found or the number of times is reached.

    Args:
        times (int): The number of times to call the element.
        element_id (str): The ID of the element to call.
        driver (webdriver): The webdriver to use.
        wait_time (int): The amount of time to wait for the element to be found.
        agree_btn (webdriver): The agree button to click if the element is found.
    """
    for i in range(times):
        try:
            element = WebDriverWait(driver, wait_time).until(
                EC.presence_of_element_located((By.ID, element_id))
            )
            agree_btn.click()
            return element
        except:
            pass
    return None
