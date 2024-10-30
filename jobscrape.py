from bs4 import BeautifulSoup
import requests
import re
import time

html_text = requests.get(
    "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation="
).text
# print(html_text)

soup = BeautifulSoup(html_text, "lxml")
jobs = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")
# print(jobs)


print("enter skills you're unfamiliar with: ")
unfamiliar_skill = input(">")
print(f"Filtering out {unfamiliar_skill} ")
print(" ")


def find_jobs():
    for index, job in enumerate(jobs):

        published = job.find("span", class_="sim-posted").text.strip()
        if "few" not in published:
            company_name = job.find("h3", class_="joblist-comp-name").text.strip()

            skills_required = job.find("div", class_="more-skills-sections").text
            skills_required = re.sub(r"\s+", " ", skills_required).strip()

            if unfamiliar_skill not in skills_required:
                with open(f"posts/{index}.txt", "w") as f:
                    link = job.a["href"]
                    f.write(f"company name:  {company_name} \n")
                    f.write(f"skills required:  {skills_required} \n")
                    f.write(f"published: {published} \n")
                    f.write(f"link:  {link} \n")

            print(f"File Saved: {index}")


if __name__ == "__main__":
    while True:
        find_jobs()
        time_wait = 10
        print(f"waiting {time_wait} minutes...")
        time.sleep(time_wait * 60)


# the file names are 0,1,2 then directly 10 because all the ones in between were published "few" days ago. In the terminal,
# it'll show all the files regardless of whether they have the skill or not but only the ones without the unfamiliar skill will get saved.
