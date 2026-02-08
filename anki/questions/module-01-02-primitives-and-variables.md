## Question

What is the output of the following code?<br><br>

```java
public class Test {
    public static void main(String[] args) {
        int x;
        System.out.println(x);
    }
}
```
<br><br>

Please select 1 option<br><br>

A) 0<br>
B) null<br>
C) Compilation error<br>
D) Runtime exception

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

<strong>CRITICAL RULE:</strong> Local variables <strong>do NOT have default values</strong>.<br><br>

Analysis:<br>
• <strong>x is a local variable</strong> (declared inside main method)<br>
• It is <strong>declared but NOT initialized</strong><br>
• Using an uninitialized local variable → <strong>compilation error</strong><br>
• Error message: "variable x might not have been initialized"<br><br>

<strong>Important distinction:</strong><br>
• <strong>Instance variables:</strong> have default values (int = 0)<br>
• <strong>Local variables:</strong> NO default values (must initialize before use)<br><br>

Correct code:<br>

```java
int x = 0;  // Must initialize
System.out.println(x);  // Now OK
```
<br>
<strong>A) is incorrect:</strong> 0 would be the default for instance variables, not local variables.<br>
<strong>B) is incorrect:</strong> Primitives can never be null.<br>
<strong>D) is incorrect:</strong> Code doesn't compile, so it never runs.

## Question

Which statements about primitive types in Java are correct?<br><br>

Please select all that apply<br><br>

A) There are exactly 8 primitive types in Java<br>
B) Primitive types can be null<br>
C) String is a primitive type<br>
D) Primitives store values directly, not references

## Réponse

<strong>Réponse correcte :</strong> A), D)<br><br>

<strong>The 8 primitive types in Java:</strong><br><br>

Integers: <strong>byte, short, int, long</strong><br>
Decimals: <strong>float, double</strong><br>
Other: <strong>char, boolean</strong><br><br>

<strong>Key characteristics:</strong><br>
• Primitives are <strong>NOT objects</strong><br>
• Store <strong>values directly</strong> (not references)<br>
• <strong>Cannot be null</strong><br>
• Stored in the <strong>stack</strong> (when local variables)<br><br>

Default literals:<br>
• Integer literal → <strong>int</strong> (e.g., 42)<br>
• Decimal literal → <strong>double</strong> (e.g., 3.14)<br><br>

<strong>B) is incorrect:</strong> Primitives can NEVER be null - only reference types can.<br>
<strong>C) is incorrect:</strong> String is a reference type (object), not a primitive.

## Question

What is the output of the following code?<br><br>

```java
public class Test {
    public static void main(String[] args) {
        int a = 5;
        int b = a++;
        int c = ++a;
        System.out.println(a + " " + b + " " + c);
    }
}
```
<br><br>

Please select 1 option<br><br>

A) 5 5 6<br>
B) 7 5 7<br>
C) 6 5 6<br>
D) 7 6 7

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>CRITICAL DIFFERENCE:</strong> Post-increment vs Pre-increment.<br><br>

Execution step-by-step:<br><br>

<strong>int a = 5;</strong><br>
• a = 5<br><br>

<strong>int b = a++;</strong> (post-increment)<br>
• Use value FIRST: b = 5<br>
• Then increment: a = 6<br><br>

<strong>int c = ++a;</strong> (pre-increment)<br>
• Increment FIRST: a = 7<br>
• Then use value: c = 7<br><br>

Final state:<br>
• a = <strong>7</strong><br>
• b = <strong>5</strong><br>
• c = <strong>7</strong><br><br>

Output: <strong>7 5 7</strong><br><br>

<strong>Key rule:</strong><br>
• <strong>a++</strong> → use then increment<br>
• <strong>++a</strong> → increment then use<br><br>

<strong>A), C), D) are incorrect:</strong> Wrong understanding of increment operators.

## Question

Given the following code:<br><br>

```java
public class Test {
    static int count;
    static String name;
    static boolean active;

    public static void main(String[] args) {
        System.out.println(count);
        System.out.println(name);
        System.out.println(active);
    }
}
```
<br><br>

What is the output?<br><br>

Please select 1 option<br><br>

