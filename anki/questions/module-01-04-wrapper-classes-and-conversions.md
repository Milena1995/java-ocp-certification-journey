## Question

What is the output of the following code?<br><br>

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

A) 0<br>
B) null<br>
C) NullPointerException at runtime<br>
D) Compilation error

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

<strong>CRITICAL UNBOXING TRAP:</strong> Unboxing a null wrapper throws NullPointerException.<br><br>

What happens during unboxing:<br><br>

<strong>int y = x;</strong> is equivalent to:<br>

```java
int y = x.intValue();  // Method call on null!
```
<br>
• <strong>x = null</strong> (wrapper can be null)<br>
• Java attempts <strong>automatic unboxing</strong><br>
• Unboxing calls <strong>intValue()</strong> method<br>
• Calling method on null → <strong>NullPointerException</strong><br><br>

<strong>Wrapper unboxing methods:</strong><br>
• Integer → <strong>intValue()</strong><br>
• Double → <strong>doubleValue()</strong><br>
• Boolean → <strong>booleanValue()</strong><br>
• Character → <strong>charValue()</strong><br><br>

Safe pattern:<br>

```java
if (x != null) {
    int y = x;  // Safe unboxing
}
```
<br>
<strong>Common exam trap:</strong> Always check for null before unboxing wrappers.<br><br>

<strong>A) is incorrect:</strong> Primitives cannot be null, and exception is thrown before assignment.<br>
<strong>B) is incorrect:</strong> Primitives cannot hold null values.<br>
<strong>D) is incorrect:</strong> Code compiles due to autoboxing/unboxing feature.

## Question

Which declarations will compile successfully?<br><br>

Please select all that apply<br><br>

A) List&lt;int&gt; list = new ArrayList&lt;&gt;();<br>
B) List&lt;Integer&gt; list = new ArrayList&lt;&gt;();<br>
C) ArrayList&lt;double&gt; list = new ArrayList&lt;&gt;();<br>
D) Set&lt;Boolean&gt; set = new HashSet&lt;&gt;();

## Réponse

<strong>Réponse correcte :</strong> B), D)<br><br>

<strong>CRITICAL RULE:</strong> Collections can ONLY hold objects, not primitives.<br><br>

<strong>Why collections need objects:</strong><br>
• Collections store <strong>references</strong><br>
• Primitives are <strong>not objects</strong><br>
• Primitives have <strong>no references</strong><br>
• Solution: use <strong>wrapper classes</strong><br><br>

<strong>Valid declarations:</strong><br>

```java
List<Integer> intList;      // ✅ Integer is a wrapper
List<Double> doubleList;    // ✅ Double is a wrapper
Set<Boolean> boolSet;       // ✅ Boolean is a wrapper
Map<String, Long> map;      // ✅ All objects
```
<br>
<strong>Invalid declarations:</strong><br>

```java
List<int> list;      // ❌ int is primitive
Set<double> set;     // ❌ double is primitive
Map<char, float> m;  // ❌ Both primitives
```
<br>
<strong>The 8 wrapper classes:</strong><br>
• byte → <strong>Byte</strong><br>
• short → <strong>Short</strong><br>
• int → <strong>Integer</strong><br>
• long → <strong>Long</strong><br>
• float → <strong>Float</strong><br>
• double → <strong>Double</strong><br>
• char → <strong>Character</strong><br>
• boolean → <strong>Boolean</strong><br><br>

<strong>Autoboxing makes it convenient:</strong><br>

```java
List<Integer> list = new ArrayList<>();
list.add(10);  // Autoboxing: int → Integer
```
<br>
<strong>A), C) are incorrect:</strong> int and double are primitives, not allowed in generics.

## Question

What is the output?<br><br>

```java
public class Test {
    public static void main(String[] args) {
        Integer a = Integer.valueOf(100);
        Integer b = Integer.valueOf(100);
        Integer c = Integer.valueOf(200);
        Integer d = Integer.valueOf(200);

        System.out.println(a == b);
        System.out.println(c == d);
    }
}
```
<br><br>

