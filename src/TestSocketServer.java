import java.net.ServerSocket;
import java.net.Socket;
import java.io.IOException;
import java.io.PrintWriter;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class TestSocketServer {

    public static void main(String[] args) {
        try {
            String fromClient; String toClient;

            ServerSocket server = new ServerSocket(8888);
            System.out.println("Waiting for connection on port 8888...");

            boolean run = true;
            while(run) {
                Socket client = server.accept();
                System.out.println("Found connection on port 8888");
                PrintWriter out = new PrintWriter(client.getOutputStream(), true);
                BufferedReader in = new BufferedReader(new InputStreamReader(client.getInputStream()));

                fromClient = in.readLine();
                System.out.println("received: " + fromClient);
                if(fromClient.equals("Quit")){
                    run = false;
                    toClient = "goodbye :)";
                    out.println(toClient);
                }
                else {
                    toClient = "Sup!";
                    out.println(toClient);
                }

            }

            System.exit(0);
        } catch(IOException exception) {
            exception.printStackTrace();
        }
    }
}