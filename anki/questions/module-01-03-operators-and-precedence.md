## Question

What is the output of the following code?<br><br>

```java
public class Test {
    public static void main(String[] args) {
        int result = 5 / 2;
        System.out.println(result);
    }
}
```
<br><br>

Please select 1 option<br><br>

A) 2.5<br>
B) 2<br>
C) 3<br>
D) Compilation error

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>INTEGER DIVISION TRAP:</strong> When both operands are integers, the result is truncated, not rounded.<br><br>

Analysis:<br>
• Both <strong>5</strong> and <strong>2</strong> are <strong>int</strong> literals<br>
• <strong>int / int</strong> → <strong>int</strong> (integer division)<br>
• Result is <strong>truncated</strong> (decimal part discarded)<br>
• 5 ÷ 2 = 2.5 → truncated to <strong>2</strong><br><br>

Output: <strong>2</strong><br><br>

<strong>Key rule:</strong> Integer division NEVER rounds - it always truncates toward zero.<br><br>

More examples:<br>

```java
7 / 2  = 3    // not 3.5
9 / 4  = 2    // not 2.25
-7 / 2 = -3   // not -3.5, truncates toward zero
```
<br>
<strong>To get decimal result:</strong><br>

```java
double result = 5.0 / 2;      // 2.5 (one operand is double)
double result = (double)5 / 2; // 2.5 (cast to double)
double result = 5 / 2.0;       // 2.5 (one operand is double)
```
<br>
<strong>Common exam trap:</strong> Expecting decimal result from integer division.<br><br>

<strong>A) is incorrect:</strong> Would require at least one operand to be double/float.<br>
<strong>C) is incorrect:</strong> Integer division truncates, doesn't round up.<br>
<strong>D) is incorrect:</strong> Code compiles successfully.

## Question

What happens when this code runs?<br><br>

```java
public class Test {
    public static void main(String[] args) {
        int x = 5 / 0;
        System.out.println(x);
    }
}
```
<br><br>

Please select 1 option<br><br>

A) Prints: 0<br>
B) Prints: Infinity<br>
C) ArithmeticException at runtime<br>
D) Compilation error

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

<strong>DIVISION BY ZERO:</strong> Integer division by zero throws ArithmeticException at runtime.<br><br>

Analysis:<br>
• <strong>5 / 0</strong> attempts to divide by zero<br>
• This is <strong>undefined mathematically</strong><br>
• Java throws <strong>ArithmeticException: / by zero</strong><br>
• Exception occurs at <strong>runtime</strong>, not compile-time<br><br>

<strong>Critical distinction:</strong><br><br>

<strong>Division BY zero:</strong><br>

```java
5 / 0   // ❌ ArithmeticException
x / 0   // ❌ ArithmeticException (if x is int)
```
<br>
<strong>Division OF zero:</strong><br>

```java
0 / 5   // ✅ OK, result = 0
0 / x   // ✅ OK (unless x is 0)
```
<br>
<strong>Floating-point division by zero (DIFFERENT behavior):</strong><br>

```java
5.0 / 0.0   // ✅ No exception, result = Infinity
0.0 / 0.0   // ✅ No exception, result = NaN (Not a Number)
```
<br>
<strong>Modulo by zero:</strong><br>

```java
5 % 0   // ❌ ArithmeticException (same as division)
```
<br>
<strong>Common exam trap:</strong><br>
• Integer division/modulo by zero → exception<br>
• Floating-point division by zero → Infinity/NaN<br><br>

<strong>Why runtime and not compile-time?</strong><br>
• Compiler cannot always determine if divisor will be zero<br>
• Division by literal zero could be detected, but Java doesn't<br>
• Consistent behavior for all division operations<br><br>

<strong>A) is incorrect:</strong> Exception is thrown, no value is printed.<br>
<strong>B) is incorrect:</strong> Infinity is for floating-point division by zero (5.0 / 0.0).<br>
<strong>D) is incorrect:</strong> Code compiles; error occurs at runtime.

## Question

What is the result?<br><br>

```java
public class Test {
    public static void main(String[] args) {
        int a = 7 % 3;
        int b = 3 % 5;
        int c = 8 % 4;
        System.out.println(a + " " + b + " " + c);
    }
}
```
<br><br>

Please select 1 option<br><br>

A) 1 3 0<br>
B) 2 2 2<br>
C) 1 0 0<br>
D) 2 3 0

## Réponse

<strong>Réponse correcte :</strong> A)<br><br>