A) Compilation error<br>
B) 0<br>
null<br>
false<br><br>

C) null<br>
null<br>
null<br><br>

D) 0<br>
empty string<br>
false

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>Static and instance variables have DEFAULT values.</strong><br><br>

Default values by type:<br><br>

<strong>Numeric primitives:</strong><br>
• byte, short, int, long → <strong>0</strong><br>
• float, double → <strong>0.0</strong><br><br>

<strong>Other primitives:</strong><br>
• boolean → <strong>false</strong><br>
• char → <strong>'\u0000'</strong><br><br>

<strong>Reference types:</strong><br>
• String, objects, arrays → <strong>null</strong><br><br>

Output:<br>
<strong>0</strong> (int default)<br>
<strong>null</strong> (String default)<br>
<strong>false</strong> (boolean default)<br><br>

<strong>IMPORTANT:</strong> This only works for instance/static variables, NOT local variables.<br><br>

<strong>A) is incorrect:</strong> Code compiles fine (static variables have defaults).<br>
<strong>C) is incorrect:</strong> Primitives cannot be null.<br>
<strong>D) is incorrect:</strong> String default is null, not empty string.

## Question

What happens when this code is executed?<br><br>

```java
public class Test {
    public static void main(String[] args) {
        String s = null;
        System.out.println(s.length());
    }
}
```
<br><br>

Please select 1 option<br><br>

A) Prints: 0<br>
B) Prints: null<br>
C) NullPointerException at runtime<br>
D) Compilation error

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

<strong>NullPointerException (NPE)</strong> occurs when you try to access a member (method or field) on a <strong>null reference</strong>.<br><br>

Analysis:<br>
• <strong>s = null</strong> means the reference points to NO object<br>
• Calling <strong>s.length()</strong> attempts to invoke a method on null<br>
• Result: <strong>NullPointerException</strong> at runtime<br><br>

<strong>Key points:</strong><br>
• <strong>null</strong> is a valid value for references<br>
• Using <strong>.</strong> (dot operator) on null → NPE<br>
• Only <strong>reference types</strong> can be null (not primitives)<br><br>

Safe code pattern:<br>

```java
if (s != null) {
    System.out.println(s.length());
}
```
<br>
<strong>Common NPE triggers:</strong><br>
• null.method()<br>
• null.field<br>
• null[index] (array access)<br><br>

<strong>A), B) are incorrect:</strong> Exception is thrown before any print.<br>
<strong>D) is incorrect:</strong> Code compiles fine - null is a valid assignment.

## Question

What is the result of this code?<br><br>

```java
public class Test {
    public static void main(String[] args) {
        int x = 10;
        modify(x);
        System.out.println(x);
    }

    static void modify(int value) {
        value = 20;
    }
}
```
<br><br>

Please select 1 option<br><br>

A) 10<br>
B) 20<br>
C) Compilation error<br>
D) 0

## Réponse

<strong>Réponse correcte :</strong> A)<br><br>

<strong>Java is ALWAYS pass-by-value.</strong><br><br>

For <strong>primitives</strong>, Java copies the <strong>value</strong>:<br><br>

Execution:<br>
1. <strong>x = 10</strong> in main<br>
2. Call <strong>modify(x)</strong><br>
3. Java <strong>copies the value 10</strong> into parameter <strong>value</strong><br>
4. Inside modify: <strong>value = 20</strong> (only affects the copy)<br>
5. Original <strong>x remains 10</strong><br><br>

Output: <strong>10</strong><br><br>

<strong>Critical rule:</strong><br>
• Modifying a <strong>primitive parameter</strong> does NOT affect the original variable<br>
• The parameter is a <strong>copy</strong>, not the original<br><br>

For <strong>reference types</strong>:<br>
• Java copies the <strong>reference</strong> (address)<br>
• Both references point to the <strong>same object</strong><br>
• Modifying the object affects the original<br>
• Reassigning the reference does NOT affect the original<br><br>

<strong>B) is incorrect:</strong> Would require pass-by-reference (Java doesn't have this).<br>
<strong>C) is incorrect:</strong> Code compiles successfully.<br>
<strong>D) is incorrect:</strong> x was never changed from its initial value of 10.

## Question

Which statements about the `final` keyword are correct?<br><br>

