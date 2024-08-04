* **docxtpl** is a python library for populating data into word file templates.
* This helps in automating reports very easily. 
* Since we are using word file templates we can use rich text features like fonts, font sizes, colors etc without any programming.

The following files are used in this blog post
* Template word files - [inviteTmpl.docx](https://github.com/nagasudhirpulla/taming_python/raw/master/blog/skills/assets/data/inviteTmpl.docx), [reportTmpl.docx](https://github.com/nagasudhirpulla/taming_python/raw/master/blog/skills/assets/data/reportTmpl.docx)
* images - [party_banner_0.png](https://github.com/nagasudhirpulla/taming_python/raw/master/blog/skills/assets/img/party_banner_0.png), [party_banner_1.png](https://github.com/nagasudhirpulla/taming_python/raw/master/blog/skills/assets/img/party_banner_1.png), [party_banner_2.png](https://github.com/nagasudhirpulla/taming_python/raw/master/blog/skills/assets/img/party_banner_2.png)

While running this scripts, create folders named ```images```, ```invites``` and ```reports```. Download the images and move them into the images folder placed in the same folder as the script file.

### Placeholder for variable in word file
If can render a variable named ```xyz``` by writing ```{{ xyz }}``` in the template word file. The variable can be text or image.

### Basic Example
* This is a simple example using ```docxtpl``` for populating words and images into a birthday invitation template word file. 
* We are using the ```DocxTemplate``` and ```InlineImage``` classes.
* Output should be created as a files named ```invitation.docx``` and ```invitation.pdf```.
* We are using the ```convert``` function from ```docx2pdf``` library for converting word file to pdf file.

# Create a brand new virtual environment
    mkvirtualenv docxtpl-env 

# List all virtual envs
    lsvirtualenv

# Start using a venv
    workon google_env

# Stop using the venv
    deactivate

# Install requirements
    pip install -r requirements.txt

# Besides the requirements.txt dependencies, need to install the following:
    sudo apt install texlive
    sudo apt install pandoc