import java.net.Socket;
import java.io.IOException;
import java.io.PrintWriter;
import java.io.BufferedReader;
import java.io.InputStreamReader;


public class TestSocket {

    public static void main(String[] args) {

        try {

            Socket socket = new Socket("localhost", 8888);
            System.out.println("Connected");
            PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
            BufferedReader in = new BufferedReader( new InputStreamReader(socket.getInputStream()));
            out.println("Sockets Created!");
            in.readLine();
            System.out.println("recieved: " + in.readLine());
            socket.close();
            System.out.println("Socket closed");
        } catch(IOException exception) {
            exception.printStackTrace();
        }
    }
}