Please select all that apply<br><br>

A) A final variable can be reassigned multiple times<br>
B) A final variable must be initialized exactly once<br>
C) final is used to declare constants<br>
D) A final variable can be left uninitialized

## Réponse

<strong>Réponse correcte :</strong> B), C)<br><br>

The <strong>final</strong> keyword prevents reassignment of a variable.<br><br>

<strong>Rules for final variables:</strong><br>
• Must be initialized <strong>exactly once</strong><br>
• <strong>Cannot be reassigned</strong> after initialization<br>
• Commonly used for <strong>constants</strong><br><br>

Example:<br>

```java
final int MAX_SIZE = 100;
MAX_SIZE = 200;  // ❌ Compilation error
```
<br>
<strong>Naming convention:</strong><br>
• Constants: <strong>UPPERCASE_WITH_UNDERSCORES</strong><br>
• Example: <strong>NUMBER_OF_MONTHS</strong>, <strong>MAX_RETRIES</strong><br><br>

<strong>Important distinction:</strong><br>
• <strong>final primitive:</strong> value cannot change<br>
• <strong>final reference:</strong> reference cannot change (but object content can)<br><br>

Example with objects:<br>

```java
final List<String> list = new ArrayList<>();
list.add("item");  // ✅ OK - modifying object content
list = new ArrayList<>();  // ❌ Error - reassigning reference
```
<br>
<strong>A) is incorrect:</strong> final variables can be assigned only ONCE.<br>
<strong>D) is incorrect:</strong> final variables MUST be initialized (either at declaration or in constructor).

## Question

What is the output?<br><br>

```java
public class Test {
    public static void main(String[] args) {
        if (true) {
            int x = 10;
        }
        System.out.println(x);
    }
}
```
<br><br>

Please select 1 option<br><br>

A) 10<br>
B) 0<br>
C) Compilation error<br>
D) Runtime exception

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

<strong>SCOPE RULE:</strong> A variable's scope is limited to the block <strong>{ }</strong> where it's declared.<br><br>

Analysis:<br>
• <strong>x</strong> is declared inside the <strong>if block</strong><br>
• The if block ends at <strong>}</strong><br>
• <strong>x does NOT exist</strong> outside the if block<br>
• Trying to use x outside → <strong>compilation error</strong><br>
• Error: "cannot find symbol - variable x"<br><br>

<strong>Scope concept:</strong><br>
• Variables exist <strong>only within their { } block</strong><br>
• Applies to: if, for, while, methods, classes<br>
• After closing <strong>}</strong>, the variable is destroyed<br><br>

Correct code:<br>

```java
int x;  // Declare outside if
if (true) {
    x = 10;  // Assign inside if
}
System.out.println(x);  // Now accessible
```
<br>
<strong>Common exam trap:</strong> Variable declared in a block is not accessible outside that block.<br><br>

<strong>A) is incorrect:</strong> x is not accessible outside the if block.<br>
<strong>B) is incorrect:</strong> Code doesn't compile (no default value can help here).<br>
<strong>D) is incorrect:</strong> Compilation fails, so code never runs.

## Question

What is the difference between `char` and `String` in Java?<br><br>

Please select 1 option<br><br>

A) char is a primitive storing one character with single quotes; String is an object with double quotes<br>
B) char and String are both primitive types<br>
C) char uses double quotes, String uses single quotes<br>
D) There is no difference, they are interchangeable

## Réponse

<strong>Réponse correcte :</strong> A)<br><br>

<strong>char vs String:</strong><br><br>

<strong>char (primitive type):</strong><br>
• Stores <strong>one character only</strong><br>
• Uses <strong>single quotes</strong> ' '<br>
• Cannot be null<br>
• Default value: <strong>'\u0000'</strong><br><br>

Example:<br>

```java
char c = 'A';         // ✅ OK
char c2 = 'AB';       // ❌ Error - more than one character
char c3 = "A";        // ❌ Error - wrong quotes
```
<br>
<strong>String (reference type / object):</strong><br>
• Stores <strong>zero or more characters</strong><br>
• Uses <strong>double quotes</strong> " "<br>
• Can be null<br>
• Default value: <strong>null</strong><br>
• Is <strong>immutable</strong><br><br>

