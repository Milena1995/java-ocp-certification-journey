## Question

What will the following code print?<br><br>

```java
public class Test {
    public static void main(String[] args) {
        try {
            int result = 10 / 0;
            System.out.print("Result: " + result);
        } catch (ArithmeticException e) {
            System.out.print("ArithmeticException caught");
        }
        System.out.print(" Done");
    }
}
```
<br><br>

Please select 1 option<br><br>

A) Result: Infinity Done<br>
B) Compilation error<br>
C) ArithmeticException caught Done<br>
D) Runtime error with no output

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

<strong>INTEGER DIVISION BY ZERO:</strong> Dividing an <strong>int</strong> by zero throws <strong>ArithmeticException</strong> at runtime.<br><br>

Execution flow:<br>
• <strong>int result = 10 / 0;</strong> throws ArithmeticException<br>
• Normal flow is interrupted immediately<br>
• Jumps to the <strong>catch block</strong><br>
• Prints <strong>"ArithmeticException caught"</strong><br>
• Continues after try-catch block<br>
• Prints <strong>" Done"</strong><br><br>

Output: <strong>ArithmeticException caught Done</strong><br><br>

<strong>CRITICAL OCP DISTINCTION:</strong><br>
• <strong>int / 0</strong> → throws ArithmeticException<br>
• <strong>double / 0</strong> → returns Infinity (NO exception)<br>
• <strong>0.0 / 0</strong> → returns NaN (NO exception)<br><br>

<strong>A) is incorrect:</strong> Infinity only occurs with double division, and there's no result printed.<br>
<strong>B) is incorrect:</strong> The code compiles; error occurs at runtime.<br>
<strong>D) is incorrect:</strong> The exception is caught, so there's controlled output.

## Question

What will the following code print?<br><br>

```java
public class Test {
    public static void main(String[] args) {
        try {
            double result = 10.0 / 0;
            System.out.print("Result: " + result);
        } catch (ArithmeticException e) {
            System.out.print("Exception caught");
        }
        System.out.print(" Done");
    }
}
```
<br><br>

Please select 1 option<br><br>

A) Result: Infinity Done<br>
B) Exception caught Done<br>
C) Result: NaN Done<br>
D) Compilation error

## Réponse

<strong>Réponse correcte :</strong> A)<br><br>

<strong>DOUBLE DIVISION BY ZERO TRAP:</strong> Dividing a <strong>double</strong> by zero does <strong>NOT</strong> throw an exception. It returns <strong>Infinity</strong>.<br><br>

Analysis:<br>
• <strong>double result = 10.0 / 0;</strong><br>
→ Result is <strong>Infinity</strong> (positive infinity)<br>
→ <strong>NO ArithmeticException is thrown</strong><br>
→ This follows IEEE 754 floating-point standard<br><br>

• Prints <strong>"Result: Infinity"</strong><br>
• Catch block is <strong>NOT executed</strong> (no exception occurred)<br>
• Continues to print <strong>" Done"</strong><br><br>

Output: <strong>Result: Infinity Done</strong><br><br>

<strong>IEEE 754 BEHAVIOR:</strong><br>
• <strong>positive / 0.0</strong> → Infinity<br>
• <strong>negative / 0.0</strong> → -Infinity<br>
• <strong>0.0 / 0.0</strong> → NaN (Not a Number)<br><br>

<strong>CRITICAL for OCP:</strong> The catch block will <strong>NEVER</strong> execute because no exception is thrown.<br><br>

<strong>B) is incorrect:</strong> No exception is thrown with double division.<br>
<strong>C) is incorrect:</strong> NaN occurs only with 0.0 / 0.0.<br>
<strong>D) is incorrect:</strong> The code compiles and runs.

## Question

Which of the following are differences between `throw` and `throws` keywords?<br><br>

Please select 2 options<br><br>

A) `throw` is used in method signature, `throws` is used inside method body<br>
B) `throw` actually throws an exception, `throws` declares that a method might throw an exception<br>
C) `throw` is followed by an exception class name, `throws` is followed by an exception object<br>
D) `throw` is used inside a method body, `throws` is used in a method signature

## Réponse

<strong>Réponse correcte :</strong> B), D)<br><br>

