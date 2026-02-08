## Question

What is the output of the following code?<br><br>

```java
public class Test {
    public static void main(String[] args) {
        String s = "Hello";
        s.toUpperCase();
        s.concat(" World");
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

<strong>STRING IMMUTABILITY TRAP:</strong> String methods return NEW objects - they don't modify the original.<br><br>

Analysis:<br><br>

<strong>String s = "Hello";</strong><br>
• s references "Hello"<br><br>

<strong>s.toUpperCase();</strong><br>
• Creates a <strong>NEW String</strong> "HELLO"<br>
• Returns the new String<br>
• Result is <strong>NOT assigned</strong> to s<br>
• <strong>s remains "Hello"</strong><br><br>

<strong>s.concat(" World");</strong><br>
• Creates a <strong>NEW String</strong> "Hello World"<br>
• Returns the new String<br>
• Result is <strong>NOT assigned</strong> to s<br>
• <strong>s still "Hello"</strong><br><br>

Output: <strong>Hello</strong><br><br>

<strong>KEY PRINCIPLE: Strings are IMMUTABLE</strong><br>
• String objects <strong>cannot be changed</strong> after creation<br>
• All String methods return <strong>new String objects</strong><br>
• The original String remains <strong>unchanged</strong><br><br>

<strong>Correct code to modify:</strong><br>

```java
String s = "Hello";
s = s.toUpperCase();      // Assign result
s = s.concat(" World");   // Assign result
System.out.println(s);    // HELLO WORLD
```

Or chain the operations:<br>

```java
String s = "Hello";
s = s.toUpperCase().concat(" World");
System.out.println(s);    // HELLO WORLD
```
<br>
<strong>Immutable String methods (all return new String):</strong><br>
• toUpperCase(), toLowerCase()<br>
• concat(), replace(), replaceAll()<br>
• substring(), trim(), strip()<br>
• stripLeading(), stripTrailing()<br><br>

<strong>Why Strings are immutable:</strong><br>
• <strong>Thread safety</strong> - can be shared safely across threads<br>
• <strong>Security</strong> - used in security contexts (passwords, file paths)<br>
• <strong>String Pool</strong> optimization - safe to reuse<br>
• <strong>Hashcode caching</strong> - hash won't change<br><br>

<strong>Common exam trap:</strong> Forgetting to assign the result of String methods.<br><br>

<strong>A) is incorrect:</strong> Would require assigning both method results.<br>
<strong>B) is incorrect:</strong> Would require assigning concat() result.<br>
<strong>D) is incorrect:</strong> Code compiles fine.

## Question

What is the output?<br><br>

```java
public class Test {
    public static void main(String[] args) {
        String s = "   Java   ";
        System.out.println(s.length());
        System.out.println(s.trim().length());
        System.out.println(s.length());
    }
}
```
<br><br>

Please select 1 option<br><br>

A) 10<br>
4<br>
4<br><br>

B) 10<br>
4<br>
10<br><br>

C) 4<br>
4<br>
4<br><br>

D) 4<br>
10<br>
10

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>IMMUTABILITY + trim():</strong> trim() returns a new String without modifying the original.<br><br>

Analysis:<br><br>

<strong>String s = "   Java   ";</strong><br>
• s has 3 leading spaces + "Java" (4 chars) + 3 trailing spaces<br>
• Total: <strong>10 characters</strong><br><br>

<strong>s.length()</strong> (first call)<br>
• Returns length of s<br>
• Result: <strong>10</strong><br><br>

<strong>s.trim().length()</strong><br>
• <strong>s.trim()</strong> creates NEW String without leading/trailing spaces<br>
• New String: "Java" (4 characters)<br>
• Returns length of the NEW String<br>
• Result: <strong>4</strong><br>
• <strong>IMPORTANT:</strong> s is NOT modified<br><br>

<strong>s.length()</strong> (second call)<br>
• s still contains original value "   Java   "<br>
• Result: <strong>10</strong><br><br>

Output:<br>
<strong>10</strong><br>
<strong>4</strong><br>
<strong>10</strong><br><br>

<strong>trim() method:</strong><br>
• Removes <strong>leading and trailing</strong> whitespace<br>
• Does <strong>NOT</strong> remove spaces in the middle<br>
• Returns <strong>new String</strong><br>
• Original String <strong>unchanged</strong><br><br>

<strong>Examples:</strong><br>

```java
"  Hello  ".trim()     // "Hello"
"Hello".trim()         // "Hello" (no change needed)
"  ".trim()            // "" (empty string)
"Hello World".trim()   // "Hello World" (middle spaces kept)
```
<br>
<strong>strip() vs trim() (Java 11+):</strong><br>
• <strong>strip()</strong> - Unicode-aware whitespace removal<br>
• <strong>trim()</strong> - removes characters ≤ '\\u0020'<br>
• <strong>stripLeading()</strong> - removes only leading whitespace<br>
• <strong>stripTrailing()</strong> - removes only trailing whitespace<br><br>

<strong>Common use case - validation:</strong><br>

```java
String userInput = "  John  ";
userInput = userInput.trim();  // MUST assign to modify
if (userInput.isEmpty()) {
    // Handle empty input
}
```
<br>
<strong>Typical exam pattern:</strong><br>

```java
String s = "  test  ";
s.trim();              // ❌ Result not assigned
System.out.println(s); // Still "  test  "
```
<br>
<strong>A) is incorrect:</strong> Third call would require s to be modified (but it's not).<br>
<strong>C) is incorrect:</strong> First call returns 10, not 4.<br>
<strong>D) is incorrect:</strong> Order and values are reversed.

## Question

What is the result?<br><br>

```java
public class Test {
    public static void main(String[] args) {
        String s = "Java Programming";
        System.out.println(s.substring(5, 11));
    }
}
```
<br><br>

Please select 1 option<br><br>

A) Progr<br>
B) Program<br>
C)  Progr<br>
D) StringIndexOutOfBoundsException

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

<strong>substring(beginIndex, endIndex):</strong> Extracts from beginIndex (inclusive) to endIndex (exclusive).<br><br>

Analysis:<br><br>

<strong>String s = "Java Programming";</strong><br><br>

Character indices:<br>

```
Index:  0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
Char:   J a v a   P r o g r a  m  m  i  n  g
```
<br>
<strong>s.substring(5, 11)</strong><br>
• Start at index <strong>5</strong> (inclusive) → space ' '<br>
• End at index <strong>11</strong> (exclusive) → 'm'<br>
• Extract indices: 5, 6, 7, 8, 9, 10<br>
• Characters: ' ', 'P', 'r', 'o', 'g', 'r'<br>
• Result: <strong>" Progr"</strong> (with leading space)<br><br>

Output: <strong> Progr</strong> (note the leading space)<br><br>

<strong>substring() rules:</strong><br><br>

<strong>Two-argument version:</strong><br>

```java
substring(int beginIndex, int endIndex)
```

• beginIndex: <strong>inclusive</strong> (included)<br>
• endIndex: <strong>exclusive</strong> (NOT included)<br>
• Length of result: <strong>endIndex - beginIndex</strong><br><br>

<strong>One-argument version:</strong><br>

```java
substring(int beginIndex)
```

• From beginIndex to <strong>end of string</strong><br><br>

<strong>Examples:</strong><br>

```java
String s = "Hello World";

