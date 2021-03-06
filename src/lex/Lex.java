package lex;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;



public class Lex {
	
	ArrayList<Token> tokenList;
	String fileName;
	Token[][] tokenArray;
	
	public Lex(String fileText) throws FileNotFoundException {
		fileName = fileText;
		tokenList = new ArrayList<Token>();
		Scanner input = new Scanner(new File(fileText));
		
		for(int i = 0; input.hasNextLine(); i++) { 
			processLine(input.nextLine(), i); // processline 
		}

		tokenArray = new Token[tokenList.get(tokenList.size() - 1).getRow() + 1][];
		int row = -1;
		for(int i = tokenList.size() - 1; i >= 0; i--) {
			Token t = tokenList.get(i);
			if(row != t.getRow()) {
				row = t.getRow();
				tokenArray[t.getRow()] = new Token[t.getCol() + 1];
			}
			tokenArray[t.getRow()][t.getCol()] = t;
		}
	}
	// print the arraylist of tokens 
	public String toString() {
		StringBuilder result = new StringBuilder();
		result.append("File: " + fileName + "\n");
		
		int j = 0;
		for(int i = 0; i < tokenList.size(); i++) {
			Token t = tokenList.get(i);
			if(t.getRow() != j) {
				j = t.getRow();
				result.append("\n"); // creates a space as it find one in the file 
			}
			result.append(t.getLexeme()+ " "); // gets the lexeme 
			if (t.getType() == Tokens.unknown)
			{
				result.append("token causes error on line " + (t.getRow()+1)); 
				break; 
				
			}
			else 
			result.append(t.getType() + ", "); // gets the type of lexeme 
			
				
		}
		
		return result.toString();
	}
	
	private void processLine(String line, int lineNo) {
		Scanner scan = new Scanner(line); // read in line 
		int i = 0; 
			while(scan.hasNext()) {
			String tok = scan.next(); // read it into tok 
			tokenList.add(new Token(lookup(tok), tok, lineNo, i)); // take tok , run it through the look up function and add it to the list 
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
			else {
				return Tokens.unknown;
                         			
			}
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

	public String[] getLineTokens( int lineNo) {
		Token[] resultTokens = tokenArray[lineNo];
		String[] result = new String[resultTokens.length];
		for(int i=0; i<resultTokens.length; i++) {
			Token t = resultTokens[i];
			result[t.getCol()] = t.getType().name();
		}
		return result;
	}

	public String[] getLineLexeme( int lineNo) {
		Token[] resultTokens = tokenArray[lineNo];
		String[] result = new String[resultTokens.length];
		for(int i=0; i<resultTokens.length; i++) {
			Token t = resultTokens[i];
			result[t.getCol()] = t.getLexeme();
		}
		return result;
	}

	public String[] getTokensAndLexemes() {
	    String[] result = new String[tokenList.size() * 4];
	    for(int i=0; i<tokenList.size(); i++) {
			Token t = tokenList.get(i);
			result[i * 4] = t.getType().name();
			result[i * 4 + 1] = t.getLexeme();
			result[i * 4 + 2] = Integer.toString(t.getRow());
			result[i * 4 + 3] = Integer.toString(t.getCol());
		}
		return result;
	}
}