<strong>B) is correct:</strong><br>
• <strong>throw</strong> actually creates and throws an exception object:<br>
```java
throw new IllegalArgumentException("Invalid input");
```
• <strong>throws</strong> only declares that a method may throw an exception:<br>
```java
public void readFile() throws IOException { }
```
It's a declaration, not an action.<br><br>

<strong>D) is correct:</strong><br>
• <strong>throw</strong> is used <strong>inside</strong> a method body to throw an exception<br>
• <strong>throws</strong> is used in the <strong>method signature</strong> after the parameter list<br><br>

<strong>A) is incorrect:</strong> It's the <strong>opposite</strong>: throw is in method body, throws is in signature.<br><br>

<strong>C) is incorrect:</strong> It's the <strong>opposite</strong>:<br>
• <strong>throw</strong> is followed by an <strong>exception object</strong>: throw new Exception()<br>
• <strong>throws</strong> is followed by an <strong>exception class name</strong>: throws IOException

## Question

What is the result of compiling and running this code?<br><br>

```java
public class Test {
    public static void main(String[] args) {
        try {
            System.out.print("A");
            throw new RuntimeException();
            System.out.print("B");
        } catch (RuntimeException e) {
            System.out.print("C");
        }
        System.out.print("D");
    }
}
```
<br><br>

Please select 1 option<br><br>

A) ACD<br>
B) ABCD<br>
C) AB<br>
D) Compilation error

## Réponse

<strong>Réponse correcte :</strong> D)<br><br>

<strong>UNREACHABLE CODE TRAP:</strong> Code after a <strong>throw</strong> statement in the same block is <strong>unreachable</strong> and causes a <strong>compilation error</strong>.<br><br>

Analysis:<br>
• <strong>throw new RuntimeException();</strong> will always throw an exception<br>
• The line <strong>System.out.print("B");</strong> can <strong>never be reached</strong><br>
• The compiler detects this and reports: <strong>"unreachable statement"</strong><br><br>

<strong>CRITICAL RULE:</strong> Any statement immediately after <strong>throw</strong>, <strong>return</strong>, or unconditional control flow transfer in the same block is unreachable and causes a compilation error.<br><br>

<strong>If the code could compile, it would print:</strong> ACD (but it doesn't compile)<br><br>

Similar unreachable code errors:<br>
```java
return;
System.out.print("X");  // unreachable

if (true) {
    throw new Exception();
}
System.out.print("Y");  // reachable (compiler can't prove it won't execute)
```
<br><br>

<strong>A), B), C) are incorrect:</strong> The code does not compile.

## Question

What will the following code print?<br><br>

```java
public class Test {
    public static void main(String[] args) {
        try {
            System.out.print("A");
            int x = 10 / 0;
            System.out.print("B");
        } catch (NullPointerException e) {
            System.out.print("C");
        } catch (ArithmeticException e) {
            System.out.print("D");
        } catch (Exception e) {
            System.out.print("E");
        }
        System.out.print("F");
    }
}
```
<br><br>

Please select 1 option<br><br>

A) ADF<br>
B) ACF<br>
C) AEF<br>
D) ABF

## Réponse

<strong>Réponse correcte :</strong> A)<br><br>

<strong>EXCEPTION MATCHING:</strong> Java uses the <strong>first matching catch block</strong> based on exception type.<br><br>

Execution flow:<br>
• Prints <strong>"A"</strong><br>
• <strong>int x = 10 / 0;</strong> throws <strong>ArithmeticException</strong><br>
• "B" is NOT printed (exception occurred)<br><br>

Catch block matching:<br>
• First catch: <strong>NullPointerException</strong> → NO match (wrong type)<br>
• Second catch: <strong>ArithmeticException</strong> → <strong>MATCH</strong><br>
→ Prints <strong>"D"</strong><br>
→ Exits try-catch (only ONE catch executes)<br><br>

• Third catch: <strong>Exception</strong> → NOT evaluated (already caught)<br>
• Prints <strong>"F"</strong><br><br>

Output: <strong>ADF</strong><br><br>

<strong>KEY RULE:</strong> Only the <strong>first matching</strong> catch block executes. Once caught, exception handling is complete.<br><br>

