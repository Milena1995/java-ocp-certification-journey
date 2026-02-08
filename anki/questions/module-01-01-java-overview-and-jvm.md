## Question

What is the correct sequence of steps when a Java program is executed?<br><br>

Please select 1 option<br><br>

A) Source code (.java) → JVM → Machine code → Execution<br>
B) Source code (.java) → Compiler (javac) → Bytecode (.class) → JVM → Machine code → Execution<br>
C) Source code (.java) → Bytecode (.class) → Machine code → JVM → Execution<br>
D) Source code (.java) → Compiler (javac) → Machine code → JVM → Execution

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

The complete compilation and execution chain is:<br><br>

1. Developer writes <strong>.java files</strong> (source code)<br>
2. <strong>javac compiler</strong> transforms .java into <strong>.class files</strong> (bytecode)<br>
3. <strong>JVM loads</strong> the .class files<br>
4. JVM <strong>interprets or compiles</strong> bytecode into <strong>machine code</strong><br>
5. CPU <strong>executes</strong> the machine code<br><br>

<strong>Key point:</strong> The processor never sees bytecode - only machine code.<br><br>

<strong>A) is incorrect:</strong> Missing the compilation step (javac) and bytecode generation.<br>
<strong>C) is incorrect:</strong> Machine code comes AFTER the JVM processes bytecode, not before.<br>
<strong>D) is incorrect:</strong> javac produces bytecode, not machine code.

## Question

Which statements about the JIT (Just-In-Time) compiler are correct?<br><br>

Please select all that apply<br><br>

A) The JIT compiler is part of the JVM<br>
B) The JIT compiler transforms .java files into .class files<br>
C) The JIT compiler converts frequently executed bytecode into machine code<br>
D) The JIT compiler runs before the program starts

## Réponse

<strong>Réponse correcte :</strong> A), C)<br><br>

The <strong>JIT (Just-In-Time) compiler</strong> is an optimization component of the JVM.<br><br>

How it works:<br>
• The JVM starts by <strong>interpreting bytecode</strong> (slow but fast startup)<br>
• The JIT <strong>detects frequently executed code</strong> (hot spots)<br>
• It <strong>compiles that bytecode into machine code</strong><br>
• The compiled code is <strong>cached and reused</strong><br>
• Result: <strong>much faster execution</strong> for repeated code<br><br>

<strong>B) is incorrect:</strong> The javac compiler (not JIT) transforms .java → .class.<br>
<strong>D) is incorrect:</strong> JIT works <strong>during execution</strong>, not before (that's why it's "Just-In-Time").

## Question

What is the output of the following code?<br><br>

```java
public class Test {
    public static void main(String[] args) {
        System.out.println(args.length);
    }
}
```

Executed with: <strong>java Test</strong><br><br>

Please select 1 option<br><br>

A) Compilation error<br>
B) NullPointerException<br>
C) 0<br>
D) 1

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

When no program arguments are provided, <strong>args is an empty array</strong>, not null.<br><br>

Key points:<br>
• <strong>args.length == 0</strong> when no arguments are passed<br>
• <strong>args is never null</strong> in main method<br>
• The JVM always creates the array (empty if no args)<br><br>

If executed with: <strong>java Test hello world</strong><br>
• args.length would be <strong>2</strong><br>
• args[0] = "hello", args[1] = "world"<br><br>

<strong>A) is incorrect:</strong> Code compiles fine.<br>
<strong>B) is incorrect:</strong> args is never null.<br>
<strong>D) is incorrect:</strong> No arguments were provided.

## Question

Given the following command:<br><br>

<strong>java -Xmx1024m -Denv=production MyApp input.txt debug</strong><br><br>

Which statements are correct?<br><br>

Please select all that apply<br><br>

A) "-Xmx1024m" is a JVM argument that sets maximum memory<br>
B) "input.txt" is received in args[0] of the main method<br>
C) "-Denv=production" is a program argument<br>
D) "debug" is received in args[1] of the main method

