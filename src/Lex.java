import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;



public class Lex {
	
	ArrayList<Token> tokenList;
	
	public void Lex(String file) throws FileNotFoundException {
		tokenList = new ArrayList<Token>();
		
		Scanner input = new Scanner(System.in);
		System.out.println("Input token to be scanned by lex...");
		System.out.println("Your tokens is: " + lookup(input.next()));
	}
	
	
	private void processLine(String line, int lineNo) {
		Scanner scan = new Scanner(line);
		int i = 0;
		while(scan.hasNext()) {
			String tok = scan.next();
			tokenList.add(new Token(lookup(tok), tok, lineNo, i));
			i++;
		}
	}
	
	private static Tokens lookup(String lexeme) {
		//Inputs a lexeme string and outputs the specific token
		
		if(Character.isLetter(lexeme.charAt(0)))
			return Tokens.id;
		else if(Character.isDigit(lexeme.charAt(0)))
			return Tokens.literal_integer;
		else if(lexeme.charAt(0) == '=') {
			if (lexeme.length() == 1)
				return Tokens.assignment_operator;
			else
				return Tokens.eq_operator;
		}
		else if(lexeme.charAt(0) == '<') {
			if(lexeme.equals("<="))
				return Tokens.le_operator;
			else
				return Tokens.lt_operator;
		}
		else if(lexeme.charAt(0) == '>') {
			if(lexeme.equals(">="))
				return Tokens.ge_operator;
			else
				return Tokens.gt_operator;
		}
		else if(lexeme.equals("~="))
			return Tokens.ne_operator;
		else if(lexeme.equals("+"))
			return Tokens.add_operator;
		else if(lexeme.equals("-"))
			return Tokens.sub_operator;
		else if(lexeme.equals("*"))
			return Tokens.mul_operator;
		else if(lexeme.equals("/"))
			return Tokens.div_operator;
		else
			return Tokens.unknown;
	}

}