<strong>B) is incorrect:</strong> NullPointerException doesn't match ArithmeticException.<br>
<strong>C) is incorrect:</strong> ArithmeticException is caught by its specific handler before reaching Exception.<br>
<strong>D) is incorrect:</strong> "B" is never printed because the exception occurs before it.

## Question

Given the following code:<br><br>

```java
class Calculator {
    double average(int[] values) {
        int sum = 0;
        for (int v : values) {
            sum += v;
        }
        return sum / values.length;
    }
}

public class Test {
    public static void main(String[] args) {
        Calculator c = new Calculator();
        int[] nums = {};
        System.out.println(c.average(nums));
    }
}
```
<br><br>

What is the result?<br><br>

Please select 1 option<br><br>

A) 0<br>
B) 0.0<br>
C) ArithmeticException at runtime<br>
D) ArrayIndexOutOfBoundsException at runtime

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

<strong>EMPTY ARRAY DIVISION TRAP:</strong><br><br>

Analysis:<br>
• <strong>int[] nums = {};</strong> creates an empty array<br>
• <strong>values.length</strong> is <strong>0</strong><br>
• Loop executes 0 times, sum remains <strong>0</strong><br>
• <strong>return sum / values.length;</strong> becomes <strong>0 / 0</strong><br><br>

<strong>CRITICAL:</strong> Even though return type is <strong>double</strong>, the division is performed as <strong>int / int</strong> because both operands are int:<br>
• sum is <strong>int</strong><br>
• values.length is <strong>int</strong><br>
• <strong>int / int</strong> performs integer division<br>
• <strong>0 / 0</strong> with integers throws <strong>ArithmeticException</strong><br><br>

The result is then implicitly cast to double, but the exception occurs <strong>before</strong> the cast.<br><br>

<strong>If it were:</strong><br>
```java
return sum / (double)values.length;  // would return NaN, no exception
```
<br><br>

<strong>A), B) are incorrect:</strong> Integer division by zero throws an exception.<br>
<strong>D) is incorrect:</strong> No array access occurs; the error is division by zero.

## Question

Which of the following exceptions are checked exceptions?<br><br>

Please select 2 options<br><br>

A) IOException<br>
B) NullPointerException<br>
C) FileNotFoundException<br>
D) ArithmeticException

## Réponse

<strong>Réponse correcte :</strong> A), C)<br><br>

<strong>CHECKED vs UNCHECKED EXCEPTIONS:</strong><br><br>

<strong>A) is correct:</strong> <strong>IOException</strong> is a <strong>checked exception</strong>. It must be either caught or declared with throws.<br>
```java
public void readFile() throws IOException {
    // must declare or catch
}
```
<br><br>

<strong>C) is correct:</strong> <strong>FileNotFoundException</strong> is a <strong>checked exception</strong> (subclass of IOException). It must be handled.<br><br>

<strong>CHECKED EXCEPTIONS:</strong><br>
• Extend <strong>Exception</strong> but NOT RuntimeException<br>
• Checked at <strong>compile time</strong><br>
• Must be handled with try-catch OR declared with throws<br>
• Examples: IOException, SQLException, ClassNotFoundException<br><br>

<strong>B) is incorrect:</strong> <strong>NullPointerException</strong> extends <strong>RuntimeException</strong> → unchecked.<br>
<strong>D) is incorrect:</strong> <strong>ArithmeticException</strong> extends <strong>RuntimeException</strong> → unchecked.<br><br>

<strong>UNCHECKED EXCEPTIONS:</strong><br>
• Extend <strong>RuntimeException</strong><br>
• NOT checked at compile time<br>
• Handling is optional<br>
• Examples: NullPointerException, ArithmeticException, ArrayIndexOutOfBoundsException

## Question

What will the following code print?<br><br>

```java
public class Test {
    static void methodA() {
        methodB();
        System.out.print("A");
    }

    static void methodB() {
        throw new RuntimeException();
    }

    public static void main(String[] args) {
        try {
            methodA();
        } catch (RuntimeException e) {
            System.out.print("B");
        }
        System.out.print("C");
    }
}
```
<br><br>

Please select 1 option<br><br>