Please select 1 option<br><br>

A) true<br>
true<br><br>

B) false<br>
false<br><br>

C) true<br>
false<br><br>

D) false<br>
true

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

<strong>INTEGER CACHE TRAP:</strong> Java caches Integer objects from <strong>-128 to 127</strong>.<br><br>

How Integer.valueOf() works:<br><br>

<strong>For values -128 to 127:</strong><br>
• Returns <strong>cached objects</strong><br>
• Same object reused<br>
• <strong>== returns true</strong><br><br>

<strong>For values outside range:</strong><br>
• Creates <strong>new objects</strong><br>
• Different references<br>
• <strong>== returns false</strong><br><br>

Execution:<br>

```java
Integer a = Integer.valueOf(100);  // Cached
Integer b = Integer.valueOf(100);  // Same cached object
a == b  // true (same reference)

Integer c = Integer.valueOf(200);  // New object
Integer d = Integer.valueOf(200);  // Another new object
c == d  // false (different references)
```
<br>
Output:<br>
<strong>true</strong><br>
<strong>false</strong><br><br>

<strong>Why the cache exists:</strong><br>
• Small integers used frequently<br>
• Memory optimization<br>
• Performance improvement<br><br>

<strong>Best practice:</strong> ALWAYS use <strong>.equals()</strong> to compare wrapper objects:<br>

```java
a.equals(b)  // true (compares values)
c.equals(d)  // true (compares values)
```
<br>
<strong>Common exam trap:</strong> == with wrappers compares references, not values.<br><br>

<strong>A) is incorrect:</strong> 200 is outside cache range.<br>
<strong>B) is incorrect:</strong> 100 is within cache range.<br>
<strong>D) is incorrect:</strong> Cache behavior is reversed.

## Question

What is the result of the following conversions?<br><br>

```java
public class Test {
    public static void main(String[] args) {
        String s1 = "123";
        int x = Integer.parseInt(s1);
        Integer y = Integer.valueOf(s1);

        System.out.println(x instanceof Integer);
        System.out.println(y instanceof Integer);
    }
}
```
<br><br>

Please select 1 option<br><br>

A) true<br>
true<br><br>

B) false<br>
false<br><br>

C) Compilation error<br><br>

D) false<br>
true

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

<strong>CRITICAL ERROR:</strong> Cannot use instanceof with primitive types.<br><br>

Compilation error at:<br>

```java
System.out.println(x instanceof Integer);
```
<br>
Error: "Inconvertible types; cannot cast 'int' to 'Integer'"<br><br>

<strong>Why it fails:</strong><br>
• <strong>x</strong> is a <strong>primitive int</strong> (from parseInt)<br>
• <strong>instanceof</strong> only works with <strong>reference types</strong><br>
• Primitives are <strong>not objects</strong>, have no type hierarchy<br><br>

<strong>String to number conversions:</strong><br><br>

<strong>Integer.parseInt(String):</strong><br>
• Returns <strong>primitive int</strong><br>
• Fast, no object creation<br>

```java
int x = Integer.parseInt("123");  // x = 123 (primitive)
```
<br>
<strong>Integer.valueOf(String):</strong><br>
• Returns <strong>Integer object</strong><br>
• Uses cache when possible<br>

```java
Integer y = Integer.valueOf("123");  // y = Integer object
```
<br>
<strong>Number to String conversions:</strong><br>

```java
String.valueOf(123)    // "123"
Integer.toString(123)  // "123"
123 + ""               // "123" (concatenation)
```
<br>
<strong>Correct code:</strong><br>

```java
Integer boxed = Integer.valueOf(x);
System.out.println(boxed instanceof Integer);  // true
```
<br>
<strong>A), B), D) are incorrect:</strong> Code doesn't compile, so there's no output.

## Question

What is the output?<br><br>

```java
public class Test {
    public static void main(String[] args) {
        Integer a = 10;
        Integer b = 10;
        Integer c = new Integer(10);

        System.out.println(a == b);
        System.out.println(a == c);
        System.out.println(a.equals(c));
    }
}
```
<br><br>

