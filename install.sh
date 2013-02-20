# Clone the repo to where you like, I like a nice ~/workspace folder
mkdir -p ~/workspace && cd ~/workspace

# Make a note of the where we cloned to
export REPO_ROOT=$(pwd)
git clone https://github.com/philipforget/parser-api-to-html.git

# Make yourself a ~/bin dir if you dont have it and add it to your path
mkdir -p ~/bin
echo "export PATH=~/bin:$PATH" >> ~/.bash_profile && source $!

# Install the symlink
cd ~/bin && ln -s "$REPO_ROOT/parser-api-to-html/parser.py" ~/bin/parse

# Make it executable 
chmod +x ~/bin/parse