A) ABC<br>
B) BC<br>
C) AC<br>
D) Runtime error

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>EXCEPTION PROPAGATION:</strong> If a method doesn't catch an exception, it <strong>propagates up</strong> to the calling method.<br><br>

Execution flow:<br>
• main() calls <strong>methodA()</strong> inside try block<br>
• methodA() calls <strong>methodB()</strong><br>
• methodB() throws <strong>RuntimeException</strong><br>
→ methodB() has no catch block → <strong>exception propagates</strong> to methodA()<br>
• methodA() has no catch block → <strong>exception propagates</strong> to main()<br>
• <strong>System.out.print("A");</strong> in methodA is <strong>NEVER reached</strong><br>
• main()'s catch block catches the exception<br>
→ Prints <strong>"B"</strong><br>
• Continues after try-catch<br>
→ Prints <strong>"C"</strong><br><br>

Output: <strong>BC</strong><br><br>

<strong>KEY CONCEPT:</strong> When an exception is thrown, the normal flow stops immediately. Code after the throw point in the call stack is NOT executed until the exception is caught.<br><br>

<strong>A) is incorrect:</strong> "A" is never printed because the exception occurs before that line.<br>
<strong>C) is incorrect:</strong> "B" is printed by the catch block.<br>
<strong>D) is incorrect:</strong> The exception is caught in main().

## Question

What will the following code print?<br><br>

```java
public class Test {
    public static void main(String[] args) {
        try {
            System.out.print("A");
            return;
        } catch (Exception e) {
            System.out.print("B");
        } finally {
            System.out.print("C");
        }
        System.out.print("D");
    }
}
```
<br><br>

Please select 1 option<br><br>

A) AC<br>
B) ACD<br>
C) ABCD<br>
D) Compilation error

## Réponse

<strong>Réponse correcte :</strong> D)<br><br>

<strong>UNREACHABLE CODE + FINALLY:</strong><br><br>

Two issues in this code:<br><br>

1. <strong>finally block execution:</strong><br>
• The finally block executes even when return is called<br>
• If the code could run, it would print "AC"<br><br>

2. <strong>Unreachable statement:</strong><br>
• <strong>System.out.print("D");</strong> after the try-catch-finally is <strong>unreachable</strong><br>
• The try block has <strong>return</strong>, which exits the method<br>
• No exception is thrown, so catch is never reached<br>
• finally executes, then method exits<br>
• "D" can never be reached<br><br>

<strong>Compilation error:</strong> "unreachable statement"<br><br>

<strong>To fix, remove the line after finally or change the control flow:</strong><br>
```java
// Option 1: Remove unreachable code
try {
    System.out.print("A");
    return;
} finally {
    System.out.print("C");
}

// Option 2: Make return conditional
try {
    System.out.print("A");
    if (false) return;
} finally {
    System.out.print("C");
}
System.out.print("D");  // now reachable
```
<br><br>

<strong>A), B), C) are incorrect:</strong> The code does not compile.

## Question

Which statements about RuntimeException are correct?<br><br>

Please select 3 options<br><br>

A) RuntimeException and its subclasses are unchecked exceptions<br>
B) Methods that throw RuntimeException must declare it with throws<br>
C) RuntimeException extends Exception<br>
D) Catching RuntimeException is optional

## Réponse

<strong>Réponse correcte :</strong> A), C), D)<br><br>

<strong>A) is correct:</strong> <strong>RuntimeException</strong> and all its subclasses (NullPointerException, ArithmeticException, etc.) are <strong>unchecked exceptions</strong>.<br><br>

<strong>C) is correct:</strong> <strong>RuntimeException</strong> extends <strong>Exception</strong> in the exception hierarchy:<br>
```
Object
  ↳ Throwable
       ↳ Exception
            ↳ RuntimeException
```
<br><br>

<strong>D) is correct:</strong> Catching RuntimeException is <strong>optional</strong>. The compiler does NOT enforce handling of unchecked exceptions.<br><br>

<strong>B) is incorrect:</strong> Methods that throw RuntimeException are <strong>NOT required</strong> to declare it with throws (though they can). This is what makes them "unchecked":<br>
```java
// Both are valid:
void method1() {
    throw new RuntimeException();  // no throws declaration needed
}

void method2() throws RuntimeException {
    throw new RuntimeException();  // declaration is optional
}
```
<br><br>

