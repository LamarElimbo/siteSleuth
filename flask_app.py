from flask import Flask, request, render_template, make_response
from string import Template
from io import StringIO
import urllib
import csv
import mergeInfo
import htmlSegCreator
import searchResult
import urlNormalizer


app = Flask(__name__)
requiredInfo=[]

@app.route('/')
@app.route('/search.html')
def search():
    return render_template('search.html')

@app.route('/result.html', methods=['POST'])
def result():
    try:
        websites = request.form['website']
        websiteList = urlNormalizer.normalizeURL(websites)
        global requiredInfo
        requiredInfo=[]
        requiredInfo += mergeInfo.runSearch(websiteList)
        profileSeg = htmlSegCreator.createHTML(requiredInfo)
        resultTemplate = searchResult.getResult()
        return resultTemplate.substitute(profileSegment=profileSeg)
    except urllib.error.HTTPError:
        return render_template('error.html')
    except urllib.error.URLError:
        return render_template('search.html')
    except UnicodeDecodeError:
        return render_template('error.html')

@app.route("/downloadCSV")
def downloadCSV():
        
    print('required info: ', requiredInfo)
    si = StringIO()
    w = csv.DictWriter(si, requiredInfo[0].keys())
    w.writeheader()
    w.writerows(requiredInfo)
    
    output = make_response(si.getvalue())
    output.headers["Content-Disposition"] = "attachment; filename=siteSleuth.csv"
    output.headers["Content-type"] = "text/csv"
    
    return output

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)