Please select 1 option<br><br>

A) true<br>
true<br>
true<br><br>

B) true<br>
false<br>
true<br><br>

C) false<br>
false<br>
true<br><br>

D) true<br>
true<br>
false

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>REFERENCE vs VALUE comparison trap.</strong><br><br>

Analysis:<br><br>

<strong>Integer a = 10;</strong> (autoboxing)<br>
• Equivalent to: <strong>Integer.valueOf(10)</strong><br>
• Returns <strong>cached object</strong> (10 is in -128 to 127 range)<br><br>

<strong>Integer b = 10;</strong> (autoboxing)<br>
• Also returns the <strong>same cached object</strong><br>
• a and b reference the <strong>same object</strong><br><br>

<strong>Integer c = new Integer(10);</strong><br>
• Explicitly creates a <strong>NEW object</strong><br>
• Bypasses the cache<br>
• Different reference from a and b<br><br>

Results:<br><br>

<strong>a == b</strong> → <strong>true</strong><br>
• Same cached object<br>
• Same reference<br><br>

<strong>a == c</strong> → <strong>false</strong><br>
• Different objects<br>
• Different references<br>
• new Integer() always creates new object<br><br>

<strong>a.equals(c)</strong> → <strong>true</strong><br>
• .equals() compares <strong>values</strong>, not references<br>
• Both contain value 10<br><br>

<strong>Key takeaway:</strong><br>
• <strong>==</strong> compares references for objects<br>
• <strong>.equals()</strong> compares values (content)<br>
• <strong>new Integer()</strong> bypasses cache (deprecated in modern Java)<br><br>

<strong>Note:</strong> new Integer() is deprecated since Java 9. Use Integer.valueOf() instead.<br><br>

<strong>A) is incorrect:</strong> new Integer() creates a different object.<br>
<strong>C) is incorrect:</strong> a and b reference the same cached object.<br>
<strong>D) is incorrect:</strong> equals() compares values, both are 10.

## Question

Where are the following stored in memory?<br><br>

```java
String s1 = "Java";
String s2 = new String("Java");
Integer x = 100;
```
<br><br>

Please select 1 option<br><br>

A) s1: String Pool, s2: Heap, x: Stack<br>
B) s1: String Pool, s2: Heap, x: Heap<br>
C) All in Heap<br>
D) All in String Pool

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>Java memory organization:</strong><br><br>

<strong>STACK:</strong><br>
• Local variables (references)<br>
• Method call information<br>
• Fast, limited size<br><br>

<strong>HEAP:</strong><br>
• <strong>ALL objects</strong> (including String, Integer, arrays)<br>
• Instance variables<br>
• Larger capacity<br>
• Garbage collected<br><br>

<strong>String Pool (inside Heap):</strong><br>
• Special area within the heap<br>
• Stores <strong>String literals</strong><br>
• Enables string reuse<br><br>

Analysis:<br><br>

<strong>String s1 = "Java";</strong><br>
• "Java" is a <strong>string literal</strong><br>
• Stored in <strong>String Pool</strong> (which is in Heap)<br>
• Reference s1 is in Stack<br><br>

<strong>String s2 = new String("Java");</strong><br>
• <strong>new</strong> keyword creates object in <strong>Heap</strong> (not String Pool)<br>
• "Java" literal also goes to String Pool<br>
• Actually creates <strong>2 objects</strong> if "Java" wasn't already pooled<br>
• Reference s2 is in Stack<br><br>

<strong>Integer x = 100;</strong><br>
• Autoboxing creates <strong>Integer object</strong><br>
• All objects are in <strong>Heap</strong><br>
• Uses cached object (100 is in -128 to 127 range)<br>
• Reference x is in Stack<br><br>

<strong>Important clarification:</strong><br>
• String Pool is <strong>NOT outside</strong> the heap<br>
• String Pool is a <strong>special region within</strong> the heap<br><br>

