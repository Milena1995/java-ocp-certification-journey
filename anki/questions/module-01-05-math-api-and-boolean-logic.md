## Question

What is the output of the following code?<br><br>

```java
public class Test {
    public static void main(String[] args) {
        double result = Math.sqrt(4 / 9);
        System.out.println(result);
    }
}
```
<br><br>

Please select 1 option<br><br>

A) 0.666...<br>
B) 0.0<br>
C) 2/3<br>
D) Compilation error

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>INTEGER DIVISION TRAP:</strong> The division happens BEFORE Math.sqrt() is called.<br><br>

Analysis step-by-step:<br><br>

<strong>Step 1: Evaluate 4 / 9</strong><br>
• Both <strong>4</strong> and <strong>9</strong> are <strong>int</strong> literals<br>
• <strong>int / int</strong> → <strong>int</strong> (integer division)<br>
• 4 ÷ 9 = 0 (truncated, not rounded)<br><br>

<strong>Step 2: Call Math.sqrt(0)</strong><br>
• Math.sqrt(0) = <strong>0.0</strong><br><br>

<strong>Step 3: Result</strong><br>
• result = <strong>0.0</strong><br><br>

Output: <strong>0.0</strong><br><br>

<strong>Why this is a trap:</strong><br>
• You might expect: √(4/9) = √(0.444...) ≈ 0.666...<br>
• But integer division happens first: 4 / 9 = 0<br>
• Then: √0 = 0.0<br><br>

<strong>Correct code to get expected result:</strong><br>

```java
// Option 1: Use double literals
double result = Math.sqrt(4.0 / 9.0);  // 0.666...

// Option 2: Cast to double
double result = Math.sqrt((double)4 / 9);  // 0.666...

// Option 3: Use one double literal (promotes the other)
double result = Math.sqrt(4.0 / 9);  // 0.666...
```
<br>
<strong>Key principle:</strong><br>
• Type of division is determined <strong>BEFORE</strong> the method call<br>
• int / int → int (even if assigned to double later)<br>
• Method receives the result of the division<br><br>

<strong>More examples:</strong><br>

```java
Math.pow(1 / 2, 2)     // Math.pow(0, 2) = 0.0 (not 0.25)
Math.sqrt(1 / 4)       // Math.sqrt(0) = 0.0 (not 0.5)
Math.abs(5 / 10)       // Math.abs(0) = 0 (not 0.5)
```
<br>
<strong>Common exam trap:</strong> Expecting decimal result when integers are involved.<br><br>

<strong>A) is incorrect:</strong> Would require at least one operand to be double.<br>
<strong>C) is incorrect:</strong> Java doesn't have fraction types; this would be a syntax error.<br>
<strong>D) is incorrect:</strong> Code compiles successfully.

## Question

What is the result?<br><br>

```java
public class Test {
    public static void main(String[] args) {
        System.out.println(Math.floor(-2.7));
        System.out.println(Math.ceil(-2.7));
        System.out.println(Math.round(-2.7));
    }
}
```
<br><br>

Please select 1 option<br><br>

A) -2.0<br>
-3.0<br>
-3<br><br>

B) -3.0<br>
-2.0<br>
-3<br><br>

C) -2.0<br>
-2.0<br>
-3<br><br>

D) -3.0<br>
-3.0<br>
-3

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>NEGATIVE NUMBER ROUNDING TRAP:</strong> floor/ceil follow the number line, not "remove decimals" logic.<br><br>

Analysis:<br><br>

<strong>Math.floor(-2.7):</strong><br>
• floor = always rounds <strong>DOWN</strong> (toward negative infinity)<br>
• On number line: -3 is DOWN from -2.7<br>
• Result: <strong>-3.0</strong><br>
• Return type: <strong>double</strong><br><br>

<strong>Math.ceil(-2.7):</strong><br>
• ceil = always rounds <strong>UP</strong> (toward positive infinity)<br>
• On number line: -2 is UP from -2.7<br>
• Result: <strong>-2.0</strong><br>
• Return type: <strong>double</strong><br><br>

