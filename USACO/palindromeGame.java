import java.util.*;
import java.io.*;

public class palindromgame {
    public static void main(String[] args) throws IOException{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

        int I = Integer.parseInt(in.readLine());
        for(int i = 0; i < I; i++) {
            int testCase = Integer.parseInt(in.readLine());
            if(testCase % 10 == 0) {
                System.out.print("E");
            } else {
                System.out.print("B");
            }
        }
    }
}