s.substring(0, 5)    // "Hello"
s.substring(6)       // "World"
s.substring(6, 11)   // "World"
s.substring(0, s.length())  // "Hello World" (entire string)
s.substring(3, 3)    // "" (empty string - valid!)
```
<br>
<strong>Edge cases:</strong><br>

```java
s.substring(0, 0)           // "" (empty)
s.substring(5, 5)           // "" (empty)
s.substring(0, s.length())  // Entire string
s.substring(s.length())     // "" (empty)
```
<br>
<strong>Exceptions:</strong><br>

```java
s.substring(-1, 5)     // ❌ StringIndexOutOfBoundsException
s.substring(0, 100)    // ❌ StringIndexOutOfBoundsException
s.substring(5, 2)      // ❌ StringIndexOutOfBoundsException (begin > end)
```
<br>
<strong>Common pattern - extract word:</strong><br>

```java
String email = "user@example.com";
int atIndex = email.indexOf('@');
String username = email.substring(0, atIndex);      // "user"
String domain = email.substring(atIndex + 1);        // "example.com"
```
<br>
<strong>Important:</strong> substring() also returns a NEW String (immutability).<br><br>

<strong>A) is incorrect:</strong> Missing the leading space at index 5.<br>
<strong>B) is incorrect:</strong> Would be substring(5, 12), and still missing leading space.<br>
<strong>D) is incorrect:</strong> Indices are valid (5 and 11 are within bounds).

## Question

What is the output?<br><br>

```java
public class Test {
    public static void main(String[] args) {
        String s = "a,b,c,d";
        String[] arr = s.split(",");
        System.out.println(arr.length);
        System.out.println(arr[0]);
        System.out.println(arr[3]);
    }
}
```
<br><br>

Please select 1 option<br><br>

A) 4<br>
a<br>
d<br><br>

B) 3<br>
a<br>
c<br><br>

C) 4<br>
a,b<br>
d<br><br>

D) 7<br>
a<br>
,

## Réponse

<strong>Réponse correcte :</strong> A)<br><br>

<strong>split()</strong> divides a String into an array based on a delimiter (regex).<br><br>

Analysis:<br><br>

<strong>String s = "a,b,c,d";</strong><br><br>

<strong>String[] arr = s.split(",");</strong><br>
• Splits by comma <strong>","</strong><br>
• Delimiter is a <strong>regular expression</strong><br>
• Creates array of substrings<br>
• Result: <strong>["a", "b", "c", "d"]</strong><br><br>

<strong>arr.length</strong><br>
• Array has <strong>4</strong> elements<br><br>

<strong>arr[0]</strong><br>
• First element: <strong>"a"</strong><br><br>

<strong>arr[3]</strong><br>
• Fourth element (index 3): <strong>"d"</strong><br><br>

Output:<br>
<strong>4</strong><br>
<strong>a</strong><br>
<strong>d</strong><br><br>

<strong>split() method signature:</strong><br>

```java
String[] split(String regex)
```

Takes a <strong>regular expression</strong> as delimiter<br><br>

<strong>Common delimiters:</strong><br>

```java
"a,b,c".split(",")        // ["a", "b", "c"]
"a b c".split(" ")        // ["a", "b", "c"]
"a:b:c".split(":")        // ["a", "b", "c"]
"a|b|c".split("\\|")      // ["a", "b", "c"] - escape | (regex special char)
"a.b.c".split("\\.")      // ["a", "b", "c"] - escape . (regex special char)
```
<br>
<strong>Edge cases:</strong><br>

```java
"".split(",")             // [""] - array with one empty string
"a".split(",")            // ["a"] - no delimiter found
"a,".split(",")           // ["a"] - trailing delimiter ignored
",a".split(",")           // ["", "a"] - leading empty string
"a,,b".split(",")         // ["a", "", "b"] - empty string between
```
<br>
<strong>Splitting by multiple characters:</strong><br>

```java
"a, b, c".split(", ")     // ["a", "b", "c"] - two-char delimiter
"a  b  c".split(" +")     // ["a", "b", "c"] - regex: one or more spaces
"a\tb\tc".split("\\s+")   // ["a", "b", "c"] - regex: any whitespace
```
<br>
<strong>Limit parameter (optional):</strong><br>

```java
"a,b,c,d".split(",", 2)   // ["a", "b,c,d"] - limit to 2 parts
```
<br>
<strong>Common use case - CSV parsing:</strong><br>

```java
String csvLine = "John,Doe,30,Engineer";
String[] fields = csvLine.split(",");
String firstName = fields[0];  // "John"
String lastName = fields[1];   // "Doe"
int age = Integer.parseInt(fields[2]);  // 30
```
<br>
<strong>Common use case - splitting lines:</strong><br>

```java
String text = "Line1\nLine2\nLine3";
String[] lines = text.split("\n");
// OR (more robust for different line endings)
String[] lines = text.split("\\R");  // Java 8+
```
<br>
<strong>Important regex special characters to escape:</strong><br>
• <strong>.</strong> → use <strong>\\.</strong><br>
• <strong>|</strong> → use <strong>\\|</strong><br>
• <strong>*</strong> → use <strong>\\*</strong><br>
• <strong>+</strong> → use <strong>\\+</strong><br>
• <strong>?</strong> → use <strong>\\?</strong><br><br>

<strong>B) is incorrect:</strong> Array has 4 elements, not 3.<br>
<strong>C) is incorrect:</strong> Split removes delimiters, doesn't include them.<br>
<strong>D) is incorrect:</strong> Delimiters are removed, not counted.

## Question

Which statements about String methods are correct?<br><br>

Please select all that apply<br><br>

A) isEmpty() returns true if the String has zero length<br>
B) contains() checks if a String contains a specific substring<br>
C) replace() modifies the original String<br>
D) charAt() returns the character at a specified index

## Réponse

<strong>Réponse correcte :</strong> A), B), D)<br><br>

<strong>String methods review:</strong><br><br>

<strong>A) isEmpty() - CORRECT</strong><br>

```java
boolean isEmpty()
```

Returns <strong>true</strong> if length is 0:<br>

```java
"".isEmpty()         // true
"Hello".isEmpty()    // false
"   ".isEmpty()      // false (contains spaces!)
```
<br>
<strong>Important distinction:</strong><br>

```java
String s = "";
s.isEmpty()          // true (empty string)

