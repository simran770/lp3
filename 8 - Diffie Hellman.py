"""

Implement the Diffie-Hellman key exchange Algorithm to generate the Shared
Secrete Key.
Assume following details.
Prime Number q=11,
Primitive root alpha=2,
Sender side private key XA =8,
Receiver side select private key XB =4.

"""

import math


P = 11  # Prime Number
G = 2  # Primitive Root
Xa = 8  # Sender side private key
Xb = 4  # Receiver side private key


print(f'Prime Number(P): {P}')
print(f'Primitive Root(G): {G}')
print(f'Sender side private key(Xa): {Xa}')
print(f'Receiver side private key(Xb): {Xb}')

# Generated Secret keys for Sender & Receiver
A = pow(G, Xa) % P
B = pow(G, Xb) % P

print()

print(f'Generated key for Sender(Ka): {A}')
print(f'Generated key for Receiver(Kb): {B}')


# Generated Private keys for Sender & Receiver
Ka = pow(B, Xa) % P
Kb = pow(A, Xb) % P

print()

# print(f'Generated Public key for Sender(Ka): {Ka}')
# print(f'Generated Public key for Receiver(Kb): {Kb}')

if(Ka == Kb):
    print(f"Symmetric Secret Key for Encryption: {Ka}")
