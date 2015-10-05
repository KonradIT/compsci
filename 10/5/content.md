#Checking ISBN digits
<!---
this helps: http://www.nationallibrary.fi/publishers/isbn/revision.html
-->

* a) 194872349
* b) 188246131
* c) 194242439
* d) 187892156

then check if they are correct

---

**a)**

1  9  4  8  7  2  3  4  9
1  3  1  3  1  3  1  3  1
1  27 4  24 7  6  3  12 9

= 3

276 = 25

**b)** 

1  8  8  2  4  6  1  3  1
1  3  1  3  1  3  1  3  1
1  24 8  6  4  18 1  9  1

= 3

232 = 21

**c)**

1  9  4  2  4  2  4  3  9
1  3  1  3  1  3  1  3  1
1  27 4  6  4  6  4  9  9

= 6

220 = 20

**d)**

1  8  7  8  9  2  1  5  6
1  3  1  3  1  3  1  3  1
1  24 7  24 9  6  1  15 6

297 = 27

##Database task

* Name: Format check (checks if the input are alphabetical characters and that its not empty)
* Surname: Format check, presence check
* DOB: Length check, length check, parse check (dd/MM/YYYY)
* State/Province/Country: Lookup table using google maps data, presence check
* Age: format check, range check (8-18), presence check
* Gender: checkboxes
* email address: format check, length check, type check (check if it has an @ and a .xyz)
* password: check if its between 4 and 12 characters long (length check), check if it has 1 Uppercase letter, 1 number (format check), presence check and character check (no symbols, only letters and numbers)

