# Clone the repo to where you like, I like a nice ~/workspace folder
mkdir -p ~/workspace && cd ~/workspace

# Make a note of the where we cloned to
export REPO_ROOT=$(pwd)
git clone https://github.com/philipforget/parser-api-to-html.git

# Make yourself a ~/bin dir if you dont have it
mkdir -p ~/bin

# Install the symlink
cd ~/bin && ln -s "$REPO_ROOT/parser-api-to-html/parser.py" ~/bin/parser
# Make it executable 
chmod +x ~/bin/parser
