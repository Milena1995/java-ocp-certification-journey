## Question

How do you convert a Calendar instance to a Date object in Java?<br><br>

Please select 1 option<br><br>

A) calendar.toDate();<br>
B) Date date = Calendar.toDate(calendar);<br>
C) Date date = calendar.getTime();<br>
D) Date date = new Date(calendar);

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

The correct method is <strong>calendar.getTime()</strong>.<br><br>

Example:<br>
Calendar calendar = Calendar.getInstance();<br>
Date date = calendar.getTime();<br><br>

Note: This is the old API (java.util). In modern code, use java.time.<br><br>

<strong>A), B), D) are incorrect:</strong> Non-existent methods or incorrect syntax.

## Question

What is the difference between LocalDateTime and ZonedDateTime?<br><br>

Please select 1 option<br><br>

A) LocalDateTime does not include a time zone, ZonedDateTime includes a specific time zone<br>
B) LocalDateTime is always in UTC, ZonedDateTime adjusts to the system<br>
C) ZonedDateTime can only store dates, LocalDateTime stores date and time<br>
D) LocalDateTime requires manual conversion to timestamps before comparison

## Réponse

<strong>Réponse correcte :</strong> A)<br><br>

<strong>Key difference:</strong><br><br>

<strong>LocalDateTime:</strong><br>
• Date + time<br>
• ❌ <strong>No time zone</strong><br>
• Local representation without geographical context<br><br>

<strong>ZonedDateTime:</strong><br>
• Date + time + <strong>time zone</strong><br>
• ✅ Includes ZoneId<br>
• Automatically handles DST<br>
• Complete representation with context<br><br>

<strong>B), C), D) are incorrect:</strong> False statements.

## Question

What does java.time.Clock provide?<br><br>

Please select 1 option<br><br>

A) Automatic synchronization with an atomic clock<br>
B) A high-precision timer for measuring execution speed<br>
C) An abstraction over the system time, allowing time control and testing<br>
D) A fixed timestamp that never changes

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

<strong>java.time.Clock</strong> provides an <strong>abstraction over system time</strong>.<br><br>

Benefits:<br>
• Allows <strong>time control</strong> in tests<br>
• Makes code <strong>testable</strong><br>
• Can simulate different time zones<br>
• Can freeze time for testing<br><br>

Example usage:<br>
• Production: Clock.systemDefaultZone()<br>
• Tests: Clock.fixed() for constant time<br><br>

<strong>A), B), D) are incorrect:</strong> Not the primary purpose.

## Question

What is the main purpose of the java.time.temporal package?<br><br>

Please select 1 option<br><br>

A) Define high-level date-time classes like LocalDateTime<br>
B) Provide low-level support for date-time manipulation (adding/subtracting units)<br>
C) Manage system clocks in Java applications<br>
D) Replace SimpleDateFormat for date formatting

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>java.time.temporal</strong> provides <strong>low-level support</strong> for date-time manipulation.<br><br>

Contains:<br>
• <strong>Temporal</strong>: interface for date-time objects<br>
• <strong>TemporalAmount</strong>: interface for time quantities<br>
• <strong>TemporalUnit</strong>: time units (ChronoUnit)<br>
• <strong>TemporalField</strong>: date-time fields<br>
• <strong>TemporalAdjuster</strong>: custom adjustments<br><br>

Enables operations like:<br>
• Adding/subtracting units<br>
• Querying fields<br>
• Complex adjustments<br><br>

<strong>A) is incorrect:</strong> java.time contains LocalDateTime.<br>
<strong>C) is incorrect:</strong> Clocks are in Clock class.<br>
<strong>D) is incorrect:</strong> Formatting is in java.time.format.

## Question

Which method allows adding a duration to an Instant?<br><br>

Please select 1 option<br><br>

A) instant.plus(duration);<br>
B) instant.add(duration);<br>
C) instant.plusDuration(duration);<br>
D) Duration.add(instant, duration);

## Réponse

<strong>Réponse correcte :</strong> A)<br><br>

The correct method is <strong>instant.plus(duration)</strong>.<br><br>