<strong>MODULO OPERATOR (%):</strong> Returns the remainder of integer division.<br><br>

Analysis:<br><br>

<strong>int a = 7 % 3;</strong><br>
• 7 ÷ 3 = 2 remainder <strong>1</strong><br>
• a = <strong>1</strong><br><br>

<strong>int b = 3 % 5;</strong><br>
• 3 ÷ 5 = 0 remainder <strong>3</strong><br>
• When dividend < divisor, result = <strong>dividend</strong><br>
• b = <strong>3</strong><br><br>

<strong>int c = 8 % 4;</strong><br>
• 8 ÷ 4 = 2 remainder <strong>0</strong><br>
• Evenly divisible → remainder = <strong>0</strong><br>
• c = <strong>0</strong><br><br>

Output: <strong>1 3 0</strong><br><br>

<strong>Modulo rules:</strong><br><br>

1. <strong>When dividend < divisor:</strong><br>

```java
3 % 5 = 3    // dividend returned
2 % 10 = 2
1 % 100 = 1
```
<br>
2. <strong>When evenly divisible:</strong><br>

```java
10 % 5 = 0
8 % 4 = 0
6 % 3 = 0
```
<br>
3. <strong>When dividend > divisor:</strong><br>

```java
7 % 3 = 1    // remainder of 7 ÷ 3
10 % 3 = 1
11 % 3 = 2
```
<br>
4. <strong>Special case - zero:</strong><br>

```java
0 % 5 = 0    // zero divided by anything = 0
5 % 0        // ❌ ArithmeticException
```
<br>
<strong>Common uses of modulo:</strong><br>
• Check if even/odd: <strong>n % 2 == 0</strong> (even)<br>
• Cycle through values: <strong>index % arrayLength</strong><br>
• Check divisibility: <strong>n % 10 == 0</strong> (multiple of 10)<br><br>

<strong>B), C), D) are incorrect:</strong> Wrong calculation of remainders.

## Question

What is the output?<br><br>

```java
public class Test {
    public static void main(String[] args) {
        boolean result = 3 < 5 == true;
        System.out.println(result);
    }
}
```
<br><br>

Please select 1 option<br><br>

A) true<br>
B) false<br>
C) Compilation error<br>
D) Runtime exception

## Réponse

<strong>Réponse correcte :</strong> A)<br><br>

<strong>OPERATOR PRECEDENCE TRAP:</strong> Comparison operators (<, >) have higher precedence than equality operators (==, !=).<br><br>

Evaluation order:<br><br>

<strong>Step 1: Evaluate 3 < 5</strong> (comparison has higher precedence)<br>

```java
3 < 5  →  true
```
<br>
<strong>Step 2: Evaluate true == true</strong><br>

```java
true == true  →  true
```
<br>
Output: <strong>true</strong><br><br>

<strong>Precedence hierarchy for comparisons:</strong><br>
1. <strong>< > <= >=</strong> (relational operators) - higher precedence<br>
2. <strong>== !=</strong> (equality operators) - lower precedence<br><br>

The expression is evaluated as:<br>

```java
(3 < 5) == true
```

NOT as (which would be invalid):<br>

```java
3 < (5 == true)  // ❌ Cannot compare int with boolean
```
<br>
<strong>More examples:</strong><br>

```java
5 > 2 == true     // (5 > 2) == true  →  true
10 < 3 == false   // (10 < 3) == false  →  true
7 >= 7 != false   // (7 >= 7) != false  →  true
```
<br>
<strong>Common exam trap:</strong><br>
• Many think this expression is invalid<br>
• They expect compilation error<br>
• But it's valid due to operator precedence<br><br>

<strong>Why this compiles:</strong><br>
• Comparison returns <strong>boolean</strong><br>
• Equality compares two <strong>booleans</strong><br>
• Both sides are same type → valid<br><br>

<strong>B) is incorrect:</strong> (3 < 5) is true, and true == true is true.<br>
<strong>C) is incorrect:</strong> Expression is valid due to precedence rules.<br>
<strong>D) is incorrect:</strong> No exception occurs.

## Question

What is the output?<br><br>

```java
public class Test {
    public static void main(String[] args) {
        int result = 10 + 5 * 2 - 8 / 4;
        System.out.println(result);
    }
}
```
<br><br>

Please select 1 option<br><br>

A) 28<br>
B) 18<br>
C) 22<br>
D) 15

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>ARITHMETIC OPERATOR PRECEDENCE:</strong> Multiplication, division, and modulo have higher precedence than addition and subtraction.<br><br>