String s = null;
s.isEmpty()          // ❌ NullPointerException (null is not empty!)
```
<br>
<strong>Java 11+ alternative:</strong><br>

```java
"   ".isBlank()      // true (whitespace-only is blank)
"".isBlank()         // true (empty is blank)
"Hello".isBlank()    // false
```
<br>
<strong>B) contains() - CORRECT</strong><br>

```java
boolean contains(CharSequence s)
```

Checks if String contains substring:<br>

```java
"Hello World".contains("World")   // true
"Hello World".contains("world")   // false (case-sensitive!)
"Hello World".contains("")        // true (empty string always contained)
"Hello".contains("Hello World")   // false
```
<br>
<strong>Case-insensitive contains:</strong><br>

```java
String s = "Hello World";
s.toLowerCase().contains("world".toLowerCase())  // true
```
<br>
<strong>D) charAt() - CORRECT</strong><br>

```java
char charAt(int index)
```

Returns character at specified index:<br>

```java
String s = "Java";
s.charAt(0)    // 'J'
s.charAt(1)    // 'a'
s.charAt(3)    // 'a'
s.charAt(4)    // ❌ StringIndexOutOfBoundsException
s.charAt(-1)   // ❌ StringIndexOutOfBoundsException
```
<br>
<strong>Common pattern - iterate through String:</strong><br>

```java
String s = "Java";
for (int i = 0; i < s.length(); i++) {
    char c = s.charAt(i);
    System.out.println(c);
}
```
<br>
<strong>C) replace() - INCORRECT</strong><br>

```java
String replace(char oldChar, char newChar)
String replace(CharSequence target, CharSequence replacement)
```

<strong>Does NOT modify</strong> the original String:<br>

```java
String s = "Hello";
s.replace('l', 'L');   // Creates new String "HeLLo"
System.out.println(s); // Still "Hello" - original unchanged!

