# basic git comands :
## clone -> change -> commit -> push
```
git clone https://github.com/yonibenda/ybd_playground.git
<make changes>
git add <stage files>
git commit -m "<my commit messge>" 
git push origin
```
## pull -> merge -> push
```
git pull origin
<Option 1: no conflicts:>
    git push origin
<Option 2: conflicts:>
    <merge using merge tool -> p4merge.exe>
    git status  //make sure all conflict were resolved
    git commit  // commit the merge 
    git push origin
```

## helpful gui commands :
```
git citool &    // Open a previe of changes, simple "add" & "Commit"
gitk &          // Open Commit history, see changes, when, by whom
```

## information commands :
```
git status   
git --version   
git log 
git blame <path to file>
git fetch origin        //download content from repository with out merging
```
## Other Links to gt tutoriols
- https://www.w3schools.com/git/git_exercises.asp
- https://www.youtube.com/watch?v=DVRQoVRzMIY&t=127s
- https://www.youtube.com/watch?v=BCQHnlnPusY&t=13s

## close issus with commit  
to close an issue in github using the commit tools:
```
git commit -a -m "<commit message> close #<num>" 
```