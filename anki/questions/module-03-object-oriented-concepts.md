## Question

Which statements about method overloading are correct?<br><br>

Please select all that apply<br><br>

A) Overloaded methods must have different return types<br>
B) Overloaded methods must have different parameter lists<br>
C) Overloaded methods can have different access modifiers<br>
D) Overloaded methods must be in the same class

## Réponse

<strong>Réponse correcte :</strong> B), C)<br><br>

<strong>B) is correct:</strong><br>
• Method overloading requires different parameter lists (different number or types)<br>
• This is part of the method signature<br>
• Example: <strong>calculate(int a)</strong> and <strong>calculate(int a, int b)</strong><br><br>

<strong>C) is correct:</strong><br>
• Overloaded methods can have different access modifiers<br>
• Example: <strong>public void process()</strong> and <strong>private void process(int x)</strong><br><br>

<strong>A) is incorrect:</strong> Return type alone is NOT sufficient for overloading - methods with same parameters but different return types cause compilation error.<br>
<strong>D) is incorrect:</strong> Overloaded methods can exist across inheritance hierarchy (parent and child classes can both have overloaded versions).

## Question

What happens when this code is compiled?<br><br>

```java
public class Calculator {
    public int add(int a, int b) {
        return a + b;
    }
    
    public double add(int a, int b) {
        return a + b + 0.0;
    }
}
```
<br><br>

Please select 1 option<br><br>

A) Code compiles successfully<br>
B) Compilation error: method add(int,int) is already defined<br>
C) Runtime exception when calling add()<br>
D) Code compiles but cannot be instantiated

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>Compilation error:</strong> Return type is NOT part of the method signature.<br><br>

Method signature consists of:<br>
• Method name<br>
• Parameter types and order<br>
• Number of parameters<br><br>

<strong>Return type is NOT included</strong> in the signature.<br><br>

Both methods have identical signatures:<br>
• Name: <strong>add</strong><br>
• Parameters: <strong>(int, int)</strong><br><br>

The compiler cannot distinguish between them based solely on return type.<br><br>

Error message:<br>
<strong>"method add(int,int) is already defined in class Calculator"</strong><br><br>

<strong>A) is incorrect:</strong> Code fails compilation.<br>
<strong>C), D) are incorrect:</strong> Error occurs at compile time, not runtime.

## Question

Given this class:<br><br>

```java
public class Account {
    private double balance;
    
    public void setBalance(double balance) {
        balance = balance;
    }
    
    public double getBalance() {
        return balance;
    }
}

Account acc = new Account();
acc.setBalance(100.0);
System.out.println(acc.getBalance());
```
<br><br>

What is printed?<br><br>

Please select 1 option<br><br>

A) 100.0<br>
B) 0.0<br>
C) null<br>
D) Compilation error

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>MAJOR TRAP:</strong> Missing <strong>this</strong> keyword in setter.<br><br>

The code prints <strong>0.0</strong> (default value unchanged).<br><br>

Problem in setBalance():<br>
• <strong>balance = balance;</strong> assigns parameter to itself<br>
• Instance variable is never modified<br>
• Instance variable retains default value: <strong>0.0</strong><br><br>

Correct implementation:<br>
```java
public void setBalance(double balance) {
    this.balance = balance;  // ✅
}
```
<br><br>

<strong>this.balance</strong> refers to instance variable<br>
<strong>balance</strong> refers to method parameter<br><br>

<strong>A) is incorrect:</strong> Requires proper use of this keyword.<br>
<strong>C) is incorrect:</strong> Primitive double defaults to 0.0, not null.<br>
<strong>D) is incorrect:</strong> Code compiles successfully but has logical error.

## Question

Which access modifier allows a field to be accessed only within the same class?<br><br>

Please select 1 option<br><br>

A) public<br>
B) protected<br>
C) default (no modifier)<br>
D) private

## Réponse

<strong>Réponse correcte :</strong> D)<br><br>

<strong>private</strong> is the most restrictive access modifier.<br><br>

Access levels from most to least restrictive:<br><br>

<strong>private:</strong><br>
• Accessible only within the same class<br>
• Not visible to subclasses or other classes<br>
• Used for encapsulation<br><br>

<strong>default (package-private):</strong><br>
• Accessible within the same package<br><br>

<strong>protected:</strong><br>
• Accessible within same package AND subclasses<br><br>

<strong>public:</strong><br>
• Accessible from anywhere<br><br>

Example:<br>
```java
public class Account {
    private double balance;  // Only accessible in Account class
}
```
<br><br>

<strong>A) is incorrect:</strong> public allows access from anywhere.<br>
<strong>B) is incorrect:</strong> protected allows access from subclasses and same package.<br>
<strong>C) is incorrect:</strong> default allows access from same package.

## Question

What is the result of compiling and running this code?<br><br>

```java
public class Counter {
    private int count = 0;
    
    public void increment() {
        int count = 10;
        count++;
    }
    
    public int getCount() {
        return count;
    }
}

Counter c = new Counter();
c.increment();
c.increment();
System.out.println(c.getCount());
```
<br><br>

Please select 1 option<br><br>

A) 2<br>
B) 0<br>
C) 20<br>
D) 22

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>CRITICAL TRAP:</strong> Local variable shadows instance variable.<br><br>

The code prints <strong>0</strong>.<br><br>

Problem analysis:<br>
• In <strong>increment()</strong>, local variable <strong>count</strong> is declared<br>
• This shadows the instance variable <strong>count</strong><br>
• <strong>count++</strong> increments the local variable (from 10 to 11)<br>
• Instance variable remains at <strong>0</strong><br>
• Local variable is destroyed when method ends<br><br>

Correct implementation:<br>
```java
public void increment() {
    this.count++;  // ✅ Increments instance variable
}
```
<br>
or simply:<br>
```java
public void increment() {
    count++;  // ✅ No shadowing, increments instance variable
}
```
<br><br>

<strong>A) is incorrect:</strong> Would require modifying instance variable.<br>
<strong>C), D) are incorrect:</strong> Local variable modifications don't affect instance variable.

## Question

Which statements about encapsulation are true?<br><br>

Please select 2 options<br><br>

A) Encapsulation means making all fields public<br>
B) Encapsulation protects the internal state of an object<br>
C) Getters and setters are commonly used to implement encapsulation<br>
D) Encapsulation requires all methods to be private

## Réponse

<strong>Réponse correcte :</strong> B), C)<br><br>

<strong>B) is correct:</strong><br>
• Encapsulation hides internal implementation details<br>
• Prevents direct access to internal state<br>
• Protects data integrity<br><br>

<strong>C) is correct:</strong><br>
• Private fields + public getters/setters = encapsulation<br>
• Controlled access to data<br>
• Can add validation in setters<br><br>

Example:<br>
```java
public class Account {
    private double balance;  // Encapsulated
    
    public double getBalance() {
        return balance;
    }
    
    public void setBalance(double balance) {
        if (balance >= 0) {  // Validation
            this.balance = balance;
        }
    }
}
```
<br><br>

<strong>A) is incorrect:</strong> Encapsulation uses PRIVATE fields, not public.<br>
<strong>D) is incorrect:</strong> Methods providing controlled access should be public, not private.

## Question

Which method declarations are valid overloads of <strong>process(int x)</strong>?<br><br>

Please select all that apply<br><br>

A) public void process(int y)<br>
B) public void process(double x)<br>
C) public int process(int x, int y)<br>
D) private void process(int x)

## Réponse

<strong>Réponse correcte :</strong> B), C)<br><br>

<strong>B) is correct:</strong><br>
• Different parameter type: <strong>double</strong> instead of <strong>int</strong><br>
• Valid overload<br><br>

<strong>C) is correct:</strong><br>
• Different number of parameters: 2 instead of 1<br>
• Valid overload<br>
• Return type can also differ<br><br>

Method signature components:<br>
• Method name<br>
• Number of parameters<br>
• Type of parameters<br>
• Order of parameters<br><br>

<strong>NOT part of signature:</strong><br>
• Parameter names<br>
• Return type<br>
• Access modifiers<br><br>

<strong>A) is incorrect:</strong> Parameter name doesn't matter - same signature as original (int).<br>
<strong>D) is incorrect:</strong> Access modifier doesn't matter - same signature as original, compilation error.

## Question

What happens when this code runs?<br><br>

```java
public class Student {
    private String name;
    
    public void setName(String n) {
        this.name = n;
    }
    
    public void printName() {
        String name = "Anonymous";
        System.out.println(name);
        System.out.println(this.name);
    }
}

Student s = new Student();
s.setName("Alice");
s.printName();
```
<br><br>

Please select 1 option<br><br>

A) Alice<br>
Alice<br><br>

B) Anonymous<br>
Alice<br><br>

C) Anonymous<br>
Anonymous<br><br>

D) Compilation error

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

Output:<br>
Anonymous<br>
Alice<br><br>

Explanation:<br>
• <strong>printName()</strong> declares local variable <strong>name</strong><br>
• Local variable shadows instance variable<br>
• First <strong>println(name)</strong>: prints local variable "Anonymous"<br>
• Second <strong>println(this.name)</strong>: prints instance variable "Alice"<br><br>

Scope rules:<br>
• Local variable has priority in its scope<br>
• <strong>this</strong> keyword accesses instance variable explicitly<br>
• Instance variable set by <strong>setName("Alice")</strong> remains intact<br><br>

<strong>A) is incorrect:</strong> First println uses shadowing local variable.<br>
<strong>C) is incorrect:</strong> this.name accesses instance variable, which is "Alice".<br>
<strong>D) is incorrect:</strong> Code compiles successfully.

## Question

What is the result of compiling this code?<br><br>

```java
public class Calculator {
    public int calculate(int a, int b) {
        return a + b;
    }
    
    public int calculate(int x, int y) {
        return x * y;
    }
}
```
<br><br>

Please select 1 option<br><br>

A) Code compiles successfully<br>
B) Compilation error: method calculate(int,int) is already defined<br>
C) Code compiles but throws exception at runtime<br>
D) Compilation error: duplicate method

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>Compilation error:</strong> Both methods have identical signatures.<br><br>

Method signature comparison:<br><br>

First method:<br>
• Name: <strong>calculate</strong><br>
• Parameters: <strong>(int, int)</strong><br><br>

Second method:<br>
• Name: <strong>calculate</strong><br>
• Parameters: <strong>(int, int)</strong><br><br>

<strong>CRITICAL:</strong> Parameter names (a, b vs x, y) are NOT part of the signature.<br><br>

The signatures are identical:<br>
<strong>calculate(int, int)</strong><br><br>

Error: <strong>"method calculate(int,int) is already defined in class Calculator"</strong><br><br>

For valid overloading, need different:<br>
• Number of parameters, OR<br>
• Types of parameters, OR<br>
• Order of parameter types<br><br>

<strong>A) is incorrect:</strong> Duplicate signature causes compilation error.<br>
<strong>C), D) are incorrect:</strong> Error occurs at compile time with specific message about duplicate method.

## Question

Which code correctly demonstrates encapsulation?<br><br>

Please select 1 option<br><br>

A) public class Person {<br>
&nbsp;&nbsp;&nbsp;&nbsp;public String name;<br>
}<br><br>

B) public class Person {<br>
&nbsp;&nbsp;&nbsp;&nbsp;private String name;<br>
&nbsp;&nbsp;&nbsp;&nbsp;public String getName() { return name; }<br>
&nbsp;&nbsp;&nbsp;&nbsp;public void setName(String name) { this.name = name; }<br>
}<br><br>

C) public class Person {<br>
&nbsp;&nbsp;&nbsp;&nbsp;private String name;<br>
}<br><br>

D) public class Person {<br>
&nbsp;&nbsp;&nbsp;&nbsp;String name;<br>
&nbsp;&nbsp;&nbsp;&nbsp;public String getName() { return name; }<br>
}

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>Proper encapsulation requires:</strong><br>
• Private fields<br>
• Public getter/setter methods for controlled access<br><br>

Option B demonstrates:<br>
• <strong>private String name;</strong> - field is hidden<br>
• <strong>public getName()</strong> - controlled read access<br>
• <strong>public setName()</strong> - controlled write access<br><br>

Benefits:<br>
• Internal state is protected<br>
• Can add validation in setters<br>
• Can change internal implementation without breaking clients<br>
• Follows JavaBeans convention<br><br>

Example with validation:<br>
```java
public void setName(String name) {
    if (name != null && !name.isEmpty()) {
        this.name = name;
    }
}
```
<br><br>

<strong>A) is incorrect:</strong> Public field violates encapsulation - direct access allowed.<br>
<strong>C) is incorrect:</strong> No way to access the field - too restrictive to be useful.<br>
<strong>D) is incorrect:</strong> Package-private field allows direct access within package.

## Question

Which statements about instance variables versus local variables are correct?<br><br>

Please select all that apply<br><br>

A) Instance variables have default values, local variables do not<br>
B) Instance variables exist for the lifetime of the object<br>
C) Local variables can be accessed from anywhere in the class<br>
D) Instance variables can be shadowed by local variables with the same name

## Réponse

<strong>Réponse correcte :</strong> A), B), D)<br><br>

<strong>A) is correct:</strong><br>
• Instance variables: default values (0, false, null)<br>
• Local variables: MUST be initialized before use<br>
• Uninitialized local variable = compilation error<br><br>

<strong>B) is correct:</strong><br>
• Instance variables live as long as the object exists<br>
• Created when object is instantiated<br>
• Destroyed when object is garbage collected<br><br>

<strong>D) is correct:</strong><br>
```java
private int count = 10;  // Instance variable

public void test() {
    int count = 20;  // Local variable shadows instance variable
    System.out.println(count);      // prints 20
    System.out.println(this.count); // prints 10
}
```
<br><br>

<strong>C) is incorrect:</strong> Local variables are scoped to their declaring block - they can only be accessed within the method/block where declared.

## Question

What happens when this code is executed?<br><br>

```java
public class Demo {
    public void process() {
        int x = 10;
    }
    
    public void display() {
        System.out.println(x);
    }
}

Demo d = new Demo();
d.process();
d.display();
```
<br><br>

Please select 1 option<br><br>

A) Prints 10<br>
B) Prints 0<br>
C) Compilation error: cannot find symbol x<br>
D) Runtime exception: variable not initialized

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

<strong>Compilation error:</strong> Local variable <strong>x</strong> is not accessible outside its declaring method.<br><br>

Scope analysis:<br>
• <strong>x</strong> is declared as local variable in <strong>process()</strong><br>
• Local variables exist only within their method<br>
• <strong>x</strong> is destroyed when <strong>process()</strong> exits<br>
• <strong>display()</strong> cannot access <strong>x</strong><br><br>

Error message:<br>
<strong>"cannot find symbol: variable x"</strong><br><br>

Solutions:<br><br>

Option 1 - Instance variable:<br>
```java
public class Demo {
    private int x;  // Instance variable
    
    public void process() {
        x = 10;
    }
    
    public void display() {
        System.out.println(x);
    }
}
```
<br><br>

Option 2 - Pass as parameter:<br>
```java
public void display(int x) {
    System.out.println(x);
}
```
<br><br>

<strong>A), B) are incorrect:</strong> Code doesn't compile.<br>
<strong>D) is incorrect:</strong> Error occurs at compilation, not runtime.

## Question
What will the following code print?<br><br>
```java
public class TV {
    String status = "off";
    void on() { status = "on"; }
    void off() { status = "off"; }
}

public class Main {
    public static void main(String[] args) {
        TV remote1 = new TV();
        TV remote2 = remote1;
        remote1.on();
        remote2.off();
        System.out.println(remote1.status);
    }
}
```
<br><br>
Please select 1 option<br><br>
A) on<br>
B) Compilation error<br>
C) off<br>
D) NullPointerException

