# basic shell-bash comands :

```
ls -l
ll
mkdir
cd
pwd
rm
mv
cp
cat
less
history
grep <string> <path> // usful flags (r,i,n,color)
find <path> -name <file name>
echo
```
### information commands :
```
top     - conflict
jobs
kill
man     - conflict
```

# other bash capabilties
Pipe commands
- example 1:  
  grep "string" from the history
    > history | grep <string>
- example 2:  
  grep "string" from the list of file in directory
    > ls -l | grep "string"
- example 2:  
  grep "string" from in file and exclude resolts with "other_string"
    > grep "string" | grep -v "other_string"

Open/create txt file and insert some information to it:
- example 1:
  > echo hello_world > example_1.txt
- example 2:
  > ls -l > example_2.txt