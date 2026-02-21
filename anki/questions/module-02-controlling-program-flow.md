## Question

What is the output of the following code?<br><br>

```java
int[] nums = {1, 2, 3};
for (int i = 0; i < nums.length; i++);
{
    System.out.println(nums[i]);
}
```
<br><br>

Please select 1 option<br><br>

A) 1<br>
2<br>
3<br>
B) Compilation error: variable i might not have been initialized<br>
C) 3<br>
D) Runtime error: ArrayIndexOutOfBoundsException

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>CRITICAL TRAP:</strong> The semicolon after the for loop terminates it immediately.<br><br>

Code analysis:<br>
• The semicolon <strong>;</strong> after <strong>for(...)</strong> creates an empty loop body<br>
• The loop executes 3 times doing nothing<br>
• After the loop, <strong>i</strong> no longer exists (out of scope)<br>
• The block <strong>{ System.out.println(nums[i]); }</strong> is a separate block<br>
• Variable <strong>i</strong> is not accessible outside the for loop scope<br><br>

Result: <strong>Compilation error</strong><br><br>

<strong>A) is incorrect:</strong> Would require removing the semicolon and using i inside the loop.<br>
<strong>C) is incorrect:</strong> i is not accessible outside the loop.<br>
<strong>D) is incorrect:</strong> Code doesn't compile, so no runtime error occurs.

## Question

Which statements about blocks and variable scope are true?<br><br>

Please select 2 options<br><br>

A) A variable declared in a block is accessible outside that block<br>
B) A variable declared in a for loop initialization is accessible only within the loop<br>
C) Blocks can be nested and inner blocks can access outer block variables<br>
D) Variables with the same name can be declared in the same scope

## Réponse

<strong>Réponse correcte :</strong> B), C)<br><br>

<strong>Scope rules:</strong><br><br>

<strong>B) is correct:</strong><br>
• Variables declared in for loop initialization exist only within the loop<br>
• Example: <strong>for(int i=0; i<5; i++)</strong> - i is not accessible after the loop<br><br>

<strong>C) is correct:</strong><br>
• Inner blocks can access variables from outer blocks<br>
• This is called lexical scoping<br><br>

Example:<br>
```java
{
    int x = 10;
    {
        System.out.println(x); // ✅ accessible
    }
}
```
<br><br>

<strong>A) is incorrect:</strong> Variables declared in a block are NOT accessible outside that block - they are destroyed when the block ends.<br>
<strong>D) is incorrect:</strong> Java does not allow variable shadowing in the same scope - compilation error.

## Question

What is the result of executing this code?<br><br>

```java
int sum = 0;
for (int i = 1; i <= 5; i++) {
    if (i == 3) continue;
    sum += i;
}
System.out.println(sum);
```
<br><br>

Please select 1 option<br><br>

A) 15<br>
B) 12<br>
C) 10<br>
D) Compilation error

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

The code prints <strong>12</strong>.<br><br>

Execution breakdown:<br>
• i=1: sum = 0 + 1 = 1<br>
• i=2: sum = 1 + 2 = 3<br>
• i=3: <strong>continue</strong> skips to next iteration (3 is NOT added)<br>
• i=4: sum = 3 + 4 = 7<br>
• i=5: sum = 7 + 5 = 12<br><br>

<strong>continue</strong> statement skips the rest of the current iteration and moves to the next one.<br><br>

<strong>A) is incorrect:</strong> Would be the result without the continue (1+2+3+4+5=15).<br>
<strong>C) is incorrect:</strong> Incorrect calculation.<br>
<strong>D) is incorrect:</strong> Code compiles successfully.

## Question

Given the following code:<br><br>

```java
List<Integer> numbers = new ArrayList<>();
numbers.add(10);
numbers.add(20);
numbers.add(30);

for (Integer n : numbers) {
    n = n + 5;
}

System.out.println(numbers.get(0));
```
<br><br>

What is printed?<br><br>

Please select 1 option<br><br>

A) 15<br>
B) 10<br>
C) 35<br>
D) Compilation error

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>MAJOR TRAP:</strong> The enhanced for loop variable is a copy.<br><br>

The code prints <strong>10</strong> (original value unchanged).<br><br>

Why?<br>
• In the for-each loop, <strong>n</strong> is a local variable containing a copy of each element<br>
• <strong>n = n + 5</strong> modifies the copy, NOT the original element<br>
• The ArrayList remains unchanged<br>
• Integer is immutable, so reassignment doesn't affect the collection<br><br>