## Réponse
<strong>Réponse correcte :</strong> C)<br><br>
<strong>KEY CONCEPT:</strong> When you assign one object reference to another (<strong>remote2 = remote1</strong>), both variables point to the <strong>same object</strong> in memory.<br><br>
Step-by-step execution:<br>
• remote1 is created and points to a new TV object<br>
• remote2 = remote1 means remote2 now points to the <strong>same TV object</strong><br>
• remote1.on() sets status to "on" on the shared object<br>
• remote2.off() sets status to "off" on the <strong>same shared object</strong><br>
• Printing remote1.status prints <strong>"off"</strong><br><br>
<strong>A) is incorrect:</strong> remote2.off() changed the status back to "off" on the same object.<br>
<strong>B) is incorrect:</strong> The code compiles and runs without errors.<br>
<strong>D) is incorrect:</strong> Both references are valid; no null dereference occurs.

## Question
Given the following class:<br><br>
```java
public class Clothing {
    String description;
    double price;

    public Clothing() {}

    public Clothing(String description, double price) {
        description = description;
        price = price;
    }
}
```
<br><br>
What is the result of executing this code?<br><br>
```java
Clothing item = new Clothing("Jacket", 29.99);
System.out.println(item.description + " " + item.price);
```
<br><br>
Please select 1 option<br><br>
A) Jacket 29.99<br>
B) Compilation error<br>
C) null 29.99<br>
D) null 0.0

## Réponse
<strong>Réponse correcte :</strong> D)<br><br>
<strong>TRICKY:</strong> The constructor parameters <strong>shadow</strong> the instance fields.<br><br>
In the constructor:<br>
• <strong>description = description</strong> assigns the parameter to itself, NOT to the instance field<br>
• <strong>price = price</strong> assigns the parameter to itself, NOT to the instance field<br>
• The instance fields remain at their <strong>default values</strong>: null for String, 0.0 for double<br><br>
The correct code should use the <strong>this</strong> keyword:<br>
<strong>this.description = description;</strong><br>
<strong>this.price = price;</strong><br><br>
<strong>A) is incorrect:</strong> Would require proper use of this keyword.<br>
<strong>B) is incorrect:</strong> The code compiles without error; shadowing is legal.<br>
<strong>C) is incorrect:</strong> Both fields remain at default values.

## Question
Which of the following statements about constructors in Java are correct?<br><br>
Please select 2 options<br><br>
A) A constructor does not have a return type, not even void<br>
B) A constructor must always be declared public<br>
C) If you define a parameterized constructor, the compiler still provides a default no-argument constructor<br>
D) Constructor overloading allows a class to have multiple constructors with different parameter lists

## Réponse
<strong>Réponse correcte :</strong> A), D)<br><br>
<strong>A) is correct:</strong> Constructors have <strong>no return type</strong>. The return type is implicitly the class type itself. Adding a return type (even void) would make it a regular method, not a constructor.<br><br>
<strong>D) is correct:</strong> <strong>Constructor overloading</strong> allows multiple constructors with different parameter lists. This is the same concept as method overloading applied to constructors.<br><br>
<strong>B) is incorrect:</strong> Constructors can have <strong>any access modifier</strong>: public, protected, private, or package-private. A private constructor is used in patterns like Singleton.<br>
<strong>C) is incorrect:</strong> The compiler provides a default no-argument constructor <strong>only if no constructors are explicitly defined</strong>. Once you define any constructor, the default constructor is NOT provided automatically.

## Question
What will the following code print?<br><br>
```java
public class Clothing {
    String description;
    double price;
    static double minPrice = 5.0;

    public Clothing(String desc, double p) {
        this.description = desc;
        this.price = Math.max(p, minPrice);
    }
}

public class Main {
    public static void main(String[] args) {
        Clothing item1 = new Clothing("Socks", 2.99);
        Clothing item2 = new Clothing("Jacket", 29.99);
        Clothing.minPrice = 10.0;
        System.out.println(item1.price + " " + item2.price);
    }
}
```
<br><br>
Please select 1 option<br><br>
A) 2.99 29.99<br>
B) 5.0 29.99<br>
C) 10.0 29.99<br>
D) 10.0 10.0

## Réponse
<strong>Réponse correcte :</strong> B)<br><br>
<strong>KEY CONCEPTS:</strong> Static variables and constructor execution timing.<br><br>
Step-by-step:<br>
• When item1 is created with price 2.99, <strong>Math.max(2.99, 5.0) = 5.0</strong><br>
• When item2 is created with price 29.99, <strong>Math.max(29.99, 5.0) = 29.99</strong><br>
• Changing <strong>Clothing.minPrice = 10.0</strong> after construction does NOT retroactively change the prices already stored in item1 and item2<br>
• The prices were computed and assigned at <strong>construction time</strong><br><br>
<strong>A) is incorrect:</strong> The minPrice check ensures price cannot be below 5.0.<br>
<strong>C) is incorrect:</strong> Changing minPrice after construction has no effect on already-assigned instance field values.<br>
<strong>D) is incorrect:</strong> Same reason as C; prices were already computed during construction.

## Question
What happens when the following code is compiled and run?<br><br>
```java
public class Clothing {
    String description;
    double price;
}

public class Main {
    public static void main(String[] args) {
        Clothing[] items = new Clothing[3];
        items[0] = new Clothing();
        items[0].description = "Jacket";
        System.out.println(items[1].description);
    }
}
```
<br><br>
Please select 1 option<br><br>
A) null<br>
B) Jacket<br>
C) NullPointerException at runtime<br>
D) Compilation error

## Réponse
<strong>Réponse correcte :</strong> C)<br><br>
<strong>CRITICAL TRAP:</strong> Creating an array of objects does <strong>NOT</strong> instantiate the objects themselves.<br><br>
Analysis:<br>
• <strong>new Clothing[3]</strong> creates an array with 3 slots, all initialized to <strong>null</strong><br>
• Only <strong>items[0]</strong> is assigned a new Clothing object<br>
• <strong>items[1]</strong> is still <strong>null</strong><br>
• Calling <strong>items[1].description</strong> throws <strong>NullPointerException</strong> because you cannot access a field on a null reference<br><br>
<strong>A) is incorrect:</strong> Would be true if items[1] had been instantiated with new Clothing().<br>
<strong>B) is incorrect:</strong> items[1] is a different element from items[0].<br>
<strong>D) is incorrect:</strong> The code compiles; the error occurs at runtime.

## Question
Given the following code:<br><br>
```java
public class Clothing {
    String description;
    double price;

    public Clothing(String d, double p) {
        this.description = d;
        this.price = p;
    }
}

public class Main {
    public static void main(String[] args) {
        Clothing[] items = {
            new Clothing("Jacket", 15.5),
            new Clothing("Socks", 3.99)
        };
        items[0] = items[1];
        items[1].description = "Hat";
        System.out.println(items[0].description);
    }
}
```
<br><br>
Please select 1 option<br><br>
A) Jacket<br>
B) Socks<br>
C) null<br>
D) Hat

## Réponse
<strong>Réponse correcte :</strong> D)<br><br>
<strong>OBJECT REFERENCE TRAP:</strong> Array elements store <strong>object references</strong>, not copies of objects.<br><br>
Step-by-step:<br>
• items[0] points to Clothing("Jacket", 15.5)<br>
• items[1] points to Clothing("Socks", 3.99)<br>
• <strong>items[0] = items[1]</strong> makes items[0] point to the <strong>same object</strong> as items[1]<br>
• The Jacket object is now unreferenced (eligible for garbage collection)<br>
• <strong>items[1].description = "Hat"</strong> changes the description of the shared object<br>
• Since items[0] and items[1] point to the <strong>same object</strong>, items[0].description is also <strong>"Hat"</strong><br><br>
<strong>A) is incorrect:</strong> The Jacket object was dereferenced when items[0] was reassigned.<br>
<strong>B) is incorrect:</strong> The description was changed from "Socks" to "Hat".<br>
<strong>C) is incorrect:</strong> The object is still valid; only its description changed.

## Question
Which statements about the stack and heap in the Java Virtual Machine are correct?<br><br>
Please select 2 options<br><br>
A) Primitive local variables are stored on the stack with their actual values<br>
B) Objects are allocated on the stack and references are stored on the heap<br>
C) An array of primitives is stored entirely on the stack<br>
D) An object reference variable on the stack holds a pointer to the object's location on the heap

## Réponse
<strong>Réponse correcte :</strong> A), D)<br><br>
<strong>A) is correct:</strong> Primitive local variables (int, double, etc.) are stored <strong>directly on the stack</strong> with their actual values. For example, <strong>double total = 3.14</strong> stores 3.14 directly in the stack frame.<br><br>
<strong>D) is correct:</strong> Object reference variables on the stack hold a <strong>memory address</strong> (pointer) that points to the actual object allocated on the <strong>heap</strong>.<br><br>
<strong>B) is incorrect:</strong> It is the <strong>opposite</strong>: objects are allocated on the <strong>heap</strong> and references are stored on the <strong>stack</strong>.<br>
<strong>C) is incorrect:</strong> Arrays in Java are <strong>objects</strong>, even arrays of primitives. The array object is allocated on the <strong>heap</strong>. The variable referencing the array is on the stack.

## Question
What will the following code print?<br><br>
```java
public class Counter {
    static int count = 0;
    String name;

    public Counter(String name) {
        this.name = name;
        count++;
    }

    public static void main(String[] args) {
        Counter c1 = new Counter("A");
        Counter c2 = new Counter("B");
        Counter c3 = new Counter("C");
        c1 = c2;
        System.out.println(Counter.count + " " + c1.name);
    }
}
```
<br><br>
Please select 1 option<br><br>
A) 3 B<br>
B) 2 B<br>
C) 3 A<br>
D) 2 A

## Réponse
<strong>Réponse correcte :</strong> A)<br><br>
<strong>Static variable behavior:</strong><br>
• <strong>count</strong> is static and shared across all instances<br>
• Each constructor call increments count: after c1 → 1, after c2 → 2, after c3 → <strong>3</strong><br>
• Reassigning <strong>c1 = c2</strong> does NOT decrement count or destroy the original object<br><br>
<strong>Reference reassignment:</strong><br>
• After <strong>c1 = c2</strong>, c1 now points to the same object as c2 (name = "B")<br>
• The original "A" object becomes eligible for garbage collection, but count remains 3<br><br>
Output: <strong>3 B</strong><br><br>
<strong>B) is incorrect:</strong> count is not decremented when references are reassigned.<br>
<strong>C) is incorrect:</strong> c1 now points to the "B" object after reassignment.<br>
<strong>D) is incorrect:</strong> Both count value and name are wrong.

## Question
What is the result of compiling and running this code?<br><br>
```java
public class Item {
    String name;

    public Item(String name) {
        this.name = name;
    }

    public static void main(String[] args) {
        Item a = new Item("Book");
        Item b = new Item("Pen");
        Item c = a;
        a = b;
        b = c;
        System.out.println(a.name + " " + b.name + " " + c.name);
    }
}
```
<br><br>
Please select 1 option<br><br>
A) Book Pen Book<br>
B) Pen Book Pen<br>
C) Pen Book Book<br>
D) Book Pen Pen

## Réponse
<strong>Réponse correcte :</strong> C)<br><br>
<strong>REFERENCE SWAP TRAP:</strong> This is a classic reference swap operation.<br><br>
Tracing the references:<br>
• Initially: a → "Book", b → "Pen"<br>
• <strong>c = a</strong> → c now points to "Book" (c → "Book")<br>
• <strong>a = b</strong> → a now points to "Pen" (a → "Pen")<br>
• <strong>b = c</strong> → b now points to "Book" (b → "Book")<br><br>
Final state:<br>
• a.name = <strong>"Pen"</strong><br>
• b.name = <strong>"Book"</strong><br>
• c.name = <strong>"Book"</strong> (c still points to the original "Book" object)<br><br>
Output: <strong>Pen Book Book</strong><br><br>
<strong>A) is incorrect:</strong> The swap changed a and b.<br>
<strong>B) is incorrect:</strong> c was never reassigned after the initial assignment.<br>
<strong>D) is incorrect:</strong> c points to the original "Book" object, not "Pen".

## Question
What will the following code print?<br><br>
```java
public class Clothing {
    String description;
    double price;
    String size;

    public Clothing(String d, double p) {
        this.description = d;
        this.price = p;
    }

    public static void main(String[] args) {
        Clothing[] items = {
            new Clothing("Jacket", 15.5),
            new Clothing("Socks", 3.99)
        };
        items[0].description = items[1].description;
        items[1].description = "Hat";
        System.out.print(items[0].description + " ");
        items[1] = items[0];
        System.out.print(items[0].description + " ");
        items[0] = new Clothing("Shoes", 49.99);
        System.out.print(items[1].description);
    }
}
```
<br><br>
Please select 1 option<br><br>
A) Socks Socks Hat<br>
B) Hat Hat Hat<br>
C) Socks Hat Socks<br>
D) Socks Socks Socks

## Réponse
<strong>Réponse correcte :</strong> D)<br><br>
<strong>MULTIPLE REFERENCE TRAPS:</strong><br><br>
Step-by-step trace:<br>
• items[0] → Clothing("Jacket", 15.5), items[1] → Clothing("Socks", 3.99)<br><br>
1. <strong>items[0].description = items[1].description</strong><br>
→ items[0] description changes from "Jacket" to <strong>"Socks"</strong><br>
→ This copies the String <strong>value</strong>, not the reference to items[1]<br><br>
2. <strong>items[1].description = "Hat"</strong><br>
→ items[1] description changes to "Hat"; items[0] is <strong>unaffected</strong> (still "Socks")<br>
→ Print: <strong>"Socks "</strong><br><br>
3. <strong>items[1] = items[0]</strong><br>
→ items[1] now points to the same object as items[0]<br>
→ Print: <strong>"Socks "</strong><br><br>
4. <strong>items[0] = new Clothing("Shoes", 49.99)</strong><br>
→ items[0] now points to a new object, but items[1] still points to the <strong>old</strong> items[0] object<br>
→ Print: <strong>"Socks"</strong><br><br>
Output: <strong>Socks Socks Socks</strong><br><br>
<strong>A) is incorrect:</strong> items[1] was reassigned to items[0] before the final print.<br>
<strong>B) is incorrect:</strong> Changing items[1].description to "Hat" did not affect items[0].<br>
<strong>C) is incorrect:</strong> Misunderstands the order of reference assignments.

## Question
Which statements about static methods and variables in Java are correct?<br><br>
Please select 3 options<br><br>
A) A static variable is shared among all instances of the class<br>
B) A static method can access instance variables directly without an object reference<br>
C) Static methods and variables can be accessed without creating an instance of the class<br>
D) A static variable is a good candidate for data that should be the same across all object instances

## Réponse
<strong>Réponse correcte :</strong> A), C), D)<br><br>
<strong>A) is correct:</strong> A static variable belongs to the <strong>class</strong>, not to individual objects. All instances share the <strong>same copy</strong> of the static variable.<br><br>
<strong>C) is correct:</strong> Static members can be accessed using the <strong>class name</strong> directly (e.g., <strong>Clothing.minPrice</strong>) without instantiating an object with <strong>new</strong>.<br><br>
<strong>D) is correct:</strong> A value like <strong>minPrice</strong> that should be consistent across all instances is an ideal candidate for a static variable. It avoids redundant storage in each object.<br><br>
<strong>B) is incorrect:</strong> A static method does <strong>NOT</strong> have access to instance variables or instance methods directly. It can only access other <strong>static</strong> members. To access instance members, it must use an explicit object reference.

