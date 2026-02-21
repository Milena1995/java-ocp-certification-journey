## Question

What is the output of the following code?<br><br>

```java
int[] nums = new int[3];
System.out.println(nums[0] + " " + nums[1] + " " + nums[2]);
```
<br><br>

Please select 1 option<br><br>

A) null null null<br>
B) 0 0 0<br>
C) Compilation error<br>
D) ArrayIndexOutOfBoundsException

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>ARRAY DEFAULT VALUES:</strong><br>
• <strong>int[]</strong> → default value is <strong>0</strong><br>
• <strong>double[]</strong> → default value is <strong>0.0</strong><br>
• <strong>boolean[]</strong> → default value is <strong>false</strong><br>
• <strong>char[]</strong> → default value is <strong>'\u0000'</strong><br>
• <strong>Object[]</strong> → default value is <strong>null</strong><br><br>

<strong>A) is incorrect:</strong> null is the default for object types, not primitives.<br>
<strong>C) is incorrect:</strong> The code compiles fine.<br>
<strong>D) is incorrect:</strong> Indices 0, 1, 2 are valid for a size-3 array.

## Question

What is the output of the following code?<br><br>

```java
int[] arr = {10, 20, 30};
System.out.println(arr.length);
System.out.println(arr.length());
```
<br><br>

Please select 1 option<br><br>

A) 3 then 3<br>
B) 3 then compilation error<br>
C) Compilation error on both lines<br>
D) 3 then ArrayIndexOutOfBoundsException

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>CRITICAL TRAP:</strong> Arrays have a <strong>field</strong> called <code>length</code>, NOT a method.<br><br>

• <code>arr.length</code> → ✅ valid — prints <strong>3</strong><br>
• <code>arr.length()</code> → ❌ <strong>compilation error</strong> — no such method exists<br><br>

Compare with String:<br>
• <code>str.length()</code> → ✅ String has a <em>method</em> <code>length()</code><br>
• <code>str.length</code> → ❌ no such field<br><br>

Memory tip: <strong>Array = field</strong>, <strong>String = method</strong>.

## Question

What is the output of the following code?<br><br>

```java
String[] words = {"banana", "apple", "cherry"};
java.util.Arrays.sort(words);
System.out.println(java.util.Arrays.toString(words));
```
<br><br>

Please select 1 option<br><br>

A) [banana, apple, cherry]<br>
B) [apple, banana, cherry]<br>
C) [cherry, banana, apple]<br>
D) Compilation error

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>Arrays.sort():</strong> Sorts in-place using <strong>natural ordering</strong> (alphabetical for Strings).<br><br>

• <code>Arrays.sort(arr)</code> → modifies the original array<br>
• <code>Arrays.toString(arr)</code> → returns a readable String like <code>[a, b, c]</code><br><br>

Key facts about <code>Arrays.sort()</code>:<br>
• Primitives → uses <strong>Dual-Pivot QuickSort</strong><br>
• Objects → uses <strong>TimSort</strong> (stable)<br>
• The array is <strong>sorted in-place</strong> — no new array is created<br><br>

<strong>A) is incorrect:</strong> The array is sorted.<br>
<strong>C) is incorrect:</strong> Natural ordering is ascending, not descending.<br>
<strong>D) is incorrect:</strong> The code compiles and runs.

## Question

What is the output of the following code?<br><br>

```java
int[] arr = {1, 3, 5, 7, 9};
int idx = java.util.Arrays.binarySearch(arr, 5);
int notFound = java.util.Arrays.binarySearch(arr, 4);
System.out.println(idx + " " + notFound);
```
<br><br>

Please select 1 option<br><br>

A) 2 -3<br>
B) 2 -2<br>
C) 2 -1<br>
D) -1 -3

## Réponse

<strong>Réponse correcte :</strong> A)<br><br>

<strong>Arrays.binarySearch() rules:</strong><br>
• Array <strong>must be sorted</strong> first<br>
• Found → returns the <strong>index</strong> of the element<br>
• Not found → returns <strong>-(insertion point) - 1</strong><br><br>

Calculation for value <strong>4</strong>:<br>
• 4 would be inserted at index 2 (between 3 and 5)<br>
• Result = -(2) - 1 = <strong>-3</strong><br><br>

<strong>CRITICAL OCP TRAP:</strong> If the array is unsorted, the result is undefined — do NOT call binarySearch on an unsorted array.<br><br>

<strong>B) is incorrect:</strong> The formula is -(insertion point) - 1, not -(insertion point).<br>
<strong>C) is incorrect:</strong> -1 would only occur if insertion point is 0.<br>
<strong>D) is incorrect:</strong> idx = 2 because 5 is at index 2.

## Question

What is the output of the following code?<br><br>

```java
int[] original = {1, 2, 3, 4, 5};
int[] copy = java.util.Arrays.copyOf(original, 3);
int[] extended = java.util.Arrays.copyOf(original, 7);
System.out.println(java.util.Arrays.toString(copy));
System.out.println(java.util.Arrays.toString(extended));
```
<br><br>

