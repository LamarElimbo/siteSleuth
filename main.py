# Main function to call and collect all useful information in dictionary

import sliceURL
import scrapeGivenURL
import scrapeWhoIs
import scrapeAlexa
import getTimezone

def runSearch(pURL):
    
    slicedURL = sliceURL.sliceURL(pURL)
    siteTitle, siteDescription, socials, icon = scrapeGivenURL.scrapeGivenURL(pURL)
    adminName, adminAddress, adminCity, adminStateOrProvince, adminCountry, adminPhone, adminEmail = scrapeWhoIs.scrapeWhoIs(pURL)
    score, keywords = scrapeAlexa.scrapeAlexa(slicedURL)
    
    timezoneId=''
    timezoneName=''
    if adminCity == 'No city found.' or adminStateOrProvince == 'No state or province found.':
        timezoneId = 'No timezone ID found.'
        timezoneName = 'No timezone name found.'
    else:
        timezoneId, timezoneName = getTimezone.getTimezone(adminCity, adminStateOrProvince)
        
    requiredInfo = {'Title': siteTitle, 'Description': siteDescription, 'Socials': socials, 'Icon': icon, "Admin's Name": adminName, 'Address': adminAddress, 'City': adminCity, 'State': adminStateOrProvince, 'Country': adminCountry, 'Phone': adminPhone, 'Email': adminEmail, 'Alexa Score': score, 'Keywords': keywords, 'Timezone ID': timezoneId, 'Timezone Name': timezoneName}
    
    return requiredInfo