## Question
What is the result of compiling and running this code?<br><br>
```java
public class Widget {
    int value;

    Widget(int v) { this.value = v; }

    public static void main(String[] args) {
        Widget w1 = new Widget(10);
        Widget w2 = new Widget(20);
        Widget w3 = w1;
        w3.value = 30;
        w1 = w2;
        w2 = w3;
        System.out.println(w1.value + " " + w2.value + " " + w3.value);
    }
}
```
<br><br>
Please select 1 option<br><br>
A) 10 20 30<br>
B) 20 30 30<br>
C) 20 10 10<br>
D) 30 30 20

## Réponse
<strong>Réponse correcte :</strong> B)<br><br>
<strong>ADVANCED REFERENCE TRACING:</strong><br><br>
Let Object-A = Widget(10), Object-B = Widget(20).<br><br>
Step-by-step:<br>
• w1 → Object-A (value=10), w2 → Object-B (value=20)<br>
• <strong>w3 = w1</strong> → w3 → Object-A<br>
• <strong>w3.value = 30</strong> → Object-A value becomes <strong>30</strong> (w1 and w3 both see this)<br>
• <strong>w1 = w2</strong> → w1 now → Object-B (value=20)<br>
• <strong>w2 = w3</strong> → w2 now → Object-A (value=30)<br><br>
Final state:<br>
• w1 → Object-B → value = <strong>20</strong><br>
• w2 → Object-A → value = <strong>30</strong><br>
• w3 → Object-A → value = <strong>30</strong><br><br>
Output: <strong>20 30 30</strong><br><br>
<strong>A) is incorrect:</strong> Ignores the mutation w3.value = 30.<br>
<strong>C) is incorrect:</strong> Misunderstands which objects the references point to.<br>
<strong>D) is incorrect:</strong> w1 was reassigned to Object-B before w2 was reassigned.

## Question
An object on the heap becomes eligible for garbage collection when:<br><br>
Please select 1 option<br><br>
A) The object's finalize() method is called<br>
B) System.gc() is invoked<br>
C) The static variable count reaches zero<br>
D) No active reference variable in the program points to that object

## Réponse
<strong>Réponse correcte :</strong> D)<br><br>
An object becomes <strong>eligible</strong> for garbage collection when there are <strong>no more active references</strong> pointing to it from the stack or from other reachable objects.<br><br>
For example:<br>
• If <strong>item2</strong> was the only reference to an object, and you reassign <strong>item2 = item1</strong>, the original object referenced by item2 has <strong>no remaining references</strong> and becomes eligible for garbage collection.<br><br>
<strong>A) is incorrect:</strong> finalize() is called <strong>by</strong> the garbage collector (if at all); it does not trigger garbage collection. It is also deprecated since Java 9.<br>
<strong>B) is incorrect:</strong> System.gc() is a <strong>suggestion</strong> to the JVM, not a guarantee. It does not determine eligibility; it merely requests a collection cycle.<br>
<strong>C) is incorrect:</strong> Garbage collection is based on <strong>reachability</strong>, not on any counter. There is no automatic reference counting mechanism in standard Java GC.

## Question
What will the following code print?<br><br>
```java
public class Clothing {
    String description;
    double price;

    Clothing() {
        this("Unknown", 0.0);
    }

    Clothing(String description, double price) {
        this.description = description;
        this.price = price;
    }

    public static void main(String[] args) {
        Clothing c1 = new Clothing();
        Clothing c2 = new Clothing("Shirt", 19.99);
        c1 = c2;
        c2 = new Clothing();
        System.out.println(c1.description + " " + c2.description);
    }
}
```
<br><br>
Please select 1 option<br><br>
A) Unknown Unknown<br>
B) Shirt Shirt<br>
C) Shirt Unknown<br>
D) Unknown Shirt

## Réponse
<strong>Réponse correcte :</strong> C)<br><br>
<strong>CONSTRUCTOR CHAINING + REFERENCE TRAP:</strong><br><br>
Analysis:<br>
• <strong>Clothing()</strong> calls <strong>this("Unknown", 0.0)</strong> — this is <strong>constructor chaining</strong><br>
• c1 → Clothing("Unknown", 0.0), c2 → Clothing("Shirt", 19.99)<br><br>
Reference changes:<br>
• <strong>c1 = c2</strong> → c1 now points to the "Shirt" object<br>
• <strong>c2 = new Clothing()</strong> → c2 now points to a <strong>new</strong> "Unknown" object<br>
• c1 still points to the "Shirt" object (unaffected by c2's reassignment)<br><br>
Output: <strong>Shirt Unknown</strong><br><br>
<strong>A) is incorrect:</strong> c1 was reassigned to point to the "Shirt" object.<br>
<strong>B) is incorrect:</strong> c2 was reassigned to a new "Unknown" object.<br>
<strong>D) is incorrect:</strong> The order is reversed from the actual output.


## Question
Which of the following methods can coexist in the same class?<br><br>
Please select 2 options<br><br>
A) `int calculate(int x, int y)` and `double calculate(int x, int y)`<br>
B) `int calculate(int x, int y)` and `int calculate(int a, int b, int c)`<br>
C) `void process(String s)` and `void process(String str)`<br>
D) `int add(int x, double y)` and `int add(double x, int y)`

## Réponse
<strong>Réponse correcte :</strong> B), D)<br><br>
<strong>METHOD OVERLOADING RULE:</strong> Methods can coexist if they have <strong>different signatures</strong>.<br><br>
Signature = method name + parameter list (types and order).<br><br>
<strong>B) is correct:</strong><br>
• calculate(int, int) vs calculate(int, int, int)<br>
• Different number of parameters → <strong>different signatures</strong> → valid overloading<br><br>
<strong>D) is correct:</strong><br>
• add(int, double) vs add(double, int)<br>
• Same types but <strong>different order</strong> → different signatures → valid overloading<br><br>
<strong>A) is incorrect:</strong><br>
• calculate(int, int) vs calculate(int, int)<br>
• <strong>Same signature</strong> (return type is NOT part of signature)<br>
• <strong>Compilation error:</strong> duplicate method<br><br>
<strong>C) is incorrect:</strong><br>
• process(String) vs process(String)<br>
• <strong>Parameter names do NOT affect signature</strong><br>
• Compilation error: duplicate method

## Question
What will the following code print?<br><br>
```java
class Test {
    static int count = 0;
    
    void increment() {
        int count = 5;
        count++;
        System.out.print(count + " ");
        System.out.print(this.count + " ");
    }
    
    public static void main(String[] args) {
        Test t = new Test();
        Test.count = 10;
        t.increment();
    }
}
```
<br><br>
Please select 1 option<br><br>
A) 6 10<br>
B) 11 11<br>
C) 5 10<br>
D) 6 11

## Réponse
<strong>Réponse correcte :</strong> A)<br><br>
<strong>VARIABLE SHADOWING TRAP:</strong> Local variable <strong>count</strong> shadows the static variable <strong>count</strong>.<br><br>
Step-by-step:<br>
• Static variable Test.count is set to <strong>10</strong><br>
• Inside increment(), local variable <strong>int count = 5</strong> is created<br>
• This local variable <strong>shadows</strong> the static variable within the method scope<br>
• <strong>count++</strong> increments the <strong>local</strong> variable: 5 → <strong>6</strong><br>
• <strong>this.count</strong> accesses the static variable (still <strong>10</strong>)<br><br>
Output: <strong>6 10</strong><br><br>
<strong>B) is incorrect:</strong> Would require incrementing the static variable.<br>
<strong>C) is incorrect:</strong> Forgot the increment of the local variable.<br>
<strong>D) is incorrect:</strong> The static variable was never incremented.

## Question
What is the result of compiling and running this code?<br><br>
```java
class Animal {
    void makeSound() {
        System.out.print("Animal sound ");
    }
}

class Dog extends Animal {
    void makeSound() {
        System.out.print("Bark ");
    }
}

public class Test {
    public static void main(String[] args) {
        Animal a = new Dog();
        Dog d = new Dog();
        a.makeSound();
        d.makeSound();
    }
}
```
<br><br>
Please select 1 option<br><br>
A) Animal sound Animal sound<br>
B) Animal sound Bark<br>
C) Bark Bark<br>
D) Compilation error

## Réponse
<strong>Réponse correcte :</strong> C)<br><br>
<strong>POLYMORPHISM + METHOD OVERRIDING:</strong> The actual method called is determined by the <strong>object type at runtime</strong>, NOT the reference type.<br><br>
Analysis:<br>
• <strong>Animal a = new Dog();</strong><br>
→ Reference type: Animal<br>
→ Object type: <strong>Dog</strong><br>
→ Calls Dog's makeSound() → prints <strong>"Bark "</strong><br><br>
• <strong>Dog d = new Dog();</strong><br>
→ Both reference and object are Dog<br>
→ Calls Dog's makeSound() → prints <strong>"Bark "</strong><br><br>
<strong>KEY RULE:</strong> In method overriding, the JVM uses the <strong>actual object type</strong> (Dog), not the reference type (Animal).<br><br>
Output: <strong>Bark Bark</strong><br><br>
<strong>A), B) are incorrect:</strong> Would only be true if the decision was based on reference type (it's not).<br>
<strong>D) is incorrect:</strong> The code compiles and runs successfully.

## Question
What will the following code print?<br><br>
```java
class Parent {
    Parent() {
        System.out.print("Parent ");
    }
}

class Child extends Parent {
    Child() {
        System.out.print("Child ");
    }
}

public class Test {
    public static void main(String[] args) {
        Child c = new Child();
    }
}
```
<br><br>
Please select 1 option<br><br>
A) Child Parent<br>
B) Parent Child<br>
C) Child<br>
D) Compilation error

## Réponse
<strong>Réponse correcte :</strong> B)<br><br>
<strong>CONSTRUCTOR CHAINING:</strong> When a child class is instantiated, the <strong>parent constructor is called first</strong>.<br><br>
Execution order:<br>
1. Child constructor is invoked<br>
2. First line of Child constructor is an <strong>implicit super()</strong> call<br>
3. Parent constructor executes → prints <strong>"Parent "</strong><br>
4. Control returns to Child constructor → prints <strong>"Child "</strong><br><br>
Output: <strong>Parent Child</strong><br><br>
<strong>IMPORTANT RULE:</strong> If you don't explicitly call super(), Java inserts <strong>super()</strong> as the first statement in the child constructor.<br><br>
<strong>A) is incorrect:</strong> Parent always executes before child.<br>
<strong>C) is incorrect:</strong> Parent constructor is always called in inheritance.<br>
<strong>D) is incorrect:</strong> The code compiles successfully.

## Question
What is the result of compiling and running this code?<br><br>
```java
abstract class Shape {
    abstract void draw();
    
    void display() {
        System.out.print("Shape ");
    }
}

class Circle extends Shape {
    void draw() {
        System.out.print("Circle ");
    }
}

public class Test {
    public static void main(String[] args) {
        Shape s = new Circle();
        s.draw();
        s.display();
    }
}
```
<br><br>
Please select 1 option<br><br>
A) Circle Shape<br>
B) Compilation error: cannot instantiate abstract class<br>
C) Shape Circle<br>
D) Compilation error: Circle must override display()

## Réponse
<strong>Réponse correcte :</strong> A)<br><br>
<strong>ABSTRACT CLASS RULES:</strong><br>
• You <strong>cannot</strong> instantiate an abstract class directly (new Shape() would fail)<br>
• You <strong>CAN</strong> have a reference of abstract type pointing to a concrete subclass<br>
• Abstract classes can have <strong>both abstract and concrete methods</strong><br>
• Child classes must implement <strong>all abstract methods</strong><br><br>
Code analysis:<br>
• <strong>Shape s = new Circle();</strong> → Valid (polymorphism)<br>
• <strong>s.draw();</strong> → Calls Circle's implementation → prints <strong>"Circle "</strong><br>
• <strong>s.display();</strong> → Calls inherited concrete method from Shape → prints <strong>"Shape "</strong><br><br>
Output: <strong>Circle Shape</strong><br><br>
<strong>B) is incorrect:</strong> We're not instantiating Shape; we're creating a Circle and using Shape reference.<br>
<strong>C) is incorrect:</strong> draw() is called first, then display().<br>
<strong>D) is incorrect:</strong> display() is NOT abstract, so overriding it is optional.

## Question
Which statement about the `this` keyword in Java is correct?<br><br>
Please select 1 option<br><br>
A) `this` can be used in static methods<br>
B) `this` is required when accessing all instance variables<br>
C) `this` can be used in a constructor to call another constructor in the same class<br>
D) `this` refers to the parent class instance

## Réponse
<strong>Réponse correcte :</strong> C)<br><br>
<strong>C) is correct:</strong> <strong>this()</strong> can be used in a constructor to call another constructor in the <strong>same class</strong>. This is called <strong>constructor chaining</strong>.<br><br>
Example:<br>
```java
class Person {
    String name;
    int age;
    
    Person() {
        this("Unknown", 0);  // calls other constructor
    }
    
    Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
}
```
<br><br>
<strong>A) is incorrect:</strong> <strong>this</strong> refers to the current object instance. Static methods have <strong>no instance context</strong>, so this cannot be used in static methods.<br>
<strong>B) is incorrect:</strong> <strong>this</strong> is only required when there is <strong>variable shadowing</strong> (e.g., parameter has same name as instance variable). Otherwise, it's optional.<br>
<strong>D) is incorrect:</strong> <strong>this</strong> refers to the <strong>current</strong> object. <strong>super</strong> refers to the parent class.

## Question
What will the following code print?<br><br>
```java
class Animal {
    void eat() {
        System.out.print("Animal eating ");
    }
}

class Dog extends Animal {
    void eat() {
        System.out.print("Dog eating ");
    }
    
    void bark() {
        System.out.print("Barking ");
    }
}

public class Test {
    public static void main(String[] args) {
        Animal a = new Dog();
        a.eat();
        a.bark();
    }
}
```
<br><br>
Please select 1 option<br><br>
A) Animal eating Barking<br>
B) Dog eating Barking<br>
C) Compilation error at line: a.bark()<br>
D) Dog eating Animal eating Barking

## Réponse
<strong>Réponse correcte :</strong> C)<br><br>
<strong>POLYMORPHISM LIMITATION:</strong> You can only call methods that are <strong>visible through the reference type</strong>.<br><br>
Analysis:<br>
• <strong>Animal a = new Dog();</strong><br>
→ Reference type: <strong>Animal</strong><br>
→ Object type: Dog<br><br>
• <strong>a.eat();</strong> → OK, eat() exists in Animal (and is overridden in Dog)<br>
• <strong>a.bark();</strong> → <strong>Compilation error</strong><br>
→ bark() does NOT exist in Animal class<br>
→ Compiler checks methods based on <strong>reference type</strong> (Animal)<br><br>
<strong>KEY RULE:</strong><br>
• Method <strong>existence</strong> is checked at <strong>compile time</strong> using reference type<br>
• Method <strong>implementation</strong> is chosen at <strong>runtime</strong> using object type<br><br>
To fix, you would need to cast: <strong>((Dog)a).bark();</strong><br><br>
<strong>A), B), D) are incorrect:</strong> The code does not compile.

## Question
What is the result of compiling and running this code?<br><br>
```java
class Parent {
    Parent(String s) {
        System.out.print(s + " ");
    }
}

class Child extends Parent {
    Child() {
        System.out.print("Child ");
    }
}

public class Test {
    public static void main(String[] args) {
        Child c = new Child();
    }
}
```
<br><br>
Please select 1 option<br><br>
A) Child<br>
B) Compilation error: implicit super constructor Parent() is undefined<br>
C) Runtime error<br>
D) Parent Child

