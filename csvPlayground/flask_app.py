from flask import Flask, Response
import csv
app = Flask(__name__)

url1 = 'url1'
siteTitle1 = 'siteTitle1'
siteDescription1 = 'siteDescription1'
socials1 = 'socials1'
icon1 = 'icon1'
adminName1 = 'adminName1'
adminAddress1 = 'adminAddress1'
adminCity1 = 'adminCity1'
adminStateOrProvince1 = 'adminStateOrProvince1'
adminCountry1 = 'adminCountry1'
adminPhone1 = 'adminPhone1'
adminEmail1 = 'adminEmail1'
score1 = 'score1'
keywords1 = 'keywords1'
timezoneId1 = 'timezoneId1'
timezoneName1 = 'timezoneName1'

url2 = 'url2'
siteTitle2 = 'siteTitle2'
siteDescription2 = 'siteDescription2'
socials2 = 'socials2'
icon2 = 'icon2'
adminName2 = 'adminName2'
adminAddress2 = 'adminAddress2'
adminCity2 = 'adminCity2'
adminStateOrProvince2 = 'adminStateOrProvince2'
adminCountry2 = 'adminCountry2'
adminPhone2 = 'adminPhone2'
adminEmail2 = 'adminEmail2'
score2 = 'score2'
keywords2 = 'keywords2'
timezoneId2 = 'timezoneId2'
timezoneName2 = 'timezoneName2'

testDict = {'Website': url, 'Title': siteTitle, 'Description': siteDescription, 'Socials': socials, 'Icon': icon, "Admin's Name": adminName, 'Address': adminAddress, 'City': adminCity, 'State': adminStateOrProvince, 'Country': adminCountry, 'Phone': adminPhone, 'Email': adminEmail, 'Alexa Score': score, 'Keywords': keywords, 'Timezone ID': timezoneId, 'Timezone Name': timezoneName}
testDict1 = {'Website': url1, 'Title': siteTitle1, 'Description': siteDescription1, 'Socials': socials1, 'Icon': icon1, "Admin's Name": adminName1, 'Address': adminAddress1, 'City': adminCity1, 'State': adminStateOrProvince1, 'Country': adminCountry1, 'Phone': adminPhone1, 'Email': adminEmail1, 'Alexa Score': score1, 'Keywords': keywords1, 'Timezone ID': timezoneId1, 'Timezone Name': timezoneName1}
testDict2 = {'Website': url2, 'Title': siteTitle2, 'Description': siteDescription2, 'Socials': socials2, 'Icon': icon2, "Admin's Name": adminName2, 'Address': adminAddress2, 'City': adminCity2, 'State': adminStateOrProvince2, 'Country': adminCountry2, 'Phone': adminPhone2, 'Email': adminEmail2, 'Alexa Score': score2, 'Keywords': keywords2, 'Timezone ID': timezoneId2, 'Timezone Name': timezoneName2}

testList = [testDict1, testDict2]


@app.route("/")
def hello():
    return '''
        <html><body>
        Hello. <a href="/getPlotCSV">Click me.</a>
        </body></html>
        '''

@app.route("/getPlotCSV")
def getPlotCSV():
    with open('siteSleuth.csv', 'w') as f:
    w = csv.DictWriter(f, testDict.keys())
    w.writeheader()
    w.writerows(testList)
    
    
    # with open("outputs/Adjacency.csv") as fp:
    #     csv = fp.read()
    #csv = '1,2,3\n4,5,6\n'
    return Response(
        siteSleuth,
        mimetype="text/csv",
        headers={"Content-disposition":
                 "attachment; filename=siteSleuth.csv"})


app.run(debug=True)