<strong>Math.round(-2.7):</strong><br>
• round = rounds to <strong>nearest integer</strong><br>
• -2.7 is closer to -3 than -2<br>
• Result: <strong>-3</strong><br>
• Return type: <strong>long</strong> (not double!)<br><br>

Output:<br>
<strong>-3.0</strong><br>
<strong>-2.0</strong><br>
<strong>-3</strong><br><br>

<strong>Number line visualization:</strong><br>

```
    -4        -3        -2        -1         0
     |         |         |         |         |
              ↑         ↑
           floor     ceil
              ↖  -2.7  ↗
```
<br>
<strong>Common misconception:</strong><br>
❌ "floor removes decimals" → floor(-2.7) = -2<br>
✅ "floor rounds DOWN" → floor(-2.7) = -3<br><br>

<strong>More examples:</strong><br>

```java
Math.floor(2.7)   // 2.0  (down on number line)
Math.floor(-2.7)  // -3.0 (down on number line)

Math.ceil(2.7)    // 3.0  (up on number line)
Math.ceil(-2.7)   // -2.0 (up on number line)

Math.round(2.5)   // 3    (nearest, rounds up on .5)
Math.round(-2.5)  // -2   (nearest, rounds up on .5)
```
<br>
<strong>Return types (important!):</strong><br>
• <strong>Math.floor()</strong> → double<br>
• <strong>Math.ceil()</strong> → double<br>
• <strong>Math.round()</strong> → long<br><br>

<strong>Edge case - exactly on integer:</strong><br>

```java
Math.floor(-3.0)  // -3.0
Math.ceil(-3.0)   // -3.0
Math.round(-3.0)  // -3
```
<br>
<strong>A), C), D) are incorrect:</strong> Wrong understanding of how floor/ceil work with negative numbers.

## Question

What is the output?<br><br>

```java
public class Test {
    public static void main(String[] args) {
        int result = Math.pow(2, 3);
        System.out.println(result);
    }
}
```
<br><br>

Please select 1 option<br><br>

A) 8<br>
B) 8.0<br>
C) Compilation error<br>
D) Runtime exception

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

<strong>TYPE MISMATCH:</strong> Math.pow() returns double, which cannot be assigned to int without cast.<br><br>

Analysis:<br><br>

<strong>Math.pow() signature:</strong><br>

```java
public static double pow(double a, double b)
```
<br>
• Takes two <strong>double</strong> parameters<br>
• Returns <strong>double</strong><br><br>

<strong>The problem:</strong><br>

```java
int result = Math.pow(2, 3);
```
<br>
• Math.pow(2, 3) returns <strong>8.0</strong> (double)<br>
• Trying to assign <strong>double</strong> to <strong>int</strong><br>
• This is a <strong>narrowing conversion</strong><br>
• Requires <strong>explicit cast</strong><br>
• ❌ <strong>Compilation error:</strong> "incompatible types: possible lossy conversion from double to int"<br><br>

<strong>Correct solutions:</strong><br><br>

<strong>Option 1: Use double variable</strong><br>

```java
double result = Math.pow(2, 3);  // 8.0
```
<br>
<strong>Option 2: Explicit cast</strong><br>

```java
int result = (int) Math.pow(2, 3);  // 8
```
<br>
<strong>Option 3: Use Math.round() for safety</strong><br>

```java
int result = (int) Math.round(Math.pow(2, 3));  // 8
```
<br>
<strong>Why Math.pow() returns double:</strong><br>
• Powers can produce fractional results<br>
• Example: Math.pow(2, 0.5) = √2 ≈ 1.414...<br>
• Example: Math.pow(2, -1) = 1/2 = 0.5<br>
• double type can represent all possible results<br><br>

<strong>Other Math methods returning double:</strong><br>

```java
Math.sqrt(x)     // double
Math.pow(a, b)   // double
Math.ceil(x)     // double
Math.floor(x)    // double
Math.random()    // double
```
<br>
<strong>Methods returning same type as input:</strong><br>

```java
Math.abs(int x)      // int
Math.max(int a, b)   // int
Math.min(int a, b)   // int
```
<br>
<strong>Method returning long:</strong><br>