// Correct usage:
s = s.replace('l', 'L');  // Assign result
System.out.println(s);    // "HeLLo"
```
<br>
<strong>replace() examples:</strong><br>

```java
"Hello".replace('l', 'L')           // "HeLLo"
"Hello".replace("ll", "LL")         // "HeLLo"
"aaa".replace('a', 'b')             // "bbb" (all occurrences)
"Hello World".replace(" ", "")      // "HelloWorld"
```
<br>
<strong>Other useful String methods:</strong><br>

```java
startsWith(String prefix)    // "Hello".startsWith("He") → true
endsWith(String suffix)      // "Hello".endsWith("lo") → true
indexOf(String str)          // "Hello".indexOf("l") → 2
lastIndexOf(String str)      // "Hello".lastIndexOf("l") → 3
toUpperCase()                // "hello" → "HELLO"
toLowerCase()                // "HELLO" → "hello"
```
<br>
<strong>All these methods return NEW values</strong> (immutability principle).<br><br>

<strong>C) is incorrect:</strong> replace() returns a new String, doesn't modify the original.

## Question

What is the output?<br><br>

```java
public class Test {
    public static void main(String[] args) {
        String s = "Java";
        System.out.println(s.startsWith("J"));
        System.out.println(s.endsWith("a"));
        System.out.println(s.contains("av"));
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
false<br><br>

C) true<br>
false<br>
true<br><br>

D) Compilation error

## Réponse

<strong>Réponse correcte :</strong> A)<br><br>

<strong>String checking methods:</strong> startsWith(), endsWith(), contains() - all case-sensitive.<br><br>

Analysis:<br><br>

<strong>String s = "Java";</strong><br><br>

<strong>s.startsWith("J")</strong><br>
• Checks if s begins with "J"<br>
• "Java" starts with "J"<br>
• Result: <strong>true</strong><br><br>

<strong>s.endsWith("a")</strong><br>
• Checks if s ends with "a"<br>
• "Java" ends with "a"<br>
• Result: <strong>true</strong><br><br>

<strong>s.contains("av")</strong><br>
• Checks if s contains "av" anywhere<br>
• "Java" contains "av" (at indices 1-2)<br>
• Result: <strong>true</strong><br><br>

Output:<br>
<strong>true</strong><br>
<strong>true</strong><br>
<strong>true</strong><br><br>

<strong>Method signatures:</strong><br>

```java
boolean startsWith(String prefix)
boolean endsWith(String suffix)
boolean contains(CharSequence s)
```

All return <strong>boolean</strong><br><br>

<strong>Case sensitivity (IMPORTANT):</strong><br>

```java
String s = "Java";

s.startsWith("j")      // false (lowercase j)
s.startsWith("J")      // true

s.endsWith("A")        // false (uppercase A)
s.endsWith("a")        // true

s.contains("JAVA")     // false
s.contains("Java")     // true
```
<br>
<strong>Case-insensitive alternatives:</strong><br>

```java
String s = "Java";

// Convert to lowercase first
s.toLowerCase().startsWith("j")     // true
s.toLowerCase().endsWith("A")       // false (still need to match case)
s.toLowerCase().endsWith("a")       // true
s.toLowerCase().contains("java")    // true
```
<br>
<strong>More examples:</strong><br>

```java
"Hello World".startsWith("Hello")    // true
"Hello World".startsWith("World")    // false
"Hello World".endsWith("World")      // true
"Hello World".endsWith("Hello")      // false
"Hello World".contains("lo Wo")      // true
"Hello World".contains(" ")          // true (space)
"Hello World".contains("")           // true (empty string always)
```
<br>
<strong>startsWith() with offset:</strong><br>

