import java.io.*;

public class LexStream {
    public static void main(String[] args) {
        try {
            BufferedReader bufferRead = new BufferedReader(new InputStreamReader(System.in));
            PrintWriter writer = new PrintWriter("result.txt", "UTF-8");
            String s = bufferRead.readLine();
            while(!s.equals("x")) {
                writer.println(s);
                s = bufferRead.readLine();
            }
            writer.close();
        } catch(IOException e) {
            e.printStackTrace();
        }
    }
}