```java
Math.round(double x)  // long (not int!)
```
<br>
<strong>Common exam trap:</strong> Forgetting that Math.pow() returns double.<br><br>

<strong>A) is incorrect:</strong> Cannot compile due to type mismatch.<br>
<strong>B) is incorrect:</strong> Would print 8.0 if assigned to double, but code doesn't compile.<br>
<strong>D) is incorrect:</strong> Code fails at compile-time, never runs.

## Question

Which statements about the Math class are correct?<br><br>

Please select all that apply<br><br>

A) All Math methods are static<br>
B) You can create instances of Math using new Math()<br>
C) Math.PI and Math.E are constants<br>
D) Math methods depend on object state

## Réponse

<strong>Réponse correcte :</strong> A), C)<br><br>

<strong>Math is a UTILITY class</strong> with only static members.<br><br>

<strong>Characteristics of Math class:</strong><br><br>

<strong>All methods are static:</strong><br>
• Called using <strong>Math.methodName()</strong><br>
• No object required<br>
• Belong to the class, not instances<br><br>

Example:<br>

```java
Math.max(5, 10)     // ✅ Correct - static method call
Math.abs(-5)        // ✅ Correct
Math.sqrt(16)       // ✅ Correct
```
<br>
<strong>Cannot instantiate Math:</strong><br>

```java
Math m = new Math();  // ❌ Compilation error
```
<br>
Why?<br>
• Math constructor is <strong>private</strong><br>
• Prevents instantiation<br>
• No need for objects - all operations are stateless<br><br>

<strong>Math constants:</strong><br>

```java
Math.PI    // π ≈ 3.141592653589793
Math.E     // e ≈ 2.718281828459045
```
<br>
These are:<br>
• <strong>public</strong><br>
• <strong>static</strong><br>
• <strong>final</strong> (cannot be modified)<br>
• type <strong>double</strong><br><br>

Example usage:<br>

```java
double circumference = 2 * Math.PI * radius;
double area = Math.PI * radius * radius;
```
<br>
Attempting to modify:<br>

```java
Math.PI = 3.14;  // ❌ Compilation error - final variable
```
<br>
<strong>Why methods are static:</strong><br>
• Math operations are <strong>stateless</strong><br>
• Result depends <strong>only on parameters</strong><br>
• No need to store data in objects<br>
• More efficient and simpler to use<br><br>

<strong>Common Math methods:</strong><br>

```java
Math.abs(x)        // absolute value
Math.max(a, b)     // maximum
Math.min(a, b)     // minimum
Math.pow(a, b)     // a to the power of b
Math.sqrt(x)       // square root
Math.round(x)      // round to nearest
Math.ceil(x)       // round up
Math.floor(x)      // round down
Math.random()      // random [0.0, 1.0)
```
<br>
All called as: <strong>Math.method()</strong> - no object needed.<br><br>

<strong>Utility class pattern:</strong><br>
• Private constructor (prevents instantiation)<br>
• All methods static<br>
• Often all methods are final<br>
• Common examples: Math, Arrays, Collections<br><br>

<strong>B) is incorrect:</strong> Math constructor is private, cannot instantiate.<br>
<strong>D) is incorrect:</strong> Math methods are stateless - result depends only on parameters, not object state.

## Question

What is the range of values returned by Math.random()?<br><br>

Please select 1 option<br><br>

A) [0.0, 1.0] (0.0 to 1.0 inclusive)<br>
B) [0.0, 1.0) (0.0 inclusive, 1.0 exclusive)<br>
C) (0.0, 1.0) (both exclusive)<br>
D) [1.0, 100.0]

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>Math.random() range:</strong> [0.0, 1.0) - includes 0.0, excludes 1.0.<br><br>

<strong>Method signature:</strong><br>

```java
public static double random()
```
<br>
Returns: <strong>double</strong> in range <strong>[0.0, 1.0)</strong><br><br>

<strong>Range breakdown:</strong><br>
• <strong>Minimum:</strong> 0.0 (inclusive, CAN be returned)<br>
• <strong>Maximum:</strong> approaching 1.0 but NEVER 1.0<br>
• Example values: 0.0, 0.157, 0.5, 0.999999... but NEVER 1.0<br><br>