Example:<br>
Instant instant = Instant.now();<br>
Duration duration = Duration.ofHours(2);<br>
Instant newInstant = instant.plus(duration);<br><br>

Other similar methods:<br>
• instant.plusSeconds(long)<br>
• instant.plusMillis(long)<br>
• instant.plusNanos(long)<br><br>

Reminder: Instant is immutable, so it returns a new object.<br><br>

<strong>B), C), D) are incorrect:</strong> Non-existent methods or incorrect syntax.

## Question

Which class from the old Date/Time API should absolutely be avoided in modern code?<br><br>

Please select 1 option<br><br>

A) java.time.LocalDate<br>
B) java.util.Date<br>
C) java.time.Instant<br>
D) java.time.ZonedDateTime

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>AVOID absolutely:</strong><br>
• java.util.Date<br>
• java.util.Calendar<br>
• java.text.SimpleDateFormat<br><br>

Reasons:<br>
• Mutable (not thread-safe)<br>
• Confusing API<br>
• Historical bugs (months starting from 0)<br>
• Mixes date/time/timezone<br><br>

<strong>USE instead:</strong><br>
• java.time.* (LocalDate, Instant, ZonedDateTime, etc.)<br><br>

<strong>A), C), D) are incorrect:</strong> These are the recommended new classes.

## Question

How do you create a fixed Clock for testing?<br><br>

Please select 1 option<br><br>

A) Clock.freeze()<br>
B) Clock.systemUTC()<br>
C) new Clock(Instant)<br>
D) Clock.fixed(Instant, ZoneId)

## Réponse

<strong>Réponse correcte :</strong> D)<br><br>

To create a <strong>fixed Clock for testing</strong>:<br>
<strong>Clock.fixed(Instant, ZoneId)</strong><br><br>

Example:<br>
Instant instant = Instant.parse("2024-01-15T10:00:00Z");<br>
Clock clock = Clock.fixed(instant, ZoneId.of("Europe/Paris"));<br>
LocalDateTime ldt = LocalDateTime.now(clock); // always Jan 15 2024 11:00<br><br>

Useful for:<br>
• Unit tests<br>
• Predictable behavior<br>
• Time logic verification<br><br>

<strong>A) and C) are incorrect:</strong> Non-existent methods.<br>
<strong>B) is incorrect:</strong> Returns current system time.

## Question

Which interface do all main date-time types implement?<br><br>

Please select 1 option<br><br>

A) Temporal<br>
B) DateTime<br>
C) TimeStamp<br>
D) Chronological

## Réponse

<strong>Réponse correcte :</strong> A)<br><br>

All main date-time types implement the <strong>Temporal</strong> interface.<br><br>

Types that implement Temporal:<br>
• LocalDate<br>
• LocalTime<br>
• LocalDateTime<br>
• ZonedDateTime<br>
• Instant<br>
• OffsetDateTime<br><br>

This allows:<br>
• Use with ChronoUnit.between()<br>
• Generic date-time manipulation<br>
• Support for TemporalAdjuster<br><br>

<strong>B), C), D) are incorrect:</strong> Non-existent interfaces.

## Question

When was the new Date & Time API (JSR-310) introduced?<br><br>

Please select 1 option<br><br>

A) Java 5<br>
B) Java 6<br>
C) Java 8<br>
D) Java 11

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

The <strong>new API (JSR-310)</strong> was introduced in <strong>Java 8</strong>.<br><br>

Implemented via:<br>
• java.time<br>
• java.time.temporal<br>
• java.time.format<br>
• java.time.zone<br><br>

Advantages:<br>
• ✅ Immutable<br>
• ✅ Thread-safe<br>
• ✅ Clear<br>
• ✅ ISO-8601<br><br>

<strong>A), B), D) are incorrect:</strong> Wrong version.

## Question

What does LocalDate represent?<br><br>

Please select 1 option<br><br>

A) A date without time or time zone<br>
B) A date with time and time zone<br>
C) A UTC timestamp<br>
D) A duration in days

## Réponse

<strong>Réponse correcte :</strong> A)<br><br>