Precedence hierarchy:<br>
1. <strong>* / %</strong> (same level, evaluate left to right)<br>
2. <strong>+ -</strong> (same level, evaluate left to right)<br><br>

Evaluation step-by-step:<br><br>

Original expression:<br>

```java
10 + 5 * 2 - 8 / 4
```
<br>
<strong>Step 1: 5 * 2 = 10</strong> (multiplication first)<br>

```java
10 + 10 - 8 / 4
```
<br>
<strong>Step 2: 8 / 4 = 2</strong> (division, same level as multiplication)<br>

```java
10 + 10 - 2
```
<br>
<strong>Step 3: 10 + 10 = 20</strong> (left to right)<br>

```java
20 - 2
```
<br>
<strong>Step 4: 20 - 2 = 18</strong><br><br>

Output: <strong>18</strong><br><br>

<strong>Important clarification:</strong><br>
• <strong>* / %</strong> are at the <strong>SAME precedence level</strong><br>
• NOT: multiply, then divide, then modulo<br>
• AT SAME LEVEL: evaluate <strong>left to right</strong><br><br>

Example:<br>

```java
20 / 4 * 2      // Left to right: (20 / 4) * 2 = 5 * 2 = 10
20 * 2 / 4      // Left to right: (20 * 2) / 4 = 40 / 4 = 10
```
<br>
<strong>Using parentheses for clarity:</strong><br>

```java
int result = 10 + (5 * 2) - (8 / 4);  // Explicit grouping
```
<br>
<strong>Full precedence table:</strong><br>
1. <strong>( )</strong> Parentheses<br>
2. <strong>! ++ --</strong> Unary operators<br>
3. <strong>* / %</strong> Multiplicative<br>
4. <strong>+ -</strong> Additive<br>
5. <strong>< > <= >=</strong> Relational<br>
6. <strong>== !=</strong> Equality<br>
7. <strong>&&</strong> Logical AND<br>
8. <strong>||</strong> Logical OR<br><br>

<strong>A) is incorrect:</strong> Would require evaluating left to right without precedence.<br>
<strong>C) is incorrect:</strong> Wrong evaluation order.<br>
<strong>D) is incorrect:</strong> Missing some operations.

## Question

What is the result of this code?<br><br>