Example:<br>

```java
String s = "A";       // ✅ OK
String s2 = "Hello";  // ✅ OK
String s3 = "";       // ✅ OK - empty string
String s4 = 'A';      // ❌ Error - wrong quotes
```
<br>
<strong>Key takeaway:</strong> String is NOT a primitive type.<br><br>

<strong>B) is incorrect:</strong> String is an object, not a primitive.<br>
<strong>C) is incorrect:</strong> Quotes are reversed.<br>
<strong>D) is incorrect:</strong> They have different types, syntax, and capabilities.

## Question

What is the result?<br><br>

```java
public class Test {
    public static void main(String[] args) {
        int[] numbers = new int[3];
        System.out.println(numbers[0]);
        System.out.println(numbers[2]);
        System.out.println(numbers[3]);
    }
}
```
<br><br>

Please select 1 option<br><br>

A) 0<br>
0<br>
0<br><br>

B) null<br>
null<br>
null<br><br>

C) 0<br>
0<br>
ArrayIndexOutOfBoundsException<br><br>

D) Compilation error

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

<strong>Array characteristics:</strong><br><br>

<strong>1. Arrays have default values:</strong><br>
• int array → elements initialized to <strong>0</strong><br>
• boolean array → <strong>false</strong><br>
• reference array → <strong>null</strong><br><br>

<strong>2. Array indices:</strong><br>
• Start at <strong>0</strong><br>
• Array of size 3: valid indices are <strong>0, 1, 2</strong><br>
• Accessing index <strong>3</strong> is OUT OF BOUNDS<br><br>

Execution:<br>
• <strong>numbers[0]</strong> → 0 (valid, default value)<br>
• <strong>numbers[2]</strong> → 0 (valid, last element)<br>
• <strong>numbers[3]</strong> → <strong>ArrayIndexOutOfBoundsException</strong> (invalid index)<br><br>

<strong>Array properties:</strong><br>
• Fixed size (cannot change after creation)<br>
• Stored in the <strong>heap</strong><br>
• Index: <strong>0 to length-1</strong><br><br>

Safe access pattern:<br>

```java
if (index >= 0 && index < numbers.length) {
    System.out.println(numbers[index]);
}
```
<br>
<strong>A) is incorrect:</strong> Index 3 doesn't exist in array of size 3.<br>
<strong>B) is incorrect:</strong> int arrays have default value 0, not null.<br>
<strong>D) is incorrect:</strong> Code compiles; error happens at runtime.

## Question

What is the output of the following code?<br><br>

```java
public class Test {
    public static void main(String[] args) {
        String s = "Hello";
        s.concat(" World");
        System.out.println(s);
    }
}
```
<br><br>

Please select 1 option<br><br>

A) Hello World<br>
B) Hello<br>
C) World<br>
D) Compilation error

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>CRITICAL CONCEPT:</strong> Strings are <strong>IMMUTABLE</strong> in Java.<br><br>

<strong>Immutability means:</strong><br>
• String objects <strong>cannot be modified</strong><br>
• Any "modification" creates a <strong>new String object</strong><br>
• The original String remains <strong>unchanged</strong><br><br>

Analysis:<br>
• <strong>s = "Hello"</strong><br>
• <strong>s.concat(" World")</strong> creates a NEW String "Hello World"<br>
• But the result is <strong>NOT assigned</strong> back to s<br>
• <strong>s still points to "Hello"</strong><br><br>

Output: <strong>Hello</strong><br><br>

Correct code to modify:<br>

```java
s = s.concat(" World");  // Assign the result
System.out.println(s);   // Now prints: Hello World
```
<br>
<strong>Why immutability?</strong><br>
• <strong>Thread safety</strong> (shared strings safe across threads)<br>
• <strong>Security</strong> (strings used in security contexts)<br>
• <strong>String pooling</strong> optimization<br><br>

<strong>Common immutable String methods:</strong><br>
• concat(), replace(), substring(), toUpperCase(), toLowerCase(), trim()<br>
• All return <strong>new String objects</strong><br><br>