<strong>LocalDate</strong> represents:<br>
• Date <strong>without time</strong><br>
• <strong>No time zone</strong><br><br>

Usage examples:<br>
• Birth date<br>
• Invoice date<br>
• Anniversary dates<br><br>

ISO format: yyyy-MM-dd<br>
Example: 2024-01-15<br><br>

<strong>B) is incorrect:</strong> That's ZonedDateTime.<br>
<strong>C) is incorrect:</strong> That's Instant.<br>
<strong>D) is incorrect:</strong> That's Period or Duration.

## Question

What does LocalTime represent?<br><br>

Please select 1 option<br><br>

A) A time with date<br>
B) A timestamp<br>
C) A time without date or time zone<br>
D) A duration

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

<strong>LocalTime</strong> represents:<br>
• Time <strong>without date</strong><br>
• <strong>No time zone</strong><br><br>

Usage examples:<br>
• Store opening time<br>
• Alarm time<br>
• Recurring schedules<br><br>

ISO format: HH:mm:ss<br>
Example: 14:30:00<br><br>

<strong>A) is incorrect:</strong> That's LocalDateTime.<br>
<strong>B) and D) are incorrect:</strong> Wrong category.

## Question

What does LocalDateTime represent?<br><br>

Please select 1 option<br><br>

A) Date + time + time zone<br>
B) Date + time without time zone<br>
C) An absolute point in time<br>
D) A duration

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>LocalDateTime</strong> represents:<br>
• <strong>Date + time</strong><br>
• ❌ <strong>No time zone</strong><br>
• Human local time<br><br>

Important: without a time zone, it's ambiguous for global events.<br><br>

Format: yyyy-MM-ddTHH:mm:ss<br>
Example: 2024-01-15T14:30:00<br><br>

<strong>OCP trap:</strong> LocalDateTime does NOT handle time zones.<br><br>

<strong>A) is incorrect:</strong> That's ZonedDateTime.<br>
<strong>C) is incorrect:</strong> That's Instant.

## Question

Which method is the safest way to create a date?<br><br>

Please select 1 option<br><br>

A) LocalDate.of(2024, 1, 15)<br>
B) LocalDate.now()<br>
C) new LocalDate(2024, 1, 15)<br>
D) LocalDate.parse("2024-01-15")

## Réponse

<strong>Réponse correcte :</strong> A)<br><br>

<strong>of()</strong> is THE SAFEST because:<br>
• Numeric values<br>
• No ambiguity<br>
• Compile-time verification<br>
• No parsing exceptions<br><br>

<strong>B)</strong> depends on system clock (can vary).<br>
<strong>C)</strong> no public constructor.<br>
<strong>D)</strong> strict ISO, possible runtime exceptions.<br><br>

LocalDate.of(2024, 1, 15); // ✅ SAFE

## Question

What happens with LocalDate.parse("2024-1-15")?<br><br>

Please select 1 option<br><br>

A) Creates the date January 15, 2024<br>
B) Compilation error<br>
C) Automatic conversion to correct format<br>
D) DateTimeParseException at runtime

## Réponse

<strong>Réponse correcte :</strong> D)<br><br>

<strong>parse()</strong> is <strong>STRICT</strong>:<br>
• Strict ISO by default<br>
• No correction<br>
• No approximation<br><br>

Expected format: yyyy-MM-dd (with zeros)<br>
Provided format: yyyy-M-d (without zeros)<br><br>

Result: <strong>DateTimeParseException</strong> at runtime.<br><br>

Java never guesses, never corrects.<br><br>

<strong>A), B), C) are incorrect:</strong> Runtime exception.

## Question

What is the difference between plusDays() and withDayOfMonth()?<br><br>

Please select 1 option<br><br>

A) No difference<br>
B) with = relative, plus = absolute<br>
C) plus = relative (addition), with = absolute (replacement)<br>
D) Both do the same thing differently

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

<strong>KEY difference:</strong><br><br>

<strong>plusDays():</strong><br>
• <strong>Relative</strong> operation<br>
• Adds days<br>
• date.plusDays(5) → +5 days<br><br>

