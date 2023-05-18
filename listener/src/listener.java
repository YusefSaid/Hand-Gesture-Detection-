import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.nio.channels.NonReadableChannelException;

public class listener {
    public static void main(String args[]) throws IOException{
        String gesture = null;
        String new_gesture = null;
        int i = 0;
        while (true){

            if (i % 10 == 0){
                File file = new File(System.getProperty("user.dir")+"//gesture.txt");
                FileReader reader = new FileReader(file);
                BufferedReader br = new BufferedReader(reader);

                
                new_gesture = br.readLine();
                if (new_gesture == null){
                    
                }

                else if (!new_gesture.equals(gesture)){
                    gesture = new_gesture;
                    System.out.println(gesture);
                    
                };

                reader.close();
            };
            i++;
        }
        
    }
    
    
}