## Réponse

<strong>Réponse correcte :</strong> A), B), D)<br><br>

<strong>JVM arguments</strong> (before class name):<br>
• <strong>-Xmx1024m</strong> → configures JVM max memory (1024 MB)<br>
• <strong>-Denv=production</strong> → sets system property<br>
• These are for the <strong>JVM itself</strong>, not the program<br><br>

<strong>Program arguments</strong> (after class name):<br>
• <strong>input.txt</strong> → args[0]<br>
• <strong>debug</strong> → args[1]<br>
• These go to <strong>String[] args</strong> in main()<br><br>

Format: <strong>java [JVM args] ClassName [Program args]</strong><br><br>

<strong>C) is incorrect:</strong> -Denv=production is a JVM argument (defines system property), not a program argument.

## Question

What is bytecode in Java?<br><br>

Please select 1 option<br><br>

A) Machine code executed directly by the CPU<br>
B) An intermediate code executed by the JVM, platform-independent<br>
C) Source code written by developers in .java files<br>
D) Compiled code specific to each operating system

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>Bytecode</strong> is the <strong>intermediate representation</strong> of Java programs.<br><br>

Characteristics:<br>
• Stored in <strong>.class files</strong><br>
• <strong>Platform-independent</strong> (same on Windows, Linux, macOS)<br>
• <strong>Not human-readable</strong><br>
• <strong>Not machine code</strong> (CPU cannot execute it directly)<br>
• <strong>Executed by the JVM</strong> (interpreted or JIT-compiled)<br><br>

This is what enables <strong>"Write Once, Run Anywhere"</strong>:<br>
• Same bytecode on all platforms<br>
• Each OS has its own JVM<br>
• JVM translates bytecode to local machine code<br><br>

<strong>A) is incorrect:</strong> Machine code is what the CPU executes, not bytecode.<br>
<strong>C) is incorrect:</strong> Source code is .java files, not bytecode.<br>
<strong>D) is incorrect:</strong> Bytecode is platform-independent, not OS-specific.

## Question

What is the difference between the JRE and the JDK?<br><br>

Please select 1 option<br><br>

A) JRE includes the compiler (javac), JDK does not<br>
B) JDK = JRE + development tools (javac, etc.)<br>
C) JRE is only for Windows, JDK is cross-platform<br>
D) JDK is required to run Java programs, JRE is only for development

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>JVM (Java Virtual Machine):</strong><br>
• Executes bytecode<br>
• Core execution engine<br><br>

<strong>JRE (Java Runtime Environment):</strong><br>
• JVM + <strong>Java libraries</strong><br>
• Needed to <strong>run</strong> Java programs<br>
• Does <strong>NOT include javac</strong><br><br>

<strong>JDK (Java Development Kit):</strong><br>
• JRE + <strong>javac compiler</strong> + development tools<br>
• Needed to <strong>develop</strong> Java programs<br><br>

Summary: <strong>JDK ⊃ JRE ⊃ JVM</strong><br><br>

<strong>A) is incorrect:</strong> JDK includes javac, not JRE.<br>
<strong>C) is incorrect:</strong> Both are cross-platform.<br>
<strong>D) is incorrect:</strong> JRE runs programs, JDK is for development.

## Question

Consider the following class structure:<br><br>

```java
public class Animal {
    public void makeSound() {
        System.out.println("Some sound");
    }
}

public class Dog extends Animal {
    @Override
    public void makeSound() {
        System.out.println("Bark");
    }
}

public class Cat extends Animal {
    @Override
    public void makeSound() {
        System.out.println("Meow");
    }
}
```

What will the following code print?<br><br>

```java
Animal a = new Dog();
Animal b = new Cat();
a.makeSound();
b.makeSound();
```
<br><br>

Please select 1 option<br><br>

A) Some sound<br>
Some sound<br><br>

B) Bark<br>
Meow<br><br>