Please select 1 option<br><br>

A) [1, 2, 3] and [1, 2, 3, 4, 5, 0, 0]<br>
B) [1, 2, 3] and [1, 2, 3, 4, 5, null, null]<br>
C) [1, 2, 3] and ArrayIndexOutOfBoundsException<br>
D) Compilation error

## Réponse

<strong>Réponse correcte :</strong> A)<br><br>

<strong>Arrays.copyOf(original, newLength):</strong><br>
• If newLength < original.length → <strong>truncates</strong><br>
• If newLength > original.length → <strong>pads with default values</strong> (0 for int)<br><br>

• <code>copyOf(original, 3)</code> → <code>[1, 2, 3]</code><br>
• <code>copyOf(original, 7)</code> → <code>[1, 2, 3, 4, 5, 0, 0]</code><br><br>

Related method:<br>
• <code>Arrays.copyOfRange(arr, from, to)</code> → copies a range (to is exclusive)<br><br>

<strong>B) is incorrect:</strong> null is for Object arrays; int default is 0.<br>
<strong>C) is incorrect:</strong> No exception — padding is handled automatically.<br>
<strong>D) is incorrect:</strong> The code compiles fine.

## Question

What is the output of the following code?<br><br>

```java
int[][] matrix = new int[3][2];
matrix[1][1] = 42;
System.out.println(matrix[0][0]);
System.out.println(matrix[1][1]);
System.out.println(matrix.length);
System.out.println(matrix[0].length);
```
<br><br>

Please select 1 option<br><br>

A) 0 / 42 / 2 / 3<br>
B) 0 / 42 / 3 / 2<br>
C) null / 42 / 3 / 2<br>
D) ArrayIndexOutOfBoundsException

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>2D ARRAYS:</strong><br>
• <code>new int[3][2]</code> → 3 rows, 2 columns<br>
• <code>matrix.length</code> → number of <strong>rows</strong> = <strong>3</strong><br>
• <code>matrix[0].length</code> → number of <strong>columns</strong> = <strong>2</strong><br>
• Default value for int = <strong>0</strong><br><br>

<strong>A) is incorrect:</strong> matrix.length is rows (3), not columns (2).<br>
<strong>C) is incorrect:</strong> int default is 0, not null.<br>
<strong>D) is incorrect:</strong> All accesses are within bounds.

## Question

Which of the following are valid array declarations in Java?<br><br>

Please select 3 options<br><br>

A) <code>int[] arr = new int[5];</code><br>
B) <code>int arr[] = new int[5];</code><br>
C) <code>int[] arr = {1, 2, 3};</code><br>
D) <code>int[] arr = new int[5] {1,2,3,4,5};</code><br>
E) <code>int[] arr; arr = {1, 2, 3};</code>

## Réponse

<strong>Réponse correcte :</strong> A), B), C)<br><br>

<strong>Valid array declarations:</strong><br>
• <code>int[] arr = new int[5];</code> ✅ — standard<br>
• <code>int arr[] = new int[5];</code> ✅ — C-style, valid in Java<br>
• <code>int[] arr = {1, 2, 3};</code> ✅ — array initializer<br><br>

<strong>Invalid:</strong><br>
• <code>new int[5] {1,2,3,4,5}</code> ❌ — cannot specify both size AND initializer<br>
• <code>arr = {1, 2, 3};</code> ❌ — anonymous array initializer only works in declaration context. Use <code>arr = new int[]{1,2,3};</code><br><br>

<strong>D) is incorrect:</strong> You can't specify both length and values in the initializer.<br>
<strong>E) is incorrect:</strong> Array initializer syntax is only valid at declaration; use <code>new int[]{}</code> for assignment.

## Question

What is the output of the following code?<br><br>

```java
String[] a = {"x", "y"};
Object[] b = a;
b[0] = "z";
b[1] = 42;
System.out.println(a[0]);
```
<br><br>

Please select 1 option<br><br>

A) x<br>
B) z<br>
C) ArrayStoreException at runtime when assigning 42<br>
D) Compilation error

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

<strong>ARRAY COVARIANCE TRAP:</strong><br>
• Java allows <code>String[]</code> to be assigned to <code>Object[]</code> — this compiles<br>
• But the array is still a <code>String[]</code> at runtime<br>
• Assigning <code>42</code> (Integer) into a <code>String[]</code> → <strong>ArrayStoreException</strong> at runtime<br><br>

Execution:<br>
• <code>b[0] = "z"</code> → ✅ OK — String is compatible<br>
• <code>b[1] = 42</code> → ❌ <strong>ArrayStoreException</strong> — Integer cannot be stored in String[]<br>
• The print line is never reached<br><br>

<strong>B) is incorrect:</strong> Code crashes before printing.<br>
<strong>D) is incorrect:</strong> Array covariance is allowed at compile time — it's a runtime check.

## Question

Which statements about <code>ArrayList</code> are correct?<br><br>

Please select 3 options<br><br>

