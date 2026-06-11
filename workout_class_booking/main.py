import os
from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by   import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ACCOUNT_EMAIL = "steven@poop.com"
ACCOUNT_PASSWORD = "Poop!2"
GYM_URL = "https://appbrewery.github.io/gym/"

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")

service = Service("/usr/local/bin/chromedriver")


options = Options()
options.binary_location = "/opt/google/chrome/chrome"
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_experimental_option("detach", True)
options.add_argument(f"--user-data-dir={user_data_dir}")


driver = webdriver.Chrome(service=service, options=options)
driver.get(GYM_URL)

wait = WebDriverWait(driver, 10)

booked = 0

waitlisted = 0

existing = 0

processed_classes = []

def login():

    login_button = wait.until(EC.visibility_of_element_located((By.ID, "login-button")))
    login_button.click()

    input_email = wait.until(EC.visibility_of_element_located((By.ID, "email-input")))
    input_email.send_keys(ACCOUNT_EMAIL)

    input_password = wait.until(EC.visibility_of_element_located((By.ID, "password-input")))
    input_password.send_keys(ACCOUNT_PASSWORD)

    submit_button = wait.until(EC.visibility_of_element_located((By.ID, "submit-button")))
    submit_button.click()

    wait.until(EC.presence_of_element_located((By.ID, "schedule-page")))

login()

class_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")

for card in class_cards:

    day_group = card.find_element(By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]")
    day_title = day_group.find_element(By.TAG_NAME, "h2").text

    if "Tue" in day_title or "Thu" in day_title:

        time_text = card.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text

        if "6:00 PM" in time_text:

            class_name = card.find_element(By.CSS_SELECTOR, "h3[id^='class-name-']").text

            booked_button_el = card.find_element(By.CLASS_NAME, "ClassCard_bookButton__DMM1I")

            button = card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")

            class_info = f"{class_name} on {day_title}"

            if booked_button_el.text == "Book Class":

                button.click()

                print("booked")

                booked =+ 1

                processed_classes.append(f"[Booked] {class_info}")

            elif booked_button_el.text == "Booked":

                print("class already booked")

                existing =+ 1

                processed_classes.append(f"[Booked] {class_info}")

            elif booked_button_el.text == "Join Waitlist":

                button.click()

                print("waitlisted")

                waitlisted =+ 1

                processed_classes.append(f"[Booked] {class_info}")

print(f"--- BOOKING SUMMARY ---\n"
      f"Classes booked: {booked}\n"
      f"Waitlists joined: {waitlisted}\n"
      f"Already booked/waitlisted: {existing}\n"
      f"Total Tuesday & Thursday 6pm classes processed: {booked + waitlisted + existing}")

total_booked = booked + waitlisted + existing

my_bookings = wait.until(EC.presence_of_element_located((By.ID, "my-bookings-link")))
my_bookings.click()

verified_count = 0

all_cards = driver.find_elements(By.CSS_SELECTOR, "div[id*='card-']")

for card in all_cards:
    try:
        when_paragraph = card.find_element(By.XPATH, ".//p[strong[text()='When:']]")

        when_text = when_paragraph.text

        if ("Tue" in when_text or "Thu" in when_text) and "6:00 PM" in when_text:

            class_name = card.find_element(By.TAG_NAME, "h3").text

            print(f"  Verified: {class_name}")

            verified_count += 1

    except NoSuchElementException:

        pass

print(f"\n--- VERIFICATION RESULT ---")
print(f"Expected: {total_booked} bookings")
print(f"Found: {verified_count} bookings")

if total_booked == verified_count:
    print("all bookings verified!")
else:
    print(f"missing {total_booked - verified_count} bookings")


print("\n--- DETAILED CLASS LIST ---")
for class_detail in processed_classes:
    print(f"  • {class_detail}")