<strong>CHECKED vs UNCHECKED summary:</strong><br>
• <strong>Checked:</strong> Must be caught or declared (IOException, SQLException)<br>
• <strong>Unchecked:</strong> Optional handling (RuntimeException subclasses)

## Question

What will the following code print?<br><br>

```java
public class Test {
    public static void main(String[] args) {
        try {
            double result = 0.0 / 0.0;
            System.out.print("Result: " + result);
        } catch (ArithmeticException e) {
            System.out.print("Exception");
        }
        System.out.print(" Done");
    }
}
```
<br><br>

Please select 1 option<br><br>

A) Result: NaN Done<br>
B) Result: Infinity Done<br>
C) Exception Done<br>
D) Result: 0.0 Done

## Réponse

<strong>Réponse correcte :</strong> A)<br><br>

<strong>0.0 / 0.0 SPECIAL CASE:</strong> Dividing <strong>0.0 by 0.0</strong> returns <strong>NaN</strong> (Not a Number), not Infinity, and does <strong>NOT</strong> throw an exception.<br><br>

Analysis:<br>
• <strong>double result = 0.0 / 0.0;</strong><br>
→ Result is <strong>NaN</strong> (special double value)<br>
→ <strong>NO ArithmeticException</strong> is thrown<br>
→ IEEE 754 floating-point standard behavior<br><br>

• Prints <strong>"Result: NaN"</strong><br>
• Catch block is <strong>NOT executed</strong> (no exception)<br>
• Prints <strong>" Done"</strong><br><br>

Output: <strong>Result: NaN Done</strong><br><br>

<strong>CRITICAL OCP DISTINCTIONS:</strong><br>
• <strong>10 / 0</strong> (int) → ArithmeticException<br>
• <strong>10.0 / 0</strong> (double) → Infinity<br>
• <strong>-10.0 / 0</strong> (double) → -Infinity<br>
• <strong>0.0 / 0.0</strong> (double) → <strong>NaN</strong><br><br>

<strong>NaN properties:</strong><br>
• NaN is not equal to anything, including itself: <strong>NaN != NaN</strong> is true<br>
• Use <strong>Double.isNaN(value)</strong> to test for NaN<br><br>

<strong>B) is incorrect:</strong> 0.0 / 0.0 produces NaN, not Infinity.<br>
<strong>C) is incorrect:</strong> No exception is thrown.<br>
<strong>D) is incorrect:</strong> Result is NaN, not 0.0.

## Question

What is the result of compiling this code?<br><br>

```java
public class Test {
    void methodA() throws IOException {
        throw new IOException();
    }

    void methodB() {
        methodA();
    }
}
```
<br><br>

Please select 1 option<br><br>

A) Compiles successfully<br>
B) Compilation error: IOException is a checked exception<br>
C) Compilation error: methodA must declare throws Exception<br>
D) Compilation error: methodB must be declared with throws IOException

## Réponse

<strong>Réponse correcte :</strong> D)<br><br>

<strong>CHECKED EXCEPTION HANDLING RULE:</strong> If a method calls another method that throws a <strong>checked exception</strong>, it must either:<br>
1. Catch the exception with try-catch, OR<br>
2. Declare the exception with throws<br><br>

Analysis:<br>
• <strong>methodA()</strong> declares <strong>throws IOException</strong> (checked exception)<br>
• <strong>methodB()</strong> calls methodA()<br>
• methodB() does <strong>NOT</strong> handle IOException<br>
• methodB() does <strong>NOT</strong> declare throws IOException<br><br>

<strong>Compilation error:</strong> "unreported exception IOException; must be caught or declared to be thrown"<br><br>

<strong>To fix, methodB must either:</strong><br><br>

Option 1: Catch the exception<br>
```java
void methodB() {
    try {
        methodA();
    } catch (IOException e) {
        // handle
    }
}
```
<br><br>

Option 2: Declare throws<br>
```java
void methodB() throws IOException {
    methodA();
}
```
<br><br>

