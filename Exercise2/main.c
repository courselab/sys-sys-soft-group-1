/*
 *    SPDX-FileCopyrightText: 2021 Monaco F. J. <monaco@usp.br>
 *    SPDX-FileCopyrightText: 2024 AlvaroJoseLopes <alvarojoselopes@hotmail.com>
 *   
 *    SPDX-License-Identifier: GPL-3.0-or-later
 *
 *  This file is a derivative work from SYSeg (https://gitlab.com/monaco/syseg)
 *  and contains modifications carried out by the following author(s):
 *  AlvaroJoseLopes <alvarojoselopes@hotmail.com>
 */

#include "bios.h"
#include "utils.h"

#define PROMPT "$ "		/* Prompt sign.      */
#define SIZE 20			/* Read buffer size. */

char buffer[SIZE];		/* Read buffer.      */

void cat(void) {
  println(" /\\_/\\");
  println("( o.o )");
  println(" > ^ <");
}


int main()
{
  clear();
  
  println  ("Boot Command 1.0");

  while (1)
    {
      print(PROMPT);		/* Show prompt.               */
      readln(buffer);		/* Read use input.            */

      if (buffer[0])		/* Execute built-in command.  */
	{
	  if (!strcmp(buffer,"help"))
	    println("List of commands: [help, cat]");
    else if (!strcmp(buffer,"cat"))
      cat();
	  else 
	    println("Unkown command.");
	}
    }
  
  return 0;

}

