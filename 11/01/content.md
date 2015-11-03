###I/O

###Going to an ATM for cash:

* Input the type of operation (get cash)
* Input the number of cash to get
* Output an LED to indicate that the card needs to be entered
* Input the physical card into the machine
* Input the card PIN
* Input a confirmation to get the cash
* Output the cash
* Output recipe

###Making a cup of tea

* Input tea into a pot
* Input sugar into a pot
* Input water
* Input heat
* Output steam
* Output sound

###Logging into a computer

* Input, output, domain
* Output access or denial

###Example

```
PROGRAM Git-upload.sh

INPUT add-arg
OUTPUT confirm
IF add-arg = .
THEN
files=regex(/*/*)
	ELSE
		files=add(add-arg)
ENDIF
INPUT CommitMessage
commit(files, CommitMessage) > commId
INPUT Branch
INPUT Username
INPUT Password
push(branch, commId, Username, Password)
OUTPUT Revhash, date, repo, sync status
ENDPROGRAM
```