## Réponse
<strong>Réponse correcte :</strong> B)<br><br>
<strong>SUPER CONSTRUCTOR TRAP:</strong> If the parent class does NOT have a no-argument constructor, the child constructor <strong>must explicitly call</strong> a parent constructor using <strong>super(...)</strong>.<br><br>
Problem:<br>
• Parent class has ONLY <strong>Parent(String s)</strong> constructor<br>
• No no-argument <strong>Parent()</strong> constructor exists<br>
• Child constructor has an <strong>implicit super()</strong> call (no-argument)<br>
• This implicit call fails because <strong>Parent()</strong> doesn't exist<br><br>
<strong>Compilation error:</strong> "implicit super constructor Parent() is undefined. Must explicitly invoke another constructor"<br><br>
<strong>To fix, Child constructor must call:</strong><br>
```java
Child() {
    super("Parent");  // explicit call
    System.out.print("Child ");
}
```
<br><br>
<strong>A) is incorrect:</strong> The code does not compile.<br>
<strong>C) is incorrect:</strong> The error is caught at compile time.<br>
<strong>D) is incorrect:</strong> The code does not run.

## Question
Which statements about interfaces in Java are correct?<br><br>
Please select 3 options<br><br>
A) A class can implement multiple interfaces<br>
B) An interface can extend multiple interfaces<br>
C) All methods in an interface are implicitly public abstract<br>
D) An interface can have instance variables

## Réponse
<strong>Réponse correcte :</strong> A), B), C)<br><br>
<strong>A) is correct:</strong> A class can implement <strong>multiple interfaces</strong> using commas:<br>
```java
class Bird implements Flyable, Swimmable { }
```
This solves the "multiple inheritance" problem in Java.<br><br>
<strong>B) is correct:</strong> An interface can <strong>extend multiple interfaces</strong>:<br>
```java
interface Movable extends Flyable, Swimmable { }
```
<br><br>
<strong>C) is correct:</strong> All methods in an interface are <strong>implicitly public abstract</strong> (unless they are default, static, or private since Java 8+). You don't need to write these modifiers explicitly.<br><br>
<strong>D) is incorrect:</strong> Interfaces cannot have <strong>instance variables</strong>. They can only have <strong>public static final constants</strong> (implicitly).

## Question
What will the following code print?<br><br>
```java
class Test {
    void display() {
        int x;
        if (true) {
            x = 10;
        }
        System.out.print(x);
    }
    
    public static void main(String[] args) {
        new Test().display();
    }
}
```
<br><br>
Please select 1 option<br><br>
A) 10<br>
B) 0<br>
C) Compilation error: variable x might not have been initialized<br>
D) Runtime error

## Réponse
<strong>Réponse correcte :</strong> A)<br><br>
<strong>LOCAL VARIABLE INITIALIZATION RULE:</strong> Local variables must be <strong>definitely assigned</strong> before use.<br><br>
Analysis:<br>
• <strong>int x;</strong> declares x but does NOT initialize it<br>
• <strong>if (true) { x = 10; }</strong> assigns x = 10<br>
• The compiler recognizes that <strong>if (true)</strong> will <strong>always execute</strong><br>
• Therefore, x is <strong>definitely assigned</strong> before the print statement<br>
• Prints: <strong>10</strong><br><br>
<strong>IMPORTANT NUANCE:</strong> If the condition was a variable (e.g., if (flag)), the compiler would NOT guarantee execution, and a compilation error would occur.<br><br>
Example that would fail:<br>
```java
boolean flag = true;
int x;
if (flag) { x = 10; }  // compiler can't guarantee this runs
System.out.print(x);   // ERROR: might not be initialized
```
<br><br>
<strong>B) is incorrect:</strong> Local variables have no default values.<br>
<strong>C) is incorrect:</strong> The compiler can prove x is initialized because if (true) always executes.<br>
<strong>D) is incorrect:</strong> No runtime error occurs.

## Question
What is the result of compiling and running this code?<br><br>
```java
class Calculator {
    int add(int a, int b) {
        return a + b;
    }
    
    int add(int a, int b, int c) {
        return a + b + c;
    }
    
    double add(double a, double b) {
        return a + b;
    }
}

public class Test {
    public static void main(String[] args) {
        Calculator c = new Calculator();
        System.out.print(c.add(5, 10) + " ");
        System.out.print(c.add(5, 10, 15) + " ");
        System.out.print(c.add(5.0, 10.0));
    }
}
```
<br><br>
Please select 1 option<br><br>
A) 15 30 15<br>
B) 15.0 30.0 15.0<br>
C) Compilation error: ambiguous method call<br>
D) 15 30 15.0

## Réponse
<strong>Réponse correcte :</strong> D)<br><br>
<strong>METHOD OVERLOADING RESOLUTION:</strong> The compiler selects the most <strong>specific method</strong> based on the argument types.<br><br>
Analysis:<br>
• <strong>c.add(5, 10)</strong><br>
→ Arguments: int, int<br>
→ Matches: <strong>add(int, int)</strong><br>
→ Returns: <strong>15</strong> (int)<br><br>
• <strong>c.add(5, 10, 15)</strong><br>
→ Arguments: int, int, int<br>
→ Matches: <strong>add(int, int, int)</strong><br>
→ Returns: <strong>30</strong> (int)<br><br>
• <strong>c.add(5.0, 10.0)</strong><br>
→ Arguments: double, double<br>
→ Matches: <strong>add(double, double)</strong><br>
→ Returns: <strong>15.0</strong> (double)<br><br>
Output: <strong>15 30 15.0</strong><br><br>
<strong>KEY CONCEPT:</strong> Overload resolution happens at <strong>compile time</strong> based on argument types.<br><br>
<strong>A) is incorrect:</strong> The third call returns a double (15.0), not an int.<br>
<strong>B) is incorrect:</strong> The first two calls return int values.<br>
<strong>C) is incorrect:</strong> No ambiguity exists; each call has a unique match.

## Question
What will the following code print?<br><br>
```java
class Parent {
    void display() {
        System.out.print("Parent ");
    }
}

class Child extends Parent {
    void display() {
        super.display();
        System.out.print("Child ");
    }
}

public class Test {
    public static void main(String[] args) {
        Parent p = new Child();
        p.display();
    }
}
```
<br><br>
Please select 1 option<br><br>
A) Parent<br>
B) Parent Child<br>
C) Child Parent<br>
D) Child

## Réponse
<strong>Réponse correcte :</strong> B)<br><br>
<strong>METHOD OVERRIDING + super KEYWORD:</strong><br><br>
Execution flow:<br>
• <strong>Parent p = new Child();</strong><br>
→ Reference type: Parent<br>
→ Object type: <strong>Child</strong><br><br>
• <strong>p.display();</strong><br>
→ Calls <strong>Child's display()</strong> (polymorphism - runtime decision)<br><br>
• Inside Child's display():<br>
→ <strong>super.display();</strong> calls Parent's version → prints <strong>"Parent "</strong><br>
→ Then prints <strong>"Child "</strong><br><br>
Output: <strong>Parent Child</strong><br><br>
<strong>KEY CONCEPTS:</strong><br>
• <strong>super.methodName()</strong> calls the parent class's version of the method<br>
• This is common when you want to <strong>extend</strong> parent behavior, not replace it<br>
• The method called is determined by the <strong>object type</strong> (Child), not reference type<br><br>
<strong>A) is incorrect:</strong> Child's display() also executes.<br>
<strong>C) is incorrect:</strong> super.display() is called first.<br>
<strong>D) is incorrect:</strong> Parent's display() is also called via super.

## Question
Given the following code:<br><br>
```java
class Person {
    private int age;
    
    public void setAge(int age) {
        if (age > 0 && age < 150) {
            this.age = age;
        }
    }
    
    public int getAge() {
        return age;
    }
}

public class Test {
    public static void main(String[] args) {
        Person p = new Person();
        p.age = 25;
        System.out.println(p.getAge());
    }
}
```
<br><br>
What is the result?<br><br>
Please select 1 option<br><br>
A) 25<br>
B) 0<br>
C) Compilation error at line: p.age = 25<br>
D) Runtime error

## Réponse
<strong>Réponse correcte :</strong> C)<br><br>
<strong>ENCAPSULATION VIOLATION:</strong> The field <strong>age</strong> is declared <strong>private</strong>.<br><br>
Analysis:<br>
• <strong>private int age;</strong> means age is <strong>only accessible within the Person class</strong><br>
• Attempting to access <strong>p.age = 25</strong> from outside the class (in Test.main) causes a <strong>compilation error</strong><br><br>
<strong>Compilation error:</strong> "age has private access in Person"<br><br>
<strong>ENCAPSULATION PRINCIPLE:</strong><br>
• Fields are declared <strong>private</strong> to hide implementation details<br>
• Access is controlled through <strong>public getter/setter methods</strong><br>
• This allows validation (e.g., age must be between 0 and 150)<br><br>
<strong>Correct usage:</strong><br>
```java
p.setAge(25);  // uses setter
System.out.println(p.getAge());  // uses getter
```
<br><br>
<strong>A), B), D) are incorrect:</strong> The code does not compile, so it never runs.

## Question
Which statements about abstract classes in Java are correct?<br><br>

Please select 3 options<br><br>

A) An abstract class can contain both abstract and non-abstract (concrete) methods<br>
B) An abstract class must declare at least one abstract method<br>
C) You cannot instantiate an abstract class directly with new<br>
D) A non-abstract subclass must implement all inherited abstract methods

## Réponse

<strong>Réponse correcte :</strong> A), C), D)<br><br>

<strong>A) is correct:</strong> An abstract class can mix abstract and concrete methods. Concrete methods provide shared behavior; abstract methods force subclasses to provide their own implementation.<br><br>

<strong>C) is correct:</strong> Writing <strong>new AbstractClass()</strong> directly causes a <strong>compilation error</strong>. However, an abstract-type reference can point to a concrete subclass:<br>
```java
Shape s = new Circle();  // valid — Circle is concrete
```
<br><br>

<strong>D) is correct:</strong> A non-abstract (concrete) subclass <strong>must override every abstract method</strong> it inherits, or the compiler reports an error.<br><br>

<strong>B) is incorrect:</strong> A class can be declared <strong>abstract without any abstract methods</strong>. This is perfectly legal and simply prevents direct instantiation:<br>
```java
abstract class Base {
    void hello() { System.out.println("Hello"); }  // no abstract method — still valid
}
```

## Question
What is the result of compiling this code?<br><br>

```java
abstract class Animal {
    abstract void makeSound();

    void breathe() {
        System.out.print("Breathing ");
    }
}

class Fish extends Animal {
    void breathe() {
        System.out.print("Gill breathing ");
    }
}
```
<br><br>

Please select 1 option<br><br>

A) Compiles successfully; Fish inherits an empty makeSound() from Animal<br>
B) Compiles successfully; Fish overrides breathe() and inherits makeSound()<br>
C) Compilation error: Fish is not abstract and does not override abstract method makeSound()<br>
D) Runtime error when makeSound() is called on a Fish instance

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

<strong>ABSTRACT METHOD CONTRACT:</strong> A non-abstract subclass <strong>must implement every abstract method</strong> it inherits.<br><br>

Problem:<br>
• Animal declares <strong>abstract void makeSound()</strong><br>
• Fish extends Animal but does <strong>NOT</strong> override makeSound()<br>
• Fish is not declared abstract<br>
• <strong>Compilation error:</strong> "Fish is not abstract and does not override abstract method makeSound() in Animal"<br><br>

Two valid fixes:<br>
1. Implement makeSound() in Fish:<br>
```java
class Fish extends Animal {
    void makeSound() { System.out.print("Blub "); }
    void breathe()   { System.out.print("Gill breathing "); }
}
```
<br>
2. Declare Fish as abstract (defer the obligation):<br>
```java
abstract class Fish extends Animal {
    void breathe() { System.out.print("Gill breathing "); }
}
```
<br><br>

<strong>A) is incorrect:</strong> Abstract methods have no body; there is no default empty implementation.<br>
<strong>B) is incorrect:</strong> makeSound() cannot simply be "inherited" unimplemented in a concrete class.<br>
<strong>D) is incorrect:</strong> The error occurs at compile time, not runtime.

## Question
What will the following code print?<br><br>

```java
interface Printable {
    default void print() {
        System.out.print("Default ");
    }
    void preview();
}

class Document implements Printable {
    public void preview() {
        System.out.print("Preview ");
    }
}

public class Test {
    public static void main(String[] args) {
        Document doc = new Document();
        doc.print();
        doc.preview();
    }
}
```
<br><br>

Please select 1 option<br><br>

A) Compilation error: Document must override print()<br>
B) Default Preview<br>
C) Compilation error: Document does not implement preview()<br>
D) Preview Default

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>INTERFACE DEFAULT METHODS (Java 8+):</strong> A <strong>default method</strong> provides a ready-made implementation in the interface. Implementing classes are <strong>not required</strong> to override it.<br><br>

Analysis:<br>
• <strong>print()</strong> is a default method → Document uses it as-is<br>
• <strong>preview()</strong> is an abstract method → Document <strong>must</strong> implement it (it does)<br>
• <strong>doc.print()</strong> → calls the default implementation → prints <strong>"Default "</strong><br>
• <strong>doc.preview()</strong> → calls Document's implementation → prints <strong>"Preview "</strong><br><br>

Output: <strong>Default Preview</strong><br><br>

<strong>KEY RULE:</strong><br>
• Regular interface methods (no body) → must be implemented by any non-abstract class<br>
• <strong>default</strong> interface methods → optional to override; the interface's body is used if not overridden<br><br>

<strong>A) is incorrect:</strong> Default methods do not need to be overridden.<br>
<strong>C) is incorrect:</strong> Document does implement preview().<br>
<strong>D) is incorrect:</strong> print() is called before preview().

## Question
Which statements about implementing an interface in Java are correct?<br><br>

Please select 2 options<br><br>

A) A non-abstract class that implements an interface must provide implementations for all abstract methods declared in that interface<br>
B) A class can implement at most one interface<br>
C) An abstract class that implements an interface is not required to implement the interface's abstract methods<br>
D) Interface fields are instance variables, so each implementing class gets its own copy

## Réponse

<strong>Réponse correcte :</strong> A), C)<br><br>

<strong>A) is correct:</strong> A concrete (non-abstract) class must implement <strong>every abstract method</strong> inherited from the interface, or a compilation error occurs.<br><br>

<strong>C) is correct:</strong> An abstract class implementing an interface may leave abstract methods unimplemented, deferring the obligation to its first concrete subclass:<br>
```java
interface Flyable { void fly(); }

abstract class Bird implements Flyable {
    // fly() not implemented here — Bird is abstract, so this is valid
}

class Eagle extends Bird {
    public void fly() { System.out.print("Eagle flying "); }  // must implement here
}
```
<br><br>

<strong>B) is incorrect:</strong> A class can implement <strong>multiple interfaces</strong>:<br>
```java
class Duck implements Flyable, Swimmable { ... }
```
<br><br>

<strong>D) is incorrect:</strong> Interface fields are implicitly <strong>public static final</strong> (constants). They are shared class-level values, not per-instance variables.

## Question
What is the result of compiling this code?<br><br>

```java
class Vehicle {
    public void start() {
        System.out.print("Vehicle start ");
    }
}

class Car extends Vehicle {
    private void start() {
        System.out.print("Car start ");
    }
}
```
<br><br>

Please select 1 option<br><br>