<strong>A) is incorrect:</strong> Would require assigning the result: s = s.concat(" World");<br>
<strong>C) is incorrect:</strong> Original string is unchanged.<br>
<strong>D) is incorrect:</strong> Code compiles fine.

## Question

Which statements about stack and heap memory are correct?<br><br>

Please select all that apply<br><br>

A) Local variables are stored in the stack<br>
B) Objects are stored in the heap<br>
C) References to objects are stored in the stack<br>
D) Primitives are always stored in the heap

## Réponse

<strong>Réponse correcte :</strong> A), B), C)<br><br>

<strong>Stack vs Heap in Java:</strong><br><br>

<strong>STACK memory:</strong><br>
• <strong>Local variables</strong> (including primitives)<br>
• <strong>References to objects</strong> (not the objects themselves)<br>
• Method call information<br>
• Fast access<br>
• Limited size<br><br>

<strong>HEAP memory:</strong><br>
• <strong>Objects</strong> (instances of classes)<br>
• <strong>Arrays</strong> (arrays are objects)<br>
• <strong>Instance variables</strong> (fields of objects)<br>
• Larger capacity<br>
• Managed by <strong>Garbage Collector</strong><br><br>

Example:<br>

```java
public void method() {
    int x = 10;           // Stack: primitive value
    String s = "Hello";   // Stack: reference 's'
                          // Heap: String object "Hello"

    Person p = new Person();  // Stack: reference 'p'
                              // Heap: Person object
}
```
<br>
<strong>Key distinction:</strong><br>
• <strong>Reference</strong> (address) → stack<br>
• <strong>Object</strong> (actual data) → heap<br><br>

<strong>D) is incorrect:</strong> Local primitives are stored in the stack. Only primitives that are instance variables (fields) are stored in the heap as part of their containing object.

## Question

What is the decimal value of the hexadecimal number `1F`?<br><br>

Please select 1 option<br><br>

A) 15<br>
B) 31<br>
C) 115<br>
D) 21

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>Hexadecimal (base 16) to Decimal (base 10) conversion:</strong><br><br>

Hexadecimal digits:<br>
• 0-9 → 0-9<br>
• A → 10<br>
• B → 11<br>
• C → 12<br>
• D → 13<br>
• E → 14<br>
• F → 15<br><br>

Conversion formula:<br>

```
1F (hex) = (1 × 16¹) + (F × 16⁰)
         = (1 × 16) + (15 × 1)
         = 16 + 15
         = 31 (decimal)
```
<br>
<strong>Number systems (radix/base):</strong><br>
• <strong>Binary:</strong> base 2 (digits: 0-1)<br>
• <strong>Octal:</strong> base 8 (digits: 0-7)<br>
• <strong>Decimal:</strong> base 10 (digits: 0-9)<br>
• <strong>Hexadecimal:</strong> base 16 (digits: 0-9, A-F)<br><br>

<strong>Java hexadecimal literals:</strong><br>

```java
int x = 0x1F;  // Prefix 0x indicates hexadecimal
System.out.println(x);  // Prints: 31
```
<br>
<strong>A) is incorrect:</strong> That's the value of F alone, not 1F.<br>
<strong>C) is incorrect:</strong> Wrong calculation.<br>
<strong>D) is incorrect:</strong> Incorrect conversion formula.

## Question

What happens when this code runs?<br><br>

```java
public class Test {
    public static void main(String[] args) {
        Integer x = null;
        int y = x;
        System.out.println(y);
    }
}
```
<br><br>

Please select 1 option<br><br>

A) Prints: 0<br>
B) Prints: null<br>
C) NullPointerException at runtime<br>
D) Compilation error

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

<strong>AUTOBOXING/UNBOXING TRAP:</strong> Unboxing a null wrapper throws NullPointerException.<br><br>

<strong>What happens:</strong><br><br>

1. <strong>Integer x = null;</strong><br>
   • x is a wrapper object<br>
   • Wrappers CAN be null<br><br>

2. <strong>int y = x;</strong> (unboxing)<br>
   • Java attempts <strong>automatic unboxing</strong><br>
   • Equivalent to: <strong>int y = x.intValue();</strong><br>
   • But x is <strong>null</strong><br>
   • Calling method on null → <strong>NullPointerException</strong><br><br>

