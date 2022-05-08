import java.math.*;
import java.util.Scanner;
class RSA
{
public static void main(String args[])
{
Scanner sc=new Scanner(System.in);
int p,q,n,z,d=0,e,i;
System.out.println(&quot;Enter the number to be encrypted and
decrypted&quot;);
int msg=sc.nextInt();
double c;
BigInteger msgback;
System.out.println(&quot;Enter 1st prime number p&quot;);
p=sc.nextInt();
System.out.println(&quot;Enter 2nd prime number q&quot;);
q=sc.nextInt();
n=p*q;
z=(p-1)*(q-1);
System.out.println(&quot;the value of z = &quot;+z);
for(e=2;e&lt;z;e++)
{
if(gcd(e,z)==1) // e is for public key exponent
{
break;
}
}
System.out.println(&quot;the value of e = &quot;+e);
for(i=0;i&lt;=9;i++)
{
int x=1+(i*z);
if(x%e==0) //d is for private key exponent
{
d=x/e;
break;
}
}
System.out.println(&quot;the value of d = &quot;+d);
c=(Math.pow(msg,e))%n;
System.out.println(&quot;Encrypted message is : -&quot;);
System.out.println(c);
//converting int value of n to BigInteger
BigInteger N = BigInteger.valueOf(n);
//converting float value of c to BigInteger
BigInteger C = BigDecimal.valueOf(c).toBigInteger();
msgback = (C.pow(d)).mod(N);
System.out.println(&quot;Derypted message is : -&quot;);
System.out.println(msgback);
}
static int gcd(int e, int z)
{
if(e==0)
return z;
else
return gcd(z%e,e);

}
}