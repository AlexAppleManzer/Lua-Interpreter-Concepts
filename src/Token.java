
public class Token {
	private Tokens type;
	private String lexeme;
	private int row;
	private int col;
	
	public Token(Tokens type, String lexeme, int row, int col) {
		this.type = type;
		this.lexeme = lexeme;
		this.row = row;
		this.col = col;
	}

	public Tokens getType(){
		return type;
	}
	
	public String getLexeme(){
		return lexeme;
	}
	
	public int getRow(){
		return row;
	}
	
	public int getCol(){
		return col;
	}
}