To actually modify the list, you would need:<br>
```java
for (int i = 0; i < numbers.size(); i++) {
    numbers.set(i, numbers.get(i) + 5);
}
```
<br><br>

<strong>A) is incorrect:</strong> Would require modifying the actual list elements.<br>
<strong>C), D) are incorrect:</strong> Code compiles and runs but doesn't modify the list.

## Question

What is the output?<br><br>

```java
int x = 5;
do {
    x--;
    if (x == 3) break;
    System.out.print(x + " ");
} while (x > 0);
```
<br><br>

Please select 1 option<br><br>

A) 4 3 2 1 0<br>
B) 4<br>
C) 4 2 1 0<br>
D) 5 4 3

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

The code prints <strong>4</strong>.<br><br>

Execution trace:<br>
• First iteration: x becomes 4 (5-1), x != 3, prints "4 "<br>
• Second iteration: x becomes 3 (4-1), x == 3, <strong>break</strong> exits the loop<br>
• Loop terminates before printing 3<br><br>

<strong>break</strong> statement immediately exits the loop completely.<br><br>

<strong>A) is incorrect:</strong> break stops the loop at x=3.<br>
<strong>C) is incorrect:</strong> break prevents further iterations.<br>
<strong>D) is incorrect:</strong> x is decremented before first print.

## Question

Which statements about arrays and Collections are correct?<br><br>

Please select all that apply<br><br>

A) Arrays can store primitives, Collections cannot<br>
B) Collections use generics, arrays do not<br>
C) Map extends the Collection interface<br>
D) ArrayList can dynamically resize, arrays cannot

## Réponse

<strong>Réponse correcte :</strong> A), B), D)<br><br>

<strong>A) is correct:</strong><br>
• Arrays: <strong>int[] nums = {1,2,3};</strong> ✅<br>
• Collections: <strong>List<int></strong> is illegal ❌<br>
• Collections require wrapper classes: <strong>List<Integer></strong><br><br>

<strong>B) is correct:</strong><br>
• Collections use generics: <strong>List<T></strong>, <strong>Set<E></strong><br>
• Arrays use type notation: <strong>String[]</strong>, <strong>int[]</strong><br><br>

<strong>D) is correct:</strong><br>
• Arrays: fixed size at creation<br>
• ArrayList: dynamic resizing with <strong>add()</strong>, <strong>remove()</strong><br><br>

<strong>C) is incorrect:</strong> <strong>Map does NOT extend Collection</strong> - this is a common OCP trap. Map is part of the Collections Framework but has a separate hierarchy.

## Question

What happens when this code is compiled and run?<br><br>

```java
Set<String> set = new HashSet<>();
set.add("Apple");
set.add("Banana");
set.add("Apple");

for (String fruit : set) {
    System.out.print(fruit + " ");
}
```
<br><br>

Please select 1 option<br><br>

A) Apple Banana Apple<br>
B) Apple Banana (order guaranteed)<br>
C) Banana Apple or Apple Banana (order not guaranteed, 2 elements)<br>
D) Compilation error

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

<strong>HashSet characteristics:</strong><br><br>

• <strong>No duplicates:</strong> "Apple" is added only once<br>
• <strong>No guaranteed order:</strong> HashSet does not maintain insertion order<br>
• Final set contains: {"Apple", "Banana"}<br><br>

Output could be:<br>
• "Banana Apple "<br>
• OR "Apple Banana "<br><br>

The order is unpredictable and may change between executions.<br><br>

For guaranteed order, use <strong>LinkedHashSet</strong>.<br><br>

<strong>A) is incorrect:</strong> Set eliminates duplicates.<br>
<strong>B) is incorrect:</strong> HashSet does not guarantee order.<br>
<strong>D) is incorrect:</strong> Code compiles successfully.

## Question

Consider this code:<br><br>

```java
int count = 0;
while (count < 3) {
    count++;
}
System.out.println(count);
```
<br><br>

What is the value of count when printed?<br><br>

Please select 1 option<br><br>

A) 2<br>
B) 3<br>
C) 4<br>
D) The loop never terminates

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

The code prints <strong>3</strong>.<br><br>

