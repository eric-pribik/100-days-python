#!/usr/bin/env python3

Mathematical Pperations:
() Parentheses
** Exponent
*  Multiply
/  Devision to floating type 
// Devision to int 
+  Addition 
-  Subtraction 
%  Modulo (remander)

+= iadd (add  to variable)
-= 
*= 
/= 

>  Greater Than
<  Less Than
>= Greater than or equal to
<= Less than or equal to
== Equal to
!= Not equal to

Operators:
A and B
C or D
not E

#f-strings
print(f" {var} ")


Git help

Setting up SSH:

Creating SSH Key (in ~/.ssh):
ssh-keygen -t ed25519 -C eric.pribik@gmail.com

Adding SSH key:
ssh-add ~/.ssh/github_sshkey

cat pub and add to GitHubL
cat ~/.ssh/github_sshkey.pub


Cloning Remote Repository:
use git clone to download repostory onto local computer:
git clone git@github.com:ahungrypear/100-days-python.git

List changes since last time you commited code (Green means go):
git status

run agaiast files to see what changed:
git diff FILENAME

Add a change to the commit:
git add FILENAME

To prepare commit changes:
-m for message
git commit -m "Your message here"

To send commited changes to the repository (use main or master):
git push origin main
