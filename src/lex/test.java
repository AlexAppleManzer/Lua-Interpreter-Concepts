package lex;

import java.io.FileNotFoundException;
import java.io.File;

public class test {
	
	public static void main(String[] args) throws FileNotFoundException {
		
		Lex l = new Lex("test1.lua");
		System.out.println(l.toString()); //should print out every token in the test file
		l = new Lex("test2.lua");
		System.out.println(l.toString()); //should print out every token in the test file
		l = new Lex("test3.lua");
		System.out.println(l.toString()); //should print out every token in the test file
		l = new Lex("test4.lua");
		System.out.println(l.toString()); //should print out every token in the test file
    }
}
