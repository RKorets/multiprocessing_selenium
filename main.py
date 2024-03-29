from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
from time import sleep
from multiprocessing import Pool


class ChromeOptions:

    def __init__(self, profile_number: str):
        self.option = Options()
        self.option.add_argument('--allow-profiles-outside-user-dir')
        self.option.add_argument('--enable-profile-shortcut-manager')
        self.option.add_argument(f'user-data-dir=/Users/rk/Downloads/chrome_cash {profile_number}')
        self.option.add_argument(f'--profile-directory=Profile {profile_number}')
        
def like(number, lst):
    account = ChromeOptions(f'{number}')
    print(f"pid={os.getpid()}, x={number} ")
    with Chrome(service=Service(ChromeDriverManager().install()), options=account.option) as driver:
        for users in lst:
            driver.get(users)
            sleep(3)
            try:
                # driver.find_element(by=By.CLASS_NAME, value='_9AhH0').click()
                driver.find_element(by=By.CLASS_NAME, value='_ac7v').click()
                sleep(3)
                driver.find_element(by=By.CLASS_NAME, value="_aamw").click()
                sleep(1)
                print(f"Success {users}")
            except NoSuchElementException:
                with open(f"not_like_profile-{number}.txt", "a+") as files:
                    files.write(users)
                print("Error like: NoSuchElementException")



def create_list():
    result = []
    with open("data_file__.txt", "r") as file:
        lines = file.readlines()
        count_account = 5
        for users in lines:
            if count_account:
                count_account -= 1
                result.append(users)
    del lines[0:5]
    with open("data_file__.txt", "w+") as file:
        for line in lines:
            file.write(line)
    return result


def multip():
    pool = Pool(processes=3)
    for i in range(0, 3):
        pool.apply_async(like, args=(i, create_list(),))
    pool.close()
    pool.join()
    
    
if __name__ == "__main__":
   multip()