A) ArrayList is backed by a dynamic array<br>
B) ArrayList maintains insertion order<br>
C) ArrayList allows duplicate elements<br>
D) ArrayList is synchronized (thread-safe)<br>
E) ArrayList does not allow null values

## Réponse

<strong>Réponse correcte :</strong> A), B), C)<br><br>

<strong>ArrayList characteristics:</strong><br>
• <strong>Backed by a dynamic array</strong> → resizes automatically<br>
• <strong>Maintains insertion order</strong> → elements are retrieved in the order added<br>
• <strong>Allows duplicates</strong> → same value can appear multiple times<br>
• <strong>Allows null</strong> → null is a valid element<br>
• <strong>NOT synchronized</strong> → not thread-safe by default<br><br>

Default initial capacity: <strong>10</strong><br><br>

<strong>D) is incorrect:</strong> ArrayList is not synchronized. Use <code>Collections.synchronizedList()</code> or <code>CopyOnWriteArrayList</code>.<br>
<strong>E) is incorrect:</strong> ArrayList accepts null.

## Question

What is the output of the following code?<br><br>

```java
import java.util.*;
List<String> list = new ArrayList<>(List.of("a", "b", "c"));
list.add("d");
list.remove("b");
list.remove(0);
System.out.println(list);
```
<br><br>

Please select 1 option<br><br>

A) [a, c, d]<br>
B) [c, d]<br>
C) [b, c, d]<br>
D) UnsupportedOperationException

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

Step-by-step:<br>
1. Start: <code>[a, b, c]</code><br>
2. <code>list.add("d")</code> → <code>[a, b, c, d]</code><br>
3. <code>list.remove("b")</code> → removes <strong>by object</strong> → <code>[a, c, d]</code><br>
4. <code>list.remove(0)</code> → removes <strong>by index 0</strong> → removes "a" → <code>[c, d]</code><br><br>

<strong>CRITICAL TRAP:</strong> <code>remove()</code> has two overloads:<br>
• <code>remove(int index)</code> → removes by position<br>
• <code>remove(Object o)</code> → removes by value<br><br>

For <code>List&lt;Integer&gt;</code>: <code>remove(1)</code> removes index 1; <code>remove(Integer.valueOf(1))</code> removes value 1.<br><br>

<strong>D) is incorrect:</strong> The list is created as a mutable <code>ArrayList</code> copy — modifications are allowed.

## Question

What is the output of the following code?<br><br>

```java
import java.util.*;
List<String> immutable = List.of("a", "b", "c");
immutable.add("d");
```
<br><br>

Please select 1 option<br><br>

A) [a, b, c, d]<br>
B) Compilation error<br>
C) UnsupportedOperationException at runtime<br>
D) NullPointerException

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

<strong>List.of() creates an IMMUTABLE list:</strong><br>
• <strong>No add</strong> → UnsupportedOperationException<br>
• <strong>No remove</strong> → UnsupportedOperationException<br>
• <strong>No set</strong> → UnsupportedOperationException<br>
• <strong>No null elements</strong> → NullPointerException<br>
• <strong>Allows duplicates</strong><br><br>

To create a mutable copy: <code>new ArrayList&lt;&gt;(List.of(...))</code><br><br>

Same rules apply to:<br>
• <code>Set.of()</code> — immutable + no duplicates + no null<br>
• <code>Map.of()</code> — immutable + no duplicate keys + no null<br><br>

<strong>B) is incorrect:</strong> The code compiles — the exception is at runtime.

## Question

What happens when you call <code>List.of("a", null, "b")</code>?<br><br>

Please select 1 option<br><br>

A) Returns a list [a, null, b]<br>
B) Compilation error<br>
C) NullPointerException at runtime<br>
D) Returns [a, b] — null is silently ignored

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

<strong>List.of() does NOT allow null elements:</strong><br>
• Passing null → <strong>NullPointerException</strong> at runtime<br><br>

Comparison:<br>
| | null allowed? | duplicates? | mutable? |<br>
|---|---|---|---|<br>
| <code>new ArrayList&lt;&gt;()</code> | ✅ | ✅ | ✅ |<br>
| <code>List.of()</code> | ❌ NPE | ✅ | ❌ UOE |<br>
| <code>Set.of()</code> | ❌ NPE | ❌ IAE | ❌ UOE |<br>
| <code>Map.of()</code> | ❌ NPE | ❌ IAE | ❌ UOE |<br><br>

<strong>D) is incorrect:</strong> null is never silently ignored — it throws immediately.

## Question

What is the output of the following code?<br><br>

```java
import java.util.*;
Set<String> set = new HashSet<>();
set.add("banana");
set.add("apple");
set.add("cherry");
set.add("apple");
System.out.println(set.size());
System.out.println(set.contains("apple"));
```
<br><br>

Please select 1 option<br><br>

A) 4 and true<br>
B) 3 and true<br>
C) 3 and false<br>
D) 2 and true

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>HashSet characteristics:</strong><br>
• <strong>No duplicates</strong> — "apple" added twice, stored once<br>
• <strong>No guaranteed order</strong> — iteration order is unpredictable<br>
• Allows <strong>one null</strong><br>
• <strong>O(1)</strong> for add, remove, contains<br><br>