Memory diagram:<br>

```
STACK           HEAP
-----           ----
s1 ─────────> String Pool: "Java"
s2 ─────────> Heap object: "Java"
x  ─────────> Integer cache: 100
```
<br>
<strong>A) is incorrect:</strong> Integer objects are in Heap, not Stack (only the reference x is in Stack).<br>
<strong>C) is incorrect:</strong> Doesn't distinguish String Pool from regular heap.<br>
<strong>D) is incorrect:</strong> String Pool is only for String literals, not Integer objects.

## Question

What is the output?<br><br>

```java
public class Test {
    public static void main(String[] args) {
        String s1 = "Java";
        String s2 = "Java";
        String s3 = new String("Java");

        System.out.println(s1 == s2);
        System.out.println(s1 == s3);
        System.out.println(s1.equals(s3));
    }
}
```
<br><br>

Please select 1 option<br><br>

A) true<br>
true<br>
true<br><br>

B) false<br>
false<br>
true<br><br>

C) true<br>
false<br>
true<br><br>

D) false<br>
true<br>
false

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

<strong>String literal vs new String() comparison.</strong><br><br>

Analysis:<br><br>

<strong>String s1 = "Java";</strong><br>
• Literal goes to <strong>String Pool</strong><br><br>

<strong>String s2 = "Java";</strong><br>
• Same literal<br>
• Java <strong>reuses</strong> the object from String Pool<br>
• s1 and s2 reference the <strong>same object</strong><br><br>

<strong>String s3 = new String("Java");</strong><br>
• <strong>new</strong> keyword forces creation of <strong>new object</strong> in heap<br>
• Creates object <strong>outside String Pool</strong><br>
• Different reference from s1 and s2<br><br>

Results:<br><br>

<strong>s1 == s2</strong> → <strong>true</strong><br>
• Both reference the same String Pool object<br>
• Same reference<br><br>

<strong>s1 == s3</strong> → <strong>false</strong><br>
• s1: String Pool object<br>
• s3: new heap object<br>
• Different references<br><br>

<strong>s1.equals(s3)</strong> → <strong>true</strong><br>
• .equals() compares <strong>content</strong>, not references<br>
• Both contain "Java"<br><br>

<strong>Why String Pool exists:</strong><br>
• Strings are used <strong>very frequently</strong><br>
• Reduces memory usage (reuse identical strings)<br>
• Improves performance<br><br>

<strong>String Pool behavior:</strong><br>

```java
String a = "Hello";
String b = "Hello";     // Reuses a's object
a == b                  // true

String c = new String("Hello");  // New object
a == c                  // false
a.equals(c)             // true
```
<br>
<strong>Best practice:</strong> Always use <strong>.equals()</strong> to compare String content.<br><br>

<strong>A) is incorrect:</strong> new String() creates a different object.<br>
<strong>B) is incorrect:</strong> String literals are pooled and reused.<br>
<strong>D) is incorrect:</strong> Both statements are reversed.

## Question

Which statements about String, StringBuilder, and StringBuffer are correct?<br><br>

Please select all that apply<br><br>

A) String is immutable and thread-safe<br>
B) StringBuilder is mutable and thread-safe<br>
C) StringBuffer is mutable and thread-safe<br>
D) StringBuilder is faster than StringBuffer

## Réponse

<strong>Réponse correcte :</strong> A), C), D)<br><br>

<strong>String vs StringBuilder vs StringBuffer:</strong><br><br>

<strong>String:</strong><br>
• <strong>Immutable</strong> (cannot be modified)<br>
• <strong>Thread-safe</strong> (immutability guarantees safety)<br>
• Every modification creates <strong>new object</strong><br>
• Slow for many concatenations<br>
• Stored in String Pool (literals)<br><br>

<strong>StringBuilder:</strong><br>
• <strong>Mutable</strong> (can be modified)<br>
• <strong>NOT thread-safe</strong> (no synchronization)<br>
• <strong>Fastest</strong> for string manipulation<br>
• Best for single-threaded scenarios<br><br>

