from string import Template

def getResult():
    resultTemplate = Template("""<!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Site Sleuth</title>
        <link rel="stylesheet" href="../static/app.css">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
        <link href='//fonts.googleapis.com/css?family=Didact Gothic' rel='stylesheet'>
        <!-- Latest compiled and minified CSS -->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u"
            crossorigin="anonymous">
        <!-- Optional theme -->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp"
            crossorigin="anonymous">
        <!-- Latest compiled and minified JavaScript -->
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa"
            crossorigin="anonymous"></script>
        <script src="../static/sample_website.js"></script>
    </head>

    <body class="bodystyle">

        <div id="header">
        <div class="navbar-header">
            <a class="navbar-brand" href="search.html">Site Sleuth</a>
        </div>
    </div>
        <div class="container">
            <h1 class="page-header">It took some tough interrogations but I found some info for you!</h1>

            <div class="row">
                <div class="col-xs-11 col-md-5 maintext">
                    <h2>Try another website or list of websites separated by a comma here...</h2>
                    <textarea type='textarea' id='siteInput' form='textform' name='website'></textarea>
                    <form action="/result.html" id='textform' method='post'>
                      <input type="submit" id='submitButton' form='textform'>
                    </form>
                    <br>
                    
                    <h2><center>...or give me a try by selecting from one of the websites below:</center></h2>
                    <div>
                        <p><center><b class="sample_website">http://www.lamartalkscode.com</b></center></p>
                        <p><center><b class="sample_website">http://www.hubba.com/</b></center></p>
                        <p><center><b class="sample_website">http://www.everynoise.com</b></center></p>
                        <p><center><b class="sample_website">http://www.last.fm/</b></center></p>
                        <p><center><b class="sample_website">http://www.goodreads.com/</b></center></p>
                        <p><center><b class="sample_website">http://www.quora.com/</b></center></p>
                        <p><center><b class="sample_website">http://www.dictionary.com/</b></center></p>
                        <p><center><b class="sample_website">http://www.ted.com/</b></center></p>
                        <p><center><b class="sample_website">http://www.trendhunter.com/</b></center></p>
                        <p><center><b class="sample_website">http://www.flipboard.com/</b></center></p>
                    </div>
                </div>

                <div class="col-xs-11 col-md-5 maintext" style='position:absolute; right:7%;'>
                <a href='/downloadCSV'><img id='download' src='/static/logos/download.png'></a>
                    $profileSegment
                </div>
            </div>
        </div>
    </body>

    </html>""")
    return resultTemplate