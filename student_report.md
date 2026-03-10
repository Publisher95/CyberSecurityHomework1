## Objective
Identify the cryptographic misuse and recover the secret.

Secret47 was the secret. 


## Explanation
- What is broken?
    What is broken is the encryption, we were able to find the non-repeating and plug that into the oracle file to find the sercret keyword.


- Why is it insecure?
    It is insecure because the data is only hidden behind repeating data that can easily be ignored and deduced that the only important data is unique data.


## Solution
- Attack strategy
    Our Attack strategy was reading the bin, turning it into hex, and sorting the 16 byte strings accroding to if we had seen before or only once.

- Code overview
    A basic loop that will copy 16 bytes of hex into a array and then sort the array into other arrays.

## Mitigation
- How should this be fixed?
    I think that this is a good start because it is effectivly salting the data but the salt needs to not be the same piece of data. 