Loop execution:<br>
• count = 0: condition (0 < 3) is true, count becomes 1<br>
• count = 1: condition (1 < 3) is true, count becomes 2<br>
• count = 2: condition (2 < 3) is true, count becomes 3<br>
• count = 3: condition (3 < 3) is <strong>false</strong>, loop exits<br><br>

The while loop checks the condition <strong>before</strong> each iteration.<br><br>

When the condition becomes false, the loop stops and count retains its last value: <strong>3</strong>.<br><br>

<strong>A) is incorrect:</strong> Loop executes one more time after count=2.<br>
<strong>C) is incorrect:</strong> Loop stops when count reaches 3.<br>
<strong>D) is incorrect:</strong> Loop terminates correctly when count=3.

## Question

What is the result of this code?<br><br>

```java
List<String> list = new ArrayList<>();
list.add("A");
list.add("B");
list.add("C");

for (int i = 0; i <= list.size(); i++) {
    System.out.print(list.get(i) + " ");
}
```
<br><br>

Please select 1 option<br><br>

A) A B C<br>
B) A B C null<br>
C) Runtime exception: IndexOutOfBoundsException<br>
D) Compilation error

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

<strong>CRITICAL TRAP:</strong> The loop condition uses <strong><=</strong> instead of <strong><</strong>.<br><br>

Execution:<br>
• list.size() returns 3<br>
• Loop runs while i <= 3: i = 0, 1, 2, <strong>3</strong><br>
• Valid indices are 0, 1, 2<br>
• When i=3, <strong>list.get(3)</strong> throws <strong>IndexOutOfBoundsException</strong><br><br>

List indices are 0-based:<br>
• First element: index 0<br>
• Last element: index (size - 1)<br><br>

Correct loop condition: <strong>i < list.size()</strong><br><br>

<strong>A) is incorrect:</strong> Exception thrown before completion.<br>
<strong>B) is incorrect:</strong> Lists don't have null at invalid indices, they throw exceptions.<br>
<strong>D) is incorrect:</strong> Code compiles successfully.

## Question

Which loop type guarantees execution at least once?<br><br>

Please select 1 option<br><br>

A) for loop<br>
B) while loop<br>
C) do-while loop<br>
D) enhanced for loop (for-each)

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

The <strong>do-while</strong> loop guarantees at least one execution.<br><br>

Comparison:<br><br>

<strong>while loop:</strong><br>
```java
int x = 10;
while (x < 5) {  // Condition checked FIRST
    System.out.println("Never prints");
}
```
<br><br>

<strong>do-while loop:</strong><br>
```java
int x = 10;
do {
    System.out.println("Prints once");  // Executes FIRST
} while (x < 5);  // Condition checked AFTER
```
<br><br>

Key difference:<br>
• <strong>do-while:</strong> executes body THEN checks condition<br>
• Other loops: check condition THEN execute body<br><br>

<strong>A), B), D) are incorrect:</strong> These loops check the condition before first execution, so they may never execute if the condition is initially false.

## Question

What is the output of this code?<br><br>

```java
int[] numbers = {10, 20, 30, 40};
int i = 0;
for (int num : numbers) {
    if (i++ == 2) {
        System.out.print(num);
        break;
    }
}
```
<br><br>

Please select 1 option<br><br>

A) 30<br>
B) 20<br>
C) 10<br>
D) 40

## Réponse

<strong>Réponse correcte :</strong> A)<br><br>

The code prints <strong>30</strong>.<br><br>

<strong>Execution trace:</strong><br>
• Iteration 1: num=10, i++ evaluates to 0 (then i becomes 1), 0 != 2, continue<br>
• Iteration 2: num=20, i++ evaluates to 1 (then i becomes 2), 1 != 2, continue<br>
• Iteration 3: num=30, i++ evaluates to 2 (then i becomes 3), 2 == 2 ✅<br>
• Prints 30 and breaks<br><br>

<strong>TRAP:</strong> The post-increment <strong>i++</strong> returns the old value BEFORE incrementing.<br><br>

When <strong>i++</strong> is evaluated:<br>
• Returns current value of i<br>
• Then increments i by 1<br><br>

<strong>B), C), D) are incorrect:</strong> The condition becomes true on the third iteration when num=30.

## Question

Given this code:<br><br>

```java
String[] words = {"cat", "dog", "bird"};
for (String word : words) {
    word = word.toUpperCase();
}
System.out.println(words[0]);
```
<br><br>