<strong>StringBuffer:</strong><br>
• <strong>Mutable</strong> (can be modified)<br>
• <strong>Thread-safe</strong> (synchronized methods)<br>
• Slower than StringBuilder (synchronization overhead)<br>
• Use only when thread safety is needed<br><br>

Comparison table:<br>

```
              Immutable  Thread-safe  Performance
String        ✅         ✅           Slow (concat)
StringBuilder ❌         ❌           Fast
StringBuffer  ❌         ✅           Medium
```
<br>
<strong>When to use each:</strong><br><br>

<strong>String:</strong><br>
• Few modifications<br>
• String literals<br>
• Thread safety needed<br><br>

<strong>StringBuilder:</strong><br>
• Many modifications<br>
• Single-threaded context<br>
• Performance critical<br><br>

<strong>StringBuffer:</strong><br>
• Many modifications<br>
• Multi-threaded context<br>
• Thread safety required<br><br>

Example:<br>

```java
// Slow - creates many objects
String s = "";
for (int i = 0; i < 1000; i++) {
    s += i;  // 1000 new String objects!
}

// Fast - modifies same object
StringBuilder sb = new StringBuilder();
for (int i = 0; i < 1000; i++) {
    sb.append(i);  // Modifies sb
}
```
<br>
<strong>B) is incorrect:</strong> StringBuilder is NOT thread-safe (that's StringBuffer).

## Question

What is the output?<br><br>

```java
public class Test {
    public static void main(String[] args) {
        String s = "Hello";
        s.concat(" World");
        s.toUpperCase();
        System.out.println(s);
    }
}
```
<br><br>

Please select 1 option<br><br>

A) HELLO WORLD<br>
B) Hello World<br>
C) Hello<br>
D) Compilation error

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

<strong>STRING IMMUTABILITY TRAP:</strong> String methods return NEW objects, don't modify the original.<br><br>

Analysis:<br><br>

<strong>String s = "Hello";</strong><br>
• s references "Hello" in String Pool<br><br>

<strong>s.concat(" World");</strong><br>
• Creates a <strong>NEW String</strong> "Hello World"<br>
• Returns the new String<br>
• Result is <strong>NOT assigned</strong> to s<br>
• Original s <strong>remains unchanged</strong><br><br>

<strong>s.toUpperCase();</strong><br>
• Creates a <strong>NEW String</strong> "HELLO"<br>
• Returns the new String<br>
• Result is <strong>NOT assigned</strong> to s<br>
• Original s <strong>still unchanged</strong><br><br>

Output: <strong>Hello</strong><br><br>

<strong>Why Strings are immutable:</strong><br>
• <strong>Thread safety</strong> - shared strings safe across threads<br>
• <strong>Security</strong> - strings used in security contexts cannot be altered<br>
• <strong>String Pool</strong> optimization - safe to reuse<br>
• <strong>Hashcode caching</strong> - can cache since value won't change<br><br>

<strong>Correct code:</strong><br>

```java
String s = "Hello";
s = s.concat(" World");  // Assign result
s = s.toUpperCase();     // Assign result
System.out.println(s);   // HELLO WORLD
```
<br>
<strong>Immutable String methods (all return new String):</strong><br>
• concat(), replace(), substring(), trim()<br>
• toUpperCase(), toLowerCase()<br>
• strip(), stripLeading(), stripTrailing()<br><br>

<strong>Common exam trap:</strong> Forgetting to assign the result of String methods.<br><br>

<strong>A) is incorrect:</strong> Would require assigning both method results.<br>
<strong>B) is incorrect:</strong> Would require assigning concat() result.<br>
<strong>D) is incorrect:</strong> Code compiles fine (just doesn't do what might be expected).

## Question

What is the result?<br><br>

```java
public class Test {
    public static void main(String[] args) {
        StringBuilder sb = new StringBuilder("Java");
        StringBuffer sbf = new StringBuffer("Java");

        sb.append(" 21");
        sbf.append(" 21");

        System.out.println(sb);
        System.out.println(sbf);
    }
}
```
<br><br>

Please select 1 option<br><br>

A) Java<br>
Java<br><br>