C) Compilation error<br><br>

D) Dog<br>
Cat

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

This demonstrates <strong>polymorphism</strong> in Java.<br><br>

<strong>Critical rule:</strong> The method executed depends on the <strong>actual object type</strong>, not the reference type.<br><br>

Analysis:<br>
• <strong>Animal a = new Dog();</strong><br>
  - Reference type: Animal<br>
  - <strong>Actual object: Dog</strong><br>
  - Calls: Dog.makeSound() → "Bark"<br><br>

• <strong>Animal b = new Cat();</strong><br>
  - Reference type: Animal<br>
  - <strong>Actual object: Cat</strong><br>
  - Calls: Cat.makeSound() → "Meow"<br><br>

Output:<br>
<strong>Bark</strong><br>
<strong>Meow</strong><br><br>

<strong>Key benefit:</strong> Same method call (makeSound()), different behaviors - this is polymorphism.<br><br>

<strong>A) is incorrect:</strong> Would require actual objects of type Animal.<br>
<strong>C) is incorrect:</strong> Code compiles and runs fine.<br>
<strong>D) is incorrect:</strong> makeSound() prints sounds, not class names.

## Question

What does the term "encapsulation" mean in OOP?<br><br>

Please select 1 option<br><br>

A) Simply making all fields private<br>
B) Protecting data and controlling modifications through methods with validation rules<br>
C) Hiding all methods from external classes<br>
D) Creating getters and setters for all fields

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>Encapsulation is NOT just "make it private".</strong><br><br>

True encapsulation means:<br>
• <strong>Protect data</strong> (usually with private fields)<br>
• <strong>Control access</strong> via public methods<br>
• <strong>Enforce validation rules</strong> in those methods<br>
• <strong>Prevent inconsistent states</strong><br><br>

Example:<br>

```java
public class BankAccount {
    private double balance;  // Protected

    public void deposit(double amount) {
        if (amount > 0) {  // Validation rule
            balance += amount;
        } else {
            throw new IllegalArgumentException("Amount must be positive");
        }
    }
}
```
<br>
<strong>Encapsulation = data + rules</strong><br><br>

<strong>A) is incorrect:</strong> Making fields private is only the first step, not encapsulation itself.<br>
<strong>C) is incorrect:</strong> Encapsulation is about data protection, not hiding methods.<br>
<strong>D) is incorrect:</strong> Simple getters/setters without validation rules are NOT true encapsulation.

## Question

What is the role of the "build" process in Java?<br><br>

Please select all that apply<br><br>

A) The build is a compiler that transforms .java files into .class files<br>
B) The build process calls the javac compiler<br>
C) The build organizes files and often creates a JAR file<br>
D) The build process replaces the JVM

## Réponse

<strong>Réponse correcte :</strong> B), C)<br><br>

The <strong>build</strong> is a <strong>process</strong>, not a tool or compiler.<br><br>

What the build does:<br>
• <strong>Calls javac</strong> to compile .java → .class<br>
• <strong>Organizes files</strong> (classes, resources, libraries)<br>
• <strong>Creates packaging</strong> (usually JAR files)<br>
• <strong>Prepares the application</strong> for execution or delivery<br><br>

<strong>Build ≠ Compiler:</strong><br>
• The build <strong>uses</strong> the compiler<br>
• The build does <strong>more than just compile</strong><br><br>

Common build tools: <strong>Maven, Gradle, Ant</strong><br><br>

<strong>A) is incorrect:</strong> The build is a process that calls the compiler, it's not a compiler itself.<br>
<strong>D) is incorrect:</strong> The build prepares files; the JVM executes them (completely different roles).

## Question

What is a JAR file?<br><br>

Please select 1 option<br><br>

A) A Java source code file containing multiple .java files<br>
B) A compressed archive containing .class files, resources, and metadata (MANIFEST.MF)<br>
C) A configuration file for the JVM<br>
D) An executable file specific to the Windows operating system

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>JAR (Java ARchive)</strong> is a package format for Java applications.<br><br>