<strong>withDayOfMonth():</strong><br>
• <strong>Absolute</strong> operation<br>
• Direct replacement<br>
• date.withDayOfMonth(15) → day = 15<br><br>

<strong>Rule:</strong> plus/minus = relative, with = absolute<br><br>

<strong>A), B), D) are incorrect:</strong> There is an important difference.

## Question

What is "machine-scale" vs "human-scale"?<br><br>

Please select 1 option<br><br>

A) Performance scales<br>
B) Machine = absolute UTC time, Human = calendar with human rules<br>
C) Different Java versions<br>
D) Different date formats

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>Machine-scale:</strong><br>
• Absolute time<br>
• UTC<br>
• Independent of humans<br>
• Classes: Instant, Duration<br><br>

<strong>Human-scale:</strong><br>
• Calendar<br>
• Human rules (months, years, DST)<br>
• Classes: LocalDate, LocalDateTime, Period, ZonedDateTime<br><br>

<strong>A), C), D) are incorrect:</strong> Wrong category.

## Question

What is the epoch in Java?<br><br>

Please select 1 option<br><br>

A) January 1, 1970 00:00:00 UTC<br>
B) The moment the JVM is created<br>
C) January 1, 1900 at midnight<br>
D) January 1, 2000 at midnight

## Réponse

<strong>Réponse correcte :</strong> A)<br><br>

The <strong>epoch</strong> is the reference point:<br>
<strong>1970-01-01T00:00:00Z (UTC)</strong><br><br>

Instant is based on the epoch:<br>
• Instant.ofEpochSecond(0) → epoch<br>
• Instant.ofEpochMilli(1000) → +1 second<br><br>

Timestamps are often expressed in milliseconds since the epoch.<br><br>

<strong>B), C), D) are incorrect:</strong> Wrong date.

## Question

What does Instant.toEpochMilli() do?<br><br>

Please select 1 option<br><br>

A) Converts to LocalDateTime<br>
B) Converts to ISO format<br>
C) Returns the number of milliseconds since the epoch (1970)<br>
D) Returns the current year

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

<strong>toEpochMilli()</strong> returns a <strong>long</strong> representing the number of milliseconds since the epoch (1970-01-01T00:00:00Z).<br><br>

Example:<br>
Instant instant = Instant.now();<br>
long millis = instant.toEpochMilli();<br><br>

Useful for:<br>
• Interoperability with old APIs<br>
• Database storage<br>
• Numeric comparisons<br><br>

<strong>A), B), D) are incorrect:</strong> Wrong function.

## Question

How do you convert an Instant to a human representation?<br><br>

Please select 1 option<br><br>

A) instant.toLocalDateTime()<br>
B) instant.format()<br>
C) new ZonedDateTime(instant)<br>
D) instant.atZone(ZoneId)

## Réponse

<strong>Réponse correcte :</strong> D)<br><br>

To convert <strong>Instant → human representation</strong>:<br>
<strong>instant.atZone(ZoneId)</strong><br><br>

Example:<br>
Instant instant = Instant.now();<br>
ZonedDateTime zdt = instant.atZone(ZoneId.of("Europe/Paris"));<br><br>

This method adds the time zone context necessary for human display.<br><br>

<strong>A) is incorrect:</strong> Must specify a zone.<br>
<strong>B) and C) are incorrect:</strong> Incorrect syntax.

## Question

Why did the old Calendar API use months starting from 0?<br><br>

Please select 1 option<br><br>

A) To optimize memory<br>
B) To facilitate calculations<br>
C) Legacy from C/Unix design (historical error)<br>
D) It's more logical

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

The old Calendar API used months starting from 0 due to <strong>legacy from C/Unix design</strong>.<br><br>

Problem:<br>
• January = 0<br>
• February = 1<br>
• ...<br>
• December = 11<br><br>

This was a constant source of <strong>bugs</strong>.<br><br>

The new API (java.time) corrects this:<br>
• January = 1<br>
• December = 12<br><br>

<strong>A), B), D) are incorrect:</strong> It was a design error.

## Question

