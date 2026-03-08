from pages.base_page import BasePage, BasketPage

#Бутут переписаны. В них сейчас нет необходимости

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasePage(browser, link)
    page.open()
    page.should_be_basket_button()
    page.go_to_basket_page()
    page.should_not_be_products_in_basket()
    page.should_see_message_basket_is_empty()