```java
boolean startsWith(String prefix, int offset)
```

Check if string starts with prefix at specific position:<br>

```java
"Java Programming".startsWith("Programming", 5)  // true
// Checks if substring from index 5 starts with "Programming"
```
<br>
<strong>Common use cases:</strong><br><br>

<strong>File extension check:</strong><br>

```java
String filename = "document.pdf";
if (filename.endsWith(".pdf")) {
    // Handle PDF file
}
```
<br>
<strong>URL protocol check:</strong><br>

```java
String url = "https://example.com";
if (url.startsWith("https://")) {
    // Secure connection
}
```
<br>
<strong>Substring search:</strong><br>

```java
String text = "Error: File not found";
if (text.contains("Error")) {
    // Handle error
}
```
<br>
<strong>B) is incorrect:</strong> All checks are true for "Java".<br>
<strong>C) is incorrect:</strong> endsWith("a") is also true.<br>
<strong>D) is incorrect:</strong> Code compiles successfully.

## Question

What is the result?<br><br>

```java
public class Test {
    public static void main(String[] args) {
        String s1 = "Java";
        String s2 = s1.replace('a', 'A');
        String s3 = s2.concat(" Programming");
        System.out.println(s1);
        System.out.println(s2);
        System.out.println(s3);
    }
}
```
<br><br>

Please select 1 option<br><br>

A) Java<br>
Java<br>
Java<br><br>

B) JAvA<br>
JAvA Programming<br>
JAvA Programming<br><br>

C) Java<br>
JAvA<br>
JAvA Programming<br><br>

D) Compilation error

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

<strong>IMMUTABILITY with assignment:</strong> Each method creates a NEW String, assigned to a NEW variable.<br><br>

Analysis:<br><br>

<strong>String s1 = "Java";</strong><br>
• s1 references "Java"<br><br>

<strong>String s2 = s1.replace('a', 'A');</strong><br>
• s1.replace() creates <strong>NEW String</strong> "JAvA"<br>
• Result is <strong>assigned to s2</strong><br>
• s1 remains <strong>"Java"</strong> (unchanged)<br>
• s2 now references <strong>"JAvA"</strong><br><br>

<strong>String s3 = s2.concat(" Programming");</strong><br>
• s2.concat() creates <strong>NEW String</strong> "JAvA Programming"<br>
• Result is <strong>assigned to s3</strong><br>
• s2 remains <strong>"JAvA"</strong> (unchanged)<br>
• s3 now references <strong>"JAvA Programming"</strong><br><br>

Output:<br>
<strong>Java</strong> (s1 unchanged)<br>
<strong>JAvA</strong> (s2 has replaced chars)<br>
<strong>JAvA Programming</strong> (s3 has concatenation)<br><br>

<strong>Key difference from previous examples:</strong><br>
• Here, results ARE assigned to <strong>new variables</strong><br>
• Each variable maintains its own reference<br>
• Original variables never change<br><br>

<strong>Contrast with NOT assigning:</strong><br>

```java
String s1 = "Java";
s1.replace('a', 'A');     // Result NOT assigned
System.out.println(s1);   // Still "Java"
```
<br>
<strong>Contrast with reassigning same variable:</strong><br>

```java
String s = "Java";
s = s.replace('a', 'A');  // Reassign to same variable
System.out.println(s);    // "JAvA"
```
<br>
<strong>Memory visualization:</strong><br>

```
After all operations:

HEAP (String Pool)
  "Java"  ← s1
  "JAvA"  ← s2
  "JAvA Programming"  ← s3

Each variable points to different String object
All objects are immutable
```
<br>
<strong>Method chaining (common pattern):</strong><br>

```java
String result = "  hello  "
    .trim()           // "hello"
    .toUpperCase()    // "HELLO"
    .concat(" WORLD") // "HELLO WORLD"
    .replace('O', '0'); // "HELL0 W0RLD"

System.out.println(result);  // "HELL0 W0RLD"
```
<br>
<strong>Each method in the chain:</strong><br>
• Returns a <strong>new String</strong><br>
• That new String is used by the <strong>next method</strong><br>
• Final result assigned to <strong>result</strong><br><br>

<strong>Important notes:</strong><br>
• String immutability is <strong>FUNDAMENTAL</strong> to Java<br>
• Every String method that "modifies" creates <strong>new object</strong><br>
• You must <strong>use the returned value</strong> (assign or chain)<br>
• Original String is <strong>NEVER changed</strong><br><br>

<strong>A) is incorrect:</strong> s2 and s3 would require methods not being called.<br>
<strong>B) is incorrect:</strong> s1 remains unchanged (immutability).<br>
<strong>D) is incorrect:</strong> Code compiles successfully.