Which code is INCORRECT due to immutability? (OCP trap)<br><br>

Please select 1 option<br><br>

A) date = date.plusDays(1);<br>
B) date.plusDays(1);<br>
C) LocalDate newDate = date.plusDays(1);<br>
D) date = date.withYear(2025);

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>INCORRECT:</strong> date.plusDays(1);<br><br>

Problem:<br>
• plusDays() returns a <strong>new object</strong><br>
• The result is <strong>lost</strong> (not assigned)<br>
• date remains <strong>unchanged</strong><br><br>

<strong>Major OCP trap:</strong> Forgetting to assign the result.<br><br>

<strong>A), C), D) are correct:</strong> They assign the result.

## Question

In java.time, are all classes immutable and thread-safe?<br><br>

Please select 1 option<br><br>

A) Yes, all without exception<br>
B) Yes, the main classes (LocalDate, Instant, ZonedDateTime, etc.)<br>
C) No, none are thread-safe<br>
D) Only Instant is immutable

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>Yes</strong>, the main java.time classes are <strong>immutable</strong> and <strong>thread-safe</strong>:<br>
• LocalDate<br>
• LocalTime<br>
• LocalDateTime<br>
• ZonedDateTime<br>
• Instant<br>
• Duration<br>
• Period<br>
• DateTimeFormatter<br><br>

This is a major advantage over the old API.<br><br>

<strong>A) is almost correct:</strong> A few rare exceptions exist.<br>
<strong>C) and D) are incorrect:</strong> False.

## Question

Which method returns the Instant corresponding to January 1, 1970 00:00:00 UTC?<br><br>

Please select 1 option<br><br>

A) Instant.epoch()<br>
B) Instant.ofEpochSecond(0)<br>
C) Instant.zero()<br>
D) new Instant(0)

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

The correct method is <strong>Instant.ofEpochSecond(0)</strong>.<br><br>

This returns the reference point (epoch):<br>
1970-01-01T00:00:00Z<br><br>

Other examples:<br>
• Instant.ofEpochMilli(1000) → +1 second<br>
• Instant.ofEpochSecond(86400) → +1 day<br><br>

<strong>A), C), D) are incorrect:</strong> Non-existent methods.

## Question

What happens at compile time with LocalDate.parse("15/01/2024")?<br><br>

Please select 1 option<br><br>

A) Compilation error<br>
B) Compiles OK, exception at runtime<br>
C) Automatic conversion to ISO format<br>
D) Warning but compiles OK

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>Fundamental parse() rule:</strong><br>
• ✔️ Compilation → OK (String syntactically valid)<br>
• ❌ Runtime → exception if invalid format<br><br>

The compiler does NOT verify String values.<br><br>

For "15/01/2024", you would need to use an appropriate DateTimeFormatter.<br><br>

<strong>A) is incorrect:</strong> Compilation succeeds.<br>
<strong>C) is incorrect:</strong> Java never converts automatically.<br>
<strong>D) is incorrect:</strong> No warning at compilation.

## Question

What is the proper use case for measuring a system process execution time?<br><br>

Please select 1 option<br><br>

A) Period between two LocalDate<br>
B) Duration between two Instant<br>
C) ChronoUnit.DAYS.between() with LocalDateTime<br>
D) Difference between two ZonedDateTime

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

To measure <strong>execution time</strong> of a system process:<br>
<strong>Duration between two Instant</strong><br><br>

Reasons:<br>
• <strong>Exact</strong> measurement in nanoseconds<br>
• Machine-scale<br>
• Independent of calendar and DST<br><br>

Example:<br>
Instant start = Instant.now();<br>
// process<br>
Instant end = Instant.now();<br>
Duration duration = Duration.between(start, end);<br><br>

<strong>A), C), D) are incorrect:</strong> Not suitable for exact system measurements.

## Question

What is Instant in Java?<br><br>

Please select 1 option<br><br>

A) A local time with time zone<br>
B) A date without time<br>
C) A time offset<br>
D) An absolute point in time (UTC), independent of time zones

## Réponse

<strong>Réponse correcte :</strong> D)<br><br>