A) Compiles successfully; Car.start() overrides Vehicle.start() with private access<br>
B) Compilation error: cannot reduce the visibility of the inherited method from Vehicle<br>
C) Compiles successfully; Car.start() hides Vehicle.start()<br>
D) Runtime error when start() is called on a Car reference

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>METHOD OVERRIDING VISIBILITY RULE:</strong> When overriding a method, the access modifier in the subclass <strong>cannot be more restrictive</strong> than in the superclass.<br><br>

Problem:<br>
• Vehicle.start() is <strong>public</strong><br>
• Car.start() is <strong>private</strong><br>
• private is MORE restrictive than public<br>
• <strong>Compilation error:</strong> "start() in Car cannot override start() in Vehicle; attempting to assign weaker access privileges"<br><br>

Valid access modifier changes when overriding:<br>
• <strong>public → public</strong> ✅ (same)<br>
• <strong>protected → protected or public</strong> ✅ (same or broader)<br>
• <strong>package-private → package-private, protected, or public</strong> ✅ (same or broader)<br>
• <strong>Never reduce visibility</strong> ❌<br><br>

<strong>A) is incorrect:</strong> Reducing visibility to private is not allowed — compilation error.<br>
<strong>C) is incorrect:</strong> Method hiding applies only to <strong>static</strong> methods, not instance methods.<br>
<strong>D) is incorrect:</strong> The error occurs at compile time, not runtime.

## Question
What will the following code print?<br><br>
```java
public class Test {
    public static void main(String[] args) {
        int x = 5;
        switch(x) {
            case 5:
                System.out.print("Five ");
                break;
            case 10:
                System.out.print("Ten ");
        }
        System.out.print("Done");
    }
}
```
<br><br>
Please select 1 option<br><br>
A) Five Ten Done<br>
B) Five<br>
C) Five Done<br>
D) Done

## Réponse
<strong>Réponse correcte :</strong> C)<br><br>
<strong>BREAK BEHAVIOR:</strong> The <strong>break</strong> statement exits the <strong>switch statement only</strong>, not the entire method.<br><br>
Execution flow:<br>
• x = 5 matches <strong>case 5:</strong><br>
• Prints <strong>"Five "</strong><br>
• <strong>break;</strong> exits the switch<br>
• Program continues after the switch<br>
• Prints <strong>"Done"</strong><br><br>
Output: <strong>Five Done</strong><br><br>
<strong>KEY DISTINCTION:</strong><br>
• <strong>break</strong> = exits switch or loop only<br>
• <strong>return</strong> = exits the entire method<br><br>
<strong>A) is incorrect:</strong> break prevents fall-through to case 10.<br>
<strong>B) is incorrect:</strong> Program continues after the switch.<br>
<strong>D) is incorrect:</strong> case 5 matches and prints "Five " first.

## Question
What will the following code print?<br><br>
```java
public class Test {
    public static void main(String[] args) {
        String s1 = "Hello";
        s1.concat(" World");
        s1.toUpperCase();
        System.out.println(s1);
    }
}
```
<br><br>
Please select 1 option<br><br>
A) Hello<br>
B) Hello World<br>
C) HELLO WORLD<br>
D) HELLO

## Réponse
<strong>Réponse correcte :</strong> A)<br><br>
<strong>STRING IMMUTABILITY TRAP:</strong> Strings in Java are <strong>immutable</strong>. All String methods return <strong>new String objects</strong> without modifying the original.<br><br>
Analysis:<br>
• <strong>String s1 = "Hello";</strong> → s1 points to "Hello"<br>
• <strong>s1.concat(" World");</strong> → Creates new String "Hello World" but <strong>NOT assigned</strong> to s1<br>
• <strong>s1.toUpperCase();</strong> → Creates new String "HELLO" but <strong>NOT assigned</strong> to s1<br>
• s1 remains unchanged: <strong>"Hello"</strong><br><br>
<strong>Correct code would be:</strong><br>
```java
s1 = s1.concat(" World");
s1 = s1.toUpperCase();
```
<br><br>
<strong>KEY CONCEPT:</strong> String objects cannot be modified. All operations return <strong>new String objects</strong> that must be assigned if you want to use them.<br><br>
<strong>B) is incorrect:</strong> concat() result was not assigned.<br>
<strong>C) is incorrect:</strong> Neither method result was assigned.<br>
<strong>D) is incorrect:</strong> Only the original value remains.

## Question
What will the following code print?<br><br>
```java
public class Test {
    public static void main(String[] args) {
        String[] names = {"Alice", "Bob"};
        String[] copy = names;
        copy[0] = "Charlie";
        System.out.println(names[0] + " " + copy[0]);
    }
}
```
<br><br>
Please select 1 option<br><br>
A) Alice Alice<br>
B) Alice Charlie<br>
C) Charlie Alice<br>
D) Charlie Charlie

## Réponse
<strong>Réponse correcte :</strong> D)<br><br>
<strong>ARRAY REFERENCE TRAP:</strong> Assigning an array to another variable copies the <strong>reference</strong>, NOT the array content.<br><br>
Step-by-step:<br>
• <strong>String[] names = {"Alice", "Bob"};</strong><br>
→ Creates array with "Alice" at index 0<br><br>
• <strong>String[] copy = names;</strong><br>
→ Does NOT create a new array<br>
→ <strong>copy</strong> now points to the <strong>same array</strong> as names<br><br>
• <strong>copy[0] = "Charlie";</strong><br>
→ Changes the array at index 0<br>
→ Both <strong>names</strong> and <strong>copy</strong> see this change (same array)<br><br>
Output: <strong>Charlie Charlie</strong><br><br>
<strong>CRITICAL RULE:</strong> Arrays are objects. Assigning one array variable to another copies the <strong>reference</strong> (pointer), not the contents.<br><br>
To create a true copy:<br>
```java
String[] copy = names.clone();
// OR
String[] copy = Arrays.copyOf(names, names.length);
```
<br><br>
<strong>A), B), C) are incorrect:</strong> Both variables reference the same array.

## Question
What is the output of this code?<br><br>
```java
public class Test {
    static void process(int value) {
        switch(value) {
            case 1:
                System.out.print("One ");
                return;
            case 2:
                System.out.print("Two ");
                break;
            default:
                System.out.print("Other ");
        }
        System.out.print("End");
    }
    
    public static void main(String[] args) {
        process(1);
        System.out.print(" | ");
        process(2);
    }
}
```
<br><br>
Please select 1 option<br><br>
A) One End | Two End<br>
B) One | Two End<br>
C) One Two End<br>
D) One | Two

## Réponse
<strong>Réponse correcte :</strong> B)<br><br>
<strong>RETURN vs BREAK in switch:</strong><br><br>
<strong>First call: process(1)</strong><br>
• Matches <strong>case 1:</strong><br>
• Prints <strong>"One "</strong><br>
• <strong>return;</strong> exits the <strong>entire method</strong><br>
• "End" is <strong>NOT printed</strong><br><br>
<strong>Second call: process(2)</strong><br>
• Matches <strong>case 2:</strong><br>
• Prints <strong>"Two "</strong><br>
• <strong>break;</strong> exits the <strong>switch only</strong><br>
• Continues to print <strong>"End"</strong><br><br>
Output: <strong>One | Two End</strong><br><br>
<strong>KEY DIFFERENCES:</strong><br>
• <strong>return</strong> = exits the entire method immediately<br>
• <strong>break</strong> = exits only the switch/loop, method continues<br><br>
<strong>A) is incorrect:</strong> return in case 1 prevents "End" from printing.<br>
<strong>C) is incorrect:</strong> The separator " | " is printed between calls.<br>
<strong>D) is incorrect:</strong> After break in case 2, "End" is printed.

## Question
What will the following code print?<br><br>
```java
public class Test {
    public static void main(String[] args) {
        String s1 = "Java";
        String s2 = "Java";
        String s3 = new String("Java");
        
        System.out.print((s1 == s2) + " ");
        System.out.print((s1 == s3) + " ");
        System.out.print(s1.equals(s3));
    }
}
```
<br><br>
Please select 1 option<br><br>
A) true true true<br>
B) false false true<br>
C) true false true<br>
D) true true false

## Réponse
<strong>Réponse correcte :</strong> C)<br><br>
<strong>STRING COMPARISON TRAP:</strong> <strong>==</strong> compares references, <strong>equals()</strong> compares content.<br><br>
Analysis:<br>
• <strong>String s1 = "Java";</strong><br>
→ String literal stored in <strong>String pool</strong><br><br>
• <strong>String s2 = "Java";</strong><br>
→ Java reuses the <strong>same object</strong> from String pool<br>
→ s1 and s2 point to the <strong>same object</strong><br>
→ <strong>s1 == s2</strong> = <strong>true</strong><br><br>
• <strong>String s3 = new String("Java");</strong><br>
→ Creates a <strong>new object</strong> on the heap<br>
→ s3 points to a <strong>different object</strong> than s1<br>
→ <strong>s1 == s3</strong> = <strong>false</strong><br><br>
• <strong>s1.equals(s3)</strong><br>
→ Compares <strong>content</strong>, not references<br>
→ Both contain "Java"<br>
→ <strong>true</strong><br><br>
Output: <strong>true false true</strong><br><br>
<strong>CRITICAL RULE for OCP:</strong><br>
• Use <strong>==</strong> only for reference comparison<br>
• Use <strong>equals()</strong> for content comparison<br><br>
<strong>A) is incorrect:</strong> new String() creates a different object.<br>
<strong>B) is incorrect:</strong> String literals are pooled.<br>
<strong>D) is incorrect:</strong> equals() compares content (true).

## Question
Which statements about arrays and ArrayList are correct?<br><br>
Please select 2 options<br><br>
A) An array has a fixed size that cannot be changed after creation<br>
B) ArrayList can store primitive types like int directly<br>
C) Arrays provide an add() method to insert elements<br>
D) ArrayList size grows dynamically as elements are added

## Réponse
<strong>Réponse correcte :</strong> A), D)<br><br>
<strong>A) is correct:</strong> Arrays have a <strong>fixed size</strong> set at creation time. Once created, the size cannot change.<br>
```java
int[] arr = new int[5];  // size is 5 forever
```
<br><br>
<strong>D) is correct:</strong> ArrayList is <strong>dynamic</strong>. It automatically grows when you add elements beyond its current capacity.<br>
```java
List<String> list = new ArrayList<>();
list.add("A");  // size becomes 1
list.add("B");  // size becomes 2
```
<br><br>
<strong>B) is incorrect:</strong> ArrayList can <strong>ONLY</strong> store objects, not primitives. You must use <strong>wrapper classes</strong>:<br>
```java
ArrayList<Integer> list = new ArrayList<>();  // NOT ArrayList<int>
```
<br><br>
<strong>C) is incorrect:</strong> Arrays do <strong>NOT</strong> have an add() method. You must access elements by index:<br>
```java
arr[0] = 10;  // correct
arr.add(10);  // ERROR: arrays don't have add()
```

## Question
What happens when this code is executed?<br><br>
```java
public class Test {
    public static void main(String[] args) {
        int count = 0;
        while(count < 5) {
            System.out.print(count + " ");
        }
    }
}
```
<br><br>
Please select 1 option<br><br>
A) Prints: 0 1 2 3 4<br>
B) Prints: 0 1 2 3 4 5<br>
C) Compilation error<br>
D) Infinite loop printing 0 repeatedly

## Réponse
<strong>Réponse correcte :</strong> D)<br><br>
<strong>INFINITE LOOP TRAP:</strong> The loop condition never changes because <strong>count</strong> is never modified inside the loop.<br><br>
Analysis:<br>
• <strong>while(count < 5)</strong> checks if count < 5<br>
• count starts at 0 (0 < 5 is true)<br>
• Prints <strong>0</strong><br>
• Loop repeats<br>
• count is <strong>still 0</strong> (never incremented)<br>
• Condition is <strong>still true</strong><br>
• Loop continues <strong>forever</strong><br><br>
<strong>CRITICAL RULE:</strong> A loop must modify the variable(s) in its condition, or it will run infinitely.<br><br>
<strong>Correct code:</strong><br>
```java
while(count < 5) {
    System.out.print(count + " ");
    count++;  // REQUIRED
}
```
<br><br>
<strong>A) is incorrect:</strong> Would require count++ inside the loop.<br>
<strong>B) is incorrect:</strong> Same issue, plus wrong range.<br>
<strong>C) is incorrect:</strong> The code compiles (but runs forever).

## Question
What will the following code print?<br><br>
```java
public class Test {
    static int calculate(String op, int a, int b) {
        switch(op) {
            case "+":
                return a + b;
            case "-":
                return a - b;
            case "*":
                return a * b;
            default:
                return 0;
        }
    }
    
    public static void main(String[] args) {
        System.out.print(calculate("+", 5, 3) + " ");
        System.out.print(calculate("-", 5, 3) + " ");
        System.out.print(calculate("/", 5, 3));
    }
}
```
<br><br>
Please select 1 option<br><br>
A) 8 2 0<br>
B) 8 2 0<br>
C) Compilation error: missing break statements<br>
D) 8 2 ArithmeticException

## Réponse
<strong>Réponse correcte :</strong> B)<br><br>
<strong>RETURN in switch:</strong> Using <strong>return</strong> eliminates the need for <strong>break</strong> statements.<br><br>
Execution:<br>
• <strong>calculate("+", 5, 3)</strong><br>
→ Matches case "+"<br>
→ <strong>return 5 + 3;</strong> exits method immediately with value <strong>8</strong><br><br>
• <strong>calculate("-", 5, 3)</strong><br>
→ Matches case "-"<br>
→ <strong>return 5 - 3;</strong> exits method immediately with value <strong>2</strong><br><br>
• <strong>calculate("/", 5, 3)</strong><br>
→ No matching case<br>
→ Falls to <strong>default</strong><br>
→ <strong>return 0;</strong> exits method with value <strong>0</strong><br><br>
Output: <strong>8 2 0</strong><br><br>
<strong>KEY CONCEPT:</strong> <strong>return</strong> immediately exits the method, so no <strong>break</strong> is needed. This is a common pattern for methods that return values from switch statements.<br><br>
<strong>A) is incorrect:</strong> This is the same as B (typo in options).<br>
<strong>C) is incorrect:</strong> return statements make break unnecessary.<br>
<strong>D) is incorrect:</strong> No division occurs; default returns 0.

## Question
What will the following code print?<br><br>
```java
public class Test {
    public static void main(String[] args) {
        String str1 = "hello";
        String str2 = "hello";
        String str3 = str1;
        
        if (str1 == str2) {
            System.out.print("A");
        }
        
        if (str1.equals(str2)) {
            System.out.print("B");
        }
        
        if (str1 == str3) {
            System.out.print("C");
        }
        
        if (!str1.equals("world")) {
            System.out.print("D");
        }
    }
}
```
<br><br>
Please select 1 option<br><br>
A) ABCD<br>
B) BCD<br>
C) ABCD<br>
D) ABD

## Réponse
<strong>Réponse correcte :</strong> C)<br><br>
<strong>STRING COMPARISON COMPREHENSIVE:</strong><br><br>
• <strong>if (str1 == str2)</strong><br>
→ Both are string literals "hello"<br>
→ Java uses <strong>String pool</strong>: both reference the <strong>same object</strong><br>
→ Reference comparison: <strong>true</strong> → prints <strong>"A"</strong><br><br>
• <strong>if (str1.equals(str2))</strong><br>
→ Content comparison<br>
→ Both contain "hello"<br>
→ <strong>true</strong> → prints <strong>"B"</strong><br><br>
• <strong>if (str1 == str3)</strong><br>
→ str3 = str1 (reference assignment)<br>
→ Both point to the <strong>same object</strong><br>
→ Reference comparison: <strong>true</strong> → prints <strong>"C"</strong><br><br>
• <strong>if (!str1.equals("world"))</strong><br>
→ str1 is "hello", not "world"<br>
→ equals() returns false<br>
→ <strong>!</strong> negates it to <strong>true</strong> → prints <strong>"D"</strong><br><br>
Output: <strong>ABCD</strong><br><br>
<strong>KEY CONCEPTS:</strong><br>
• String literals are pooled (same reference for same value)<br>
• Reference assignment (=) copies the pointer<br>
• <strong>!</strong> negates a boolean expression<br><br>
<strong>A), C) are identical:</strong> Both are ABCD (correct).<br>
<strong>B), D) are incorrect:</strong> All four conditions are true.