## Question

What happens when this code runs?<br><br>

```java
public class Test {
    public static void main(String[] args) {
        String s = null;
        System.out.println(s.isEmpty());
    }
}
```
<br><br>

Please select 1 option<br><br>

A) Prints: true<br>
B) Prints: false<br>
C) NullPointerException<br>
D) Compilation error

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

<strong>NULL CHECK TRAP:</strong> Calling any method on a null reference throws NullPointerException.<br><br>

Analysis:<br><br>

<strong>String s = null;</strong><br>
• s is a reference that points to <strong>no object</strong><br>
• s is <strong>NOT an empty String</strong><br>
• s is <strong>null</strong><br><br>

<strong>s.isEmpty()</strong><br>
• Attempts to call isEmpty() method on null<br>
• You cannot call methods on null<br>
• ❌ <strong>NullPointerException</strong> at runtime<br><br>

<strong>Critical distinction:</strong><br>

```java
String s = "";           // Empty string (object exists)
s.isEmpty()              // ✅ true (valid call)

String s = null;         // No object
s.isEmpty()              // ❌ NullPointerException
```
<br>
<strong>null vs empty:</strong><br>

```
null        = reference points to NO object
""          = reference points to String object with zero length
"   "       = reference points to String with spaces (not empty!)
```
<br>
<strong>Safe pattern - null check first:</strong><br>

```java
String s = null;

// Unsafe
if (s.isEmpty()) { }  // ❌ NPE

// Safe
if (s != null && s.isEmpty()) { }  // ✅ OK
// Short-circuit: if s is null, s.isEmpty() NOT evaluated
```
<br>
<strong>Common validation pattern:</strong><br>

```java
String input = getUserInput();

// Check both null and empty
if (input == null || input.isEmpty()) {
    System.out.println("Invalid input");
    return;
}

// Safe to use input here
```
<br>
<strong>Java 11+ - isBlank() with null:</strong><br>

```java
String s = null;
s.isBlank()    // ❌ Still NPE! (null check still needed)

String s = "";
s.isBlank()    // ✅ true

String s = "   ";
s.isBlank()    // ✅ true
```
<br>
<strong>Utility methods for null-safe checks:</strong><br>

```java
// Apache Commons Lang
StringUtils.isEmpty(null)       // true (null-safe)
StringUtils.isEmpty("")         // true
StringUtils.isEmpty("  ")       // false (has spaces)

StringUtils.isBlank(null)       // true (null-safe)
StringUtils.isBlank("")         // true
StringUtils.isBlank("  ")       // true (whitespace)
```
<br>
<strong>Java 8+ - Optional pattern:</strong><br>

```java
Optional<String> opt = Optional.ofNullable(getUserInput());
opt.filter(s -> !s.isEmpty())
   .ifPresent(s -> System.out.println("Valid: " + s));
```
<br>
<strong>Why this matters for OCP:</strong><br>
• Common exam trap: null vs empty String<br>
• Must understand when NPE will occur<br>
• Know how to write null-safe code<br><br>

<strong>More NPE scenarios with Strings:</strong><br>

```java
String s = null;
s.length()           // ❌ NPE
s.charAt(0)          // ❌ NPE
s.contains("x")      // ❌ NPE
s.trim()             // ❌ NPE
s.toUpperCase()      // ❌ NPE
```

All method calls on null throw NPE!<br><br>

<strong>A) is incorrect:</strong> null is not empty; exception thrown before any print.<br>
<strong>B) is incorrect:</strong> Exception thrown before any print.<br>
<strong>D) is incorrect:</strong> Code compiles; error occurs at runtime.

## Question

What is the output?<br><br>

```java
public class Test {
    public static void main(String[] args) {
        String s = "Java";
        char[] chars = s.toCharArray();
        chars[0] = 'j';
        System.out.println(s);
        System.out.println(chars[0]);
    }
}
```
<br><br>

Please select 1 option<br><br>

A) java<br>
j<br><br>

B) Java<br>
j<br><br>

C) Java<br>
J<br><br>

D) Compilation error

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>toCharArray() creates a NEW array:</strong> Modifying the array does NOT affect the original String.<br><br>

Analysis:<br><br>

<strong>String s = "Java";</strong><br>
• s references immutable String "Java"<br><br>

<strong>char[] chars = s.toCharArray();</strong><br>
• Creates a <strong>NEW char array</strong>: ['J', 'a', 'v', 'a']<br>
• This is a <strong>copy</strong> of String's characters<br>
• Array is <strong>separate from</strong> the String<br><br>

<strong>chars[0] = 'j';</strong><br>
• Modifies the <strong>array</strong>: ['j', 'a', 'v', 'a']<br>
• Does <strong>NOT affect</strong> the String s<br>
• String s remains <strong>"Java"</strong> (immutable)<br><br>

