#Homework for 10/06

Page: eBay.com

Lets propose a user wants to create a new account in eBay. 

###Timeline

* The user goes to eBay.com
* The user clicks on REGISTER button
* The user is prompted with **screen 1**
* The user fills the text boxes
* Account successfully created

###Validation types by instances

* First name: Format check (ONLY ALPHABETICAL CHARACTERS), presence check
* Last name: Format check (ONLY ALPHABETICAL CHARACTERS), presence check
* Email: Type check (check if it has an @ and contains a .xyz), presence check
* Password: Length check (6-64 characters), character check (must contain at least 1 symbol), case sensitivity check, presence check. **Screen 2**
* Confirm password: equality check, presence check

If any of the required boxes does not match the data or the string returns null, **screen 3** is shown

---

##Screen 1

![](http://i.imgur.com/su0rvTV.png)

##Screen 2
![](http://i.imgur.com/W4x6NKP.png?1)

##Screen 3

![](http://i.imgur.com/kbZPDQk.png)

