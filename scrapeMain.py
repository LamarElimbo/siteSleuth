# Collect from main URL
# Required info collected: (1a) Title & (1b) Description & (7) Social media pages and handles 

import soupTheLink
import sliceURL

def scrapeMain(pURL):
    souped = soupTheLink.soupTheLink(pURL)
    
    # Collect site title
    splitSiteTitle=[]
    try:
        siteTitle = souped.title.get_text()
        siteTitle = str(siteTitle)
        if len(siteTitle) == 0:
            siteTitle = sliceURL.sliceURL(pURL).replace('.com', '').replace('/', '')
        else:
            splitSiteTitle = siteTitle.split('–')
            if len(splitSiteTitle) == 1:
                splitSiteTitle = siteTitle.split('|')
                if len(splitSiteTitle) == 1:
                    splitSiteTitle = siteTitle.split(':')
                    if len(splitSiteTitle) == 1:
                        splitSiteTitle = siteTitle.split('-')
                        
            siteTitle = splitSiteTitle[0]
        print('title: ', siteTitle)
    except AttributeError:
        siteTitle = sliceURL.sliceURL(pURL).replace('.com', '').replace('/', '')
        
    # Collect site description
    if len(splitSiteTitle) == 2:
        siteDescription = splitSiteTitle[1]
    else:
        try:
            siteDescription = souped.find(id='site-description').get_text()

            if len(siteDescription) == 0:
                siteDescription = souped.find(name='description').get_text()


            print('description: ', siteDescription)
        except AttributeError:
            siteDescription = 'No description found.'
    
    # Collect social media
    commonSocialMedia = ['facebook', 'instagram', 'youtube', 'twitter', 'pinterest', 'linkedin', 'google', 'yelp', 'tumblr', 'github']

    listedURLs = [link.get('href') for link in souped.find_all('a')]
    socials=[]

    for link in listedURLs:

        for social in commonSocialMedia:
            try:
                if social in link:
                    socials.append((link, social))
                else:
                    continue
            except TypeError:
                continue

    print('social media: ', socials)
    
    if len(socials) == 0:
        socials.append(('No socials found.', 'None'))
    
    return siteTitle, siteDescription, socials