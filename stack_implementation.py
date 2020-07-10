web_browsing_session = []

web_browsing_session.append(101)
web_browsing_session.append(102)
web_browsing_session.append(103)
web_browsing_session.append(104)
print(web_browsing_session)

btn_status = 1

while btn_status != 0:

    btn_status = int(input("Enter 0 for close or any number for last page\n"))
    if btn_status != 0:

        last_page = web_browsing_session.pop()
        print("Number of pages in stack: ", web_browsing_session)

        if not web_browsing_session:
            print("You were in the final page")
            break

        current_page = web_browsing_session[-1]
        print("last page: ", last_page, "current page: ", current_page)
        print("\n")