Contents of a JAR:<br>
• <strong>.class files</strong> (compiled bytecode)<br>
• <strong>Resources</strong> (images, properties, etc.)<br>
• <strong>MANIFEST.MF</strong> (metadata file)<br>
• <strong>Libraries</strong> (other JARs if needed)<br><br>

Purpose:<br>
• <strong>Easy distribution</strong> (single file instead of hundreds)<br>
• <strong>Easy execution:</strong> java -jar myapp.jar<br>
• <strong>Professional delivery format</strong><br><br>

<strong>Important:</strong> You deliver JARs, never .java files.<br><br>

<strong>A) is incorrect:</strong> JARs contain .class files (bytecode), not .java (source).<br>
<strong>C) is incorrect:</strong> JARs are application packages, not JVM config files.<br>
<strong>D) is incorrect:</strong> JARs are cross-platform (run on any OS with a JVM).

## Question

What is the output of the following code?<br><br>

```java
public class Args {
    public static void main(String[] args) {
        if (args.length > 0) {
            int value = Integer.parseInt(args[0]);
            System.out.println(value * 2);
        }
    }
}
```

Executed with: <strong>java Args 10</strong><br><br>

Please select 1 option<br><br>

A) 10<br>
B) 20<br>
C) 102<br>
D) Compilation error

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

Program arguments are <strong>always String</strong>, even when they look like numbers.<br><br>

Execution breakdown:<br>
• Command: <strong>java Args 10</strong><br>
• args[0] = <strong>"10"</strong> (String, not int)<br>
• args.length = <strong>1</strong> (condition is true)<br>
• <strong>Integer.parseInt("10")</strong> converts String → int<br>
• value = <strong>10</strong> (int)<br>
• value * 2 = <strong>20</strong><br><br>

Output: <strong>20</strong><br><br>

<strong>Critical point:</strong> Program arguments are ALWAYS strings - conversion is required for numeric operations.<br><br>

<strong>A) is incorrect:</strong> Forgot the multiplication by 2.<br>
<strong>C) is incorrect:</strong> Would happen if we did string concatenation: "10" + "2" (but we converted to int first).<br>
<strong>D) is incorrect:</strong> Code compiles successfully.

## Question

Which statements about classes and objects are correct?<br><br>

Please select all that apply<br><br>

A) A class is a blueprint, an object is a concrete instance<br>
B) Multiple objects can be created from the same class<br>
C) A class exists in memory and can perform actions<br>
D) Objects share the same structure but can have different values

## Réponse

<strong>Réponse correcte :</strong> A), B), D)<br><br>

<strong>Class vs Object:</strong><br><br>

<strong>Class:</strong><br>
• A <strong>plan, description, idea</strong><br>
• Defines <strong>what</strong> an object is and what it can do<br>
• Does <strong>NOT exist in memory</strong> (just a template)<br>
• Cannot perform actions by itself<br>
• Analogy: <strong>blueprint of a house</strong><br><br>

<strong>Object:</strong><br>
• A <strong>concrete instance</strong> created from a class<br>
• <strong>Exists in memory</strong> and can act<br>
• Multiple objects from same class = <strong>same structure, different data</strong><br>
• Analogy: <strong>actual house built from blueprint</strong><br><br>

Example:<br>
• Class <strong>Car</strong> = blueprint<br>
• Objects: myCar, yourCar = <strong>different instances</strong> with different colors, speeds, etc.<br><br>

<strong>C) is incorrect:</strong> Classes are templates - they do NOT exist in memory and cannot act. Only objects do.

## Question

What is the primary purpose of using Object-Oriented Programming (OOP)?<br><br>

Please select 1 option<br><br>

A) To make programs run faster<br>
B) To reduce code size and memory usage<br>
C) To organize code and make large programs understandable and maintainable<br>
D) To eliminate the need for testing

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

