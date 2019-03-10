import lex.*;
import java.io.FileNotFoundException;

public class TestLex {
	
	public static void main(String[] args) throws FileNotFoundException {
		Lex l = new Lex("test1.lua");
		System.out.println(l.toString()); //should print out every token in the test file
		System.out.println();
		l = new Lex("test2.lua");
		System.out.println(l.toString()); //should print out every token in the test file
		System.out.println();
		l = new Lex("test3.lua");
		System.out.println(l.toString()); //should print out every token in the test file
		System.out.println();
		l = new Lex("test4.lua");
		System.out.println(l.toString()); //should print out every token in the test file
		System.out.println();
    }
}