B) Java 21<br>
Java 21<br><br>

C) Compilation error<br><br>

D) Java 21<br>
Java

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>StringBuilder and StringBuffer are MUTABLE</strong> - they modify the original object.<br><br>

Analysis:<br><br>

<strong>StringBuilder sb = new StringBuilder("Java");</strong><br>
• Creates mutable StringBuilder with "Java"<br><br>

<strong>StringBuffer sbf = new StringBuffer("Java");</strong><br>
• Creates mutable StringBuffer with "Java"<br><br>

<strong>sb.append(" 21");</strong><br>
• <strong>Modifies</strong> the original StringBuilder object<br>
• sb now contains "Java 21"<br>
• Returns reference to <strong>same object</strong> (for chaining)<br><br>

<strong>sbf.append(" 21");</strong><br>
• <strong>Modifies</strong> the original StringBuffer object<br>
• sbf now contains "Java 21"<br>
• Returns reference to <strong>same object</strong><br><br>

Output:<br>
<strong>Java 21</strong><br>
<strong>Java 21</strong><br><br>

<strong>Key difference from String:</strong><br>

```java
// String (immutable)
String s = "Java";
s.concat(" 21");     // Creates NEW object, s unchanged
System.out.println(s);  // "Java"

// StringBuilder (mutable)
StringBuilder sb = new StringBuilder("Java");
sb.append(" 21");    // MODIFIES same object
System.out.println(sb);  // "Java 21"
```
<br>
<strong>StringBuilder/StringBuffer common methods:</strong><br>
• <strong>append()</strong> - add to end<br>
• <strong>insert()</strong> - add at position<br>
• <strong>delete()</strong> - remove characters<br>
• <strong>reverse()</strong> - reverse content<br>
• <strong>replace()</strong> - replace range<br><br>

All these methods <strong>modify the object</strong> and return <strong>this</strong> for method chaining:<br>

```java
sb.append("A").append("B").append("C");  // Chaining works
```
<br>
<strong>A) is incorrect:</strong> Both StringBuilder and StringBuffer are mutable and modify the original.<br>
<strong>C) is incorrect:</strong> Code compiles successfully.<br>
<strong>D) is incorrect:</strong> Both classes behave the same way (both mutable).

## Question

Which statements correctly describe autoboxing and unboxing?<br><br>

Please select all that apply<br><br>

A) Autoboxing converts a primitive to its wrapper<br>
B) Unboxing converts a wrapper to its primitive<br>
C) Autoboxing happens automatically in assignments and method calls<br>
D) Unboxing never throws exceptions

## Réponse

<strong>Réponse correcte :</strong> A), B), C)<br><br>

<strong>Autoboxing and Unboxing</strong> are automatic conversions between primitives and wrappers.<br><br>

<strong>AUTOBOXING (primitive → wrapper):</strong><br>

```java
Integer x = 10;  // Autoboxing: int → Integer
```

Equivalent to:<br>

```java
Integer x = Integer.valueOf(10);
```
<br>
<strong>UNBOXING (wrapper → primitive):</strong><br>

```java
Integer x = 100;
int y = x;  // Unboxing: Integer → int
```

Equivalent to:<br>

```java
int y = x.intValue();
```
<br>
<strong>Automatic contexts:</strong><br><br>

1. <strong>Assignment:</strong><br>

```java
Integer x = 5;        // Autoboxing
int y = x;            // Unboxing
```
<br>
2. <strong>Method arguments:</strong><br>

```java
void method(Integer x) { }
method(10);  // Autoboxing

void method2(int x) { }
Integer val = 10;
method2(val);  // Unboxing
```
<br>
3. <strong>Collections:</strong><br>

```java
List<Integer> list = new ArrayList<>();
list.add(5);         // Autoboxing
int x = list.get(0); // Unboxing
```
<br>
4. <strong>Operators:</strong><br>

