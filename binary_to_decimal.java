import java.util.Scanner;
class binary_to_decimal
{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter binary number(don't give spaces");
        String bin=sc.next();
        int len=bin.length();
        int dec=0;
        for(int i=0;i<len;i++)
        {
            if(Character.toString(bin.charAt(i))=="1")
            {
                dec+=Math.pow(2,i);
            }
        }
        System.out.println(bin+" in decimal = "+dec);
    }
}