<strong>A) is incorrect:</strong> The code does not compile.<br>
<strong>B) is incorrect:</strong> While IOException is checked, the issue is with methodB, not methodA.<br>
<strong>C) is incorrect:</strong> methodA correctly declares throws IOException.

## Question

What will the following code print?<br><br>

```java
public class Test {
    public static void main(String[] args) {
        try {
            System.out.print("A");
            int x = 10 / 0;
        } catch (ArithmeticException | NullPointerException e) {
            System.out.print("B");
        } catch (Exception e) {
            System.out.print("C");
        } finally {
            System.out.print("D");
        }
        System.out.print("E");
    }
}
```
<br><br>

Please select 1 option<br><br>

A) ACDE<br>
B) ABDE<br>
C) ADE<br>
D) ABDE

## Réponse

<strong>Réponse correcte :</strong> D)<br><br>

<strong>MULTI-CATCH + FINALLY:</strong> Java allows catching multiple exception types in a single catch block using <strong>|</strong>.<br><br>

Execution flow:<br>
• Prints <strong>"A"</strong><br>
• <strong>int x = 10 / 0;</strong> throws <strong>ArithmeticException</strong><br><br>

• First catch: <strong>ArithmeticException | NullPointerException</strong><br>
→ Matches ArithmeticException → <strong>catches it</strong><br>
→ Prints <strong>"B"</strong><br><br>

• Second catch: <strong>Exception</strong><br>
→ <strong>NOT evaluated</strong> (exception already caught)<br><br>

• <strong>finally block</strong> executes<br>
→ Prints <strong>"D"</strong><br>
→ finally <strong>always executes</strong> (unless System.exit() or JVM crash)<br><br>

• Continues after try-catch-finally<br>
→ Prints <strong>"E"</strong><br><br>

Output: <strong>ABDE</strong><br><br>

<strong>MULTI-CATCH SYNTAX (Java 7+):</strong><br>
```java
catch (ExceptionType1 | ExceptionType2 | ExceptionType3 e) {
    // handle all three types
}
```
<br><br>

<strong>RESTRICTIONS:</strong><br>
• Exception types in multi-catch cannot have inheritance relationship<br>
• The variable <strong>e</strong> is implicitly <strong>final</strong><br><br>

<strong>A), B), C) are incorrect:</strong> All have wrong combinations of output.

## Question

Given the following code:<br><br>

```java
class Calculator {
    double calculateAverage(int[] values) throws ArithmeticException {
        if (values.length == 0) {
            throw new ArithmeticException("Empty array");
        }
        int sum = 0;
        for (int v : values) {
            sum += v;
        }
        return (double) sum / values.length;
    }
}

public class Test {
    public static void main(String[] args) {
        Calculator c = new Calculator();
        int[] nums = {};
        System.out.println(c.calculateAverage(nums));
    }
}
```
<br><br>

What is the result?<br><br>

Please select 1 option<br><br>

A) 0.0<br>
B) Compilation error: must handle ArithmeticException<br>
C) Runtime exception: ArithmeticException: Empty array<br>
D) NaN

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

<strong>THROW STATEMENT + UNCHECKED EXCEPTION:</strong><br><br>

Analysis:<br>
• <strong>ArithmeticException</strong> is a <strong>RuntimeException</strong> (unchecked)<br>
• Even though calculateAverage() declares <strong>throws ArithmeticException</strong>, handling is <strong>NOT required</strong> because it's unchecked<br>
• The code compiles successfully<br><br>

Runtime execution:<br>
• <strong>int[] nums = {};</strong> creates empty array<br>
• <strong>values.length == 0</strong> is true<br>
• <strong>throw new ArithmeticException("Empty array");</strong> executes<br>
• Exception is thrown from calculateAverage()<br>
• main() has <strong>NO try-catch</strong><br>
• Exception propagates to JVM<br>
• Program terminates with <strong>ArithmeticException: Empty array</strong><br><br>

<strong>KEY CONCEPTS:</strong><br>
• <strong>throws</strong> declaration for RuntimeException is <strong>optional but allowed</strong><br>
• It serves as documentation but doesn't require handling<br>
• The exception is actually thrown with <strong>throw</strong> statement<br><br>

