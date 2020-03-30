#!/bin/bash
# Install home brew
echo "installing home brew and caskroom...."
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew update
brew install homebrew/cask-cask
brew tap homebrew/cask-versions

echo "install python3 and pipenv..."

brew install python3
pip3 install pipenv

echo "Setting up virtualenv..."
virtualenv -p python3 myenv
source myenv/bin/activate
pip install django
echo "you have to activate virtualenv for your work"

echo "Installing mongodb using brew"
brew tap mongodb/brew
brew install mongodb-community@4.0
brew services start mongodb-community@4.0