<strong>Common use cases:</strong><br><br>

<strong>Random integer from 0 to 9:</strong><br>

```java
int random = (int)(Math.random() * 10);
// Range: [0, 10) → 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
```
<br>
<strong>Random integer from 1 to 10:</strong><br>

```java
int random = (int)(Math.random() * 10) + 1;
// Range: [1, 11) → 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
```
<br>
<strong>Random integer from min to max (inclusive):</strong><br>

```java
int random = (int)(Math.random() * (max - min + 1)) + min;
```
<br>
<strong>Why 1.0 is excluded:</strong><br>

```java
// If random() could return 1.0:
int value = (int)(Math.random() * 10);
// If random() = 1.0 → value = (int)(1.0 * 10) = 10
// But we want range [0-9], not [0-10]!

// Since random() < 1.0:
// Maximum: (int)(0.9999... * 10) = (int)(9.9999...) = 9 ✅
```
<br>
<strong>Important notes:</strong><br>
• Returns <strong>double</strong>, not int<br>
• Pseudorandom (not cryptographically secure)<br>
• For better random: use <strong>java.util.Random</strong> or <strong>ThreadLocalRandom</strong><br><br>

<strong>Examples:</strong><br>

```java
Math.random()           // Example: 0.7234512...
Math.random() * 100     // Example: 72.34512...
(int)(Math.random() * 100)  // Example: 72 (range 0-99)
```
<br>
<strong>Common exam trap:</strong><br>
• Thinking 1.0 can be returned<br>
• Calculating range incorrectly<br>
• Forgetting to cast to int<br><br>

<strong>A) is incorrect:</strong> 1.0 is excluded, not included.<br>
<strong>C) is incorrect:</strong> 0.0 IS included (can be returned).<br>
<strong>D) is incorrect:</strong> Range is always [0.0, 1.0), not [1.0, 100.0].

## Question

What is the output?<br><br>

```java
public class Test {
    public static void main(String[] args) {
        int a = 10;
        int b = 0;
        boolean result = a > 5 && b / a > 0;
        System.out.println(result);
    }
}
```
<br><br>

Please select 1 option<br><br>

A) true<br>
B) false<br>
C) ArithmeticException<br>
D) Compilation error

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>SHORT-CIRCUIT EVALUATION with &&:</strong> Both operands are evaluated because the first is true.<br><br>

Analysis step-by-step:<br><br>

<strong>Expression: a > 5 && b / a > 0</strong><br>
where a = 10, b = 0<br><br>

<strong>Step 1: Evaluate a > 5</strong><br>
• 10 > 5 → <strong>true</strong><br><br>

<strong>Step 2: Short-circuit decision</strong><br>
• For <strong>&&</strong>, if left is <strong>true</strong> → must evaluate right to determine result<br>
• Right operand <strong>IS evaluated</strong><br><br>

<strong>Step 3: Evaluate b / a > 0</strong><br>
• b / a = 0 / 10 = <strong>0</strong><br>
• 0 > 0 → <strong>false</strong><br><br>

<strong>Step 4: Combine with AND</strong><br>
• true && false → <strong>false</strong><br><br>

Output: <strong>false</strong><br><br>

<strong>Why no exception:</strong><br>
• Division is <strong>0 / 10</strong>, not 10 / 0<br>
• Dividing <strong>zero BY something</strong> is valid (result is 0)<br>
• Dividing something <strong>BY zero</strong> would throw exception<br><br>

<strong>Important distinction:</strong><br>

```java
0 / 10  // ✅ OK, result = 0
10 / 0  // ❌ ArithmeticException
```
<br>
<strong>When exception WOULD occur:</strong><br>

```java
int a = 10;
int b = 0;
boolean result = a > 5 && a / b > 0;  // ❌ ArithmeticException
// Right side IS evaluated (left is true)
// a / b = 10 / 0 → exception
```
<br>
<strong>Short-circuit preventing exception:</strong><br>

