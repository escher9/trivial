git init
git remote add origin git@github.com:escher9/%1.git
git add * --ignore-removal
git commit -m "%2"
git push origin master