<code>set.add("apple")</code> the second time returns <strong>false</strong> and doesn't change the set.<br><br>

<strong>A) is incorrect:</strong> Duplicates are ignored, size is 3.<br>
<strong>C) is incorrect:</strong> "apple" is in the set — contains returns true.<br>
<strong>D) is incorrect:</strong> 3 unique elements were added.

## Question

Which Set implementation guarantees the following behaviors?<br><br>

Please select 1 option<br><br>

A) HashSet → insertion order; LinkedHashSet → sorted order; TreeSet → no order<br>
B) HashSet → no order; LinkedHashSet → insertion order; TreeSet → natural sorted order<br>
C) HashSet → sorted order; LinkedHashSet → no order; TreeSet → insertion order<br>
D) All three maintain insertion order

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>Set implementations:</strong><br>

| Implementation | Order | Null? | Performance |<br>
|---|---|---|---|<br>
| <strong>HashSet</strong> | None (unpredictable) | ✅ one null | O(1) |<br>
| <strong>LinkedHashSet</strong> | Insertion order | ✅ one null | O(1) |<br>
| <strong>TreeSet</strong> | Natural sorted order | ❌ NullPointerException | O(log n) |<br><br>

<strong>TreeSet</strong> uses <code>compareTo()</code> — elements must implement <code>Comparable</code> or a <code>Comparator</code> must be provided.<br><br>

<strong>A), C), D) are incorrect:</strong> The order descriptions are all wrong.

## Question

What is the output of the following code?<br><br>

```java
import java.util.*;
TreeSet<String> ts = new TreeSet<>();
ts.add("banana");
ts.add("apple");
ts.add("cherry");
System.out.println(ts.first());
System.out.println(ts.last());
```
<br><br>

Please select 1 option<br><br>

A) banana / cherry<br>
B) apple / cherry<br>
C) cherry / apple<br>
D) Compilation error — TreeSet has no first()/last()

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>TreeSet</strong> stores elements in <strong>natural sorted order</strong> (alphabetical for Strings):<br>
• Sorted: <code>[apple, banana, cherry]</code><br>
• <code>first()</code> → <strong>apple</strong><br>
• <code>last()</code> → <strong>cherry</strong><br><br>

Additional useful <code>TreeSet</code> methods (NavigableSet):<br>
• <code>headSet("banana")</code> → elements strictly before "banana"<br>
• <code>tailSet("banana")</code> → elements from "banana" onwards<br>
• <code>floor("b")</code> → greatest element ≤ "b"<br>
• <code>ceiling("b")</code> → smallest element ≥ "b"<br><br>

<strong>A) is incorrect:</strong> TreeSet is sorted — "apple" comes first.<br>
<strong>D) is incorrect:</strong> <code>first()</code> and <code>last()</code> are defined on <code>SortedSet</code>, which TreeSet implements.

## Question

What is the output of the following code?<br><br>

```java
import java.util.*;
Map<String, Integer> map = new HashMap<>();
map.put("a", 1);
map.put("b", 2);
map.put("a", 99);
System.out.println(map.get("a"));
System.out.println(map.size());
```
<br><br>

Please select 1 option<br><br>

A) 1 and 3<br>
B) 99 and 3<br>
C) 99 and 2<br>
D) NullPointerException

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

<strong>HashMap key rules:</strong><br>
• Keys must be <strong>unique</strong><br>
• Putting a duplicate key <strong>replaces</strong> the value<br>
• <code>put("a", 99)</code> replaces the value 1 with 99<br>
• Size remains <strong>2</strong> (two unique keys: "a" and "b")<br><br>

<code>map.put(key, value)</code> returns the <strong>previous value</strong> (or null if no previous mapping).<br><br>

<strong>A) is incorrect:</strong> The second put replaces the value.<br>
<strong>B) is incorrect:</strong> Duplicate keys don't increase size.<br>
<strong>D) is incorrect:</strong> No null is involved here.

## Question

Which Map method returns a value if the key exists, or inserts and returns a default value if it doesn't?<br><br>

Please select 1 option<br><br>

A) <code>map.get(key)</code><br>
B) <code>map.getOrDefault(key, default)</code><br>
C) <code>map.putIfAbsent(key, value)</code><br>
D) <code>map.computeIfAbsent(key, mappingFunction)</code>

## Réponse

<strong>Réponse correcte :</strong> D) for inserting and returning; B) for returning without inserting<br><br>

<strong>Key Map methods (OCP exam favourite):</strong><br>

| Method | Behaviour |<br>
|---|---|<br>
| <code>get(key)</code> | Returns value or null if absent |<br>
| <code>getOrDefault(key, def)</code> | Returns value or <em>def</em> — does NOT insert |<br>
| <code>putIfAbsent(key, val)</code> | Inserts if absent, returns existing value |<br>
| <code>computeIfAbsent(key, fn)</code> | Inserts fn(key) if absent, returns the value |<br>
| <code>computeIfPresent(key, fn)</code> | Updates value if key exists |<br>
| <code>merge(key, val, fn)</code> | Merges existing value with new one |<br><br>

