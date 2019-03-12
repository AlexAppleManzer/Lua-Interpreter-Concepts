package lex;

import java.net.ServerSocket;
import java.net.Socket;
import java.io.IOException;
import java.io.PrintWriter;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class LexServer {
    public static void main(String[] args) {
        try {
            String fromClient; String toClient;

            Lex lex = new Lex("../test1.lua");
            ServerSocket server = new ServerSocket(8888);
            System.out.println("Server: Waiting for connection on port 8888...");

            boolean run = true;
            Socket client = server.accept();
            while(run) {
                System.out.println("Server: Found connection on port 8888");
                PrintWriter out = new PrintWriter(client.getOutputStream(), true);
                BufferedReader in = new BufferedReader(new InputStreamReader(client.getInputStream()));

                fromClient = in.readLine();
                System.out.println("Server: received: " + fromClient);
                if(fromClient == null){
                    return;
                }
                else if(fromClient.charAt(0) == 'Q'){
                    run = false;
                    toClient = "goodbye :)";
                    out.println(toClient);
                } else if(fromClient.charAt(0) == ('g')) {
                    String[] str = fromClient.split(" ");
                    if(Character.isDigit(str[1].charAt(0))) {
                        String[] output = lex.getLineTokens(Integer.valueOf(str[1]));
                        StringBuilder toClientSB = new StringBuilder();
                        for(int i=0; i<output.length; i++){
                            toClientSB.append(output[i] + " ");
                        }
                        toClient = toClientSB.toString();
                        out.println(toClient);
                    } else {
                        toClient = "Error: Number Expected";
                        out.println(toClient);
                    }

                } else if (fromClient.charAt(0) == ('c')) {
                    String[] str = fromClient.split(" ");
                    lex = new Lex("../" + str[1]);
                    toClient = "1";
                    out.println(toClient);
                } else {
                    toClient = "Sup!";
                    String[] str = fromClient.split(" ");

                    out.println(toClient);
                }

            }

            System.exit(0);
        } catch(IOException exception) {
            exception.printStackTrace();
        }
    }
}
