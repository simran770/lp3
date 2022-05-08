import java.util.*;
public class Diffie_Hellman
{
public static void main(String args[])
{
Scanner sc=new Scanner(System.in);
System.out.println(&quot;Enter Prime Number P&quot;);
int p=sc.nextInt();
System.out.println(&quot;Enter primitive root of &quot;+p);
int g=sc.nextInt();
System.out.println(&quot;Choose Private Key (Alice)&quot;);
int a=sc.nextInt();
System.out.println(&quot;Choose Private Key (BOB)&quot;);
int b=sc.nextInt();
int A = (int)Math.pow(g,a)%p;
int B = (int)Math.pow(g,b)%p;
System.out.println(&quot;Public Key (Alice) : &quot;+A);
System.out.println(&quot;Public Key (BOB) : &quot;+B);
int S_A = (int)Math.pow(B,a)%p;
int S_B =(int)Math.pow(A,b)%p;
if(S_A==S_B)
{
System.out.println(&quot;ALice and Bob can communicate with each

other!!!&quot;);

System.out.println(&quot;They share a secret no = &quot;+S_A);
}
else
{
System.out.println(&quot;ALice and Bob cannot communicate with

each other!!!&quot;);
}
}
}