<strong>The problem OOP solves:</strong><br>
• When programs grow <strong>large</strong>, they become hard to understand<br>
• Complexity leads to fear of <strong>making changes</strong><br>
• Fear of changes <strong>blocks evolution</strong> of the program<br>
• Result: unmaintainable code<br><br>

<strong>OOP's solution:</strong><br>
• <strong>Organize code</strong> into logical units (classes)<br>
• <strong>Reduce complexity</strong> through encapsulation<br>
• <strong>Make code understandable</strong> over time<br>
• <strong>Enable collaboration</strong> in teams<br><br>

<strong>Key insight:</strong> OOP exists for <strong>human comprehension</strong>, not machine performance.<br><br>

<strong>Why Java forces classes:</strong> To prevent disorganized code and maintain structure in large projects.<br><br>

<strong>A) is incorrect:</strong> OOP is about maintainability, not performance.<br>
<strong>B) is incorrect:</strong> OOP may actually increase code size (but improves organization).<br>
<strong>D) is incorrect:</strong> OOP makes testing easier but doesn't eliminate it.

## Question

What is the result when this code is compiled and run?<br><br>

```java
public class Test {
    public static void main(String[] args) {
        System.out.println(args[0]);
    }
}
```

Executed with: <strong>java Test</strong><br><br>

Please select 1 option<br><br>

A) Prints: null<br>
B) Prints an empty line<br>
C) ArrayIndexOutOfBoundsException at runtime<br>
D) NullPointerException at runtime

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

<strong>CRITICAL TRAP:</strong> Accessing args[0] when no arguments are provided.<br><br>

Execution analysis:<br>
• Command: <strong>java Test</strong> (no arguments)<br>
• args.length = <strong>0</strong> (empty array, NOT null)<br>
• Attempting: <strong>args[0]</strong><br>
• But: <strong>no element at index 0</strong><br>
• Result: <strong>ArrayIndexOutOfBoundsException</strong><br><br>

<strong>Best practice - always check:</strong><br>

```java
if (args.length > 0) {
    System.out.println(args[0]);
} else {
    System.out.println("No arguments provided");
}
```
<br>
<strong>Common exam trap:</strong> args is never null, but accessing missing indices throws exception.<br><br>

<strong>A) is incorrect:</strong> args array is not null, it's empty.<br>
<strong>B) is incorrect:</strong> Exception is thrown before any print.<br>
<strong>D) is incorrect:</strong> NullPointerException would occur if args itself was null (never happens in main).

## Question

Which of the following correctly describes the compilation process in Java?<br><br>

Please select 1 option<br><br>

A) Compilation transforms source code directly into machine code for the CPU<br>
B) Compilation translates code without executing it, producing bytecode<br>
C) Compilation is the process of running Java programs on different operating systems<br>
D) Compilation happens inside the JVM during program execution

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>Compilation definition:</strong><br>
• <strong>Transforms code from one form to another</strong><br>
• <strong>Does NOT execute</strong> the code<br>
• In Java: <strong>.java → .class</strong> (bytecode)<br><br>

The Java compilation process:<br>
• Tool: <strong>javac</strong> (Java compiler)<br>
• Input: <strong>.java files</strong> (human-readable source)<br>
• Output: <strong>.class files</strong> (bytecode, JVM-readable)<br>
• Action: <strong>Syntax checking + type checking + transformation</strong><br><br>

<strong>Important distinction:</strong><br>
• <strong>Compile</strong> = translate code (javac, JIT)<br>
• <strong>Execute</strong> = run code (CPU only)<br>
• <strong>Interpret</strong> = read + translate + execute line-by-line (JVM interpreter)<br><br>

<strong>A) is incorrect:</strong> javac produces bytecode, not machine code.<br>
<strong>C) is incorrect:</strong> That describes portability, not compilation.<br>
<strong>D) is incorrect:</strong> javac compilation happens BEFORE execution; JIT compilation is different and happens during execution.
