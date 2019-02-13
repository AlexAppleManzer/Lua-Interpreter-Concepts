package lex;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;



public class Lex {
	
	ArrayList<Token> tokenList;
	
	public Lex(String fileText) throws FileNotFoundException {
		tokenList = new ArrayList<Token>();
		Scanner input = new Scanner(new File(fileText));
		
		for(int i = 0; input.hasNextLine(); i++) {
			processLine(input.nextLine(), i);
		}
	}
	
	public String toString() {
		StringBuilder result = new StringBuilder();
		for(int i = 0; i < tokenList.size(); i++) {
			result.append(tokenList.get(i).getType() + " ");
		}
		return result.toString();
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
			if (lexeme.length() == 1) 
				return Tokens.id;
			else if(lexeme.equalsIgnoreCase("function"))
				return Tokens.function_keyword;
			else if(lexeme.equalsIgnoreCase("print"))
				return Tokens.print_keyword;
			else if(lexeme.equalsIgnoreCase("end"))
				return Tokens.end_keyword;
			else if(lexeme.equalsIgnoreCase("while"))
				return Tokens.while_keyword;
			else if(lexeme.equalsIgnoreCase("do"))
				return Tokens.do_keyword;
			else if(lexeme.equalsIgnoreCase("repeat"))
				return Tokens.repeat_keyword;
			else if(lexeme.equalsIgnoreCase("until"))
				return Tokens.until_keyword;
			else if(lexeme.equalsIgnoreCase("if"))
				return Tokens.if_keyword;
			else if(lexeme.equalsIgnoreCase("then"))
				return Tokens.then_keyword;
			else if(lexeme.equalsIgnoreCase("else"))
				return Tokens.else_keyword;
			else
				return Tokens.unknown;
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
		else if(lexeme.equals("("))
			return Tokens.left_paren;
		else if(lexeme.equals(")"))
			return Tokens.right_paren;
		else
			return Tokens.unknown;
	}

}