## Question
What is the result of executing this code?<br><br>
```java
public class Test {
    public static void main(String[] args) {
        int[] arr1 = {10, 20, 30};
        int[] arr2 = arr1;
        arr2[1] = 99;
        
        arr1 = new int[]{5, 15, 25};
        arr2[0] = 100;
        
        System.out.println(arr1[0] + " " + arr1[1] + " " + arr2[1]);
    }
}
```
<br><br>
Please select 1 option<br><br>
A) 5 15 99<br>
B) 100 99 99<br>
C) 5 15 100<br>
D) 100 15 99

## Réponse
<strong>Réponse correcte :</strong> A)<br><br>
<strong>ARRAY REFERENCE REASSIGNMENT:</strong><br><br>
Initial state:<br>
• arr1 → [10, 20, 30]<br>
• arr2 = arr1 → both point to <strong>same array</strong><br><br>
• <strong>arr2[1] = 99;</strong><br>
→ Changes shared array: [10, <strong>99</strong>, 30]<br>
→ Both arr1 and arr2 see this change<br><br>
• <strong>arr1 = new int[]{5, 15, 25};</strong><br>
→ arr1 now points to a <strong>NEW array</strong>: [5, 15, 25]<br>
→ arr2 <strong>still points to the old array</strong>: [10, 99, 30]<br><br>
• <strong>arr2[0] = 100;</strong><br>
→ Changes the <strong>old array</strong>: [<strong>100</strong>, 99, 30]<br>
→ arr1 is <strong>unaffected</strong> (points to different array)<br><br>
Final state:<br>
• arr1 → [5, 15, 25]<br>
• arr2 → [100, 99, 30]<br><br>
Output: <strong>arr1[0]=5, arr1[1]=15, arr2[1]=99</strong> → <strong>5 15 99</strong><br><br>
<strong>KEY CONCEPT:</strong> Reassigning a variable (<strong>=</strong>) makes it point to a different object. The old object remains accessible through other references.<br><br>
<strong>B), C), D) are incorrect:</strong> Misunderstand which reference points to which array after reassignment.

## Question
What will the following code print?<br><br>
```java
public class Test {
    public static void main(String[] args) {
        for (int i = 0; i < 5; i++) {
            if (i == 2) {
                break;
            }
            System.out.print(i + " ");
        }
        System.out.print("Done");
    }
}
```
<br><br>
Please select 1 option<br><br>
A) 0 1 2 Done<br>
B) 0 1 2 3 4 Done<br>
C) 0 1 Done<br>
D) 0 1

## Réponse
<strong>Réponse correcte :</strong> C)<br><br>
<strong>BREAK in for loop:</strong> <strong>break</strong> exits the loop immediately, but the program continues after the loop.<br><br>
Execution:<br>
• i = 0: if (i == 2) is false → prints <strong>"0 "</strong><br>
• i = 1: if (i == 2) is false → prints <strong>"1 "</strong><br>
• i = 2: if (i == 2) is <strong>true</strong><br>
→ <strong>break;</strong> exits the loop immediately<br>
→ "2 " is <strong>NOT printed</strong><br>
• Program continues after the for loop<br>
• Prints <strong>"Done"</strong><br><br>
Output: <strong>0 1 Done</strong><br><br>
<strong>KEY DISTINCTION:</strong><br>
• <strong>break</strong> = exits the loop, program continues<br>
• <strong>return</strong> = would exit the entire method (no "Done")<br><br>
<strong>A) is incorrect:</strong> 2 is not printed because break executes before the print.<br>
<strong>B) is incorrect:</strong> Loop terminates at i=2.<br>
<strong>D) is incorrect:</strong> "Done" is printed after the loop exits.

## Question
Which statements about ArrayList are correct?<br><br>
Please select 3 options<br><br>
A) ArrayList provides a remove() method to delete elements<br>
B) ArrayList can be created without specifying a size<br>
C) ArrayList can store primitive types like int directly<br>
D) ArrayList requires importing java.util.ArrayList or java.util.List

## Réponse
<strong>Réponse correcte :</strong> A), B), D)<br><br>
<strong>A) is correct:</strong> ArrayList provides <strong>remove()</strong> to delete elements by index or by object:<br>
```java
list.remove(0);        // remove by index
list.remove("Java");   // remove by object
```
<br><br>
<strong>B) is correct:</strong> ArrayList has a <strong>dynamic size</strong>. You can create it without specifying capacity:<br>
```java
List<String> list = new ArrayList<>();  // no size needed
```
<br><br>
<strong>D) is correct:</strong> ArrayList is in the <strong>java.util</strong> package and must be imported:<br>
```java
import java.util.ArrayList;
import java.util.List;
```
<br><br>
<strong>C) is incorrect:</strong> ArrayList can <strong>ONLY</strong> store objects. For primitives, you must use <strong>wrapper classes</strong>:<br>
```java
ArrayList<Integer> nums = new ArrayList<>();  // Integer, NOT int
```
Java performs <strong>autoboxing</strong> to convert int ↔ Integer automatically, but the ArrayList itself stores Integer objects.

## Question
What will the following code print?<br><br>
```java
public class Test {
    public static void main(String[] args) {
        String result = "";
        String s1 = "Hello";
        String s2 = s1;
        s1 = s1 + " World";
        result = result + s1 + " " + s2;
        System.out.println(result);
    }
}
```
<br><br>
Please select 1 option<br><br>
A) Hello World Hello<br>
B) Hello Hello<br>
C) Hello World Hello World<br>
D) Compilation error

## Réponse
<strong>Réponse correcte :</strong> A)<br><br>
<strong>STRING IMMUTABILITY + CONCATENATION:</strong><br><br>
Step-by-step:<br>
• <strong>String s1 = "Hello";</strong><br>
→ s1 points to "Hello"<br><br>
• <strong>String s2 = s1;</strong><br>
→ s2 also points to "Hello" (same object)<br><br>
• <strong>s1 = s1 + " World";</strong><br>
→ Creates a <strong>NEW String</strong> "Hello World"<br>
→ s1 now points to the new String<br>
→ s2 <strong>still points to original</strong> "Hello"<br>
→ String immutability means the original "Hello" is unchanged<br><br>
• <strong>result = result + s1 + " " + s2;</strong><br>
→ result = "" + "Hello World" + " " + "Hello"<br>
→ result = <strong>"Hello World Hello"</strong><br><br>
Output: <strong>Hello World Hello</strong><br><br>
<strong>KEY CONCEPTS:</strong><br>
• String concatenation with <strong>+</strong> creates new String objects<br>
• Strings are immutable: original objects never change<br>
• Reference assignment copies the pointer, but later reassignment breaks the connection<br><br>
<strong>B) is incorrect:</strong> s1 was concatenated with " World".<br>
<strong>C) is incorrect:</strong> s2 was never modified; still points to "Hello".<br>
<strong>D) is incorrect:</strong> The code compiles and runs successfully.

## Question

Which statements about inheritance in Java are correct?<br><br>

Please select 3 options<br><br>

A) A class can extend multiple classes using commas<br>
B) A subclass inherits non-private methods and fields from its parent<br>
C) A subclass inherits the constructors of its parent class<br>
D) The keyword `extends` establishes an "is-a" relationship

## Réponse

<strong>Réponse correcte :</strong> B), D)<br><br>

<strong>B) is correct:</strong> A subclass inherits all <strong>non-private</strong> members (methods and fields) from its parent. Private members exist in the parent object but are <strong>not directly accessible</strong> from the subclass.<br><br>

<strong>D) is correct:</strong> <strong>extends</strong> creates an "is-a" relationship: <strong>Dog extends Animal</strong> means "a Dog IS an Animal".<br><br>

<strong>A) is incorrect:</strong> Java supports <strong>single inheritance only</strong>. A class can extend <strong>exactly one</strong> class:<br>
```java
class Dog extends Animal { }          // ✅ valid
class Dog extends Animal, Pet { }     // ❌ compilation error
```
For multiple capabilities, use interfaces: <strong>class Dog extends Animal implements Pet</strong><br><br>

<strong>C) is incorrect:</strong> Constructors are <strong>NOT inherited</strong>. A subclass must define its own constructors. The parent constructor is <strong>called</strong> (via super()), but not inherited.

## Question

What is the result of compiling this code?<br><br>

```java
class Animal {
    private String name = "Animal";

    private void display() {
        System.out.print(name);
    }
}

class Dog extends Animal {
    public static void main(String[] args) {
        Dog d = new Dog();
        System.out.print(d.name);
    }
}
```
<br><br>

Please select 1 option<br><br>

A) Animal<br>
B) null<br>
C) Compilation error: name has private access in Animal<br>
D) Runtime error

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

<strong>PRIVATE MEMBERS ARE NOT INHERITED:</strong> Private fields and methods are <strong>not accessible</strong> from subclasses.<br><br>

Analysis:<br>
• <strong>name</strong> is declared <strong>private</strong> in Animal<br>
• Dog extends Animal but <strong>cannot access</strong> private members<br>
• <strong>d.name</strong> causes compilation error<br>
• Similarly, <strong>d.display()</strong> would also fail<br><br>

<strong>What IS inherited:</strong><br>
• public members → accessible everywhere<br>
• protected members → accessible in subclasses and same package<br>
• package-private (default) members → accessible in same package<br><br>

<strong>What is NOT inherited:</strong><br>
• private members<br>
• constructors<br><br>

<strong>A), B) are incorrect:</strong> Code doesn't compile.<br>
<strong>D) is incorrect:</strong> Error occurs at compile time.

## Question

What is the result of compiling and running this code?<br><br>

```java
class Animal {
    String type = "Animal";
}

class Dog extends Animal {
    String type = "Dog";
}

public class Test {
    public static void main(String[] args) {
        Animal a = new Dog();
        Dog d = new Dog();
        System.out.print(a.type + " " + d.type);
    }
}
```
<br><br>

Please select 1 option<br><br>

A) Dog Dog<br>
B) Animal Dog<br>
C) Animal Animal<br>
D) Compilation error

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>CRITICAL OCP CONCEPT:</strong> Variables are resolved at <strong>compile time</strong> based on <strong>reference type</strong>. Unlike methods, variables are <strong>NOT polymorphic</strong>.<br><br>

Analysis:<br>
• <strong>Animal a = new Dog();</strong><br>
→ Reference type: <strong>Animal</strong><br>
→ <strong>a.type</strong> resolves to Animal's type → <strong>"Animal"</strong><br><br>

• <strong>Dog d = new Dog();</strong><br>
→ Reference type: <strong>Dog</strong><br>
→ <strong>d.type</strong> resolves to Dog's type → <strong>"Dog"</strong><br><br>

<strong>POLYMORPHISM RULE:</strong><br>
• <strong>Methods</strong> → resolved at <strong>runtime</strong> (dynamic dispatch) → polymorphic<br>
• <strong>Variables</strong> → resolved at <strong>compile time</strong> (reference type) → NOT polymorphic<br><br>

<strong>A) is incorrect:</strong> a.type uses Animal's reference type.<br>
<strong>C) is incorrect:</strong> d.type uses Dog's reference type.<br>
<strong>D) is incorrect:</strong> Field hiding is legal (no compilation error).

## Question

What is the result of compiling and running this code?<br><br>

```java
class Parent {
    int value = 10;

    int getValue() {
        return value;
    }
}

class Child extends Parent {
    int value = 20;

    int getValue() {
        return value;
    }
}

public class Test {
    public static void main(String[] args) {
        Parent p = new Child();
        System.out.print(p.value + " " + p.getValue());
    }
}
```
<br><br>

Please select 1 option<br><br>

A) 10 10<br>
B) 20 20<br>
C) 10 20<br>
D) 20 10

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

<strong>VARIABLES vs METHODS POLYMORPHISM:</strong> This is the most important distinction for the OCP exam.<br><br>

Analysis with <strong>Parent p = new Child();</strong><br><br>

• <strong>p.value</strong><br>
→ Variable → resolved at <strong>compile time</strong> → uses <strong>reference type (Parent)</strong><br>
→ Result: <strong>10</strong><br><br>

• <strong>p.getValue()</strong><br>
→ Method → resolved at <strong>runtime</strong> → uses <strong>object type (Child)</strong><br>
→ Child's getValue() returns Child's value (20)<br>
→ Result: <strong>20</strong><br><br>

Output: <strong>10 20</strong><br><br>

<strong>MEMORIZE:</strong><br>
• <strong>p.variable</strong> → compile time → Parent's variable<br>
• <strong>p.method()</strong> → runtime → Child's method<br><br>

<strong>A) is incorrect:</strong> getValue() is a method → resolved at runtime → calls Child's version.<br>
<strong>B) is incorrect:</strong> p.value is a variable → resolved at compile time → uses Parent's value.<br>
<strong>D) is incorrect:</strong> Reversed logic.

## Question

Which statements about method overriding are correct?<br><br>

Please select 3 options<br><br>

A) The overriding method must have the same signature as the parent method<br>
B) The overriding method can have a more restrictive access modifier<br>
C) The overriding method can return a subtype of the parent method's return type<br>
D) The @Override annotation is optional but recommended

## Réponse

<strong>Réponse correcte :</strong> A), C), D)<br><br>

<strong>A) is correct:</strong> Override requires the <strong>same method signature</strong> (same name, same parameter types and order).<br><br>

<strong>C) is correct:</strong> This is called <strong>covariant return type</strong>. The return type can be a subtype:<br>
```java
class Animal {
    Animal create() { return new Animal(); }
}

class Dog extends Animal {
    Dog create() { return new Dog(); }  // ✅ Dog is subtype of Animal
}
```
<br><br>

<strong>D) is correct:</strong> <strong>@Override</strong> is <strong>not required</strong> for overriding to work. However, it is strongly recommended because:<br>
• It protects against <strong>typos in method name</strong><br>
• It protects against <strong>wrong parameter types</strong><br>
• If the method does NOT actually override, the compiler reports an error<br>
• It does <strong>NOT change the behavior</strong> of the method<br><br>

<strong>B) is incorrect:</strong> The overriding method <strong>cannot reduce visibility</strong>:<br>
• public → must stay public<br>
• protected → can be protected or public<br>
• <strong>Never more restrictive</strong>

## Question

What is the result of compiling this code?<br><br>

```java
class Parent {
    void process() throws Exception {
        System.out.print("Parent ");
    }
}

class Child extends Parent {
    void process() throws Exception, RuntimeException {
        System.out.print("Child ");
    }
}
```
<br><br>

Please select 1 option<br><br>

A) Compilation error: overriding method throws a broader exception<br>
B) Compiles successfully<br>
C) Compilation error: cannot override process()<br>
D) Compilation error: multiple exceptions not allowed

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>EXCEPTION RULE IN OVERRIDING:</strong> The overriding method cannot throw <strong>new or broader checked exceptions</strong>, but can throw <strong>fewer, narrower, or unchecked exceptions</strong>.<br><br>

