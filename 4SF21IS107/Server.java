import java.io.*;
import java.net.*;
import javax.crypto.SecretKey;

public class Server{
    public static void main(String[] args) {
        try {
            ServerSocket serverSocket = new ServerSocket(8080);
            System.out.println("Server is running");

            while (true) {
                Socket socket = serverSocket.accept();
                System.out.println("Client connected");

                BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                String encryptedMessage = in.readLine();
                System.out.println("Received encrypted message: " + encryptedMessage);

                SecretKey key = Aes.getAESKey();
                String decryptedMessage = Aes.decrypt(encryptedMessage, key);  
                System.out.println("Decrypted message: " + decryptedMessage);

                PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
                out.println("Message processed");

                in.close();
                out.close();
                socket.close();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

