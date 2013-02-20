Python script to parse a url and output it to html


## Installation

### Automatic installation
```bash
bash <(curl https://raw.github.com/philipforget/parser-api-to-html/master/install.sh)
```

### Custom installation
```bash
# Clone the repo to where you like, I like a nice ~/workspace folder
mkdir -p ~/workspace && cd ~/workspace

# Make a note of the where we cloned to
export REPO_ROOT=$(pwd)
git clone git://github.com/philipforget/parser-api-to-html.git

# Make yourself a ~/bin dir if you dont have it
mkdir -p ~/bin
# And add it to your $PATH
export PATH=~/bin:$PATH

# Install the symlink
cd ~/bin && ln -s "$REPO_ROOT/parser-api-to-html/parser.py" ~/bin/parse
# Make it executable 
chmod +x ~/bin/parse

```


## Examples
```bash
# Will parse to a file called chinese-utf-8.html to the desktop
parse -t <token> http://aprtr.com/rdb/chinese/utf-8/ -o ~/Desktop/chinese-utf-8.html

# Will pipe the content to your clipboard (on OS X)
parse -t <token> http://aprtr.com/rdb/chinese/utf-8/ | pbcopy


## Options for parser.py
```bash
usage: parse [-h] [-t TOKEN] [-o OUTPUT_FILE] [-v] [-r READABILITY_ROOT] url

positional arguments:
  url                   The url to parse

optional arguments:
  -h, --help            show this help message and exit
  -t TOKEN, --token TOKEN
                        Supply a Parser API token to use, if not set looks for
                        $RDB_PARSER_TOKEN
  -o OUTPUT_FILE, --output-file OUTPUT_FILE
                        Supply a filepath to save output to
  -v, --verbose         Increase output verbosity, good for debugging
  -r READABILITY_ROOT, --readability-root READABILITY_ROOT
                        Change the root path of the parser domain from
                        http://www.readability.com
```