```java
int a = 10;
int b = 0;
boolean result = a < 5 && a / b > 0;  // ✅ false, no exception
// Left is false → right NOT evaluated → no division by zero
```
<br>
<strong>AND (&&) short-circuit rules:</strong><br>
• If left is <strong>false</strong> → result is false, right NOT evaluated<br>
• If left is <strong>true</strong> → must evaluate right to determine result<br><br>

<strong>OR (||) short-circuit rules:</strong><br>
• If left is <strong>true</strong> → result is true, right NOT evaluated<br>
• If left is <strong>false</strong> → must evaluate right to determine result<br><br>

<strong>Common exam trap:</strong> Confusing division OF zero with division BY zero.<br><br>

<strong>A) is incorrect:</strong> true && false = false.<br>
<strong>C) is incorrect:</strong> 0 / 10 is valid, no exception.<br>
<strong>D) is incorrect:</strong> Code compiles successfully.

## Question

What is the output?<br><br>

```java
public class Test {
    public static void main(String[] args) {
        boolean result = true || false && false;
        System.out.println(result);
    }
}
```
<br><br>

Please select 1 option<br><br>

A) true<br>
B) false<br>
C) Compilation error<br>
D) Depends on execution order

## Réponse

<strong>Réponse correcte :</strong> A)<br><br>

<strong>BOOLEAN OPERATOR PRECEDENCE:</strong> && has higher precedence than ||.<br><br>

Precedence hierarchy:<br>
1. <strong>!</strong> (NOT) - highest<br>
2. <strong>&&</strong> (AND)<br>
3. <strong>||</strong> (OR) - lowest<br><br>

Evaluation step-by-step:<br><br>

<strong>Original expression:</strong><br>

```java
true || false && false
```
<br>
<strong>Step 1: Group by precedence</strong><br>
• <strong>&&</strong> has higher precedence than <strong>||</strong><br>
• Expression groups as:<br>

```java
true || (false && false)
```
<br>
<strong>Step 2: Evaluate false && false</strong><br>

```java
false && false → false
```
<br>
Expression becomes:<br>

```java
true || false
```
<br>
<strong>Step 3: Evaluate true || false</strong><br>

```java
true || false → true
```
<br>
Output: <strong>true</strong><br><br>

<strong>Note: Short-circuit also applies</strong><br>
• Left operand of <strong>||</strong> is <strong>true</strong><br>
• Right operand <strong>(false && false)</strong> is NOT evaluated<br>
• Result is <strong>true</strong> immediately<br><br>

<strong>More examples:</strong><br>

```java
false && true || true
// (false && true) || true
// false || true
// true

true || false && true
// true || (false && true)
// true (right side not evaluated due to short-circuit)

!false && true || false
// (!false && true) || false
// (true && true) || false
// true || false
// true
```
<br>
<strong>Using parentheses for different grouping:</strong><br>

```java
(true || false) && false
// true && false
// false
```
<br>
<strong>Complete operator precedence (relevant):</strong><br>
1. <strong>( )</strong> Parentheses<br>
2. <strong>! ++ --</strong> Unary operators<br>
3. <strong>* / %</strong><br>
4. <strong>+ -</strong><br>
5. <strong>< > <= >=</strong><br>
6. <strong>== !=</strong><br>
7. <strong>&&</strong> Logical AND<br>
8. <strong>||</strong> Logical OR<br>
9. <strong>=</strong> Assignment<br><br>

<strong>Best practice:</strong> Use parentheses for clarity:<br>

```java
boolean result = true || (false && false);  // Explicit
```
<br>
<strong>B) is incorrect:</strong> Would require different precedence or grouping.<br>
<strong>C) is incorrect:</strong> Expression is syntactically valid.<br>
<strong>D) is incorrect:</strong> Precedence rules are deterministic, not variable.

## Question

What is the result?<br><br>

```java
public class Test {
    public static void main(String[] args) {
        if (5 = 5) {
            System.out.println("Equal");
        }
    }
}
```
<br><br>

Please select 1 option<br><br>

A) Prints: Equal<br>
B) Prints nothing<br>
C) Compilation error<br>
D) Runtime exception

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