<strong>Instant</strong> represents an <strong>absolute point in time (UTC)</strong>.<br><br>

Independent of:<br>
• Countries<br>
• Time zones<br>
• DST<br><br>

Serves as a <strong>universal reference</strong>.<br><br>

Example: number of seconds since January 1, 1970 00:00:00 UTC (epoch).<br><br>

<strong>A) is incorrect:</strong> Instant has no time zone.<br>
<strong>B) and C) are incorrect:</strong> Wrong definition.

## Question

Which type should you use to record the exact moment of a system event (log)?<br><br>

Please select 1 option<br><br>

A) LocalDateTime<br>
B) Instant<br>
C) ZonedDateTime<br>
D) LocalTime

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

For a <strong>system event</strong> (log, timestamp), use <strong>Instant</strong>.<br><br>

Reasons:<br>
• Absolute point in time<br>
• Independent of time zones<br>
• Universal reference<br>
• No ambiguity with DST<br><br>

<strong>A) and C) are incorrect:</strong> Depend on a time zone or locality.<br>
<strong>D) is incorrect:</strong> No date, only time.

## Question

Which method returns the current Instant?<br><br>

Please select 1 option<br><br>

A) Instant.getCurrentInstant()<br>
B) System.currentTimeMillis()<br>
C) ZonedDateTime.toInstant()<br>
D) Instant.now()

## Réponse

<strong>Réponse correcte :</strong> D)<br><br>

The method to get the current instant is <strong>Instant.now()</strong>.<br><br>

This method returns the current point in time (UTC).<br><br>

Example:<br>
Instant now = Instant.now();<br><br>

<strong>A) is incorrect:</strong> This method doesn't exist.<br>
<strong>C) is incorrect:</strong> That's for converting an existing ZonedDateTime.<br>
<strong>B) is incorrect:</strong> Returns a long, not an Instant (old API).

## Question

What will the following code print?<br><br>

```java
LocalDate date = LocalDate.of(2024, 1, 15);
date.plusDays(5);
System.out.println(date);
```
<br><br>

Please select 1 option<br><br>

A) 2024-01-20<br>
B) 2024-01-15<br>
C) Compilation error<br>
D) Runtime exception

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>MAJOR OCP TRAP:</strong> The code prints <strong>2024-01-15</strong>.<br><br>

Why?<br>
• LocalDate is <strong>immutable</strong><br>
• plusDays() returns a <strong>new object</strong><br>
• The result is <strong>not assigned</strong><br>
• date remains <strong>unchanged</strong><br><br>

Correct code:<br>
date = date.plusDays(5);<br><br>

<strong>A) is incorrect:</strong> Would require assignment.<br>
<strong>C) and D) are incorrect:</strong> Code compiles and runs without error.

## Question

What will the following code print?<br><br>

```java
LocalDate date = LocalDate.parse("2024-1-15");
System.out.println(date);
```
<br><br>

Please select 1 option<br><br>

A) 2024-01-15<br>
B) 2024-1-15<br>
C) Compilation error<br>
D) DateTimeParseException at runtime

## Réponse

<strong>Réponse correcte :</strong> D)<br><br>

<strong>parse()</strong> expects <strong>strict ISO-8601</strong> format: yyyy-MM-dd<br><br>

Given: "2024-1-15" (missing zero)<br>
Expected: "2024-01-15"<br><br>

Result: <strong>DateTimeParseException</strong> at runtime<br><br>

Java never guesses, never corrects format.<br><br>

<strong>A) and B) are incorrect:</strong> Exception is thrown.<br>
<strong>C) is incorrect:</strong> Compiles fine, fails at runtime.

## Question

What will the following code print?<br><br>

```java
LocalDateTime ldt1 = LocalDateTime.of(2024, 1, 15, 10, 30);
LocalDateTime ldt2 = ldt1.withDayOfMonth(20).plusHours(2);
System.out.println(ldt1);
System.out.println(ldt2);
```
<br><br>

Please select 1 option<br><br>

A) 2024-01-20T12:30<br>
2024-01-20T12:30<br><br>

