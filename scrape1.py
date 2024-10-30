from bs4 import BeautifulSoup

with open("home.html", "r") as html_file:
    content = html_file.read()
    # print(content)

    soup = BeautifulSoup(content, "lxml")
    # print(soup.prettify())

    course_tags = soup.find_all("h5")
    # print(tags)

    # for course in course_tags:
    # print(course.text)

    course_cards = soup.find_all("div", class_="card")
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]  # gets the last element

        print(f"{course_name} costs {course_price}")
