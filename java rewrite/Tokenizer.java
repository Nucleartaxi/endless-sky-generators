import java.util.*;
import java.io.FileNotFoundException;
import java.io.File;
public class Tokenizer {
    public static void main(String args[]) throws FileNotFoundException{
        file("test.txt");
    }
    public static void file(String filename) throws FileNotFoundException {
        try {
            Scanner f = new Scanner(new File(filename));
            while (f.hasNextLine()) {
                tokenizeLine(f.nextLine());
                //System.out.println();
            }
        } catch (Exception fileNotFoundException) {
            System.out.println("Error: file not found");
        }
    }
    public static void tokenizeLine(String line) { //Tokenizes a String (usually representing a line) according to the endless sky data format https://github.com/endless-sky/endless-sky/wiki/DataFormat
        /*
        For example, the string: 
            test1 "second test" `backticks "test"`
        Becomes the tokens: 
            test1, second test, backticks "test"
        */
        boolean inTicks = false;
        boolean inQuotes = false;
        String s = "";
        for (int i = 0; i < line.length(); i++) { //tokenizes strings by spaces, ignores spaces inside quotes.
            char ch = line.charAt(i);
            if (ch == '#') {//if a comment is encountered, break the loop to stop tokenizing this line. 
                break;
            }
            if (ch == '`' && !inTicks) { //leading backtick, start adding characters to string, including spaces and quotes
                inTicks = true;
                continue;
            }
            if (ch == '`' && inTicks) { //ending backtick, stop adding characters to string
                System.out.println(s.trim());
                s = "";
                inTicks = false;
                continue;
            }
            if (ch == '"' && !inQuotes && !inTicks) { //leading quote, start adding characters to string, including spaces
                inQuotes = true;
                continue;
            } 
            if (ch == '"' && inQuotes && !inTicks) { //ending quote, stop adding characters to string
                System.out.println(s.trim());
                s = "";
                inQuotes = false;
                continue;
            }
            if (ch == ' ' && !inQuotes && !inTicks) { //if outside quotes, stop adding characters to string. Separate on spaces. Space not included in string.
                System.out.println(s.trim());
                s = "";
                continue;
            }
            s = s + ch; //if outside quotes, start adding characters to string. Separate on spaces. Space not included in string.
        }
        System.out.println(s); //last token on line (because there isn't a space at the end of the line to split on)
    }
}