For the OCP exam, know the difference between <code>getOrDefault</code> (read-only) and <code>computeIfAbsent</code> (insert if absent).

## Question

Which Map implementation maintains insertion order?<br><br>

Please select 1 option<br><br>

A) HashMap<br>
B) TreeMap<br>
C) LinkedHashMap<br>
D) Hashtable

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

<strong>Map implementations:</strong><br>

| Implementation | Order | Null keys? | Null values? | Thread-safe? |<br>
|---|---|---|---|---|<br>
| <strong>HashMap</strong> | None | ✅ one | ✅ | ❌ |<br>
| <strong>LinkedHashMap</strong> | Insertion order | ✅ one | ✅ | ❌ |<br>
| <strong>TreeMap</strong> | Natural sorted (by key) | ❌ NPE | ✅ | ❌ |<br>
| <strong>Hashtable</strong> | None | ❌ NPE | ❌ NPE | ✅ (legacy) |<br><br>

<strong>A) is incorrect:</strong> HashMap order is unpredictable.<br>
<strong>B) is incorrect:</strong> TreeMap sorts by key, not insertion order.<br>
<strong>D) is incorrect:</strong> Hashtable is legacy and doesn't maintain insertion order.

## Question

What is the output of the following code?<br><br>

```java
import java.util.*;
Map<String, Integer> map = new HashMap<>();
map.put("a", 1);
map.put("b", 2);
System.out.println(map.get("c"));
System.out.println(map.getOrDefault("c", 0));
```
<br><br>

Please select 1 option<br><br>

A) NullPointerException on line 1<br>
B) null and 0<br>
C) 0 and 0<br>
D) Compilation error

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

• <code>map.get("c")</code> → key not found → returns <strong>null</strong> (not an exception)<br>
• <code>map.getOrDefault("c", 0)</code> → key not found → returns the default <strong>0</strong><br><br>

<strong>TRAP:</strong> <code>get()</code> returns <code>null</code> for missing keys — this can cause <code>NullPointerException</code> if you auto-unbox the result:<br>

```java
int val = map.get("c"); // NullPointerException! null cannot be unboxed to int
```
<br>

<strong>A) is incorrect:</strong> <code>get()</code> does not throw — it returns null.<br>
<strong>C) is incorrect:</strong> <code>get()</code> returns null, not 0.

## Question

What is the correct behaviour of a <code>PriorityQueue</code>?<br><br>

Please select 2 options<br><br>

A) Elements are retrieved in FIFO (insertion) order<br>
B) Elements are retrieved in natural ordering (smallest first by default)<br>
C) PriorityQueue does not allow null elements<br>
D) PriorityQueue allows null elements<br>
E) peek() removes the head element

## Réponse

<strong>Réponse correcte :</strong> B) et C)<br><br>

<strong>PriorityQueue:</strong><br>
• Implements <code>Queue</code><br>
• Elements retrieved in <strong>natural ordering</strong> (min-heap by default)<br>
• <strong>No null allowed</strong> → NullPointerException<br>
• Does NOT maintain insertion order<br><br>

Key methods:<br>
• <code>offer(e)</code> → add element<br>
• <code>poll()</code> → retrieves AND removes the head (null if empty)<br>
• <code>peek()</code> → retrieves WITHOUT removing (null if empty)<br><br>

Custom ordering: pass a <code>Comparator</code> to the constructor.<br><br>

<strong>A) is incorrect:</strong> PriorityQueue is NOT FIFO — use <code>LinkedList</code> or <code>ArrayDeque</code> for FIFO.<br>
<strong>D) is incorrect:</strong> PriorityQueue throws NPE on null.<br>
<strong>E) is incorrect:</strong> <code>peek()</code> does not remove — <code>poll()</code> does.

## Question

What is the recommended replacement for <code>Stack</code> in modern Java?<br><br>

Please select 1 option<br><br>

A) LinkedList<br>
B) ArrayList<br>
C) ArrayDeque<br>
D) PriorityQueue

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

<strong>Stack is a legacy class</strong> — it extends <code>Vector</code> (synchronized, slow).<br><br>

Modern replacement: <strong>ArrayDeque</strong> as a Deque (double-ended queue)<br>

```java
Deque<String> stack = new ArrayDeque<>();
stack.push("a");   // pushes to front
stack.pop();       // removes from front
stack.peek();      // looks at front
```
<br>

<strong>Deque interface methods:</strong><br>
• <strong>Stack (LIFO):</strong> <code>push()</code>, <code>pop()</code>, <code>peek()</code><br>
• <strong>Queue (FIFO):</strong> <code>offer()</code>/<code>offerLast()</code>, <code>poll()</code>/<code>pollFirst()</code>, <code>peek()</code>/<code>peekFirst()</code><br><br>

