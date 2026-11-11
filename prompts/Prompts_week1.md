Block A
---

Write a complete C++ program that prints a header line: `"Leibniz pi estimator -- v0.1"`. It should compile and run. 

Add a `double` estimate variable, for now initializing it to `4.0 * 1.0`, and print its value labeled `estimate`. For this program, disregard the first statement on uniform initialization and use copy initialization instead from now on.

Add two `int`s representing the first and second terms of the sequence, initialized to `1` and `1 / 3` respectively. Print the estimate twice, once as 4 times the first term, and then as 4 times the sum of both terms. Include number of terms used in the estimate printout.

The result is incorrect, adjust the code so the terms use double-precision floating point arithmetic

Add a constant double with the value 3.14159265358979 representing pi, to the program. After printing each estimate, print the (signed) difference between the estimate and the reference pi value

Replace the hard coded terms with a loop computing the sum $\sum_{k=0}^{N-1} \frac{(-1)^k}{2k+1}$ and let the estimate be 4 times this sum. Let `N` be a defined constant equal to 1000. Use modulus and the ternary operator instead of powers for the numerator

Before the loop, include a check that N is strictly positive. If not, throw an (uncaught) `std::invalid_argument` exception with an error message. To do this the `<stdexcept>` header needs to be included

Wrap all the code in a try block and include a catch statement catching (by reference) any `std::invalid_argument` and printing it to the screen before exiting main with return 1;

Block B
---

Extract the main computation and input validation into a function with the signature `double leibniz_estimate(int N)`

Move the difference check inside the function by changing the signature to accept a reference to an error variable, i.e. `double leibniz_estimate(int N, double &error)`
Also change it from a singed difference to an absolute error using `std::abs` from the `<cmath>` header.

Extract reporting the result to it's own function taking in as const references the N, estimate, and error

Put the two functions in a namespace called `leibniz`, and rename `leibniz_estimate` to `estimate`

Using the `<cassert>` header, assert that the estimate in the estimate function is a positive finite number, and that N is greater or equal to one in the report function

Block C
---

Create a C++ program that initializes an array called `data` of 5 doubles with values `2.1, 2.3, 1.9, 2.2, 2.0`, then loop over the array printing the value and index of each entry. 

Add a loop to compute the mean of the array, use 4 different constructors for the variables used. Copy-style for the sum, constructor style for the count, empty brace for the mean, and loop index for the sum loop by only initializing. Add comment to each describing which is which. Print the mean

Separate the mean calculation into it's own function using the signature `double mean(double *data, int n)`

Add similar function for computing the variance with signature `double variance(double* data, int n, double mean_value)`, calculate it and the standard deviation (square root of variance) to the main and print them

Add separate checks for pointers to `nullptr` and n values less than 1 and throw `std::invalid_argument` if encountered to both functions. Wrap the contents of main in a try-catch block catching and printing all exceptions