<strong>Wrapper classes:</strong><br>
• <strong>byte</strong> → Byte<br>
• <strong>short</strong> → Short<br>
• <strong>int</strong> → Integer<br>
• <strong>long</strong> → Long<br>
• <strong>float</strong> → Float<br>
• <strong>double</strong> → Double<br>
• <strong>char</strong> → Character<br>
• <strong>boolean</strong> → Boolean<br><br>

<strong>Key differences:</strong><br>
• <strong>Primitives:</strong> cannot be null, have default values<br>
• <strong>Wrappers:</strong> can be null, are objects<br><br>

<strong>Common NPE trap:</strong><br>

```java
Integer count = null;
if (count > 0) { }  // NPE! Unboxing null
```
<br>
<strong>A) is incorrect:</strong> Exception thrown before any print.<br>
<strong>B) is incorrect:</strong> Primitives cannot hold null value.<br>
<strong>D) is incorrect:</strong> Code compiles due to autoboxing/unboxing feature.

## Question

Which code is syntactically correct but semantically incorrect?<br><br>

Please select 1 option<br><br>

A) int count = "five";<br>
B) int age = -25;<br>
C) String name = null;<br>
D) double x = 1 / 0;

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>Semantic vs Syntactic correctness:</strong><br><br>

<strong>Syntactic correctness:</strong><br>
• Code follows Java <strong>grammar rules</strong><br>
• Compiles successfully<br>
• Technical validity<br><br>

<strong>Semantic correctness:</strong><br>
• Code makes <strong>logical sense</strong><br>
• Represents real-world meaning correctly<br>
• Business logic validity<br><br>

Analysis:<br><br>

<strong>int age = -25;</strong><br>
• <strong>Syntactically correct:</strong> valid Java syntax, compiles ✅<br>
• <strong>Semantically incorrect:</strong> age cannot be negative ❌<br>
• Violates real-world logic<br><br>

Other examples of semantic errors:<br>

```java
int daysInWeek = 9;           // ❌ Semantically wrong
double temperature = 999999;   // ❌ Unrealistic value
int discount = 150;            // ❌ Discount > 100% doesn't make sense
```
<br>
<strong>Why this matters:</strong><br>
• Compiler only checks <strong>syntax</strong><br>
• You must validate <strong>semantic correctness</strong><br>
• Use validation logic to prevent semantic errors<br><br>

<strong>A) is incorrect:</strong> Syntactically incorrect (type mismatch) - won't compile.<br>
<strong>C) is incorrect:</strong> Both syntactically and semantically correct (null is valid for references).<br>
<strong>D) is incorrect:</strong> Syntactically incorrect - causes ArithmeticException at runtime (or Infinity for double).

## Question

What is the output?<br><br>

```java
public class Test {
    public static void main(String[] args) {
        int result = 10 + 5 * 2;
        System.out.println(result);
    }
}
```
<br><br>

Please select 1 option<br><br>

A) 30<br>
B) 20<br>
C) 25<br>
D) Compilation error

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>Operator precedence</strong> determines evaluation order.<br><br>

<strong>Precedence hierarchy (high to low):</strong><br>
1. <strong>( )</strong> Parentheses<br>
2. <strong>++ --</strong> Increment/Decrement<br>
3. <strong>* / %</strong> Multiplication, Division, Modulus<br>
4. <strong>+ -</strong> Addition, Subtraction<br>
5. <strong>=</strong> Assignment<br><br>

Evaluation:<br>

```
10 + 5 * 2
```
<br>
Step 1: <strong>Multiplication first</strong> (* has higher precedence than +)<br>

```
5 * 2 = 10
```
<br>
Step 2: Then addition<br>

```
10 + 10 = 20
```
<br>
Output: <strong>20</strong><br><br>

<strong>Using parentheses to change order:</strong><br>

```java
int result = (10 + 5) * 2;  // Now: 15 * 2 = 30
```
<br>
<strong>Best practice:</strong> Use parentheses for clarity even when not required.<br><br>

<strong>A) is incorrect:</strong> Would require: (10 + 5) * 2<br>
<strong>C) is incorrect:</strong> Would require different operation.<br>
<strong>D) is incorrect:</strong> Code compiles and runs successfully.
