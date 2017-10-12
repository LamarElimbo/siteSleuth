from flask import Flask, request, render_template
from string import Template
import mergeInfo
import htmlSegCreator
import searchResult

app = Flask(__name__)

@app.route('/')
@app.route('/search.html')
def search():
    return render_template('search.html')

@app.route('/result.html', methods=['POST'])
def result():
    websites = request.form['website']
    websites = websites.replace(" ", "")
    websiteList = websites.split(',')
    print('websiteList: ', websiteList)
    requiredInfo = mergeInfo.runSearch(websiteList)
    profileSeg = htmlSegCreator.createHTML(requiredInfo)
    resultTemplate = searchResult.getResult()
    return resultTemplate.substitute(profileSegment=profileSeg)
    
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)