```java
public class Test {
    public static void main(String[] args) {
        boolean result = true || 5 / 0 > 1;
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

<strong>Réponse correcte :</strong> A)<br><br>

<strong>SHORT-CIRCUIT EVALUATION:</strong> The || operator does NOT evaluate the right operand if the left operand is true.<br><br>

Analysis:<br><br>

<strong>true || 5 / 0 > 1</strong><br><br>

Step 1: Evaluate left operand<br>
• Left operand = <strong>true</strong><br><br>

Step 2: Short-circuit decision<br>
• For <strong>||</strong> (OR), if left is <strong>true</strong> → result is <strong>always true</strong><br>
• Right operand <strong>NOT evaluated</strong><br>
• <strong>5 / 0</strong> is never executed<br><br>

Step 3: Result<br>
• Final result = <strong>true</strong><br>
• <strong>No exception thrown</strong><br><br>

Output: <strong>true</strong><br><br>

<strong>Short-circuit rules:</strong><br><br>

<strong>AND (&&):</strong><br>

```java
false && expression  // expression NOT evaluated
true && expression   // expression IS evaluated
```
<br>
<strong>OR (||):</strong><br>

```java
true || expression   // expression NOT evaluated
false || expression  // expression IS evaluated
```
<br>
<strong>Why short-circuit exists:</strong><br>
• <strong>Performance</strong> - avoid unnecessary evaluations<br>
• <strong>Safety</strong> - prevent errors in conditional code<br>
• <strong>Logic</strong> - result already determined<br><br>

<strong>Important OCP phrasing:</strong><br>
"Java does not evaluate the second operand because the result is already determined."<br><br>

<strong>More examples:</strong><br>

```java
false && (5 / 0 > 1)     // true (no division by zero)
true || (5 / 0 > 1)      // true (no division by zero)
false || (5 / 0 > 1)     // ArithmeticException (right evaluated)
true && (5 / 0 > 1)      // ArithmeticException (right evaluated)
```
<br>
<strong>Common use case:</strong><br>

```java
if (obj != null && obj.getValue() > 0) {
    // Safe: obj.getValue() only called if obj != null
}
```
<br>
<strong>B) is incorrect:</strong> OR with true always returns true.<br>
<strong>C) is incorrect:</strong> Division by zero is not executed due to short-circuit.<br>
<strong>D) is incorrect:</strong> Code compiles successfully.

## Question

What is the output?<br><br>

```java
public class Test {
    public static void main(String[] args) {
        boolean result = false && 5 / 0 > 1 && true;
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

<strong>SHORT-CIRCUIT WITH AND (&&):</strong> When left operand is false, the entire expression is false without evaluating remaining operands.<br><br>

Analysis:<br><br>

<strong>false && 5 / 0 > 1 && true</strong><br><br>

Step 1: Evaluate first operand<br>
• First operand = <strong>false</strong><br><br>

Step 2: Short-circuit decision for AND<br>
• For <strong>&&</strong> (AND), if any operand is <strong>false</strong> → result is <strong>false</strong><br>
• Remaining operands <strong>NOT evaluated</strong><br>
• <strong>5 / 0 > 1</strong> is never executed<br>
• <strong>true</strong> is never evaluated<br><br>

Step 3: Result<br>
• Final result = <strong>false</strong><br>
• <strong>No exception thrown</strong><br><br>

Output: <strong>false</strong><br><br>

<strong>AND short-circuit rule:</strong><br>
• If <strong>first operand is false</strong> → entire expression is <strong>false</strong><br>
• Remaining operands are <strong>NOT evaluated</strong><br>
• This is <strong>NOT about precedence</strong>, it's conditional evaluation<br><br>

<strong>More examples:</strong><br>

```java
false && anything         // false (anything not evaluated)
false && (x / 0 > 1)     // false (no exception)
false && true && true    // false (only first evaluated)
```
<br>
<strong>Contrast with OR:</strong><br>

```java
true || anything         // true (anything not evaluated)
false || expression      // Evaluates expression
```
<br>
<strong>When ALL operands are evaluated:</strong><br>

```java
true && true && (5 / 0 > 1)  // ❌ ArithmeticException
// All operands must be evaluated to determine result
```
<br>
<strong>Practical usage:</strong><br>

```java
if (count > 0 && total / count > 10) {
    // Safe: division only if count > 0
}

if (array != null && array.length > 0 && array[0] != null) {
    // Safe: each check protects the next
}
```
<br>
<strong>Key insight:</strong><br>
• Short-circuit is about <strong>optimization</strong> and <strong>safety</strong><br>
• Not every evaluation causes errors<br>
• Sometimes just avoids unnecessary work<br><br>

<strong>A) is incorrect:</strong> AND with false always returns false.<br>
<strong>C) is incorrect:</strong> Short-circuit prevents division by zero from executing.<br>
<strong>D) is incorrect:</strong> Code compiles successfully.

## Question

What is the result?<br><br>

```java
public class Test {
    public static void main(String[] args) {
        boolean a = true;
        boolean b = false;
        boolean result = !a && b || a;
        System.out.println(result);
    }
}
```
<br><br>

Please select 1 option<br><br>

A) true<br>
B) false<br>
C) Compilation error<br>
D) Runtime exception

## Réponse

<strong>Réponse correcte :</strong> A)<br><br>

<strong>LOGICAL OPERATOR PRECEDENCE:</strong> ! (NOT) > && (AND) > || (OR)<br><br>

Evaluation step-by-step:<br><br>

Original expression:<br>

```java
!a && b || a
```

where a = true, b = false<br><br>

<strong>Step 1: ! (NOT) - highest precedence</strong><br>

```java
!a  →  !true  →  false
```

Expression becomes:<br>

```java
false && b || a
```
<br>
<strong>Step 2: && (AND) - before ||</strong><br>

```java
false && b  →  false && false  →  false
```

Expression becomes:<br>

```java
false || a
```
<br>
<strong>Step 3: || (OR) - last</strong><br>

```java
false || a  →  false || true  →  true
```
<br>
Output: <strong>true</strong><br><br>

<strong>Logical operator precedence:</strong><br>
1. <strong>!</strong> (NOT) - highest<br>
2. <strong>&&</strong> (AND)<br>
3. <strong>||</strong> (OR) - lowest<br><br>

<strong>Why this order matters:</strong><br>

```java
!true && false || true
```

Read as:<br>

```java
(!true && false) || true
```

NOT as:<br>

```java
!(true && false || true)
```

NOT as:<br>