<strong>A) is incorrect:</strong> LinkedList implements Deque but is slower than ArrayDeque.<br>
<strong>B) is incorrect:</strong> ArrayList doesn't implement Deque.<br>
<strong>D) is incorrect:</strong> PriorityQueue is a priority-ordered queue, not a stack.

## Question

What is the difference between <code>Comparable</code> and <code>Comparator</code>?<br><br>

Please select 1 option<br><br>

A) Comparable is external; Comparator is built into the class<br>
B) Comparable defines natural ordering inside the class; Comparator defines custom ordering externally<br>
C) Comparable is used for primitives; Comparator is used for objects<br>
D) They are interchangeable — both define the same behaviour

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>Comparable:</strong><br>
• Interface: <code>java.lang.Comparable&lt;T&gt;</code><br>
• Method: <code>int compareTo(T other)</code><br>
• Implemented <strong>inside the class</strong> → defines <strong>natural ordering</strong><br>
• Used by <code>Collections.sort()</code>, <code>TreeSet</code>, <code>TreeMap</code> by default<br><br>

<strong>Comparator:</strong><br>
• Interface: <code>java.util.Comparator&lt;T&gt;</code><br>
• Method: <code>int compare(T o1, T o2)</code><br>
• Implemented <strong>outside the class</strong> → defines <strong>custom ordering</strong><br>
• Passed as argument: <code>list.sort(comparator)</code><br><br>

Return value rules (same for both):<br>
• negative → first is less than second<br>
• 0 → equal<br>
• positive → first is greater than second<br><br>

<strong>A) is incorrect:</strong> The roles are reversed in the answer.<br>
<strong>C) is incorrect:</strong> Both work with objects only (not primitives).

## Question

What is the output of the following code?<br><br>

```java
import java.util.*;
List<String> list = new ArrayList<>(Arrays.asList("banana", "apple", "cherry"));
list.sort(Comparator.naturalOrder());
System.out.println(list);

list.sort(Comparator.reverseOrder());
System.out.println(list);
```
<br><br>

Please select 1 option<br><br>

A) [apple, banana, cherry] then [cherry, banana, apple]<br>
B) [banana, apple, cherry] then [apple, banana, cherry]<br>
C) [apple, banana, cherry] then [apple, banana, cherry]<br>
D) Compilation error

## Réponse

<strong>Réponse correcte :</strong> A)<br><br>

<strong>Comparator factory methods:</strong><br>
• <code>Comparator.naturalOrder()</code> → ascending (A → Z, 1 → 9)<br>
• <code>Comparator.reverseOrder()</code> → descending (Z → A, 9 → 1)<br>
• <code>Comparator.comparing(keyExtractor)</code> → custom field<br>
• <code>Comparator.comparing(...).thenComparing(...)</code> → chained sorting<br><br>

Example chained comparator:<br>

```java
Comparator.comparing(String::length).thenComparing(Comparator.naturalOrder())
```
<br>

<strong>B) is incorrect:</strong> naturalOrder() sorts alphabetically.<br>
<strong>C) is incorrect:</strong> reverseOrder() reverses the list.

## Question

What is the output of the following code?<br><br>

```java
import java.util.*;
List<Integer> list = new ArrayList<>(Arrays.asList(3, 1, 4, 1, 5, 9));
Collections.sort(list);
System.out.println(Collections.min(list));
System.out.println(Collections.frequency(list, 1));
```
<br><br>

Please select 1 option<br><br>

A) 3 and 2<br>
B) 1 and 2<br>
C) 1 and 1<br>
D) 9 and 2

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>Collections utility class methods:</strong><br>
• <code>Collections.sort(list)</code> → sorts in natural order → <code>[1, 1, 3, 4, 5, 9]</code><br>
• <code>Collections.min(list)</code> → returns smallest element → <strong>1</strong><br>
• <code>Collections.max(list)</code> → returns largest element → 9<br>
• <code>Collections.frequency(list, 1)</code> → counts occurrences of 1 → <strong>2</strong><br><br>

Other useful methods:<br>
• <code>Collections.shuffle(list)</code> → random order<br>
• <code>Collections.reverse(list)</code> → reverses<br>
• <code>Collections.nCopies(3, "x")</code> → immutable list [x, x, x]<br>
• <code>Collections.unmodifiableList(list)</code> → unmodifiable view<br><br>

<strong>A) is incorrect:</strong> min is 1, not 3.<br>
<strong>C) is incorrect:</strong> frequency of 1 is 2 (appears twice).<br>
<strong>D) is incorrect:</strong> max is 9 but min is 1.

## Question

What is the difference between <code>Collections.unmodifiableList(list)</code> and <code>List.of()</code>?<br><br>

Please select 2 options<br><br>

A) Both throw UnsupportedOperationException on modification attempts<br>
B) unmodifiableList is a view — changes to the original list are reflected<br>
C) List.of() is a view of the original list<br>
D) Both prevent all mutations regardless of original list changes<br>
E) unmodifiableList prevents direct modification but the underlying list can still change

## Réponse

