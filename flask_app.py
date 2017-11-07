from flask import Flask, request, render_template, make_response
from io import StringIO
import urllib
import csv

import sys
sys.path.insert(0, './site_sleuth/')
import getResults

app = Flask(__name__)
requiredInfo=[]

@app.route('/')
@app.route('/site_sleuth_search')
def site_sleuth_search():
    return render_template('search.html', 
                           css_source='static/app.css', 
                           activeTab='site_sleuth')

@app.route('/site_sleuth_result', methods=['POST'])
def site_sleuth_result():
    try:
        websites = request.form['website']
        reqInfo = getResults.run(websites)
        requiredInfo.append(reqInfo)
        return render_template('result.html', 
                           css_source='static/app.css', 
                           activeTab='site_sleuth', 
                           requiredInfo=reqInfo)        
    except urllib.error.HTTPError:
        return render_template('error.html', 
                           css_source='static/app.css', 
                           activeTab='site_sleuth')
    except urllib.error.URLError:
        return render_template('search.html', 
                           css_source='static/app.css', 
                           activeTab='site_sleuth')
    except UnicodeDecodeError:
        return render_template('error.html', 
                           css_source='static/app.css', 
                           activeTab='site_sleuth')

@app.route("/site_sleuth_downloadCSV")
def site_sleuth_downloadCSV():
        
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