<strong>System.out.println(s);</strong><br>
• Prints the String: <strong>Java</strong><br><br>

<strong>System.out.println(chars[0]);</strong><br>
• Prints first element of array: <strong>j</strong><br><br>

Output:<br>
<strong>Java</strong><br>
<strong>j</strong><br><br>

<strong>Key principle:</strong><br>
• toCharArray() returns a <strong>COPY</strong>, not a view<br>
• String remains <strong>immutable</strong><br>
• Array is <strong>mutable</strong> and independent<br><br>

<strong>toCharArray() method:</strong><br>

```java
char[] toCharArray()
```

Returns a <strong>new</strong> character array containing String's characters<br><br>

<strong>Common use case - modify characters:</strong><br>

```java
String s = "Hello";
char[] chars = s.toCharArray();

// Modify array
for (int i = 0; i < chars.length; i++) {
    chars[i] = Character.toUpperCase(chars[i]);
}

// Create new String from modified array
String upper = new String(chars);
System.out.println(s);      // "Hello" (unchanged)
System.out.println(upper);  // "HELLO"
```
<br>
<strong>Relationship between String and char[]:</strong><br>

```java
// String → char[]
String s = "Java";
char[] arr = s.toCharArray();  // Creates NEW array

// char[] → String
char[] arr = {'J', 'a', 'v', 'a'};
String s = new String(arr);     // Creates String from array
// OR
String s = String.valueOf(arr); // Alternative
```
<br>
<strong>Why toCharArray() is useful:</strong><br>
• Need to modify individual characters<br>
• Algorithms that work with char arrays<br>
• Performance (arrays faster than String operations in loops)<br><br>

<strong>Alternative - charAt() for reading only:</strong><br>

```java
String s = "Java";
char c = s.charAt(0);  // 'J' - reading only, no array created
```
<br>
<strong>Memory visualization:</strong><br>

```
HEAP
  String object "Java"  ← s (immutable)

  char[] array ['j', 'a', 'v', 'a']  ← chars (mutable, independent)
```
<br>
<strong>Important notes:</strong><br>
• Arrays are <strong>mutable</strong> (can change elements)<br>
• Strings are <strong>immutable</strong> (cannot change)<br>
• toCharArray() creates <strong>independent copy</strong><br>
• Modifying array ≠ modifying String<br><br>

<strong>A) is incorrect:</strong> String s is immutable, remains "Java".<br>
<strong>C) is incorrect:</strong> Array was modified to 'j'.<br>
<strong>D) is incorrect:</strong> Code compiles successfully.

## Question

Which String methods return the same String object if no modification is needed?<br><br>

Please select all that apply<br><br>

A) "Hello".toUpperCase() when the String is already uppercase<br>
B) "Hello".trim() when there is no whitespace to remove<br>
C) "  Hello  ".trim() when whitespace needs to be removed<br>
D) "Hello".replace('x', 'y') when 'x' does not exist in the String

## Réponse

<strong>Réponse correcte :</strong> B), D)<br><br>

<strong>STRING OPTIMIZATION:</strong> Some methods return the SAME object if no change is needed (optimization).<br><br>

Analysis:<br><br>

<strong>B) trim() - returns same if no whitespace to remove</strong><br>

```java
String s = "Hello";
String trimmed = s.trim();
System.out.println(s == trimmed);  // true (same object)
```

• No leading/trailing whitespace<br>
• trim() returns <strong>this</strong> (same object)<br>
• ✅ <strong>Optimization</strong> - avoids creating unnecessary object<br><br>

<strong>D) replace() - returns same if character not found</strong><br>

```java
String s = "Hello";
String replaced = s.replace('x', 'y');
System.out.println(s == replaced);  // true (same object)
```

• 'x' doesn't exist in "Hello"<br>
• replace() returns <strong>this</strong> (same object)<br>
• ✅ <strong>Optimization</strong> - no replacement needed<br><br>

<strong>A) toUpperCase() - ALWAYS creates new object (even if no change)</strong><br>

```java
String s = "HELLO";
String upper = s.toUpperCase();
System.out.println(s == upper);  // false (different objects!)
```

• Even though String is already uppercase<br>
• toUpperCase() still creates <strong>new String</strong><br>
• ❌ <strong>No optimization</strong> for this method<br><br>

<strong>C) trim() - creates new object when modification needed</strong><br>

```java
String s = "  Hello  ";
String trimmed = s.trim();
System.out.println(s == trimmed);  // false (different objects)
```

• Whitespace removed<br>
• trim() creates <strong>new String</strong> "Hello"<br>
• ❌ <strong>Modification needed</strong>, new object created<br><br>

<strong>Methods with optimization (return same if unchanged):</strong><br>