<strong>Réponse correcte :</strong> B) et E) — qui sont équivalentes et décrivent la même réalité<br><br>

<strong>Key distinction:</strong><br><br>

<code>List.of()</code>:<br>
• Truly <strong>immutable</strong> — the list content never changes<br>
• Independent of any original list<br><br>

<code>Collections.unmodifiableList(original)</code>:<br>
• <strong>Unmodifiable view</strong> of the original list<br>
• You cannot modify through the view (throws UOE)<br>
• But if the <strong>original list</strong> is modified, the view reflects those changes<br><br>

```java
List<String> original = new ArrayList<>(List.of("a", "b"));
List<String> view = Collections.unmodifiableList(original);
original.add("c");
System.out.println(view); // [a, b, c] — view changed!
```
<br>

<strong>C) is incorrect:</strong> List.of() is NOT a view — it's independent.<br>
<strong>D) is incorrect:</strong> unmodifiableList does NOT prevent changes via the original reference.

## Question

What is the output of the following code?<br><br>

```java
import java.util.*;
List<String> list = new ArrayList<>(Arrays.asList("a", "b", "c", "d"));
Iterator<String> it = list.iterator();
while (it.hasNext()) {
    String s = it.next();
    if (s.equals("b")) {
        it.remove();
    }
}
System.out.println(list);
```
<br><br>

Please select 1 option<br><br>

A) [a, b, c, d]<br>
B) [a, c, d]<br>
C) ConcurrentModificationException<br>
D) Compilation error

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>Safe removal during iteration:</strong><br>
• Using <code>it.remove()</code> during iteration is <strong>safe</strong><br>
• It removes the element last returned by <code>next()</code><br><br>

<strong>CRITICAL TRAP:</strong> Never use <code>list.remove()</code> directly inside a <code>for-each</code> loop — that causes <strong>ConcurrentModificationException</strong>:<br>

```java
for (String s : list) {
    if (s.equals("b")) list.remove(s); // ConcurrentModificationException!
}
```
<br>

Safe alternatives:<br>
• <code>Iterator.remove()</code> ✅<br>
• <code>list.removeIf(s -> s.equals("b"))</code> ✅<br>
• Copy the list and remove from original ✅<br><br>

<strong>C) is incorrect:</strong> Using iterator.remove() is explicitly safe.

## Question

What is the output of the following code?<br><br>

```java
import java.util.*;
List<Integer> list = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5));
list.removeIf(n -> n % 2 == 0);
System.out.println(list);
```
<br><br>

Please select 1 option<br><br>

A) [2, 4]<br>
B) [1, 3, 5]<br>
C) [1, 2, 3, 4, 5]<br>
D) ConcurrentModificationException

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>removeIf(Predicate):</strong> Removes all elements that match the predicate.<br><br>

• Predicate: <code>n % 2 == 0</code> → matches even numbers (2, 4)<br>
• Removed: 2, 4<br>
• Remaining: <code>[1, 3, 5]</code><br><br>

This is safe — no ConcurrentModificationException.<br><br>

Other useful functional collection methods:<br>
• <code>list.forEach(System.out::println)</code> → iterate<br>
• <code>list.replaceAll(String::toUpperCase)</code> → transform each element<br>
• <code>map.forEach((k, v) -> ...)</code> → iterate map entries<br><br>

<strong>A) is incorrect:</strong> removeIf removes matching elements, not keeps them.<br>
<strong>C) is incorrect:</strong> The list is mutated.

## Question

What is the output of the following code?<br><br>

```java
import java.util.*;
var list = new ArrayList<String>();
list.add("hello");
list.add("world");
System.out.println(list.getClass().getSimpleName());
System.out.println(list.get(0).toUpperCase());
```
<br><br>

Please select 1 option<br><br>

A) List / HELLO<br>
B) ArrayList / HELLO<br>
C) Object / HELLO<br>
D) Compilation error — var cannot be used with generics

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>var with collections:</strong><br>
• <code>var</code> infers the actual type at compile time → <code>ArrayList&lt;String&gt;</code><br>
• <code>getClass().getSimpleName()</code> returns <code>"ArrayList"</code><br>
• The inferred type is <code>ArrayList&lt;String&gt;</code>, so <code>get(0)</code> returns a <code>String</code> ✅<br><br>

<strong>var key rules:</strong><br>
• Must be initialized in the same statement<br>
• Cannot be used for method parameters, fields, or return types<br>
• The compiler infers the most specific concrete type<br><br>

<strong>A) is incorrect:</strong> var infers <code>ArrayList</code>, not the <code>List</code> interface.<br>
<strong>C) is incorrect:</strong> var is not Object — it's the inferred static type.<br>
<strong>D) is incorrect:</strong> var works perfectly with generics.

## Question

What is the correct Collection hierarchy in Java?<br><br>

Please select 1 option<br><br>

A) Map extends Collection; List, Set, Queue extend Map<br>
B) Collection is the root for List, Set, Queue, and Deque; Map is separate<br>
C) List extends Set; Set extends Queue; Queue extends Collection<br>
D) Iterable, Collection, Map are all the same hierarchy

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>Java Collections hierarchy:</strong><br>