Analysis:<br>
• Parent declares <strong>throws Exception</strong><br>
• Child declares <strong>throws Exception, RuntimeException</strong><br>
• RuntimeException is a <strong>subclass of Exception</strong> (already covered by Exception)<br>
• Adding RuntimeException does not broaden the exception clause<br>
• <strong>Compiles successfully</strong><br><br>

<strong>OVERRIDE EXCEPTION RULES:</strong><br>
```java
// Parent: void m() throws IOException

void m() throws IOException { }           // ✅ same
void m() throws FileNotFoundException { }  // ✅ narrower (subclass)
void m() { }                              // ✅ fewer (none)
void m() throws RuntimeException { }      // ✅ unchecked always OK
void m() throws Exception { }             // ❌ broader
void m() throws IOException, SQLException { } // ❌ new checked exception
```
<br><br>

<strong>A) is incorrect:</strong> RuntimeException is narrower than Exception, not broader.<br>
<strong>C), D) are incorrect:</strong> The code is valid.

## Question

What is the result of compiling this code?<br><br>

```java
class Parent {
    void process() throws IOException {
        System.out.print("Parent ");
    }
}

class Child extends Parent {
    void process() throws Exception {
        System.out.print("Child ");
    }
}
```
<br><br>

Please select 1 option<br><br>

A) Compiles successfully<br>
B) Compilation error: overriding method throws a broader checked exception<br>
C) Compiles but throws exception at runtime<br>
D) Compilation error: missing import

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>BROADER EXCEPTION TRAP:</strong> An overriding method <strong>cannot throw a broader checked exception</strong> than the parent method.<br><br>

Analysis:<br>
• Parent declares <strong>throws IOException</strong><br>
• Child declares <strong>throws Exception</strong><br>
• <strong>Exception</strong> is a <strong>superclass</strong> of IOException → it is <strong>broader</strong><br>
• This violates the override exception rule<br><br>

<strong>WHY?</strong> Callers of Parent.process() only expect to handle IOException. If Child could throw Exception, it would break the contract:<br>
```java
Parent p = new Child();
try {
    p.process();  // caller only catches IOException
} catch (IOException e) {
    // wouldn't catch a broader Exception!
}
```
<br><br>

<strong>VALID alternatives for Child:</strong><br>
• throws IOException ✅ (same)<br>
• throws FileNotFoundException ✅ (narrower)<br>
• no throws clause ✅ (fewer)<br>
• throws RuntimeException ✅ (unchecked always OK)<br><br>

<strong>A) is incorrect:</strong> Exception is broader than IOException.<br>
<strong>C), D) are incorrect:</strong> Error is at compile time.

## Question

What is the result of compiling and running this code?<br><br>

```java
class Animal {
    void makeSound() {
        System.out.print("Generic ");
    }
}

class Cat extends Animal {
    void makeSound(String sound) {
        System.out.print(sound + " ");
    }
}

public class Test {
    public static void main(String[] args) {
        Cat c = new Cat();
        c.makeSound();
        c.makeSound("Meow");
    }
}
```
<br><br>

Please select 1 option<br><br>

A) Generic Meow<br>
B) Compilation error: makeSound() is ambiguous<br>
C) Meow Meow<br>
D) Compilation error: Cat must override makeSound()

## Réponse

<strong>Réponse correcte :</strong> A)<br><br>

<strong>OVERLOADING vs OVERRIDING:</strong> Cat does <strong>NOT override</strong> makeSound(). It <strong>overloads</strong> it with a different parameter list.<br><br>

Analysis:<br>
• Animal has <strong>makeSound()</strong> (no parameter)<br>
• Cat adds <strong>makeSound(String)</strong> (one parameter) → this is <strong>overloading</strong>, not overriding<br>
• Cat <strong>inherits</strong> makeSound() from Animal<br>
• Cat now has <strong>both</strong> methods available<br><br>

Execution:<br>
• <strong>c.makeSound()</strong> → calls inherited Animal version → <strong>"Generic "</strong><br>
• <strong>c.makeSound("Meow")</strong> → calls Cat's overloaded version → <strong>"Meow "</strong><br><br>

Output: <strong>Generic Meow</strong><br><br>

<strong>KEY DISTINCTION:</strong><br>
• <strong>Override</strong> = same signature → replaces parent behavior<br>
• <strong>Overload</strong> = different parameters → adds new behavior alongside<br><br>

<strong>B) is incorrect:</strong> No ambiguity; parameter count differs.<br>
<strong>C) is incorrect:</strong> makeSound() without arg uses the inherited version.<br>
<strong>D) is incorrect:</strong> Override is never mandatory for concrete methods.

## Question

What is the result of compiling and running this code?<br><br>

```java
abstract class Shape {
    int sides;

    Shape(int sides) {
        this.sides = sides;
        System.out.print("Shape(" + sides + ") ");
    }

    abstract double area();
}

class Square extends Shape {
    double side;

    Square(double side) {
        super(4);
        this.side = side;
    }

    double area() {
        return side * side;
    }
}

public class Test {
    public static void main(String[] args) {
        Square s = new Square(5.0);
        System.out.print(s.sides + " " + s.area());
    }
}
```
<br><br>

Please select 1 option<br><br>

A) Shape(4) 4 25.0<br>
B) 4 25.0<br>
C) Compilation error: abstract class cannot have a constructor<br>
D) Compilation error: abstract class cannot have instance variables

## Réponse

<strong>Réponse correcte :</strong> A)<br><br>

<strong>ABSTRACT CLASS CAN HAVE CONSTRUCTORS AND VARIABLES:</strong><br><br>

Analysis:<br>
• Abstract class Shape has:<br>
→ An <strong>instance variable</strong> (sides) ✅<br>
→ A <strong>constructor</strong> Shape(int sides) ✅<br>
→ An <strong>abstract method</strong> area() ✅<br><br>

Execution:<br>
• <strong>new Square(5.0)</strong> calls Square constructor<br>
• <strong>super(4)</strong> calls Shape(4) → prints <strong>"Shape(4) "</strong><br>
• <strong>s.sides</strong> = 4 (set by parent constructor)<br>
• <strong>s.area()</strong> = 5.0 * 5.0 = <strong>25.0</strong><br><br>

Output: <strong>Shape(4) 4 25.0</strong><br><br>

<strong>ABSTRACT CLASS CAN CONTAIN:</strong><br>
• Instance variables (non-final allowed) ✅<br>
• Constructors ✅<br>
• Concrete methods ✅<br>
• Abstract methods ✅<br>
• Static methods ✅<br><br>

<strong>ABSTRACT CLASS CANNOT:</strong><br>
• Be instantiated directly (new Shape() ❌)<br><br>

<strong>B) is incorrect:</strong> Shape constructor prints before the rest.<br>
<strong>C), D) are incorrect:</strong> Abstract classes CAN have constructors and variables.

## Question

What is the result of compiling this code?<br><br>

```java
abstract class Vehicle {
    void start() {
        System.out.print("Starting ");
    }
}

public class Test {
    public static void main(String[] args) {
        Vehicle v = new Vehicle();
        v.start();
    }
}
```
<br><br>

Please select 1 option<br><br>

A) Starting<br>
B) Compilation error: Vehicle is abstract; cannot be instantiated<br>
C) Runtime error<br>
D) Compilation error: abstract class must have abstract methods

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>ABSTRACT CLASS INSTANTIATION:</strong> You <strong>cannot</strong> create an instance of an abstract class directly with <strong>new</strong>.<br><br>

Analysis:<br>
• <strong>new Vehicle()</strong> → compilation error because Vehicle is abstract<br>
• Even though Vehicle has NO abstract methods, it is still abstract<br><br>

<strong>KEY RULES:</strong><br>
• A class declared <strong>abstract</strong> can have <strong>zero abstract methods</strong> → still valid<br>
• It simply prevents direct instantiation<br>
• Useful to force subclassing<br><br>

<strong>VALID usage:</strong><br>
```java
class Car extends Vehicle { }
Vehicle v = new Car();  // ✅ abstract reference, concrete object
v.start();              // prints "Starting"
```
<br><br>

<strong>A) is incorrect:</strong> Cannot instantiate an abstract class.<br>
<strong>C) is incorrect:</strong> Error occurs at compile time.<br>
<strong>D) is incorrect:</strong> Abstract classes do NOT require abstract methods.

## Question

Which statements about interface variables are correct?<br><br>

Please select 3 options<br><br>

A) Interface variables are implicitly public static final<br>
B) Interface variables must be initialized when declared<br>
C) Interface variables can be modified by implementing classes<br>
D) Interface variables are constants shared across all implementations

## Réponse

<strong>Réponse correcte :</strong> A), B), D)<br><br>

<strong>A) is correct:</strong> All variables in an interface are implicitly <strong>public static final</strong>, even if you don't write these modifiers:<br>
```java
interface Config {
    int MAX = 100;           // actually: public static final int MAX = 100;
    String NAME = "default"; // actually: public static final String NAME = "default";
}
```
<br><br>

<strong>B) is correct:</strong> Since they are <strong>final</strong>, they <strong>must be initialized</strong> at declaration. You cannot leave them uninitialized:<br>
```java
interface Config {
    int MAX;  // ❌ compilation error: variable MAX not initialized
}
```
<br><br>

<strong>D) is correct:</strong> Since they are <strong>static</strong>, they belong to the interface itself and are shared as <strong>constants</strong> across all implementing classes.<br><br>

<strong>C) is incorrect:</strong> Interface variables are <strong>final</strong> and <strong>cannot be modified</strong>:<br>
```java
class MyClass implements Config {
    void test() {
        MAX = 200;  // ❌ compilation error: cannot assign to final variable
    }
}
```

## Question

What is the result of compiling and running this code?<br><br>

```java
interface Printable {
    default void print() {
        System.out.print("Printable ");
    }

    static void info() {
        System.out.print("Info ");
    }
}

class Document implements Printable {
    public void print() {
        System.out.print("Document ");
    }
}

public class Test {
    public static void main(String[] args) {
        Document doc = new Document();
        doc.print();
        Printable.info();
        doc.info();
    }
}
```
<br><br>

Please select 1 option<br><br>

A) Document Info Info<br>
B) Compilation error at line: doc.info()<br>
C) Document Info<br>
D) Printable Document Info

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>INTERFACE STATIC METHODS:</strong> Static methods in an interface can <strong>only</strong> be called using the <strong>interface name</strong>, not through an instance or implementing class.<br><br>

Analysis:<br>
• <strong>doc.print()</strong> → calls Document's overridden version → OK<br>
• <strong>Printable.info()</strong> → calls static method via interface name → OK<br>
• <strong>doc.info()</strong> → <strong>compilation error</strong>: static interface methods are NOT inherited by implementing classes<br><br>

<strong>INTERFACE METHOD TYPES (Java 8/9+):</strong><br>
• <strong>abstract</strong> (default) → must be implemented by class<br>
• <strong>default</strong> (Java 8) → has body, optional to override, inherited<br>
• <strong>static</strong> (Java 8) → has body, called via InterfaceName.method(), NOT inherited<br>
• <strong>private</strong> (Java 9) → helper method, only usable within the interface<br><br>

<strong>A) is incorrect:</strong> doc.info() does not compile.<br>
<strong>C) is incorrect:</strong> The error prevents compilation.<br>
<strong>D) is incorrect:</strong> Code does not compile.

## Question

What is the result of compiling this code?<br><br>

```java
interface Flyable {
    void fly();
}

interface Swimmable {
    void swim();
}

class Duck implements Flyable, Swimmable {
    public void fly() {
        System.out.print("Flying ");
    }

    public void swim() {
        System.out.print("Swimming ");
    }
}

public class Test {
    public static void main(String[] args) {
        Flyable f = new Duck();
        f.fly();
        f.swim();
    }
}
```
<br><br>

Please select 1 option<br><br>

A) Flying Swimming<br>
B) Compilation error at line: f.swim()<br>
C) Compilation error: Duck cannot implement two interfaces<br>
D) Flying

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>INTERFACE REFERENCE LIMITATION:</strong> The reference type determines what methods are <strong>visible at compile time</strong>.<br><br>

Analysis:<br>
• <strong>Flyable f = new Duck();</strong><br>
→ Reference type: <strong>Flyable</strong><br>
→ Flyable only declares <strong>fly()</strong><br><br>

• <strong>f.fly()</strong> → OK, fly() exists in Flyable<br>
• <strong>f.swim()</strong> → <strong>compilation error</strong>: swim() is NOT in Flyable interface<br><br>

<strong>To fix:</strong><br>
```java
Duck d = new Duck();
d.fly();   // ✅
d.swim();  // ✅

// OR cast:
((Swimmable)f).swim();  // ✅
```
<br><br>

<strong>KEY RULE:</strong> A class CAN implement <strong>multiple interfaces</strong> (no limit). But you can only call methods visible through the <strong>reference type</strong>.<br><br>

<strong>A) is incorrect:</strong> f.swim() doesn't compile.<br>
<strong>C) is incorrect:</strong> Java allows multiple interfaces.<br>
<strong>D) is incorrect:</strong> Code doesn't compile (f.swim() error).

## Question

What is the result of compiling this code?<br><br>

```java
interface Runnable {
    void run();
}

class Task implements Runnable {
    void run() {
        System.out.print("Running");
    }
}
```
<br><br>

Please select 1 option<br><br>

A) Compiles successfully<br>
B) Compilation error: run() in Task must be public<br>
C) Compilation error: Task must declare run() as abstract<br>
D) Compiles but throws exception at runtime

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>INTERFACE METHOD VISIBILITY RULE:</strong> Interface methods are implicitly <strong>public abstract</strong>. When implementing them, the class <strong>must declare them as public</strong>.<br><br>

Problem:<br>
• Interface declares <strong>void run()</strong> → implicitly <strong>public abstract</strong><br>
• Task implements run() with <strong>package-private</strong> (default) access<br>
• Package-private is <strong>more restrictive</strong> than public<br>
• This violates the override rule: <strong>cannot reduce visibility</strong><br><br>

<strong>Compilation error:</strong> "run() in Task cannot implement run() in Runnable; attempting to assign weaker access privileges"<br><br>

<strong>Correct implementation:</strong><br>
```java
class Task implements Runnable {
    public void run() {  // MUST be public
        System.out.print("Running");
    }
}
```
<br><br>

<strong>A) is incorrect:</strong> Missing public modifier.<br>
<strong>C), D) are incorrect:</strong> The issue is visibility, not abstraction.

## Question

Which statements correctly describe the differences between abstract classes and interfaces?<br><br>

Please select 3 options<br><br>

A) An abstract class represents an "is-a" relationship, an interface represents a "can-do" capability<br>
B) An abstract class can have modifiable instance variables, an interface can only have constants<br>
C) A class can extend multiple abstract classes but implement only one interface<br>
D) An abstract class can have constructors, an interface cannot

## Réponse

<strong>Réponse correcte :</strong> A), B), D)<br><br>

<strong>A) is correct:</strong><br>
• Abstract class → <strong>"is-a"</strong> relationship (Dog IS an Animal)<br>
• Interface → <strong>"can-do"</strong> capability (Bird CAN Fly)<br><br>

<strong>B) is correct:</strong><br>
• Abstract class → can have <strong>mutable state</strong> (non-final instance variables)<br>
• Interface → variables are <strong>public static final</strong> (constants only, no mutable state)<br><br>

<strong>D) is correct:</strong><br>
• Abstract class → <strong>can have constructors</strong> (called via super() from subclass)<br>
• Interface → <strong>no constructors</strong> at all<br><br>

<strong>C) is incorrect:</strong> It's the <strong>opposite</strong>:<br>
• A class can extend <strong>only ONE</strong> class (abstract or not)<br>
• A class can implement <strong>MULTIPLE</strong> interfaces<br>
```java
class Duck extends Animal implements Flyable, Swimmable { }
// ONE superclass, MULTIPLE interfaces
```

