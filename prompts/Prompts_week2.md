Create a C++ program with a function evaluating a polynomial based on it's coefficients with signature `double evaluate_polynomal(const double coeffs[], int size, double x)`. Then create an array containing coefficients `1,2,3` and evaluate it at 2

Change the coefficient array into a struct called `Polynomial` containing the coefficient array pointer and degree. Ensure a constructor with signature `Polynomial(double const *coeffs, int deg)` exists. Modify the evaluation function accept the Polynomial object

Change the evaluate function into a member function of `Polynomial` called `evaluate`

Change `Polynomial` to a class, let degree and coefficients be private. Change the constructor to `Polynomial(int degree)` creating the array, and a `set_coefficient(int degree, double value)` function.

Add a safe default constructor and destructor, show by printing how the destructor is called when an object leaves scope

Add an initializer-list constructor, and use it to create a new Polynomial with coefficients `3,2,5` and evaluate at 3

Make a copy constructor and copy assignment overload, and use each to create two new `Polynomial` objects. Ensure they are deep copies

Add a static member function for creating a monomial with degree and coefficient, also a function for creating a constant value polynomial. Create one of each. Remove `set_coefficient`, it is not needed anymore

Overload `()` to replace the `evaluate` function. Overload `+` and `+=` to allow polynomial addition, and `*` for polynomial multiplication, ensure operators are marked correctly with `const` and use `const &` when appropriate.
