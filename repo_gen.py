from glob import glob
import lxml.html
from os import environ, mkdir, chdir, chmod
from requests import session
from sys import argv, exit
# custom module
import repo_gen_utils as rgu

base_dir = environ['HOLB_DIR'] + '/'
base_url = 'https://intranet.hbtn.io/'
login_url = base_url + 'auth/sign_in'

only_readme = False
all_projects = False

for item in argv:
    if item == "--readme-only":
        only_readme = True
    if item == "--all":
        all_projects = True

request_url = argv[1]

# starts new session
s = session()
# gets the login page
login = s.get(login_url)
# reformats url into list
login_html = lxml.html.fromstring(login.text)
# gets all necessary hidden inputs
hidden_inputs = login_html.xpath(r'//form//input[@type="hidden"]')
# puts them into dictionary
form = {x.attrib["name"]: x.attrib["value"] for x in hidden_inputs}

# username (make sure env variable is set)
form['user[login]'] = environ['HOLB_USERNAME']
# password (make sure env variable is set)
form['user[password]'] = environ['HOLB_PASS']
# login to holberton intranet
response = s.post(login_url, data=form)

# @TODO: parse the response object and check if login was successful
#        for that it is also make sense to check out s variable (session)

# cleans up memory
del login, login_html, hidden_inputs, form, response

# if all_projects is True:
# now that we're logged in, get the url we really want
page = s.get(request_url)
# turn it into lxml html
root = lxml.html.fromstring(page.text)

# find and make the directory:
try:
    directory = base_dir + root.xpath("//ul/li[contains(., 'Directory:')]/code")[0].text.strip()
except IndexError as e:
    # takes care of when it is a longterm project with just a Github repository field
    try:
        directory = base_dir + root.xpath("//ul/li[contains(., 'GitHub repository:')]/code")[0].text.strip()
    except:
    # this means that the project has a non-standard structure or yor credentials are incorrect.
        print("[ERROR]: Something went wrong. Please report this by creating the issue")
        exit(1)

try:
    mkdir(directory)
except FileExistsError as e:
    print("[WARNING]: Directory already exists. Aborting program to avoid accidentally overwriting your work.")
    exit(2)

# change to directory
chdir(directory)

if only_readme is False:
    # finds and makes all files and directories to be graded
    files = root.xpath("//ul/li[contains(., 'File:')]/code")
    for f in files:
        rgu.file_handle(f.text.strip())
        # chmod(f, 0o764)

    # gets code snippets with files displayed by cat
    code_snippets = root.xpath("//pre/code[contains(., 'cat')]")
    for snippet in code_snippets:
        rgu.snippet_handle(snippet.text)

rgu.generate_readme(argv[1])