```java
Integer a = 10;
Integer b = 20;
int sum = a + b;  // Both unboxed, then added
```
<br>
<strong>CRITICAL EXCEPTION CASE:</strong><br>

```java
Integer x = null;
int y = x;  // ❌ NullPointerException!
```

Unboxing calls intValue() on null → NPE<br><br>

<strong>Performance consideration:</strong><br>
• Autoboxing/unboxing has overhead<br>
• Creates objects (memory cost)<br>
• In tight loops, prefer primitives<br><br>

<strong>D) is incorrect:</strong> Unboxing a null wrapper throws NullPointerException.

## Question

What is the output?<br><br>

```java
public class Test {
    public static void main(String[] args) {
        Integer a = 127;
        Integer b = 127;
        Integer c = 128;
        Integer d = 128;

        System.out.println(a.equals(b));
        System.out.println(c.equals(d));
    }
}
```
<br><br>

Please select 1 option<br><br>

A) true<br>
true<br><br>

B) false<br>
false<br><br>

C) true<br>
false<br><br>

D) false<br>
true

## Réponse

<strong>Réponse correcte :</strong> A)<br><br>

<strong>.equals() compares VALUES, not references.</strong><br><br>

Analysis:<br><br>

<strong>a.equals(b):</strong><br>
• a = 127 (Integer object)<br>
• b = 127 (Integer object)<br>
• .equals() compares the <strong>numeric values</strong><br>
• Both contain 127<br>
• Result: <strong>true</strong><br><br>

<strong>c.equals(d):</strong><br>
• c = 128 (Integer object)<br>
• d = 128 (Integer object)<br>
• .equals() compares the <strong>numeric values</strong><br>
• Both contain 128<br>
• Result: <strong>true</strong><br><br>

Output:<br>
<strong>true</strong><br>
<strong>true</strong><br><br>

<strong>Important distinction:</strong><br><br>

<strong>== (reference comparison):</strong><br>

```java
Integer a = 127;
Integer b = 127;
Integer c = 128;
Integer d = 128;

a == b  // true (cached objects, same reference)
c == d  // false (different objects, different references)
```
<br>
<strong>.equals() (value comparison):</strong><br>

```java
a.equals(b)  // true (same value: 127)
c.equals(d)  // true (same value: 128)
```
<br>
<strong>Integer cache affects ==, NOT .equals()</strong><br><br>

<strong>Wrapper .equals() implementation:</strong><br>

```java
public boolean equals(Object obj) {
    if (obj instanceof Integer) {
        return value == ((Integer)obj).intValue();
    }
    return false;
}
```

Compares the primitive values, regardless of caching.<br><br>

<strong>Best practice for wrappers:</strong><br>
• <strong>==</strong> → unpredictable (depends on cache)<br>
• <strong>.equals()</strong> → reliable (compares values)<br>
• <strong>Always use .equals()</strong> for wrapper comparison<br><br>

<strong>B), C), D) are incorrect:</strong> .equals() compares values, both pairs have equal values.

## Question

What happens when you create a String using `new` keyword?<br><br>

```java
String s = new String("Java");
```
<br><br>

Please select 1 option<br><br>

A) Creates one object in String Pool<br>
B) Creates one object in Heap outside String Pool<br>
C) May create two objects: one in String Pool, one in Heap<br>
D) Creates objects only in Stack

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

<strong>new String() can create TWO objects:</strong><br><br>

When you write:<br>

```java
String s = new String("Java");
```
<br>
Java may create <strong>up to 2 objects</strong>:<br><br>

<strong>1. String literal "Java":</strong><br>
• The literal <strong>"Java"</strong> goes to <strong>String Pool</strong><br>
• If "Java" already exists in pool, reuses it<br>
• If not, creates it in String Pool<br><br>

<strong>2. new String() object:</strong><br>
• <strong>new</strong> keyword creates object in <strong>Heap</strong> (outside String Pool)<br>
• This object is <strong>always created</strong><br>
• References the String Pool literal<br><br>

