from bs4 import BeautifulSoup
from urllib import request
import  re

html_data  =request.urlopen("https://www.tanveerrajputtv.com/2022/03/50-places-you-must-visit-in-karachi.html").read()
soup = BeautifulSoup(html_data, "html.parser")
tag = soup.find_all("span",attrs={
'style':'color: #ffa400; font-family: Sarabun;'
})

# listofdata1 = [for refinedata  in tag if str(refinedata.next_element) == "<br/>"]
listofdata1 = []
listofdata2 = []
areadata = open("./geodata/area_data.txt","w")
for refinedata  in tag:
        if str(refinedata.next_element) == "<br/>":
            continue
        # data = refinedata.text.split(".")
        # print(refinedata.text)
        new_text= refinedata.text.replace(" ","")
        x =  re.search("\w[A-Za-z]{2,30}",new_text)
        if x:
            if x.group() != "Karachi":
                data = re.sub(r"(\w)([A-Z])", r"\1 \2", x.group())
                areadata.writelines(data+"\n")
                listofdata1.append(data)

            else: areadata.writelines("2\n")

print(listofdata1)
areadata.close()
# print(count)
# for data in tag:
#
#    print(data.find_next("span").text.rsplit("\n"))
#    print("=============MY DATA==========")