```java
!true && (false || true)
```
<br>
<strong>Using parentheses for clarity:</strong><br>

```java
boolean result = (!a && b) || a;  // Explicit grouping
```
<br>
<strong>Complete precedence (relevant operators):</strong><br>
1. <strong>( )</strong> Parentheses<br>
2. <strong>!</strong> NOT<br>
3. <strong>* / %</strong><br>
4. <strong>+ -</strong><br>
5. <strong>< > <= >=</strong><br>
6. <strong>== !=</strong><br>
7. <strong>&&</strong> AND<br>
8. <strong>||</strong> OR<br><br>

<strong>Mental model (OCP method):</strong><br>
1. Parentheses<br>
2. Unary (!, ++, --)<br>
3. Arithmetic<br>
4. Comparisons<br>
5. Equality<br>
6. Logical AND<br>
7. Logical OR<br><br>

<strong>B) is incorrect:</strong> Final OR with true makes result true.<br>
<strong>C) is incorrect:</strong> Expression is syntactically valid.<br>
<strong>D) is incorrect:</strong> No runtime errors occur.

## Question

What is the output?<br><br>

```java
public class Test {
    public static void main(String[] args) {
        int x = 0;
        boolean result = false && ++x > 0;
        System.out.println(x);
    }
}
```
<br><br>

Please select 1 option<br><br>

A) 0<br>
B) 1<br>
C) Compilation error<br>
D) Runtime exception

## Réponse

<strong>Réponse correcte :</strong> A)<br><br>

<strong>SHORT-CIRCUIT PREVENTS SIDE EFFECTS:</strong> When short-circuit skips evaluation, side effects (like ++) don't occur.<br><br>

Analysis:<br><br>

<strong>boolean result = false && ++x > 0;</strong><br><br>

Step 1: Evaluate left operand<br>
• Left operand = <strong>false</strong><br><br>

Step 2: Short-circuit<br>
• For <strong>&&</strong>, if left is <strong>false</strong> → result is <strong>false</strong><br>
• Right operand <strong>NOT evaluated</strong><br>
• <strong>++x</strong> is never executed<br>
• <strong>x remains 0</strong><br><br>

Step 3: Print x<br>
• x = <strong>0</strong> (unchanged)<br><br>

Output: <strong>0</strong><br><br>

<strong>Critical point:</strong> Short-circuit prevents BOTH:<br>
• The <strong>evaluation</strong> of the right side<br>
• The <strong>side effects</strong> (like increment)<br><br>

<strong>Contrast with evaluated expression:</strong><br>

```java
int x = 0;
boolean result = true && ++x > 0;  // Right side IS evaluated
System.out.println(x);  // 1 (x was incremented)
```
<br>
<strong>More examples:</strong><br>

```java
int a = 5;
boolean r1 = false && ++a > 0;  // a remains 5
boolean r2 = true || ++a > 0;   // a remains 5
boolean r3 = true && ++a > 0;   // a becomes 6
boolean r4 = false || ++a > 0;  // a becomes 6
```
<br>
<strong>Why this matters for OCP:</strong><br>
• Questions test if you understand side effects<br>
• Must track which expressions are evaluated<br>
• Short-circuit can hide bugs in production code<br><br>

<strong>Dangerous pattern to avoid:</strong><br>

```java
// ❌ Bad: side effect hidden in condition
if (x > 0 || ++count > 10) {
    // count might not increment!
}

// ✅ Good: side effect explicit
count++;
if (x > 0 || count > 10) {
    // clear and predictable
}
```
<br>
<strong>OCP exam insight:</strong><br>
"The increment operator is not executed because Java does not evaluate the second operand due to short-circuit evaluation."<br><br>

<strong>B) is incorrect:</strong> ++x is never executed due to short-circuit.<br>
<strong>C) is incorrect:</strong> Code compiles successfully.<br>
<strong>D) is incorrect:</strong> No exception occurs.

## Question

What is the result?<br><br>

```java
public class Test {
    public static void main(String[] args) {
        int result = 15 % 4 * 2 + 3;
        System.out.println(result);
    }
}
```
<br><br>

Please select 1 option<br><br>

A) 9<br>
B) 5<br>
C) 11<br>
D) 6

## Réponse

<strong>Réponse correcte :</strong> A)<br><br>

<strong>IMPORTANT:</strong> %, *, and / have the SAME precedence - evaluate left to right.<br><br>

Evaluation step-by-step:<br><br>

Original expression:<br>