B) 2024-01-15T10:30<br>
2024-01-20T12:30<br><br>

C) 2024-01-20T12:30<br>
2024-01-15T10:30<br><br>

D) Compilation error

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>Immutability rule:</strong><br>
• ldt1 remains <strong>unchanged</strong> (immutable)<br>
• withDayOfMonth() creates new object<br>
• plusHours() creates another new object<br>
• ldt2 = final result<br><br>

Output:<br>
ldt1: 2024-01-15T10:30 (original)<br>
ldt2: 2024-01-20T12:30 (modified)<br><br>

<strong>A), C), D) are incorrect:</strong> Wrong understanding of immutability.

## Question

What will the following code print?<br><br>

```java
Instant instant = Instant.ofEpochSecond(0);
System.out.println(instant);
```
<br><br>

Please select 1 option<br><br>

A) 1970-01-01T00:00:00Z<br>
B) 0<br>
C) 1970-01-01<br>
D) null

## Réponse

<strong>Réponse correcte :</strong> A)<br><br>

<strong>Instant.ofEpochSecond(0)</strong> creates the <strong>epoch instant</strong>:<br>
<strong>1970-01-01T00:00:00Z</strong><br><br>

The epoch is the reference point (0 seconds since Jan 1, 1970 UTC).<br><br>

<strong>B) is incorrect:</strong> Returns an Instant object, not a number.<br>
<strong>C) is incorrect:</strong> Includes time and Z (UTC indicator).<br>
<strong>D) is incorrect:</strong> Returns a valid Instant object.

## Question

What will the following code print?<br><br>

```java
LocalDate date = LocalDate.of(2024, 2, 29);
date = date.plusYears(1);
System.out.println(date);
```
<br><br>

Please select 1 option<br><br>

A) 2025-03-01<br>
B) 2025-02-28<br>
C) 2025-02-29<br>
D) DateTimeException at runtime

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>Intelligent adjustment:</strong><br>
• 2024-02-29 is valid (leap year)<br>
• 2025-02-29 doesn't exist (not a leap year)<br>
• Java adjusts to <strong>2025-02-28</strong> (last valid day of month)<br><br>

No exception, automatic adjustment to nearest valid date.<br><br>

<strong>C) is incorrect:</strong> Feb 29, 2025 doesn't exist.<br>
<strong>A) is incorrect:</strong> Java adjusts to last day of month, not next month.<br>
<strong>D) is incorrect:</strong> No exception thrown.

## Question

What will the following code print?<br><br>

```java
LocalTime time = LocalTime.of(14, 30);
System.out.println(time.plusHours(10));
System.out.println(time);
```
<br><br>

Please select 1 option<br><br>

A) 00:30<br>
14:30<br><br>

B) 24:30<br>
14:30<br><br>

C) 00:30<br>
00:30<br><br>

D) Compilation error

## Réponse

<strong>Réponse correcte :</strong> A)<br><br>

<strong>Calculation:</strong><br>
• 14:30 + 10 hours = 24:30<br>
• 24:30 wraps around to <strong>00:30</strong> (next day)<br><br>

<strong>Immutability:</strong><br>
• time remains <strong>14:30</strong> (unchanged)<br>
• plusHours() returns new object<br><br>

Output:<br>
00:30 (result of operation)<br>
14:30 (original time)<br><br>

<strong>B), C), D) are incorrect:</strong> Wrong calculation or immutability understanding.

## Question

What is the output of this code?<br><br>

```java
LocalDate date = LocalDate.of(2024, 1, 31);
date = date.plusMonths(1);
System.out.println(date);
```
<br><br>

Please select 1 option<br><br>

A) 2024-02-31<br>
B) 2024-03-02<br>
C) DateTimeException<br>
D) 2024-02-29

## Réponse

<strong>Réponse correcte :</strong> D)<br><br>

<strong>Intelligent adjustment:</strong><br>
• Jan 31 + 1 month = Feb 31<br>
• Feb 31 doesn't exist<br>
• Java adjusts to <strong>Feb 29</strong> (2024 is leap year)<br>
• Last valid day of month<br><br>

