from string import Template

def getHTMLSeg():
    htmlTemplate = Template("""<div class="profile_container">

                        <div class="infoBox" id='title'>
                            <h1>$title</h1>
                            <p><a href=$site>$site</a></p>
                            <p>Alexa Score | $alexa_score</p>
                            <p>$socials</p>
                        </div>
                        <div id='logo'><img src=$icon></div>
                        <div class="infoBox" id="description">
                            <h3>Site Description</h3>
                            <p>$description</p>
                        </div>
                        <div class="infoBox" id='keywords'>
                            <h3>Keywords</h3>
                            <p><i>$keywords</i></p>
                        </div>
                    </div>

                    <div class="profile_container">
                        <div class="infoBox" id="name">
                            <h3>Admin</h3>
                            <p>$name</p>
                        </div>
                        <div id="adminPic"></div>
                        <div id="address">
                            <div class="infoBox">
                                <h3>Address</h3>
                                <p>$address</p>
                            </div>
                            <div class="infoBox">
                                <p>$city | $state | $country</p>
                            </div>
                        </div>
                        <div class="infoBox" id="timezone">
                            <h3>Timezone</h3>
                            <p>$timezone_id | $timezone_name</p>
                        </div>
                        <div class="infoBox" id="contact">
                            <h3>Contact</h3>
                            <p>$phone | <img height=18 src=$email></p>
                        </div>
                    </div><br>
                    <div id='divider'></div><br><br>""")
    return htmlTemplate