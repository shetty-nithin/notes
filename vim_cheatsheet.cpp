/*
        Vim Cheat Sheet
        ---------------

:q  - quit
:q! - quit without saving
:wq - write and quit (save and quit)

esc     -   normal mode
v       -   visual mode (selecting the part of the line)
shift+v -   visual line mode (selecting the full line)
cntrl+v -   visual block mode (seleting column wise)

i   -   insert mode before the cursor
a   -   append mode after the cursor
o   -   open a new line below the current line and enter insert mode

I   -   insert mode at the begining of the line
A   -   insert mode at the end of the line
O   -   open a new line above the current line and enter insert mode

0   -   normal mode at the begining of the line
$   -   normal mode at the end of the line
e   -   jump to the end of the word in a normal mode

h   -   move left in the current line till the begining of the line
l   -   move right in the current line til the end of the line
j   -   move down
k   -   move up

xh  -   move left by x places  (x is any number)
xl  -   move right by x places (x is any number)
xj  -   move down by x lines   (x is any number)
xk  -   move up by x lines     (x is any number)

u       -   undo
cntrl+r -   redo
xu          -   x undo's (x is any number)
xcntrl+r    -   x redo's (x is any number)

d   -   delete the selction (in visual mode)
dd  -   delete the line
c   -   delete the selection and enter the insert mode (in visual mode)
cc  -   delete the line and enter the insert mode.
D   -   delete the rest of the line to the right
d$  -   delete the rest of the line to the right
d0  -   delete the rest of the line to the left
C   -   delete the rest of the line to the right and enters the insert mode.

y   -   yanking th selection (copying) (in visual mode)
yy  -   yanking the line (can use "Y" also instead of "yy")
p   -   paste below the current line (if the line is copied)
P   -   paste above the current line (if the line is copied)
p   -   paste after the current word (if only the word is copied)
P   -   paste before the current word (if only the word is copied)
xp  -   paste x times (x is any number)

r   -   replace
w   -   jump to the next word("-" is considered as a word saperator)
W   -   jump to the next word ("-" is not a word saperator)
b   -   jump to the previous word ("-" is considered as a word saperator)
B   -   jump to the previous word ("-" is not a word saperator)

xw/xW  -   jump to the left by x words
xb/xB  -   jump to the right by x words
dw  -   delete word
d2w -   delete 2 words
db  -   delete word
d2b -   delete 2 words
diw -   delete inner word (delete the current word also)
ciw -   delete inner word and enter the insert mode
yiw -   copy inner word

ci" -   delete the content inside the "" and enter the insert mode
di" -   delete the content inside the ""
yi" -   yank the content inside the ""
we can also use : ci[, ci(, di(, di[, etc...

%   -   to jump to the end and begining of the scope
d%  -   delete everything inside the bracket of the scopet

t*  -   jump forward 1 position before the *    (* can be anything)
f*  -   jump forward to the position of the *   (* can be anything)
T*  -   jump backward 1 position after the *    (* can be anything)
F*  -   jump backward to the position of the *  (* can be anything)

gg  -   jump to the begining of the file (combine with the number also)
G   -   jump to the end of the file (combine with the number also)
:45 -   jump to the line number 45 (can be any number)
zz  -   center the current line

==   -  auto indent of the selected code
gg=G -  auto indent the whole file
>>   -   indent to the right (if the line is selected then we can use ">")
<<   -   indent to the left (if the line is selected then we can use "<")

/url    -   search till bottom for "url"
n       -   next occurence of the search
N       -   previous occurenc of the search
?url    -   search till the top for "url"
we can also search by selecting the token and 
    -   press # (search up)
    -   press * (serach down)

.       -   executes the previously executed command.
:reg    -   to see the list of registers.
qa      -   record the macro
q       -   stop recording the macro
@a      -   to run the macro

*/


/*
LUA Configs:

Space       - Menu (Key bindings) 
Space + e   - Toggle the explorer 
Ctrl + h    - Cursor in the Explorer
Ctrl + l    - Cursor in the code.
ctrl + \    - Toggle between the Terminal and the Buffer
*/