```java
15 % 4 * 2 + 3
```
<br>
<strong>Step 1: 15 % 4</strong> (leftmost of %, *, /)<br>
• 15 ÷ 4 = 3 remainder <strong>3</strong><br>

```java
3 * 2 + 3
```
<br>
<strong>Step 2: 3 * 2</strong> (same precedence, continue left to right)<br>

```java
6 + 3
```
<br>
<strong>Step 3: 6 + 3</strong> (addition last)<br>

```java
9
```
<br>
Output: <strong>9</strong><br><br>

<strong>CRITICAL CLARIFICATION:</strong><br>
• <strong>%, *, /</strong> are at the <strong>SAME precedence level</strong><br>
• There is <strong>NO hierarchy</strong> among them<br>
• Evaluate <strong>strictly left to right</strong><br><br>

<strong>Common misconception:</strong><br>
❌ "Do division first, then modulo, then multiplication"<br>
✅ "%, *, / are equal - go left to right"<br><br>

<strong>More examples:</strong><br>

```java
20 / 4 * 5      // (20 / 4) * 5 = 5 * 5 = 25
20 * 5 / 4      // (20 * 5) / 4 = 100 / 4 = 25
10 % 3 * 2      // (10 % 3) * 2 = 1 * 2 = 2
```
<br>
<strong>Precedence levels (arithmetic):</strong><br>
1. <strong>( )</strong> Parentheses - highest<br>
2. <strong>* / %</strong> Multiplicative (SAME level, left to right)<br>
3. <strong>+ -</strong> Additive (SAME level, left to right)<br><br>

<strong>Using parentheses for clarity:</strong><br>

```java
int result = ((15 % 4) * 2) + 3;  // Explicit grouping
```
<br>
<strong>Why left-to-right matters:</strong><br>

```java
12 / 3 * 2
```

Left to right: (12 / 3) * 2 = 4 * 2 = <strong>8</strong> ✅<br>
Wrong thinking: 12 / (3 * 2) = 12 / 6 = 2 ❌<br><br>

<strong>B) is incorrect:</strong> Incorrect evaluation order.<br>
<strong>C) is incorrect:</strong> Wrong calculation.<br>
<strong>D) is incorrect:</strong> Missing the final addition.

## Question

What happens when this code runs?<br><br>

```java
public class Test {
    public static void main(String[] args) {
        int x = 0;
        int y = 10 / x;
        System.out.println(y);
    }
}
```
<br><br>

Please select 1 option<br><br>

A) Prints: 0<br>
B) Prints: Infinity<br>
C) ArithmeticException at runtime<br>
D) Compilation error

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

<strong>DIVISION BY ZERO:</strong> Dividing by a variable that is zero throws ArithmeticException.<br><br>

Analysis:<br>
• <strong>x = 0</strong><br>
• <strong>10 / x</strong> = 10 / 0<br>
• Division by zero is <strong>undefined</strong><br>
• Java throws <strong>ArithmeticException: / by zero</strong><br><br>

<strong>Why not a compilation error?</strong><br>
• Compiler cannot always determine variable values<br>
• x could have different values at runtime<br>
• Division by zero is a <strong>runtime error</strong><br><br>

<strong>Division by zero cases:</strong><br><br>

<strong>Integer division by zero:</strong><br>

```java
10 / 0          // ❌ ArithmeticException
int x = 0;
5 / x           // ❌ ArithmeticException
```
<br>
<strong>Floating-point division by zero (different!):</strong><br>

```java
10.0 / 0.0      // ✅ Result: Infinity
5.0 / 0         // ✅ Result: Infinity (int 0 promoted to double)
0.0 / 0.0       // ✅ Result: NaN (Not a Number)
```
<br>
<strong>Division OF zero (allowed):</strong><br>

```java
0 / 10          // ✅ Result: 0
0 / x           // ✅ OK if x != 0, Exception if x == 0
```
<br>
<strong>Modulo by zero:</strong><br>

```java
10 % 0          // ❌ ArithmeticException
```
<br>
<strong>Safe division pattern:</strong><br>

```java
int x = 0;
if (x != 0) {
    int y = 10 / x;
} else {
    // Handle division by zero case
}
```
<br>
<strong>Common exam trap:</strong><br>
• Integer vs floating-point division by zero<br>
• Literal 0 vs variable with value 0 (both throw exception)<br>
• Division BY zero vs division OF zero<br><br>

