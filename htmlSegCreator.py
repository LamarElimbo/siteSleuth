# Creates html segment from collected info

from string import Template
import htmlSeg

def createHTML(pRequiredInfo):
    
    htmlSegs=''
    
    for website in pRequiredInfo:
        htmlSegment = htmlSeg.getHTMLSeg()
        url = website['Website']
        
        socialSeg=''
        socials=website['Socials']
        
        if socials != [('No socials found.', 'None')]:
            for social in socials:
                socialSeg += "<a href=" + social[0] + "><img class='socials' src=/static/logos/" + social[1] + ".png></a>"
        else:
            socialSeg = "<br>"
            
        keywordSeg=''

        for keyword in website['Keywords']:
            if keyword == 'No kewords found.':
                keywordSeg = keyword
            else:
                keywordPart = '#' + keyword
                keywordSeg += keywordPart
        
        htmlSegs += htmlSegment.substitute(site=website['Website'], title=website['Title'], description=website['Description'], socials=socialSeg, icon=website['Icon'], name =website["Admin's Name"], address=website['Address'], city=website['City'], state=website['State'], country=website['Country'], phone=website['Phone'], email=website['Email'], alexa_score=website['Alexa Score'], keywords=keywordSeg, timezone_id=website['Timezone ID'], timezone_name=website['Timezone Name'])
            
    return htmlSegs