Memory diagram:<br>

```
STACK           HEAP
-----           ----
s  ──────────> new String object (Heap)
                    │
                    └─> "Java" (String Pool)
```
<br>
<strong>Why this matters:</strong><br>

```java
String s1 = "Java";              // String Pool
String s2 = new String("Java");  // Heap + String Pool

s1 == s2  // false (different references)
s1.equals(s2)  // true (same content)
```
<br>
<strong>Optimization with intern():</strong><br>

```java
String s2 = new String("Java").intern();
s1 == s2  // true (intern returns String Pool reference)
```
<br>
<strong>Why avoid new String():</strong><br>
• Creates unnecessary objects<br>
• Wastes memory<br>
• Slower performance<br>
• Bypasses String Pool optimization<br><br>

<strong>Deprecated since Java 9:</strong><br>
• Constructor String(String) is deprecated<br>
• Use string literals instead<br><br>

<strong>Best practice:</strong> Use string literals, not new String()<br>

```java
String s = "Java";  // ✅ Good - uses String Pool
String s = new String("Java");  // ❌ Bad - wastes memory
```
<br>
<strong>A) is incorrect:</strong> new keyword creates object in Heap, not just String Pool.<br>
<strong>B) is incorrect:</strong> The literal "Java" may also create an object in String Pool.<br>
<strong>D) is incorrect:</strong> Strings are objects, always stored in Heap (references in Stack).

## Question

Why is String thread-safe in Java?<br><br>

Please select 1 option<br><br>

A) Because it uses synchronized methods<br>
B) Because it is stored in String Pool<br>
C) Because it is immutable<br>
D) Because it is final class

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

<strong>Immutability guarantees thread safety.</strong><br><br>

<strong>Why String is thread-safe:</strong><br><br>

<strong>Immutability:</strong><br>
• String objects <strong>cannot be modified</strong> after creation<br>
• No setter methods<br>
• All fields are <strong>private final</strong><br>
• Methods like concat(), replace() return <strong>new objects</strong><br><br>

<strong>Thread safety consequence:</strong><br>
• Multiple threads can <strong>safely share</strong> the same String<br>
• No risk of one thread modifying it while another reads it<br>
• <strong>No synchronization needed</strong><br>
• No race conditions possible<br><br>

Example:<br>

```java
String s = "Java";

// Thread 1
String s1 = s.concat(" SE");  // Creates NEW object

// Thread 2
String s2 = s.toUpperCase();  // Creates NEW object

// Original s is UNCHANGED - both threads safe
```
<br>
<strong>Contrast with mutable classes:</strong><br>

```java
// StringBuilder is NOT thread-safe (mutable)
StringBuilder sb = new StringBuilder("Java");

// Thread 1
sb.append(" SE");  // Modifies object

// Thread 2
sb.append(" 21");  // Modifies same object
// ❌ Race condition possible!
```
<br>
<strong>Thread-safe alternatives for string building:</strong><br>
• <strong>StringBuffer</strong> - mutable + synchronized (thread-safe)<br>
• <strong>StringBuilder</strong> - mutable, no synchronization (NOT thread-safe)<br><br>

<strong>Benefits of immutability:</strong><br>
1. <strong>Thread safety</strong> (no synchronization needed)<br>
2. <strong>Security</strong> (strings in security contexts safe)<br>
3. <strong>Hashcode caching</strong> (hash won't change)<br>
4. <strong>String Pool</strong> optimization (safe to reuse)<br><br>

<strong>General rule:</strong><br>
• <strong>Immutable objects</strong> are automatically thread-safe<br>
• <strong>Mutable objects</strong> need synchronization for thread safety<br><br>

<strong>A) is incorrect:</strong> String doesn't use synchronized methods - immutability makes them unnecessary.<br>
<strong>B) is incorrect:</strong> String Pool is a memory optimization, not the reason for thread safety.<br>
<strong>D) is incorrect:</strong> Being final prevents subclassing but doesn't directly cause thread safety; immutability does.