```java
// trim() / strip()
"Hello".trim()                    // Same object
"  Hello  ".trim()                // New object

// replace()
"Hello".replace('x', 'y')         // Same object (no 'x')
"Hello".replace('l', 'L')         // New object (has 'l')

// substring() (special case)
"Hello".substring(0)              // Same object (entire string)
"Hello".substring(0, 5)           // Same object (entire string)
"Hello".substring(1, 3)           // New object (partial string)
```
<br>
<strong>Methods WITHOUT optimization (always create new):</strong><br>

```java
// toUpperCase() / toLowerCase() - ALWAYS new
"HELLO".toUpperCase()             // New object (even though already upper)
"hello".toLowerCase()             // New object (even though already lower)

// concat() - ALWAYS new
"Hello".concat("")                // New object (even with empty string)
```
<br>
<strong>Why some methods optimize and others don't:</strong><br>
• <strong>Implementation detail</strong> in Java<br>
• toUpperCase/toLowerCase would need to check every character first<br>
• More expensive than just creating new object<br>
• trim/replace can quickly check if work is needed<br><br>

<strong>Important for exam:</strong><br>
• Don't rely on == for String comparison (use .equals())<br>
• Understand immutability concept<br>
• Know that optimization exists but is implementation-specific<br><br>

<strong>Best practice:</strong><br>

```java
// Always use .equals() for content comparison
String s1 = "Hello";
String s2 = s1.trim();

// ❌ Bad - depends on optimization
if (s1 == s2) { }

// ✅ Good - compares content
if (s1.equals(s2)) { }
```
<br>
<strong>A) is incorrect:</strong> toUpperCase() always creates new object.<br>
<strong>C) is incorrect:</strong> trim() creates new object when whitespace exists.

## Question

What is the output?<br><br>

```java
public class Test {
    public static void main(String[] args) {
        String s = "a:b:c";
        String[] arr = s.split(":");
        for (String element : arr) {
            System.out.print(element);
        }
    }
}
```
<br><br>

Please select 1 option<br><br>

A) a:b:c<br>
B) abc<br>
C) ["a", "b", "c"]<br>
D) a b c

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>Enhanced for loop</strong> with String array - prints elements without separators.<br><br>

Analysis:<br><br>

<strong>String s = "a:b:c";</strong><br><br>

<strong>String[] arr = s.split(":");</strong><br>
• Splits by colon<br>
• Creates array: <strong>["a", "b", "c"]</strong><br>
• Delimiters (colons) are <strong>removed</strong><br><br>

<strong>for (String element : arr)</strong><br>
• Enhanced for loop (for-each)<br>
• Iterates through array elements<br><br>

<strong>System.out.print(element);</strong><br>
• Prints each element <strong>without newline</strong><br>
• No separator between elements<br><br>

Iteration:<br>
1. element = "a" → print "a"<br>
2. element = "b" → print "b"<br>
3. element = "c" → print "c"<br><br>

Output: <strong>abc</strong> (all on same line, no spaces)<br><br>

<strong>print() vs println():</strong><br>

```java
System.out.print()    // No newline after output
System.out.println()  // Adds newline after output
```
<br>
<strong>If using println instead:</strong><br>

```java
for (String element : arr) {
    System.out.println(element);  // With newline
}
```

Output would be:<br>

```
a
b
c
```
<br>
<strong>Adding separator:</strong><br>

```java
for (int i = 0; i < arr.length; i++) {
    System.out.print(arr[i]);
    if (i < arr.length - 1) {
        System.out.print(" ");  // Add space between elements
    }
}
```

Output: <strong>a b c</strong><br><br>

<strong>Using String.join() (Java 8+):</strong><br>

```java
String result = String.join(" ", arr);  // Join with space
System.out.println(result);  // "a b c"

String result = String.join("", arr);   // Join without separator
System.out.println(result);  // "abc"

String result = String.join("-", arr);  // Join with dash
System.out.println(result);  // "a-b-c"
```
<br>
<strong>Enhanced for loop syntax:</strong><br>

```java
for (Type variable : collection/array) {
    // Use variable
}
```

• <strong>Type:</strong> type of elements<br>
• <strong>variable:</strong> temporary variable for each element<br>
• <strong>collection/array:</strong> what to iterate over<br><br>

<strong>More examples:</strong><br>

```java
String[] words = {"Hello", "World"};

// Enhanced for
for (String word : words) {
    System.out.print(word);  // "HelloWorld"
}

// Traditional for
for (int i = 0; i < words.length; i++) {
    System.out.print(words[i]);  // "HelloWorld"
}
```
<br>
<strong>A) is incorrect:</strong> Delimiters are removed by split().<br>
<strong>C) is incorrect:</strong> Array notation is not printed, only elements.<br>
<strong>D) is incorrect:</strong> No spaces are added between elements.