No exception, automatic adjustment.<br><br>

<strong>A) is incorrect:</strong> Feb 31 doesn't exist.<br>
<strong>B) is incorrect:</strong> Doesn't overflow to next month.<br>
<strong>C) is incorrect:</strong> No exception thrown.

## Question

What will the following code print?<br><br>

```java
LocalDate date = LocalDate.of(2024, 1, 15);
System.out.println(date.getMonth());
System.out.println(date.getMonthValue());
```
<br><br>

Please select 1 option<br><br>

A) JANUARY<br>
1<br><br>

B) 1<br>
JANUARY<br><br>

C) 0<br>
JANUARY<br><br>

D) JANUARY<br>
0

## Réponse

<strong>Réponse correcte :</strong> A)<br><br>

<strong>Two different methods:</strong><br>
• getMonth() returns <strong>Month enum</strong> (JANUARY)<br>
• getMonthValue() returns <strong>int</strong> (1-12)<br><br>

Output:<br>
JANUARY (enum constant)<br>
1 (numeric value)<br><br>

<strong>Important:</strong> Java uses 1-12 for months, not 0-11 like old Calendar API.<br><br>

<strong>B), C), D) are incorrect:</strong> Wrong order or values.

## Question

Which of the following are characteristics of java.time classes?<br><br>

Please select all that apply<br><br>

A) They are immutable<br>
B) They are based on java.util.Date<br>
C) They are thread-safe<br>
D) They use months starting from 0<br>
E) They follow ISO-8601 by default

## Réponse

<strong>Réponses correctes :</strong> A), C), E)<br><br>

<strong>A) ✅ Immutable:</strong> all java.time classes are immutable.<br>
<strong>C) ✅ Thread-safe:</strong> immutability guarantees thread safety.<br>
<strong>E) ✅ ISO-8601:</strong> default format throughout java.time.<br><br>

<strong>B) ❌ Incorrect:</strong> java.time is completely separate from java.util.Date.<br>
<strong>D) ❌ Incorrect:</strong> java.time uses 1-12 for months, not 0-11.

## Question

Which of the following create a valid LocalDate?<br><br>

Please select all that apply<br><br>

A) LocalDate.of(2024, 2, 29)<br>
B) LocalDate.of(2023, 2, 29)<br>
C) LocalDate.parse("2024-01-15")<br>
D) new LocalDate(2024, 1, 15)<br>
E) LocalDate.of(2024, 13, 1)

## Réponse

<strong>Réponses correctes :</strong> A), C)<br><br>

<strong>A) ✅ Correct:</strong> 2024 is a leap year, Feb 29 is valid.<br>
<strong>C) ✅ Correct:</strong> Valid ISO-8601 format, parses successfully.<br><br>

<strong>B) ❌ Incorrect:</strong> 2023 is not a leap year, Feb 29 doesn't exist — throws DateTimeException.<br>
<strong>D) ❌ Incorrect:</strong> LocalDate has no public constructor.<br>
<strong>E) ❌ Incorrect:</strong> Month 13 doesn't exist — throws DateTimeException.

## Question

Which of the following statements about Instant are true?<br><br>

Please select all that apply<br><br>

A) Instant represents an absolute point in time<br>
B) Instant automatically adjusts for Daylight Saving Time<br>
C) Instant is expressed in UTC<br>
D) Instant can be directly formatted without a ZoneId<br>
E) Instant is immutable

## Réponse

<strong>Réponses correctes :</strong> A), C), E)<br><br>

<strong>A) ✅ Correct:</strong> Instant is a single point on the timeline, independent of time zones.<br>
<strong>C) ✅ Correct:</strong> Instant is always in UTC (Z offset).<br>
<strong>E) ✅ Correct:</strong> Instant is immutable like all java.time classes.<br><br>

<strong>B) ❌ Incorrect:</strong> Instant is UTC-based and does not apply DST — it is time-zone-agnostic.<br>
<strong>D) ❌ Incorrect:</strong> To display Instant in human-readable form, you must supply a ZoneId via atZone().