<strong>ASSIGNMENT vs COMPARISON:</strong> Using = (assignment) instead of == (comparison) in if condition.<br><br>

Analysis:<br><br>

<strong>The problem:</strong><br>

```java
if (5 = 5) { }
```
<br>
• <strong>5 = 5</strong> is an <strong>assignment</strong>, not a comparison<br>
• Trying to assign value 5 to literal 5<br>
• You cannot assign to a <strong>literal</strong><br>
• ❌ <strong>Compilation error:</strong> "unexpected type; required: variable, found: value"<br><br>

<strong>Even if it were a variable:</strong><br>

```java
int x;
if (x = 5) { }  // ❌ Still error!
```
<br>
• <strong>x = 5</strong> is an assignment (returns int)<br>
• if requires <strong>boolean</strong> expression<br>
• int cannot be used as boolean in Java<br>
• ❌ <strong>Compilation error:</strong> "incompatible types: int cannot be converted to boolean"<br><br>

<strong>Correct operators:</strong><br><br>

<strong>= (assignment):</strong><br>

```java
int x = 5;          // ✅ Assign 5 to x
x = 10;             // ✅ Reassign 10 to x
boolean b = true;   // ✅ Assign true to b
```
<br>
<strong>== (comparison):</strong><br>

```java
if (x == 5) { }          // ✅ Compare x with 5
boolean b = (5 == 5);    // ✅ Compare, result is true
while (count == 10) { }  // ✅ Compare count with 10
```
<br>
<strong>Important distinctions:</strong><br>

```java
x = 5;      // STATEMENT: assigns value, returns nothing useful
x == 5;     // EXPRESSION: compares, returns boolean

int y = (x = 5);    // ✅ OK: assignment returns value
if (x = 5) { }      // ❌ Error: assignment returns int, not boolean
```
<br>
<strong>In languages like C/C++:</strong><br>

```cpp
if (x = 5) { }  // Valid in C (assignment returns value)
                // Non-zero is truthy
```

But in Java: ❌ Type safety prevents this<br><br>

<strong>Common typo trap:</strong><br>

```java
if (x = 5)  { }  // ❌ Assignment (typo)
if (x == 5) { }  // ✅ Comparison (intended)
```
<br>
<strong>Special case - boolean assignment in if:</strong><br>

```java
boolean flag;
if (flag = true) { }  // ❌ Compiles but bad practice!
// Assignment returns boolean, so it's valid
// But confusing and likely a bug

if (flag == true) { }  // ✅ Better
if (flag) { }          // ✅ Best (for boolean)
```
<br>
<strong>A) is incorrect:</strong> Code doesn't compile.<br>
<strong>B) is incorrect:</strong> Code doesn't compile, so nothing prints.<br>
<strong>D) is incorrect:</strong> Error occurs at compile-time, not runtime.

## Question

What is the output?<br><br>

```java
public class Test {
    public static void main(String[] args) {
        System.out.println(Math.max(10, 20));
        System.out.println(Math.min(10.5, 20.5));
        System.out.println(Math.abs(-15));
    }
}
```
<br><br>

Please select 1 option<br><br>

A) 20<br>
10.5<br>
15<br><br>

B) 20<br>
20.5<br>
-15<br><br>

C) 10<br>
10.5<br>
15<br><br>

D) Compilation error

## Réponse

<strong>Réponse correcte :</strong> A)<br><br>

<strong>Math.max(), Math.min(), and Math.abs()</strong> - straightforward utility methods.<br><br>

Analysis:<br><br>

<strong>Math.max(10, 20):</strong><br>
• Returns the <strong>larger</strong> of two values<br>
• max(10, 20) = <strong>20</strong><br>
• Return type: <strong>same as input type</strong> (int)<br><br>

<strong>Math.min(10.5, 20.5):</strong><br>
• Returns the <strong>smaller</strong> of two values<br>
• min(10.5, 20.5) = <strong>10.5</strong><br>
• Return type: <strong>same as input type</strong> (double)<br><br>