<strong>A) is incorrect:</strong> Exception is thrown before any calculation.<br>
<strong>B) is incorrect:</strong> ArithmeticException is unchecked; handling is optional.<br>
<strong>D) is incorrect:</strong> No division occurs; exception is thrown first.

## Question

What will the following code print?<br><br>

```java
public class Test {
    static void process(int value) {
        try {
            if (value == 0) {
                throw new IllegalArgumentException();
            }
            System.out.print("A");
        } catch (RuntimeException e) {
            System.out.print("B");
            throw e;
        } finally {
            System.out.print("C");
        }
        System.out.print("D");
    }

    public static void main(String[] args) {
        try {
            process(0);
        } catch (Exception e) {
            System.out.print("E");
        }
    }
}
```
<br><br>

Please select 1 option<br><br>

A) BCE<br>
B) BCDE<br>
C) ACE<br>
D) ABCE

## Réponse

<strong>Réponse correcte :</strong> A)<br><br>

<strong>RE-THROWING EXCEPTION + FINALLY:</strong><br><br>

Execution flow:<br>
• process(0) is called<br>
• <strong>if (value == 0)</strong> is true<br>
• <strong>throw new IllegalArgumentException();</strong><br>
→ Exception is thrown (note: IllegalArgumentException extends RuntimeException)<br><br>

• Catch block for <strong>RuntimeException</strong> catches it<br>
→ Prints <strong>"B"</strong><br>
→ <strong>throw e;</strong> re-throws the exception<br><br>

• <strong>finally block executes</strong> (even when exception is re-thrown)<br>
→ Prints <strong>"C"</strong><br><br>

• <strong>System.out.print("D");</strong> is <strong>NEVER reached</strong><br>
→ Exception was re-thrown, so process() exits abnormally<br>
→ "D" is unreachable in this execution path<br><br>

• Exception propagates to main()<br>
• main()'s catch block catches it<br>
→ Prints <strong>"E"</strong><br><br>

Output: <strong>BCE</strong><br><br>

<strong>KEY CONCEPTS:</strong><br>
• finally executes <strong>even when exception is re-thrown</strong><br>
• Code after finally in the same method is NOT reached if exception is re-thrown<br>
• Re-throwing allows you to log/handle locally then propagate<br><br>

<strong>B), C), D) are incorrect:</strong> "D" is not printed because exception is re-thrown.

## Question

What is the result of compiling and running this code?<br><br>

```java
public class Test {
    public static void main(String[] args) {
        String str = null;
        try {
            System.out.print(str.length());
        } catch (NullPointerException e) {
            System.out.print("NPE");
            return;
        } finally {
            System.out.print(" Finally");
        }
        System.out.print(" Done");
    }
}
```
<br><br>

Please select 1 option<br><br>

A) NPE Finally<br>
B) NPE Finally Done<br>
C) NPE Done<br>
D) Finally Done

## Réponse

<strong>Réponse correcte :</strong> A)<br><br>

<strong>FINALLY with RETURN:</strong> The finally block executes <strong>even when return is called</strong> from a catch block.<br><br>

Execution flow:<br>
• <strong>String str = null;</strong><br>
• <strong>str.length()</strong> throws <strong>NullPointerException</strong><br>
→ Cannot call method on null reference<br><br>

• Catch block for <strong>NullPointerException</strong> catches it<br>
→ Prints <strong>"NPE"</strong><br>
→ <strong>return;</strong> attempts to exit the method<br><br>

• Before return completes, <strong>finally block executes</strong><br>
→ Prints <strong>" Finally"</strong><br><br>

• Method exits (return completes)<br>
• <strong>System.out.print(" Done");</strong> is <strong>NEVER reached</strong><br>
→ return statement prevents it<br><br>

Output: <strong>NPE Finally</strong><br><br>

<strong>FINALLY EXECUTION RULES:</strong><br>
• finally executes with normal completion<br>
• finally executes with return statement<br>
• finally executes with exception (caught or uncaught)<br>
• finally does <strong>NOT</strong> execute only if: System.exit() or JVM crash<br><br>

<strong>B) is incorrect:</strong> "Done" is not reached because of return in catch.<br>
<strong>C) is incorrect:</strong> finally always executes.<br>
<strong>D) is incorrect:</strong> "NPE" is printed before finally.