<strong>A) is incorrect:</strong> Exception prevents any output.<br>
<strong>B) is incorrect:</strong> Infinity is for floating-point division (10.0 / 0.0), not integer division.<br>
<strong>D) is incorrect:</strong> Code compiles; error occurs at runtime.

## Question

What is the output?<br><br>

```java
public class Test {
    public static void main(String[] args) {
        boolean result = true || 5 / 0 > 1 && false;
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

<strong>Réponse correcte :</strong> A)<br><br>

<strong>COMBINING SHORT-CIRCUIT AND PRECEDENCE:</strong> && has higher precedence than ||, but short-circuit prevents evaluation.<br><br>

Analysis:<br><br>

Original expression:<br>

```java
true || 5 / 0 > 1 && false
```
<br>
<strong>Step 1: Operator precedence (without short-circuit)</strong><br>
• <strong>&&</strong> has higher precedence than <strong>||</strong><br>
• Expression groups as:<br>

```java
true || (5 / 0 > 1 && false)
```
<br>
<strong>Step 2: Short-circuit evaluation</strong><br>
• Left operand of <strong>||</strong> is <strong>true</strong><br>
• For <strong>||</strong>, if left is true → result is <strong>true</strong><br>
• Right operand <strong>(5 / 0 > 1 && false)</strong> is <strong>NOT evaluated</strong><br>
• <strong>5 / 0</strong> never executes<br>
• <strong>No exception thrown</strong><br><br>

<strong>Step 3: Result</strong><br>
• Final result = <strong>true</strong><br><br>

Output: <strong>true</strong><br><br>

<strong>Important insight:</strong><br>
• <strong>Precedence</strong> determines how expression is grouped<br>
• <strong>Short-circuit</strong> determines what gets evaluated<br>
• These are <strong>different concepts</strong><br><br>

<strong>What if we forced evaluation?</strong><br>

```java
// Using parentheses to force different grouping
boolean result = (true || 5 / 0 > 1) && false;
// Still: left of || is true, right not evaluated, then true && false = false
```
<br>
<strong>When exception WOULD occur:</strong><br>

```java
false || 5 / 0 > 1 && false  // ❌ ArithmeticException
// Left is false, so right must be evaluated
```
<br>
<strong>Complex short-circuit example:</strong><br>

```java
true || (false && 5 / 0 > 1)
// true (nothing after || is evaluated)

false && (true || 5 / 0 > 1)
// false (nothing after && is evaluated)

