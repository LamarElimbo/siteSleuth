# Creates html segment from collected info

from string import Template
import htmlSeg

def createHTML(pRequiredInfo):
    
    htmlSegs=''
    
    for website in pRequiredInfo:
        htmlSegment = htmlSeg.getHTMLSeg()
        url = pRequiredInfo[0]
        
        socialSeg=''
        socials=website[1]['Socials']
        
        if socials != [('No socials found.', 'None')]:
            for social in socials:
                socialSeg += "<a href=" + social[0] + "><img class='socials' src=/static/logos/" + social[1] + ".png></a>"
        else:
            socialSeg = "<br>"
            
        keywordSeg=''

        for keyword in website[1]['Keywords']:
            if keyword == 'No kewords found.':
                keywordSeg = keyword
            else:
                keywordPart = '#' + keyword
                keywordSeg += keywordPart
        
        htmlSegs += htmlSegment.substitute(site=website[0], title=website[1]['Title'], description=website[1]['Description'], socials=socialSeg, icon=website[1]['Icon'], name =website[1]["Admin's Name"], address=website[1]['Address'], city=website[1]['City'], state=website[1]['State'], country=website[1]['Country'], phone=website[1]['Phone'], email=website[1]['Email'], alexa_score=website[1]['Alexa Score'], keywords=keywordSeg, timezone_id=website[1]['Timezone ID'], timezone_name=website[1]['Timezone Name'])
            
    return htmlSegs