```
Iterable
    └── Collection
            ├── List       (ArrayList, LinkedList, Vector)
            ├── Set        (HashSet, LinkedHashSet, TreeSet)
            └── Queue      (LinkedList, PriorityQueue, ArrayDeque)
                    └── Deque  (ArrayDeque, LinkedList)

Map (SEPARATE — does NOT extend Collection)
    ├── HashMap
    ├── LinkedHashMap
    └── TreeMap
```
<br>

<strong>Key point:</strong> <code>Map</code> is NOT a <code>Collection</code> — it has no <code>add()</code> or <code>iterator()</code>.<br><br>

<strong>A) is incorrect:</strong> Map does not extend Collection.<br>
<strong>C) is incorrect:</strong> List, Set, Queue are siblings — none extends the other.<br>
<strong>D) is incorrect:</strong> Iterable → Collection → List/Set/Queue; Map is completely separate.

## Question

Which of the following correctly describes the performance difference between <code>ArrayList</code> and <code>LinkedList</code>?<br><br>

Please select 2 options<br><br>

A) ArrayList is faster for random access by index<br>
B) LinkedList is faster for random access by index<br>
C) LinkedList is faster for insertions/deletions at the beginning or middle<br>
D) ArrayList is faster for insertions/deletions at the beginning<br>
E) Both have identical performance for all operations

## Réponse

<strong>Réponse correcte :</strong> A) et C)<br><br>

<strong>Performance comparison:</strong><br>

| Operation | ArrayList | LinkedList |<br>
|---|---|---|<br>
| <code>get(index)</code> | <strong>O(1)</strong> ✅ | O(n) ❌ |<br>
| Add at end | O(1) amortized | O(1) |<br>
| Add at beginning/middle | O(n) ❌ | <strong>O(1)</strong> ✅ |<br>
| Memory | Less (array) | More (node + pointers) |<br><br>

<strong>In practice:</strong> ArrayList is preferred in most cases because:<br>
• Better cache locality<br>
• Random access is very common<br>
• Modern CPUs are much faster at array access<br><br>

<strong>B) is incorrect:</strong> LinkedList must traverse from the beginning for any index access.<br>
<strong>D) is incorrect:</strong> Adding at the beginning of ArrayList requires shifting all elements — O(n).<br>
<strong>E) is incorrect:</strong> They have very different performance profiles.

## Question

What is the output of the following code?<br><br>

```java
import java.util.*;
Map<String, List<String>> map = new HashMap<>();
map.computeIfAbsent("fruits", k -> new ArrayList<>()).add("apple");
map.computeIfAbsent("fruits", k -> new ArrayList<>()).add("banana");
System.out.println(map.get("fruits"));
```
<br><br>

Please select 1 option<br><br>

A) [apple]<br>
B) [banana]<br>
C) [apple, banana]<br>
D) NullPointerException

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

<strong>computeIfAbsent(key, mappingFn):</strong><br>
• First call: key "fruits" absent → creates new <code>ArrayList</code> → stores it → returns it → <code>.add("apple")</code><br>
• Second call: key "fruits" <strong>exists</strong> → returns existing list → <code>.add("banana")</code><br>
• Result: the same list now contains both "apple" and "banana"<br><br>

This pattern is the idiomatic way to build <strong>map of lists</strong>:<br>

```java
map.computeIfAbsent(key, k -> new ArrayList<>()).add(value);
```
<br>

<strong>A) is incorrect:</strong> Both elements are added to the same list.<br>
<strong>B) is incorrect:</strong> The first element is not overwritten.<br>
<strong>D) is incorrect:</strong> computeIfAbsent handles the null case.

## Question

What is the output of the following code?<br><br>

```java
import java.util.*;
List<String> list = List.of("a", "b", "c");
List<String> copy = new ArrayList<>(list);
copy.set(0, "z");
System.out.println(list.get(0));
System.out.println(copy.get(0));
```
<br><br>

Please select 1 option<br><br>

A) z and z<br>
B) a and z<br>
C) z and a<br>
D) UnsupportedOperationException

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

• <code>list</code> is immutable (List.of) — it is NOT modified<br>
• <code>copy</code> is a <strong>new independent ArrayList</strong> — changes to it don't affect <code>list</code><br>
• <code>copy.set(0, "z")</code> changes the copy only<br><br>

<strong>Result:</strong><br>
• <code>list.get(0)</code> → <strong>a</strong> (unchanged)<br>
• <code>copy.get(0)</code> → <strong>z</strong><br><br>

<strong>IMPORTANT:</strong> <code>new ArrayList&lt;&gt;(list)</code> creates a <strong>shallow copy</strong> — for a list of objects, the references are shared, but the list structure is independent.<br><br>

<strong>A) is incorrect:</strong> The original immutable list is not modified.<br>
<strong>D) is incorrect:</strong> The exception would occur if you tried to call <code>list.set()</code> — but here you're calling it on <code>copy</code>, which is mutable.
