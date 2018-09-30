# repo_generator
generate directories for Holberton School repositories

## Setup
### Python Environment
This program is written and tested with `Python 3.4.3`
I manage my python environments using `pip`, `virtualenv` and `virtualenvwrapper` so instructions will be written assuming you have those installed.

Assuming Ubuntu:

```sh
sudo apt-get install python3-pip
pip install virtualenv && pip install virtualenvwrapper
```

You need to configure the `virtualenvwrapper`, please read how to do it here: [https://virtualenvwrapper.readthedocs.io/en/latest/](https://virtualenvwrapper.readthedocs.io/en/latest/)

First set up a new environment and install the requirements:

*On MacOS*
```sh
cd repo_generator \
&& mkvirtualenv repo_generator \
&& pip3 install lxml \
&& pip3 install -r requirements.txt
```

*On Ubuntu*
```sh
sudo apt-get install python-lxml \
&& cd repo_generator \
&& mkvirtualenv repo_generator \
&& pip3 install -r requirements.txt
```

If you choose not to use `virtualenv` and `virtualenvwrapper` then just run the `pip install` line above without `&&`.

### Environment Variables
The best way I've found so far to avoid typing your intranet username and password each time the program runs is to set environment variables with your Holberton username and password.
If anybody has suggestions for a better way to do this feel free to suggest it to me.

1. Create `.env` file in the root of this project
2. Add the following to your `.env`:
```
HOLB_DIR='</absolute/path/to/a/directory/with/your/projects>'
HOLB_USERNAME='<username>'
HOLB_PASS='<password>'
```

### repogen.sh script
To start using the *repo_generator* at this point you need to create the symbolic link to the file `repogen.sh` which is located in the root of this project:

```sh
ln -s "$PWD/repogen.sh" /usr/local/bin/
```

## Usage

With everything set up correctly, usage is as simple as

```sh
genrepo <url>
```

with `<url>` being the url for the project you're generating i.e. `https://intranet.hbtn.io/projects/248`

Make sure you have completed the quiz before generating the repo or it won't know what to generate.
If you want to also generate advanced tasks then unlock them manually before generating.
Careful about generating a folder you already have, as the program may overwrite your files.

## Contribute
Please notify me of any bugs by creating an issue in this repository or messaging me on slack. If you want to make the program better by contributing feel free to message me on Slack or come talk to me about improvements. There also may be some issues already listed that you can work on solving if you're interested.



npm ls react-native-background-geolocation