## Question

What is the result of compiling and running this code?<br><br>

```java
class Outer {
    int x = 10;
}

class Inner extends Outer {
    int x = 20;
}

public class Test {
    public static void main(String[] args) {
        Outer o = new Inner();
        Inner i = new Inner();
        System.out.print(o.x + " " + i.x);
    }
}
```
<br><br>

Please select 1 option<br><br>

A) 20 20<br>
B) 10 20<br>
C) 10 10<br>
D) Compilation error

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>FIELD HIDING (not overriding):</strong> When a subclass declares a field with the same name as the parent, it <strong>hides</strong> the parent field. Fields are resolved by <strong>reference type at compile time</strong>.<br><br>

Analysis:<br>
• <strong>Outer o = new Inner();</strong><br>
→ Reference type: Outer → <strong>o.x = 10</strong><br><br>

• <strong>Inner i = new Inner();</strong><br>
→ Reference type: Inner → <strong>i.x = 20</strong><br><br>

Output: <strong>10 20</strong><br><br>

<strong>REMEMBER:</strong><br>
• Fields → <strong>compile time</strong> resolution (reference type) → field <strong>hiding</strong><br>
• Methods → <strong>runtime</strong> resolution (object type) → method <strong>overriding</strong><br>
• This is why <strong>polymorphism applies to methods only, NOT variables</strong><br><br>

<strong>A) is incorrect:</strong> o.x uses Outer's field (reference type).<br>
<strong>C) is incorrect:</strong> i.x uses Inner's field.<br>
<strong>D) is incorrect:</strong> Field hiding is allowed.

## Question

What is the result of compiling and running this code?<br><br>

```java
interface Flyable {
    void fly();
}

abstract class Animal {
    abstract void eat();
}

public class Test {
    public static void main(String[] args) {
        Flyable[] birds = new Flyable[3];
        Animal[] animals = new Animal[2];
        System.out.print(birds.length + " ");
        System.out.print(birds[0] + " ");
        System.out.print(animals.length);
    }
}
```
<br><br>

Please select 1 option<br><br>

A) Compilation error: cannot create array of interface type<br>
B) Compilation error: cannot create array of abstract class<br>
C) 3 null 2<br>
D) NullPointerException at birds[0]

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

<strong>ARRAYS OF INTERFACE/ABSTRACT TYPE:</strong> You CAN create arrays of interface or abstract class types. The array holds <strong>references</strong>, not objects.<br><br>

Analysis:<br>
• <strong>new Flyable[3]</strong> → creates array with 3 slots, all initialized to <strong>null</strong> ✅<br>
• <strong>new Animal[2]</strong> → creates array with 2 slots, all initialized to <strong>null</strong> ✅<br>
• <strong>birds.length</strong> = <strong>3</strong><br>
• <strong>birds[0]</strong> = <strong>null</strong> (printed as "null" by System.out.print)<br>
• <strong>animals.length</strong> = <strong>2</strong><br><br>

Output: <strong>3 null 2</strong><br><br>

<strong>WHAT IS ALLOWED:</strong><br>
```java
Flyable[] arr = new Flyable[3];   // ✅ array of references
arr[0] = new Bird();              // ✅ if Bird implements Flyable
```
<br><br>

<strong>WHAT IS FORBIDDEN:</strong><br>
```java
new Flyable();   // ❌ cannot instantiate interface
new Animal();    // ❌ cannot instantiate abstract class
```
<br><br>

<strong>A), B) are incorrect:</strong> Arrays of abstract/interface type are allowed.<br>
<strong>D) is incorrect:</strong> Printing null does not throw NullPointerException (only calling a method on null does).

## Question

What is the result of compiling this code?<br><br>

```java
class Animal {
    protected void eat() {
        System.out.print("Animal eating ");
    }
}

class Dog extends Animal {
    public void eat() {
        System.out.print("Dog eating ");
    }
}
```
<br><br>

Please select 1 option<br><br>

A) Compilation error: cannot widen access from protected to public<br>
B) Compiles successfully<br>
C) Compilation error: must use @Override annotation<br>
D) Compilation error: return types are incompatible

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>WIDENING ACCESS IS ALLOWED:</strong> When overriding, you can make the method <strong>more visible</strong> (less restrictive), but never <strong>less visible</strong> (more restrictive).<br><br>

Analysis:<br>
• Animal.eat() is <strong>protected</strong><br>
• Dog.eat() is <strong>public</strong><br>
• public is <strong>less restrictive</strong> than protected → ✅ allowed<br><br>

<strong>VISIBILITY RULES FOR OVERRIDE:</strong><br>
From parent → child (allowed changes):<br>
• <strong>private</strong> → not inherited (no override possible)<br>
• <strong>default</strong> → default, protected, or public ✅<br>
• <strong>protected</strong> → protected or public ✅<br>
• <strong>public</strong> → public only ✅<br><br>

<strong>NEVER reduce:</strong><br>
• public → protected ❌<br>
• protected → default ❌<br>
• protected → private ❌<br><br>

<strong>A) is incorrect:</strong> Widening is allowed; only narrowing causes errors.<br>
<strong>C) is incorrect:</strong> @Override is optional.<br>
<strong>D) is incorrect:</strong> Return types are identical (void).

## Question

What will the following code print?<br><br>

```java
class A {
    A() {
        System.out.print("A ");
    }
}

class B extends A {
    B() {
        System.out.print("B ");
    }
}

class C extends B {
    C() {
        System.out.print("C ");
    }
}

public class Test {
    public static void main(String[] args) {
        C obj = new C();
    }
}
```
<br><br>

Please select 1 option<br><br>

A) C B A<br>
B) A B C<br>
C) C<br>
D) A C

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>CONSTRUCTOR CHAIN IN DEEP HIERARCHY:</strong> Constructors execute from <strong>top to bottom</strong> of the inheritance chain.<br><br>

Execution:<br>
• <strong>new C()</strong> calls C constructor<br>
• C() has implicit <strong>super()</strong> → calls B()<br>
• B() has implicit <strong>super()</strong> → calls A()<br>
• A() has implicit <strong>super()</strong> → calls Object() (does nothing visible)<br><br>

Order of execution:<br>
1. A() prints <strong>"A "</strong><br>
2. B() prints <strong>"B "</strong><br>
3. C() prints <strong>"C "</strong><br><br>

Output: <strong>A B C</strong><br><br>

<strong>RULE:</strong> super() is always <strong>the first statement</strong> in a constructor (implicit or explicit). The parent constructor must complete <strong>before</strong> the child constructor body executes.<br><br>

<strong>A) is incorrect:</strong> Constructors execute top-down, not bottom-up.<br>
<strong>C) is incorrect:</strong> All parent constructors are called.<br>
<strong>D) is incorrect:</strong> B's constructor is also called.

## Question

What is the result of compiling this code?<br><br>

```java
class Base {
    Base(int x) {
        System.out.print("Base ");
    }
}

class Sub extends Base {
    Sub() {
        System.out.print("Sub ");
    }

    Sub(int x) {
        super(x);
        System.out.print("Sub(" + x + ") ");
    }
}
```
<br><br>

Please select 1 option<br><br>

A) Compiles successfully<br>
B) Compilation error in Sub(): implicit super constructor Base() is undefined<br>
C) Compilation error: Base must have a no-argument constructor<br>
D) Compiles but throws exception at runtime

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>MISSING SUPER() TRAP:</strong> If the parent has <strong>no no-argument constructor</strong>, every child constructor <strong>must explicitly call</strong> super(...) with the right arguments.<br><br>

Analysis:<br>
• Base has ONLY <strong>Base(int x)</strong> → no Base() exists<br>
• <strong>Sub()</strong> has no explicit super() call → compiler inserts <strong>implicit super()</strong><br>
• <strong>super()</strong> tries to call Base() → <strong>does NOT exist</strong> → compilation error<br>
• <strong>Sub(int x)</strong> explicitly calls <strong>super(x)</strong> → OK ✅<br><br>

<strong>To fix Sub():</strong><br>
```java
Sub() {
    super(0);  // explicit call to Base(int)
    System.out.print("Sub ");
}
```
<br><br>

<strong>RULE:</strong> If your parent class has no no-argument constructor, you MUST call super(...) as the <strong>first line</strong> of every child constructor.<br><br>

<strong>A) is incorrect:</strong> Sub() constructor fails.<br>
<strong>C) is incorrect:</strong> Base doesn't need a no-arg constructor; Sub() needs to call the existing one.<br>
<strong>D) is incorrect:</strong> Error is at compile time.

## Question

What will the following code print?<br><br>

```java
interface Drawable {
    int DEFAULT_SIZE = 10;
}

class Circle implements Drawable {
    public static void main(String[] args) {
        System.out.print(DEFAULT_SIZE + " ");
        System.out.print(Drawable.DEFAULT_SIZE + " ");
        System.out.print(Circle.DEFAULT_SIZE);
    }
}
```
<br><br>

Please select 1 option<br><br>

A) 10 10 10<br>
B) Compilation error: DEFAULT_SIZE is not accessible<br>
C) 10 10<br>
D) Compilation error: cannot access interface variable from implementing class

## Réponse

<strong>Réponse correcte :</strong> A)<br><br>

<strong>INTERFACE CONSTANTS ACCESS:</strong> Interface variables (public static final) can be accessed in <strong>multiple ways</strong>.<br><br>

Analysis:<br>
• <strong>DEFAULT_SIZE</strong> → accessed directly (inherited by Circle) → <strong>10</strong> ✅<br>
• <strong>Drawable.DEFAULT_SIZE</strong> → accessed via interface name → <strong>10</strong> ✅<br>
• <strong>Circle.DEFAULT_SIZE</strong> → accessed via implementing class name → <strong>10</strong> ✅<br><br>

Output: <strong>10 10 10</strong><br><br>

<strong>INTERFACE VARIABLES REMINDER:</strong><br>
• Implicitly <strong>public static final</strong><br>
• Are <strong>constants</strong> (cannot be modified)<br>
• Can be accessed via interface name, class name, or directly in implementing class<br><br>

<strong>B), D) are incorrect:</strong> Interface constants are public and accessible from anywhere.<br>
<strong>C) is incorrect:</strong> All three access patterns work.

## Question

What is the result of compiling and running this code?<br><br>

```java
class Animal {
    static void info() {
        System.out.print("Animal ");
    }

    void sound() {
        System.out.print("... ");
    }
}

class Dog extends Animal {
    static void info() {
        System.out.print("Dog ");
    }

    void sound() {
        System.out.print("Bark ");
    }
}

public class Test {
    public static void main(String[] args) {
        Animal a = new Dog();
        a.info();
        a.sound();
    }
}
```
<br><br>

Please select 1 option<br><br>

A) Dog Bark<br>
B) Animal Bark<br>
C) Dog ...<br>
D) Animal ...

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>STATIC METHOD HIDING vs INSTANCE METHOD OVERRIDING:</strong><br><br>

Analysis with <strong>Animal a = new Dog();</strong><br><br>

• <strong>a.info()</strong> → info() is <strong>static</strong><br>
→ Static methods are <strong>NOT overridden</strong>, they are <strong>hidden</strong><br>
→ Resolved at <strong>compile time</strong> by reference type<br>
→ Reference type is Animal → calls <strong>Animal.info()</strong> → <strong>"Animal "</strong><br><br>

• <strong>a.sound()</strong> → sound() is an <strong>instance method</strong><br>
→ Instance methods ARE overridden<br>
→ Resolved at <strong>runtime</strong> by object type<br>
→ Object type is Dog → calls <strong>Dog.sound()</strong> → <strong>"Bark "</strong><br><br>

Output: <strong>Animal Bark</strong><br><br>

<strong>SUMMARY:</strong><br>
• <strong>Static methods</strong> → compile time → reference type → <strong>hiding</strong><br>
• <strong>Instance methods</strong> → runtime → object type → <strong>overriding</strong><br>
• <strong>Variables</strong> → compile time → reference type → <strong>hiding</strong><br><br>

<strong>A) is incorrect:</strong> Static methods use reference type.<br>
<strong>C), D) are incorrect:</strong> Mixes up the resolution rules.

## Question

Which of the following code snippets will compile?<br><br>

Please select 2 options<br><br>

A)<br>
```java
abstract class X {
    abstract void doSomething();
    abstract void doMore();
}
abstract class Y extends X {
    void doSomething() { System.out.print("Y"); }
}
```
<br>
B)<br>
```java
abstract class X {
    abstract void doSomething();
}
class Y extends X { }
```
<br>
C)<br>
```java
interface I { void m(); }
abstract class A implements I { }
```
<br>
D)<br>
```java
interface I { void m(); }
class A implements I { }
```

## Réponse

<strong>Réponse correcte :</strong> A), C)<br><br>

<strong>A) is correct:</strong> Y is <strong>abstract</strong>, so it does NOT need to implement all abstract methods. It implements doSomething() but leaves doMore() for the next concrete subclass. ✅<br><br>

<strong>C) is correct:</strong> A is <strong>abstract</strong>, so it does NOT need to implement I's method m(). The obligation is deferred to A's concrete subclass. ✅<br><br>

<strong>B) is incorrect:</strong> Y is a <strong>concrete class</strong> (not abstract) extending abstract X. It <strong>must implement</strong> doSomething() but doesn't → compilation error.<br><br>

<strong>D) is incorrect:</strong> A is a <strong>concrete class</strong> implementing I. It <strong>must implement</strong> m() but doesn't → compilation error.<br><br>

<strong>KEY RULE:</strong> Only <strong>abstract classes</strong> can defer implementation of abstract methods. Concrete classes must implement <strong>all</strong> inherited abstract methods.

## Question

What will the following code print?<br><br>

```java
class Animal {
    String name = "Animal";

    Animal() {
        System.out.print(getName() + " ");
    }

    String getName() {
        return name;
    }
}

class Dog extends Animal {
    String name = "Dog";

    String getName() {
        return name;
    }
}

public class Test {
    public static void main(String[] args) {
        Dog d = new Dog();
        System.out.print(d.getName());
    }
}
```
<br><br>

Please select 1 option<br><br>

A) Animal Dog<br>
B) Dog Dog<br>
C) null Dog<br>
D) Animal Animal

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

<strong>CONSTRUCTOR + POLYMORPHISM TRAP:</strong> When a parent constructor calls an overridden method, it executes the <strong>child's version</strong> — but the child's fields are <strong>not yet initialized</strong>.<br><br>

Execution:<br>
1. <strong>new Dog()</strong> → calls Dog constructor<br>
2. Implicit <strong>super()</strong> → calls Animal constructor<br>
3. Animal() calls <strong>getName()</strong><br>
→ getName() is overridden in Dog<br>
→ Polymorphism → calls <strong>Dog's getName()</strong><br>
→ Dog's <strong>name field is NOT yet initialized</strong> (still null)<br>
→ Returns <strong>null</strong> → prints <strong>"null "</strong><br>
4. Animal constructor finishes<br>
5. Dog's fields are initialized: <strong>name = "Dog"</strong><br>
6. <strong>d.getName()</strong> → returns <strong>"Dog"</strong><br><br>

Output: <strong>null Dog</strong><br><br>

<strong>CRITICAL OCP POINT:</strong> Calling overridden methods from a constructor is dangerous because child fields may not be initialized yet.<br><br>

<strong>A) is incorrect:</strong> Animal constructor calls Dog's getName(), not Animal's.<br>
<strong>B) is incorrect:</strong> Dog's name is null during parent constructor.<br>
<strong>D) is incorrect:</strong> Polymorphism applies even during construction.
