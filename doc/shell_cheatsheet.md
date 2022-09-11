# basic shell-bash comands :
```
ll      //list all files with information
ls      //list all files with out information
ls -l                                    
mkdir   //Create the DIRECTORY(ies), if they do not already exist
cd      //Change the shell working directory.
pwd     //Print the name of the current working directory.
rm      //Remove
mv      //move
cp      //Copy SOURCE to DEST
less    //open the file for read - 'q'==close.'/'==search , 'n'==next_search, 'g'==top of file. 
```


### helpful shell-bash commands :
```
```
### information commands :
```
top         //command not found
jobs        //Display status of jobs.
kill        //Send a signal to a job
man         //command not found
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
  //to amend end of file use ">>"
  > echo hello_world >> example_1.txt
- example 2:
  > ls -l > example_2.txt


## opening file to reading
```
less <file path>
```
to navigate within the "less" file:
```
q           // quit
gg          // top of file
G <shift+g> // end of file
b           // up
<space>     // down
`/`         // search example: /hello+<enter> will search for the word hello
n           // Next - used for searching
N <Shift+n> // Previous 
```