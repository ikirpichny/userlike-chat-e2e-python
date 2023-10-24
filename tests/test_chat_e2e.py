import pytest
from conftest import operator_page, customer_page

def test_chat_scenario(operator_page, customer_page):
    # operator
    operator_page
    operator_page.goto('https://www.userlike.com/')
    operator_page.locator('[data-test-id="button-to-login"]').click()
    operator_page.locator('[data-test-id="login-username-input"]').click()
    operator_page.locator('[data-test-id="login-username-input"]').fill('ilia.kirpichny@gmail.com')
    operator_page.locator('[data-test-id="login-password-input"]').click()
    operator_page.locator('[data-test-id="login-password-input"]').fill('tfh0mfw_mcd8NDT@pnw')
    operator_page.locator('[data-test-id="button-to-submit-login-form"]').click()
    operator_page.locator('a:has-text("Message Center")').click()

    # customer
    customer_page.goto('https://www.userlike.com/de/um/debug/153160')
    customer_page.frame_locator('iframe[title="Messenger button"]').click('text=Open')
    customer_page.frame_locator('iframe[title="Messenger"]').click('text=Neue Unterhaltung starten')
    customer_page.frame_locator('iframe[title="Messenger"]').click('input[placeholder="Ihre Nachricht"]')
    customer_page.frame_locator('iframe[title="Messenger"]').fill('input[placeholder="Ihre Nachricht"]', 'hello')
    customer_page.frame_locator('iframe[title="Messenger"]').locator('.frame-1d7d2m0 > button:nth-child(2)').click()

    # check that message is sended form customer
    customer_page.frame_locator('iframe[title="Messenger"]').locator('div:has-text("hello")').first().wait_for_element_state('visible')

    # check http responce after sending message form customer
    customer_response = customer_page.wait_for_response('https://api.userlike.com/api/um/chat/handle/')
    if customer_response.status() == 200:
        print('HTTP-ответ успешен (статус 200 OK).')
    else:
        print('Неверный статус: ' + str(customer_response.status()))

    # check operator
    operator_page.locator('text=Live (1)').wait_for_element_state('visible')
    operator_page.locator('text=hello').first().wait_for_element_state('visible')
    operator_page.locator('text=hello').first().click()
    operator_page.locator('.umc-16r6bns:has-text("hello")').wait_for_element_state('visible')

    # operators answer
    operator_page.locator('textarea').fill('hello hello')
    operator_page.locator('text=Nachricht senden').click()

    # check operatros answer
    operator_page.locator('.umc-16r6bns:has-text("hello hello")').wait_for_element_state('visible')

    # close chat
    operator_page.locator('div:nth-child(5) > .e1968bfk0').click()

    # check tab "Live" is empty
    operator_page.locator('text=Live (0)').wait_for_element_state('visible')

    operator_page.close()
    customer_page.close()

if __name__ == "__main__":
    pytest.main()