What is the output?<br><br>

Please select 1 option<br><br>

A) CAT<br>
B) cat<br>
C) Compilation error<br>
D) Runtime exception

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>MAJOR TRAP:</strong> The for-each loop variable is a copy, not a reference to array elements.<br><br>

The code prints <strong>cat</strong> (original unchanged).<br><br>

Why?<br>
• <strong>word</strong> is a local variable that gets a copy of each array element<br>
• <strong>word = word.toUpperCase()</strong> reassigns the local variable<br>
• The original array remains unchanged<br>
• String is immutable - toUpperCase() returns a new String<br><br>

To modify the array, use regular for loop:<br>
```java
for (int i = 0; i < words.length; i++) {
    words[i] = words[i].toUpperCase();
}
```
<br><br>

<strong>A) is incorrect:</strong> Array not modified by for-each loop.<br>
<strong>C), D) are incorrect:</strong> Code compiles and runs successfully.

## Question

What happens when this code executes?<br><br>

```java
for (int i = 0; i < 5; i++) {
    int i = 10;
    System.out.println(i);
}
```
<br><br>

Please select 1 option<br><br>

A) Prints 10 five times<br>
B) Prints 0 1 2 3 4<br>
C) Compilation error: variable i is already defined<br>
D) Runtime exception

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

<strong>Compilation error:</strong> Variable shadowing is not allowed in the same scope.<br><br>

Error analysis:<br>
• <strong>i</strong> is declared in the for loop initialization<br>
• Attempting to declare another <strong>i</strong> inside the loop body<br>
• Java does not permit variable redeclaration in overlapping scopes<br><br>

This would cause error:<br>
<strong>"variable i is already defined in method"</strong><br><br>

Valid alternative (different variable name):<br>
```java
for (int i = 0; i < 5; i++) {
    int j = 10;
    System.out.println(j);
}
```
<br><br>

<strong>A), B) are incorrect:</strong> Code doesn't compile.<br>
<strong>D) is incorrect:</strong> Compilation fails before runtime.

## Question

Which statements about autoboxing are correct?<br><br>

Please select 2 options<br><br>

A) Autoboxing allows storing primitives directly in Collections<br>
B) Integer and int can be used interchangeably due to autoboxing<br>
C) Autoboxing has no performance overhead<br>
D) Autoboxing converts primitive types to their wrapper classes automatically

## Réponse

<strong>Réponse correcte :</strong> B), D)<br><br>

<strong>B) is correct:</strong><br>
```java
List<Integer> list = new ArrayList<>();
list.add(5);  // autoboxing: int → Integer
int x = list.get(0);  // unboxing: Integer → int
```
<br><br>

<strong>D) is correct:</strong><br>
• Autoboxing: primitive → wrapper (int → Integer)<br>
• Unboxing: wrapper → primitive (Integer → int)<br>
• Happens automatically by the compiler<br><br>

<strong>A) is incorrect:</strong> Primitives are NOT stored directly - they are converted to wrapper objects first through autoboxing.<br>
<strong>C) is incorrect:</strong> Autoboxing creates objects, which has performance overhead compared to using primitives directly (memory allocation, garbage collection).

## Question

What is printed by this code?<br><br>

```java
List<Integer> nums = new ArrayList<>();
nums.add(1);
nums.add(2);
nums.add(3);

int sum = 0;
for (int i = 0; i < nums.size(); i++) {
    if (i == 1) continue;
    sum += nums.get(i);
}
System.out.println(sum);
```
<br><br>

Please select 1 option<br><br>

A) 6<br>
B) 4<br>
C) 3<br>
D) 1

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

The code prints <strong>4</strong>.<br><br>

Execution breakdown:<br>
• i=0: sum = 0 + nums.get(0) = 0 + 1 = 1<br>
• i=1: <strong>continue</strong> skips the rest (nums.get(1)=2 is NOT added)<br>
• i=2: sum = 1 + nums.get(2) = 1 + 3 = 4<br><br>

Result: 1 + 3 = <strong>4</strong><br><br>

The <strong>continue</strong> statement skips element at index 1 (value 2).<br><br>

<strong>A) is incorrect:</strong> Would be the result without continue (1+2+3=6).<br>
<strong>C) is incorrect:</strong> Only skips one element, not two.<br>
<strong>D) is incorrect:</strong> Incorrect calculation.
