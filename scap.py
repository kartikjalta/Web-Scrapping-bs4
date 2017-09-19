'''The script scrapes data from the url and writes  them to a csv file
names courses.csv. The individual link scraping is put in triple quotes
as it would require a lot of connections to be made. content in the individual
links are stroed in variable 'summary' and the link to apply for the course in
variable 'apply' for each course. they can further be used.'''


from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

#opening connection and downloading page
client=urlopen("http://online.stanford.edu/courses/allcourses")
page_html=client.read()
client.close()


#parsing to html
page_bs=soup(page_html,"html.parser")

#creating a .csv file with headers
f=open("courses.csv","w")
headers="Title, Type of course, Instructor, Platform, Start date, Fees, Status, Department\n"
f.write(headers)

#scraping data
container=page_bs.findAll("div",{"class":"clearfix block block-views"})
for contain in container:
    #breaking rows
    rows=contain.findAll("tr")
    for row in rows[1:len(rows)]:
        title=row.td.a.text.strip()
        type_course=contain.h2.text
        #breaking into columns
        cols=row.findAll("td")
        instructor=cols[1].text.strip()
        platform=cols[2].text.strip()
        start_date=cols[3].text.strip()
        reg_fees=cols[4].text.strip()
        status=cols[5].text.strip()
        department=cols[6].text.strip()

        #Writing into the csv file
        f.write(title.replace(",","|")+","+type_course+","+instructor+","+platform+","+start_date.replace(",","|")+","+reg_fees+","+status+","+department+"\n")
'''        
        #individual link scraping
        hrefer="http://online.stanford.edu"+cols[0].a["href"]
        client1=urlopen(hrefer)
        page_html1=client1.read()
        client1.close()
        pagebs=soup(page_html1,"html.parser")

        content=pagebs.findAll("div",{"class":"field field-name-body field-type-text-with-summary field-label-hidden"})

        #contains the summary of individual courses
        summary=content[0].div.div

        #link to apply
        link=pagebs.findAll("div",{"class":"group-left"})
        apply=link[0].a["href"]
'''        
        
        
f.close()        
    