false || (false && 5 / 0 > 1)
// Right IS evaluated, but AND short-circuits first
// false || false = false (no exception!)
```
<br>
<strong>OCP exam tip:</strong><br>
1. Identify precedence (how expression groups)<br>
2. Evaluate left to right considering short-circuit<br>
3. Stop when result is determined<br><br>

<strong>B) is incorrect:</strong> OR with true always returns true.<br>
<strong>C) is incorrect:</strong> Short-circuit prevents division by zero.<br>
<strong>D) is incorrect:</strong> Code compiles successfully.

## Question

Which expressions will compile successfully?<br><br>

Please select all that apply<br><br>

A) int x = 5; boolean b = x;<br>
B) int x = 5; int y = x > 3;<br>
C) boolean a = true; boolean b = !a;<br>
D) int x = 5; boolean b = (x == 5);

## Réponse

<strong>Réponse correcte :</strong> C), D)<br><br>

<strong>TYPE COMPATIBILITY:</strong> Expressions must evaluate to compatible types.<br><br>

Analysis:<br><br>

<strong>A) int x = 5; boolean b = x;</strong><br>
• <strong>x</strong> is type <strong>int</strong><br>
• <strong>b</strong> expects type <strong>boolean</strong><br>
• <strong>int cannot be converted to boolean</strong><br>
• ❌ <strong>Compilation error:</strong> "incompatible types: int cannot be converted to boolean"<br><br>

<strong>B) int x = 5; int y = x > 3;</strong><br>
• <strong>x > 3</strong> is a comparison<br>
• Comparisons return <strong>boolean</strong><br>
• <strong>y</strong> expects type <strong>int</strong><br>
• <strong>boolean cannot be converted to int</strong><br>
• ❌ <strong>Compilation error:</strong> "incompatible types: boolean cannot be converted to int"<br><br>

<strong>C) boolean a = true; boolean b = !a;</strong><br>
• <strong>a</strong> is type <strong>boolean</strong><br>
• <strong>!a</strong> applies NOT operator to boolean<br>
• <strong>!a</strong> returns <strong>boolean</strong> (false)<br>
• <strong>b</strong> expects <strong>boolean</strong><br>
• ✅ <strong>Types match - compiles successfully</strong><br><br>

<strong>D) int x = 5; boolean b = (x == 5);</strong><br>
• <strong>x == 5</strong> is an equality comparison<br>
• Comparisons return <strong>boolean</strong> (true)<br>
• <strong>b</strong> expects <strong>boolean</strong><br>
• ✅ <strong>Types match - compiles successfully</strong><br><br>

<strong>Key Java rules:</strong><br><br>

1. <strong>No implicit int ↔ boolean conversion:</strong><br>

```java
int x = 1;
if (x) { }        // ❌ Error in Java (OK in C/C++)
if (x != 0) { }   // ✅ OK (explicit boolean expression)
```
<br>
2. <strong>Expressions have types:</strong><br>

```java
5 + 3           // type: int, value: 8
5 > 3           // type: boolean, value: true
"Hi" + "!"      // type: String, value: "Hi!"
```
<br>
3. <strong>Assignment requires type compatibility:</strong><br>

```java
int x = 5;           // ✅ int = int
boolean b = true;    // ✅ boolean = boolean
int y = true;        // ❌ int = boolean (incompatible)
boolean c = 5;       // ❌ boolean = int (incompatible)
```
<br>
<strong>Common exam traps:</strong><br>
• Assigning comparison result to int variable<br>
• Using int where boolean is expected<br>
• Forgetting that comparisons return boolean<br><br>

<strong>A) is incorrect:</strong> Cannot assign int to boolean variable.<br>
<strong>B) is incorrect:</strong> Cannot assign boolean (result of comparison) to int variable.

## Question

What is the result?<br><br>

```java
public class Test {
    public static void main(String[] args) {
        int a = 10;
        int b = 3;
        int c = a / b * b + a % b;
        System.out.println(c);
    }
}
```
<br><br>

Please select 1 option<br><br>

A) 10<br>
B) 9<br>
C) 11<br>
D) 12

## Réponse

<strong>Réponse correcte :</strong> A)<br><br>

<strong>COMBINATION OF /, *, AND % WITH SAME PRECEDENCE.</strong><br><br>

Evaluation step-by-step:<br><br>

Given: a = 10, b = 3<br><br>

Original expression:<br>

```java
a / b * b + a % b
```

Substitute values:<br>

```java
10 / 3 * 3 + 10 % 3
```
<br>
<strong>Step 1: 10 / 3</strong> (leftmost of /, *, %)<br>
• Integer division: 10 ÷ 3 = <strong>3</strong> (truncated)<br>

```java
3 * 3 + 10 % 3
```
<br>
<strong>Step 2: 3 * 3</strong> (same precedence, left to right)<br>

```java
9 + 10 % 3
```
<br>
<strong>Step 3: 10 % 3</strong> (same precedence as /, *)<br>
• 10 ÷ 3 = 3 remainder <strong>1</strong><br>

```java
9 + 1
```
<br>
<strong>Step 4: 9 + 1</strong> (addition last)<br>

```java
10
```
<br>
Output: <strong>10</strong><br><br>

<strong>Interesting observation:</strong><br>
• <strong>a / b * b</strong> recovers most of a (loses the remainder)<br>
• <strong>a % b</strong> gives the remainder<br>
• <strong>a / b * b + a % b</strong> reconstructs the original value!<br><br>

Mathematical identity:<br>

```
a = (a / b) * b + (a % b)
```

This works for any integers a and b (where b ≠ 0).<br><br>

<strong>More examples:</strong><br>

```java
// a = 17, b = 5
17 / 5 * 5 + 17 % 5  =  3 * 5 + 2  =  17 ✅

// a = 20, b = 4
20 / 4 * 4 + 20 % 4  =  5 * 4 + 0  =  20 ✅

// a = 7, b = 10
7 / 10 * 10 + 7 % 10  =  0 * 10 + 7  =  7 ✅
```
<br>
<strong>Precedence reminder:</strong><br>
• <strong>/, *, %</strong> are equal precedence<br>
• Evaluate <strong>strictly left to right</strong><br>
• <strong>+, -</strong> have lower precedence<br><br>

<strong>B) is incorrect:</strong> This would be just a / b * b without the remainder.<br>
<strong>C) is incorrect:</strong> Wrong calculation.<br>
<strong>D) is incorrect:</strong> Wrong evaluation order.