<strong>Math.abs(-15):</strong><br>
• Returns the <strong>absolute value</strong> (distance from zero)<br>
• abs(-15) = <strong>15</strong><br>
• Return type: <strong>same as input type</strong> (int)<br><br>

Output:<br>
<strong>20</strong><br>
<strong>10.5</strong><br>
<strong>15</strong><br><br>

<strong>Method overloading:</strong><br>

These methods are <strong>overloaded</strong> for different types:<br>

```java
// Math.max() variants
Math.max(int a, int b)        → int
Math.max(long a, long b)      → long
Math.max(float a, float b)    → float
Math.max(double a, double b)  → double

// Math.min() variants (same pattern)
// Math.abs() variants (same pattern)
```
<br>
<strong>More examples:</strong><br>

```java
Math.max(5, 10)        // 10
Math.max(-5, -10)      // -5 (closer to positive)
Math.max(3.7, 3.9)     // 3.9

Math.min(5, 10)        // 5
Math.min(-5, -10)      // -10 (further from positive)
Math.min(3.7, 3.9)     // 3.7

Math.abs(10)           // 10
Math.abs(-10)          // 10
Math.abs(0)            // 0
Math.abs(-3.5)         // 3.5
```
<br>
<strong>Finding max/min of multiple values:</strong><br>

```java
// Chaining for more than 2 values
int max = Math.max(Math.max(5, 10), 15);  // 15

// For arrays, use streams or loops
int[] numbers = {5, 10, 15, 3};
int max = Arrays.stream(numbers).max().getAsInt();
```
<br>
<strong>Important notes:</strong><br>
• Return type matches input type<br>
• max/min with same values returns that value<br>
• abs of positive number returns same number<br>
• abs of zero returns zero<br><br>

<strong>Special cases:</strong><br>

```java
Math.max(Integer.MAX_VALUE, 10)  // Integer.MAX_VALUE
Math.min(Integer.MIN_VALUE, 10)  // Integer.MIN_VALUE
Math.abs(Integer.MIN_VALUE)      // Negative! (overflow)
```
<br>
<strong>B) is incorrect:</strong> min returns smaller value, not larger.<br>
<strong>C) is incorrect:</strong> max returns 20, not 10.<br>
<strong>D) is incorrect:</strong> Code compiles successfully.

## Question

What is the difference between && and & when used with boolean operands?<br><br>

Please select 1 option<br><br>

A) They are identical in behavior<br>
B) && uses short-circuit evaluation, & does not<br>
C) & is for bitwise operations only, cannot be used with booleans<br>
D) && is faster but less safe than &

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>SHORT-CIRCUIT (&&, ||) vs NON-SHORT-CIRCUIT (&, |)</strong> operators.<br><br>

<strong>Logical AND - two versions:</strong><br><br>

<strong>&& (Short-circuit AND):</strong><br>
• Evaluates left operand first<br>
• If left is <strong>false</strong> → stops, returns false<br>
• Right operand <strong>NOT evaluated</strong><br>
• If left is <strong>true</strong> → evaluates right<br><br>

<strong>& (Non-short-circuit AND):</strong><br>
• <strong>Always evaluates BOTH</strong> operands<br>
• Even if left is false<br>
• Then performs AND operation<br><br>

<strong>Examples:</strong><br><br>

<strong>Safe with &&:</strong><br>

```java
int x = 0;
if (x != 0 && 10 / x > 1) {  // ✅ Safe
    // x != 0 is false
    // Right side NOT evaluated → no division by zero
}
```
<br>
<strong>Unsafe with &:</strong><br>

```java
int x = 0;
if (x != 0 & 10 / x > 1) {  // ❌ ArithmeticException!
    // BOTH sides evaluated
    // 10 / x is evaluated even though x = 0
}
```
<br>
<strong>Side effects demonstration:</strong><br>

```java
int count = 0;

// With && (short-circuit)
boolean result1 = false && ++count > 0;
System.out.println(count);  // 0 (increment not executed)

count = 0;
// With & (non-short-circuit)
boolean result2 = false & ++count > 0;
System.out.println(count);  // 1 (increment WAS executed)
```
<br>
<strong>Logical OR - two versions:</strong><br><br>

