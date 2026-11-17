Block A
---

Create a C++ program defining a simple function `evaluate_polynomial` that evaluates a polynomial, given its coefficients and its degree. Then in `main` create a static array with the coefficients `{1, 2, 3}` of a polynomial of degree 2 and use the created function to evaluate it at `2`. Print the result. Document the code with short comments.

Replace the separate coefficient pointer and degree variables with a `struct` called `Polynomial`. The `struct` should store a pointer to the coefficients and the degree. Keep `evaluate_polynomial` as a standalone function for now, but pass it a `Polynomial` object. Make sure that a `Polynomial` object can be created by a constructor that takes the coefficients array and the degree as arguments.

Move `evaluate_polynomial` into the `Polynomial` `struct` as a member function called `evaluate`. Keep the `coefficients` and `degree` public for now. The `main` function should call `polynomial.evaluate(2.0)`.

Make `coefficients` and `degree` `private` attributes of `Polynomial`, so that only the class itself can access them. Keep the constructor and `evaluate` `public`. Since most of our type is now hidden, use the keyword `class` instead of `struct`

Change the constructor of `Polynomial` so that the object stores its own copy of the coefficients in a dynamically allocated array, instead of pointing to the array of the caller. Add a destructor that releases this array. Show in `main` that changing the original array no longer changes the polynomial, and that the destructor is called automatically when the object goes out of scope.

Add an initializer list constructor so that I can write `Polynomial p = {3.0, 2.0, -5.0}`. The list entries are the coefficients in increasing powers of `x`, and the degree should follow from the number of entries. The constructor should copy the coefficients into the object owned dynamic array. Keep the existing constructor, and show in `main` that both can be used.

I want to be able to create a `Polynomial` object that is a copy of an already existing one. I also want to be able to change a `Polynomial` object by assigning another one to it, making them equal copies.

Add a function that allows me to create a `Polynomial` object that is a monomial by passing its degree and coefficient. Also add one that creates a `Polynomial` object that is just a constant value. I want to use these functions so that I can quickly create `Polynomial` objects that are monomials or constants. To build them, add a private constructor that creates a polynomial of a given degree with all coefficients equal to zero.

Extend the `Polynomial` class with `operator()` for evaluation, `operator+=` for in-place addition, `operator+` for polynomial addition, and `operator*` for polynomial multiplication. Use `const` correctness: operations that do not modify the current object should be marked `const`, and input polynomials should be passed by `const` reference.

Block B
---

Replace the dynamically allocated coefficient array of `Polynomial` with a `std::vector<double>`, and remove everything that is no longer needed now that the vector manages the memory. A vector knows its own size, so do not store the degree separately: compute it in a member function `degree()`. In `main`, show that copying a polynomial still gives an independent copy.

Add a member function `print` that shows the coefficients and the degree of a polynomial. Make sure that the degree is always correct, also when terms cancel and the result is the zero polynomial, and that multiplying by the zero polynomial gives the zero polynomial.

Add a member function `derivative` that returns the derivative as a new polynomial, building its coefficients one at a time with `push_back`. Add a way to check whether two polynomials are equal, and a member function `coefficient` that returns one coefficient and reports an error for an index that does not exist. In `main`, check the derivative of $1 + 2x^3$ against $6x^2$ and ask for a coefficient that does not exist.

Write a free function `derivative_errors` that compares `derivative()` with the central difference at five fixed points and returns the five absolute errors. Use `std::array` for the points and for the result. In `main`, test it on $1 + 2x^3$ at $x = -2, -1, 0, 1, 2$ with $h = 0.001$.