<strong>|| (Short-circuit OR):</strong><br>

```java
true || expression  // expression NOT evaluated
```
<br>
<strong>| (Non-short-circuit OR):</strong><br>

```java
true | expression  // expression IS evaluated
```
<br>
<strong>Comparison table:</strong><br>

```
Operator  Short-circuit?  Both evaluated?  Use case
--------  --------------  ---------------  ---------
&&        Yes             No (if left false)  Normal logic
&         No              Always            Rare, intentional
||        Yes             No (if left true)   Normal logic
|         No              Always            Rare, intentional
```
<br>
<strong>When to use &:</strong><br>
• When you <strong>intentionally want</strong> both sides evaluated<br>
• When both sides have <strong>side effects</strong> you need<br>
• Very rare in practice<br><br>

Example:<br>

```java
// Want both methods called regardless
if (validate1() & validate2()) {
    // Both validations run, even if first fails
}

// Compare with:
if (validate1() && validate2()) {
    // If validate1() returns false, validate2() never called
}
```
<br>
<strong>Best practice:</strong><br>
• Use <strong>&&</strong> and <strong>||</strong> for boolean logic (almost always)<br>
• Only use <strong>&</strong> and <strong>|</strong> when you specifically need both sides evaluated<br><br>

<strong>A) is incorrect:</strong> They differ in short-circuit behavior.<br>
<strong>C) is incorrect:</strong> & can be used with booleans (performs AND without short-circuit).<br>
<strong>D) is incorrect:</strong> && is safer (prevents errors via short-circuit), not less safe.

## Question

What is the output?<br><br>

```java
public class Test {
    public static void main(String[] args) {
        double value = Math.round(2.5) + Math.round(3.5);
        System.out.println(value);
    }
}
```
<br><br>

Please select 1 option<br><br>

A) 6.0<br>
B) 6<br>
C) 7.0<br>
D) Compilation error

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

<strong>Math.round() RETURN TYPE:</strong> Returns long, which is then assigned to double.<br><br>

Analysis step-by-step:<br><br>

<strong>Math.round() signature:</strong><br>

```java
public static long round(double a)
```
<br>
Returns: <strong>long</strong> (not double, not int!)<br><br>

<strong>Step 1: Math.round(2.5)</strong><br>
• Rounds to nearest integer<br>
• 2.5 rounds <strong>up</strong> (ties round up in Java)<br>
• Result: <strong>3L</strong> (long)<br><br>

<strong>Step 2: Math.round(3.5)</strong><br>
• 3.5 rounds <strong>up</strong><br>
• Result: <strong>4L</strong> (long)<br><br>

<strong>Step 3: Add the results</strong><br>

```java
3L + 4L = 7L  // long
```
<br>
<strong>Step 4: Assign to double variable</strong><br>

```java
double value = 7L;  // Widening conversion: long → double
value = 7.0
```
<br>
Output: <strong>7.0</strong><br><br>

<strong>Math.round() rounding rules:</strong><br>
• Rounds to <strong>nearest integer</strong><br>
• <strong>Ties (0.5) round UP</strong> (toward positive infinity)<br>
• 2.5 → 3<br>
• 3.5 → 4<br>
• -2.5 → -2 (rounds up toward positive infinity)<br><br>

<strong>Return type variations:</strong><br>

```java
Math.round(double) → long  // Most common
Math.round(float) → int
```
<br>
<strong>Common type errors:</strong><br>

```java
int x = Math.round(2.5);  // ❌ Compilation error
// Math.round(double) returns long, not int

int x = (int) Math.round(2.5);  // ✅ Explicit cast needed
long x = Math.round(2.5);       // ✅ No cast needed
double d = Math.round(2.5);     // ✅ Widening: long → double
```
<br>
<strong>A) is incorrect:</strong> Incorrect calculation (2.5 + 3.5 = 6, but after rounding: 3 + 4 = 7).<br>
<strong>B) is incorrect:</strong> Result is double (7.0), not int (7).<br>
<strong>D) is incorrect:</strong> Code compiles successfully.
